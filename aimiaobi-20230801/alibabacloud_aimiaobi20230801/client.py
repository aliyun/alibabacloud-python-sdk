# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aimiaobi20230801 import models as ai_miao_bi_20230801_models
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
        self._endpoint = self.get_endpoint('aimiaobi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_async_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.CancelAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CancelAsyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CancelAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_async_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.CancelAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CancelAsyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CancelAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_async_task(
        self,
        request: ai_miao_bi_20230801_models.CancelAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.CancelAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_async_task_with_options(request, runtime)

    async def cancel_async_task_async(
        self,
        request: ai_miao_bi_20230801_models.CancelAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.CancelAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_async_task_with_options_async(request, runtime)

    def clear_intervenes_with_options(
        self,
        request: ai_miao_bi_20230801_models.ClearIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ClearIntervenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ClearIntervenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_intervenes_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ClearIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ClearIntervenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ClearIntervenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_intervenes(
        self,
        request: ai_miao_bi_20230801_models.ClearIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ClearIntervenesResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_intervenes_with_options(request, runtime)

    async def clear_intervenes_async(
        self,
        request: ai_miao_bi_20230801_models.ClearIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ClearIntervenesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_intervenes_with_options_async(request, runtime)

    def create_generated_content_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.CreateGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateGeneratedContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.CreateGeneratedContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not UtilClient.is_unset(request.content_text):
            body['ContentText'] = request.content_text
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CreateGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_generated_content_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.CreateGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateGeneratedContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.CreateGeneratedContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not UtilClient.is_unset(request.content_text):
            body['ContentText'] = request.content_text
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CreateGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_generated_content(
        self,
        request: ai_miao_bi_20230801_models.CreateGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.CreateGeneratedContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_generated_content_with_options(request, runtime)

    async def create_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.CreateGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.CreateGeneratedContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_generated_content_with_options_async(request, runtime)

    def create_token_with_options(
        self,
        request: ai_miao_bi_20230801_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateToken',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CreateTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_token_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateToken',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.CreateTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_token(
        self,
        request: ai_miao_bi_20230801_models.CreateTokenRequest,
    ) -> ai_miao_bi_20230801_models.CreateTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_token_with_options(request, runtime)

    async def create_token_async(
        self,
        request: ai_miao_bi_20230801_models.CreateTokenRequest,
    ) -> ai_miao_bi_20230801_models.CreateTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_token_with_options_async(request, runtime)

    def delete_generated_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteGeneratedContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_generated_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteGeneratedContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_generated_content(
        self,
        request: ai_miao_bi_20230801_models.DeleteGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.DeleteGeneratedContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_generated_content_with_options(request, runtime)

    async def delete_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.DeleteGeneratedContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_generated_content_with_options_async(request, runtime)

    def delete_intervene_rule_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteInterveneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteInterveneRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInterveneRule',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteInterveneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_intervene_rule_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteInterveneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteInterveneRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInterveneRule',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteInterveneRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_intervene_rule(
        self,
        request: ai_miao_bi_20230801_models.DeleteInterveneRuleRequest,
    ) -> ai_miao_bi_20230801_models.DeleteInterveneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_intervene_rule_with_options(request, runtime)

    async def delete_intervene_rule_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteInterveneRuleRequest,
    ) -> ai_miao_bi_20230801_models.DeleteInterveneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_intervene_rule_with_options_async(request, runtime)

    def delete_material_by_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteMaterialByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteMaterialByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMaterialById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteMaterialByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_material_by_id_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteMaterialByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteMaterialByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMaterialById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.DeleteMaterialByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_material_by_id(
        self,
        request: ai_miao_bi_20230801_models.DeleteMaterialByIdRequest,
    ) -> ai_miao_bi_20230801_models.DeleteMaterialByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_material_by_id_with_options(request, runtime)

    async def delete_material_by_id_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteMaterialByIdRequest,
    ) -> ai_miao_bi_20230801_models.DeleteMaterialByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_material_by_id_with_options_async(request, runtime)

    def export_generated_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.ExportGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportGeneratedContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_generated_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ExportGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportGeneratedContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_generated_content(
        self,
        request: ai_miao_bi_20230801_models.ExportGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.ExportGeneratedContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_generated_content_with_options(request, runtime)

    async def export_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.ExportGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.ExportGeneratedContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_generated_content_with_options_async(request, runtime)

    def export_intervenes_with_options(
        self,
        request: ai_miao_bi_20230801_models.ExportIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportIntervenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportIntervenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_intervenes_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ExportIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportIntervenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ExportIntervenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_intervenes(
        self,
        request: ai_miao_bi_20230801_models.ExportIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ExportIntervenesResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_intervenes_with_options(request, runtime)

    async def export_intervenes_async(
        self,
        request: ai_miao_bi_20230801_models.ExportIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ExportIntervenesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_intervenes_with_options_async(request, runtime)

    def feedback_dialogue_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.FeedbackDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.FeedbackDialogueResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.FeedbackDialogueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rating_tags):
            request.rating_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rating_tags, 'RatingTags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.customer_response):
            body['CustomerResponse'] = request.customer_response
        if not UtilClient.is_unset(request.good_text):
            body['GoodText'] = request.good_text
        if not UtilClient.is_unset(request.modified_response):
            body['ModifiedResponse'] = request.modified_response
        if not UtilClient.is_unset(request.rating):
            body['Rating'] = request.rating
        if not UtilClient.is_unset(request.rating_tags_shrink):
            body['RatingTags'] = request.rating_tags_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FeedbackDialogue',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.FeedbackDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_dialogue_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.FeedbackDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.FeedbackDialogueResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.FeedbackDialogueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rating_tags):
            request.rating_tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rating_tags, 'RatingTags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.customer_response):
            body['CustomerResponse'] = request.customer_response
        if not UtilClient.is_unset(request.good_text):
            body['GoodText'] = request.good_text
        if not UtilClient.is_unset(request.modified_response):
            body['ModifiedResponse'] = request.modified_response
        if not UtilClient.is_unset(request.rating):
            body['Rating'] = request.rating
        if not UtilClient.is_unset(request.rating_tags_shrink):
            body['RatingTags'] = request.rating_tags_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FeedbackDialogue',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.FeedbackDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def feedback_dialogue(
        self,
        request: ai_miao_bi_20230801_models.FeedbackDialogueRequest,
    ) -> ai_miao_bi_20230801_models.FeedbackDialogueResponse:
        runtime = util_models.RuntimeOptions()
        return self.feedback_dialogue_with_options(request, runtime)

    async def feedback_dialogue_async(
        self,
        request: ai_miao_bi_20230801_models.FeedbackDialogueRequest,
    ) -> ai_miao_bi_20230801_models.FeedbackDialogueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.feedback_dialogue_with_options_async(request, runtime)

    def fetch_image_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.FetchImageTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.FetchImageTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.FetchImageTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_id_list):
            request.task_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_id_list, 'TaskIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not UtilClient.is_unset(request.task_id_list_shrink):
            body['TaskIdList'] = request.task_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FetchImageTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.FetchImageTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_image_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.FetchImageTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.FetchImageTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.FetchImageTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_id_list):
            request.task_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_id_list, 'TaskIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not UtilClient.is_unset(request.task_id_list_shrink):
            body['TaskIdList'] = request.task_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FetchImageTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.FetchImageTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_image_task(
        self,
        request: ai_miao_bi_20230801_models.FetchImageTaskRequest,
    ) -> ai_miao_bi_20230801_models.FetchImageTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_image_task_with_options(request, runtime)

    async def fetch_image_task_async(
        self,
        request: ai_miao_bi_20230801_models.FetchImageTaskRequest,
    ) -> ai_miao_bi_20230801_models.FetchImageTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_image_task_with_options_async(request, runtime)

    def generate_file_url_by_key_with_options(
        self,
        request: ai_miao_bi_20230801_models.GenerateFileUrlByKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateFileUrlByKey',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_file_url_by_key_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateFileUrlByKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateFileUrlByKey',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_file_url_by_key(
        self,
        request: ai_miao_bi_20230801_models.GenerateFileUrlByKeyRequest,
    ) -> ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_file_url_by_key_with_options(request, runtime)

    async def generate_file_url_by_key_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateFileUrlByKeyRequest,
    ) -> ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_file_url_by_key_with_options_async(request, runtime)

    def generate_image_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.GenerateImageTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateImageTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.GenerateImageTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.paragraph_list):
            request.paragraph_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.paragraph_list, 'ParagraphList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not UtilClient.is_unset(request.paragraph_list_shrink):
            body['ParagraphList'] = request.paragraph_list_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.style):
            body['Style'] = request.style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateImageTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateImageTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_image_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.GenerateImageTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateImageTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.GenerateImageTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.paragraph_list):
            request.paragraph_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.paragraph_list, 'ParagraphList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not UtilClient.is_unset(request.paragraph_list_shrink):
            body['ParagraphList'] = request.paragraph_list_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.style):
            body['Style'] = request.style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateImageTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateImageTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_image_task(
        self,
        request: ai_miao_bi_20230801_models.GenerateImageTaskRequest,
    ) -> ai_miao_bi_20230801_models.GenerateImageTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_image_task_with_options(request, runtime)

    async def generate_image_task_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateImageTaskRequest,
    ) -> ai_miao_bi_20230801_models.GenerateImageTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_image_task_with_options_async(request, runtime)

    def generate_upload_config_with_options(
        self,
        request: ai_miao_bi_20230801_models.GenerateUploadConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateUploadConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.parent_dir):
            body['ParentDir'] = request.parent_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateUploadConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateUploadConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_upload_config_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateUploadConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateUploadConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.parent_dir):
            body['ParentDir'] = request.parent_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateUploadConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateUploadConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_upload_config(
        self,
        request: ai_miao_bi_20230801_models.GenerateUploadConfigRequest,
    ) -> ai_miao_bi_20230801_models.GenerateUploadConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_config_with_options(request, runtime)

    async def generate_upload_config_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateUploadConfigRequest,
    ) -> ai_miao_bi_20230801_models.GenerateUploadConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_upload_config_with_options_async(request, runtime)

    def generate_view_point_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.GenerateViewPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateViewPointResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.GenerateViewPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateViewPoint',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateViewPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_view_point_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.GenerateViewPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateViewPointResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.GenerateViewPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateViewPoint',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GenerateViewPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_view_point(
        self,
        request: ai_miao_bi_20230801_models.GenerateViewPointRequest,
    ) -> ai_miao_bi_20230801_models.GenerateViewPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_view_point_with_options(request, runtime)

    async def generate_view_point_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateViewPointRequest,
    ) -> ai_miao_bi_20230801_models.GenerateViewPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_view_point_with_options_async(request, runtime)

    def get_data_source_order_config_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetDataSourceOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataSourceOrderConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_order_config_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetDataSourceOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataSourceOrderConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source_order_config(
        self,
        request: ai_miao_bi_20230801_models.GetDataSourceOrderConfigRequest,
    ) -> ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_order_config_with_options(request, runtime)

    async def get_data_source_order_config_async(
        self,
        request: ai_miao_bi_20230801_models.GetDataSourceOrderConfigRequest,
    ) -> ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_source_order_config_with_options_async(request, runtime)

    def get_generated_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetGeneratedContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_generated_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetGeneratedContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_generated_content(
        self,
        request: ai_miao_bi_20230801_models.GetGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.GetGeneratedContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_generated_content_with_options(request, runtime)

    async def get_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.GetGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.GetGeneratedContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_generated_content_with_options_async(request, runtime)

    def get_intervene_global_reply_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneGlobalReplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterveneGlobalReply',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_global_reply_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneGlobalReplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterveneGlobalReply',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_global_reply(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneGlobalReplyRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_global_reply_with_options(request, runtime)

    async def get_intervene_global_reply_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneGlobalReplyRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_global_reply_with_options_async(request, runtime)

    def get_intervene_import_task_info_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneImportTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInterveneImportTaskInfo',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_import_task_info_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneImportTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInterveneImportTaskInfo',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_import_task_info(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneImportTaskInfoRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_import_task_info_with_options(request, runtime)

    async def get_intervene_import_task_info_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneImportTaskInfoRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_import_task_info_with_options_async(request, runtime)

    def get_intervene_rule_detail_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInterveneRuleDetail',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_rule_detail_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInterveneRuleDetail',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_rule_detail(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneRuleDetailRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_rule_detail_with_options(request, runtime)

    async def get_intervene_rule_detail_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneRuleDetailRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_rule_detail_with_options_async(request, runtime)

    def get_intervene_template_file_url_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterveneTemplateFileUrl',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_template_file_url_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterveneTemplateFileUrl',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_template_file_url(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_template_file_url_with_options(request, runtime)

    async def get_intervene_template_file_url_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_template_file_url_with_options_async(request, runtime)

    def get_material_by_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetMaterialByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetMaterialByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMaterialById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetMaterialByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_material_by_id_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetMaterialByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetMaterialByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMaterialById',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetMaterialByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_material_by_id(
        self,
        request: ai_miao_bi_20230801_models.GetMaterialByIdRequest,
    ) -> ai_miao_bi_20230801_models.GetMaterialByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_material_by_id_with_options(request, runtime)

    async def get_material_by_id_async(
        self,
        request: ai_miao_bi_20230801_models.GetMaterialByIdRequest,
    ) -> ai_miao_bi_20230801_models.GetMaterialByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_material_by_id_with_options_async(request, runtime)

    def get_properties_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetPropertiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProperties',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetPropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_properties_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetPropertiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProperties',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.GetPropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_properties(
        self,
        request: ai_miao_bi_20230801_models.GetPropertiesRequest,
    ) -> ai_miao_bi_20230801_models.GetPropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_properties_with_options(request, runtime)

    async def get_properties_async(
        self,
        request: ai_miao_bi_20230801_models.GetPropertiesRequest,
    ) -> ai_miao_bi_20230801_models.GetPropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_properties_with_options_async(request, runtime)

    def import_intervene_file_with_options(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportInterveneFile',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ImportInterveneFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_intervene_file_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportInterveneFile',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ImportInterveneFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_intervene_file(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileRequest,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_intervene_file_with_options(request, runtime)

    async def import_intervene_file_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileRequest,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_intervene_file_with_options_async(request, runtime)

    def import_intervene_file_async_with_options(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportInterveneFileAsync',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_intervene_file_async_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.file_key):
            body['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportInterveneFileAsync',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_intervene_file_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileAsyncRequest,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_intervene_file_async_with_options(request, runtime)

    async def import_intervene_file_async_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileAsyncRequest,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_intervene_file_async_with_options_async(request, runtime)

    def insert_intervene_global_reply_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.InsertInterveneGlobalReplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.InsertInterveneGlobalReplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reply_messag_list):
            request.reply_messag_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reply_messag_list, 'ReplyMessagList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.reply_messag_list_shrink):
            body['ReplyMessagList'] = request.reply_messag_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertInterveneGlobalReply',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_intervene_global_reply_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.InsertInterveneGlobalReplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.InsertInterveneGlobalReplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reply_messag_list):
            request.reply_messag_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reply_messag_list, 'ReplyMessagList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.reply_messag_list_shrink):
            body['ReplyMessagList'] = request.reply_messag_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertInterveneGlobalReply',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_intervene_global_reply(
        self,
        request: ai_miao_bi_20230801_models.InsertInterveneGlobalReplyRequest,
    ) -> ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_intervene_global_reply_with_options(request, runtime)

    async def insert_intervene_global_reply_async(
        self,
        request: ai_miao_bi_20230801_models.InsertInterveneGlobalReplyRequest,
    ) -> ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_intervene_global_reply_with_options_async(request, runtime)

    def insert_intervene_rule_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.InsertInterveneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.InsertInterveneRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.InsertInterveneRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intervene_rule_config):
            request.intervene_rule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intervene_rule_config, 'InterveneRuleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.intervene_rule_config_shrink):
            body['InterveneRuleConfig'] = request.intervene_rule_config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertInterveneRule',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.InsertInterveneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_intervene_rule_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.InsertInterveneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.InsertInterveneRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.InsertInterveneRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intervene_rule_config):
            request.intervene_rule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intervene_rule_config, 'InterveneRuleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.intervene_rule_config_shrink):
            body['InterveneRuleConfig'] = request.intervene_rule_config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertInterveneRule',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.InsertInterveneRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_intervene_rule(
        self,
        request: ai_miao_bi_20230801_models.InsertInterveneRuleRequest,
    ) -> ai_miao_bi_20230801_models.InsertInterveneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_intervene_rule_with_options(request, runtime)

    async def insert_intervene_rule_async(
        self,
        request: ai_miao_bi_20230801_models.InsertInterveneRuleRequest,
    ) -> ai_miao_bi_20230801_models.InsertInterveneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_intervene_rule_with_options_async(request, runtime)

    def list_async_tasks_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListAsyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListAsyncTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListAsyncTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_status_list):
            request.task_status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_status_list, 'TaskStatusList', 'json')
        if not UtilClient.is_unset(tmp_req.task_type_list):
            request.task_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_type_list, 'TaskTypeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.task_code):
            body['TaskCode'] = request.task_code
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_status_list_shrink):
            body['TaskStatusList'] = request.task_status_list_shrink
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.task_type_list_shrink):
            body['TaskTypeList'] = request.task_type_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAsyncTasks',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListAsyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_async_tasks_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListAsyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListAsyncTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListAsyncTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_status_list):
            request.task_status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_status_list, 'TaskStatusList', 'json')
        if not UtilClient.is_unset(tmp_req.task_type_list):
            request.task_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_type_list, 'TaskTypeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.task_code):
            body['TaskCode'] = request.task_code
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_status_list_shrink):
            body['TaskStatusList'] = request.task_status_list_shrink
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.task_type_list_shrink):
            body['TaskTypeList'] = request.task_type_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAsyncTasks',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListAsyncTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_async_tasks(
        self,
        request: ai_miao_bi_20230801_models.ListAsyncTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListAsyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_async_tasks_with_options(request, runtime)

    async def list_async_tasks_async(
        self,
        request: ai_miao_bi_20230801_models.ListAsyncTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListAsyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_async_tasks_with_options_async(request, runtime)

    def list_build_configs_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListBuildConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListBuildConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBuildConfigs',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListBuildConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_build_configs_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListBuildConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListBuildConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBuildConfigs',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListBuildConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_build_configs(
        self,
        request: ai_miao_bi_20230801_models.ListBuildConfigsRequest,
    ) -> ai_miao_bi_20230801_models.ListBuildConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_build_configs_with_options(request, runtime)

    async def list_build_configs_async(
        self,
        request: ai_miao_bi_20230801_models.ListBuildConfigsRequest,
    ) -> ai_miao_bi_20230801_models.ListBuildConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_build_configs_with_options_async(request, runtime)

    def list_dialogues_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListDialoguesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDialoguesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.dialogue_type):
            body['DialogueType'] = request.dialogue_type
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDialogues',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListDialoguesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dialogues_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListDialoguesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDialoguesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.dialogue_type):
            body['DialogueType'] = request.dialogue_type
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDialogues',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListDialoguesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dialogues(
        self,
        request: ai_miao_bi_20230801_models.ListDialoguesRequest,
    ) -> ai_miao_bi_20230801_models.ListDialoguesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dialogues_with_options(request, runtime)

    async def list_dialogues_async(
        self,
        request: ai_miao_bi_20230801_models.ListDialoguesRequest,
    ) -> ai_miao_bi_20230801_models.ListDialoguesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dialogues_with_options_async(request, runtime)

    def list_generated_contents_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListGeneratedContentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListGeneratedContentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGeneratedContents',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListGeneratedContentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_generated_contents_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListGeneratedContentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListGeneratedContentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGeneratedContents',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListGeneratedContentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_generated_contents(
        self,
        request: ai_miao_bi_20230801_models.ListGeneratedContentsRequest,
    ) -> ai_miao_bi_20230801_models.ListGeneratedContentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_generated_contents_with_options(request, runtime)

    async def list_generated_contents_async(
        self,
        request: ai_miao_bi_20230801_models.ListGeneratedContentsRequest,
    ) -> ai_miao_bi_20230801_models.ListGeneratedContentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_generated_contents_with_options_async(request, runtime)

    def list_hot_news_with_type_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListHotNewsWithTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListHotNewsWithTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.news_types):
            request.news_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.news_types, 'NewsTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.news_type):
            body['NewsType'] = request.news_type
        if not UtilClient.is_unset(request.news_types_shrink):
            body['NewsTypes'] = request.news_types_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotNewsWithType',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_news_with_type_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListHotNewsWithTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListHotNewsWithTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.news_types):
            request.news_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.news_types, 'NewsTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.news_type):
            body['NewsType'] = request.news_type
        if not UtilClient.is_unset(request.news_types_shrink):
            body['NewsTypes'] = request.news_types_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotNewsWithType',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_news_with_type(
        self,
        request: ai_miao_bi_20230801_models.ListHotNewsWithTypeRequest,
    ) -> ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hot_news_with_type_with_options(request, runtime)

    async def list_hot_news_with_type_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotNewsWithTypeRequest,
    ) -> ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_news_with_type_with_options_async(request, runtime)

    def list_intervene_cnt_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneCntRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneCntResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneCnt',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneCntResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervene_cnt_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneCntRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneCntResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneCnt',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneCntResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervene_cnt(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneCntRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneCntResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_intervene_cnt_with_options(request, runtime)

    async def list_intervene_cnt_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneCntRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneCntResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_intervene_cnt_with_options_async(request, runtime)

    def list_intervene_import_tasks_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneImportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneImportTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneImportTasks',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneImportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervene_import_tasks_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneImportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneImportTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneImportTasks',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneImportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervene_import_tasks(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneImportTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneImportTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_intervene_import_tasks_with_options(request, runtime)

    async def list_intervene_import_tasks_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneImportTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneImportTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_intervene_import_tasks_with_options_async(request, runtime)

    def list_intervene_rules_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneRules',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervene_rules_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInterveneRules',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListInterveneRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervene_rules(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneRulesRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_intervene_rules_with_options(request, runtime)

    async def list_intervene_rules_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneRulesRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_intervene_rules_with_options_async(request, runtime)

    def list_intervenes_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListIntervenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.intervene_type):
            body['InterveneType'] = request.intervene_type
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListIntervenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervenes_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListIntervenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.intervene_type):
            body['InterveneType'] = request.intervene_type
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIntervenes',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListIntervenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervenes(
        self,
        request: ai_miao_bi_20230801_models.ListIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ListIntervenesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_intervenes_with_options(request, runtime)

    async def list_intervenes_async(
        self,
        request: ai_miao_bi_20230801_models.ListIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ListIntervenesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_intervenes_with_options_async(request, runtime)

    def list_material_documents_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListMaterialDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListMaterialDocumentsResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListMaterialDocumentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_type_list):
            request.doc_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_type_list, 'DocTypeList', 'json')
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.doc_type_list_shrink):
            body['DocTypeList'] = request.doc_type_list_shrink
        if not UtilClient.is_unset(request.generate_public_url):
            body['GeneratePublicUrl'] = request.generate_public_url
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.update_time_end):
            body['UpdateTimeEnd'] = request.update_time_end
        if not UtilClient.is_unset(request.update_time_start):
            body['UpdateTimeStart'] = request.update_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMaterialDocuments',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListMaterialDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_material_documents_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListMaterialDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListMaterialDocumentsResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListMaterialDocumentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_type_list):
            request.doc_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_type_list, 'DocTypeList', 'json')
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.doc_type_list_shrink):
            body['DocTypeList'] = request.doc_type_list_shrink
        if not UtilClient.is_unset(request.generate_public_url):
            body['GeneratePublicUrl'] = request.generate_public_url
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.update_time_end):
            body['UpdateTimeEnd'] = request.update_time_end
        if not UtilClient.is_unset(request.update_time_start):
            body['UpdateTimeStart'] = request.update_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMaterialDocuments',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListMaterialDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_material_documents(
        self,
        request: ai_miao_bi_20230801_models.ListMaterialDocumentsRequest,
    ) -> ai_miao_bi_20230801_models.ListMaterialDocumentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_material_documents_with_options(request, runtime)

    async def list_material_documents_async(
        self,
        request: ai_miao_bi_20230801_models.ListMaterialDocumentsRequest,
    ) -> ai_miao_bi_20230801_models.ListMaterialDocumentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_material_documents_with_options_async(request, runtime)

    def list_versions_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVersions',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_versions_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVersions',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.ListVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_versions(
        self,
        request: ai_miao_bi_20230801_models.ListVersionsRequest,
    ) -> ai_miao_bi_20230801_models.ListVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_versions_with_options(request, runtime)

    async def list_versions_async(
        self,
        request: ai_miao_bi_20230801_models.ListVersionsRequest,
    ) -> ai_miao_bi_20230801_models.ListVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_versions_with_options_async(request, runtime)

    def query_async_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.QueryAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.QueryAsyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.QueryAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_async_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.QueryAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.QueryAsyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.QueryAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_async_task(
        self,
        request: ai_miao_bi_20230801_models.QueryAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.QueryAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_async_task_with_options(request, runtime)

    async def query_async_task_async(
        self,
        request: ai_miao_bi_20230801_models.QueryAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.QueryAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_async_task_with_options_async(request, runtime)

    def save_data_source_order_config_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveDataSourceOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SaveDataSourceOrderConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_config_data_source_list):
            request.user_config_data_source_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_config_data_source_list, 'UserConfigDataSourceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.user_config_data_source_list_shrink):
            body['UserConfigDataSourceList'] = request.user_config_data_source_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveDataSourceOrderConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_data_source_order_config_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveDataSourceOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SaveDataSourceOrderConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_config_data_source_list):
            request.user_config_data_source_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_config_data_source_list, 'UserConfigDataSourceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.user_config_data_source_list_shrink):
            body['UserConfigDataSourceList'] = request.user_config_data_source_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveDataSourceOrderConfig',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_data_source_order_config(
        self,
        request: ai_miao_bi_20230801_models.SaveDataSourceOrderConfigRequest,
    ) -> ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_data_source_order_config_with_options(request, runtime)

    async def save_data_source_order_config_async(
        self,
        request: ai_miao_bi_20230801_models.SaveDataSourceOrderConfigRequest,
    ) -> ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_data_source_order_config_with_options_async(request, runtime)

    def save_material_document_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveMaterialDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveMaterialDocumentResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SaveMaterialDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_keywords):
            request.doc_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.author):
            body['Author'] = request.author
        if not UtilClient.is_unset(request.both_save_private_and_share):
            body['BothSavePrivateAndShare'] = request.both_save_private_and_share
        if not UtilClient.is_unset(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.html_content):
            body['HtmlContent'] = request.html_content
        if not UtilClient.is_unset(request.pub_time):
            body['PubTime'] = request.pub_time
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.src_from):
            body['SrcFrom'] = request.src_from
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.text_content):
            body['TextContent'] = request.text_content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveMaterialDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveMaterialDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_material_document_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveMaterialDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveMaterialDocumentResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SaveMaterialDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_keywords):
            request.doc_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.author):
            body['Author'] = request.author
        if not UtilClient.is_unset(request.both_save_private_and_share):
            body['BothSavePrivateAndShare'] = request.both_save_private_and_share
        if not UtilClient.is_unset(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.html_content):
            body['HtmlContent'] = request.html_content
        if not UtilClient.is_unset(request.pub_time):
            body['PubTime'] = request.pub_time
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.src_from):
            body['SrcFrom'] = request.src_from
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.text_content):
            body['TextContent'] = request.text_content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveMaterialDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SaveMaterialDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_material_document(
        self,
        request: ai_miao_bi_20230801_models.SaveMaterialDocumentRequest,
    ) -> ai_miao_bi_20230801_models.SaveMaterialDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_material_document_with_options(request, runtime)

    async def save_material_document_async(
        self,
        request: ai_miao_bi_20230801_models.SaveMaterialDocumentRequest,
    ) -> ai_miao_bi_20230801_models.SaveMaterialDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_material_document_with_options_async(request, runtime)

    def search_news_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SearchNewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SearchNewsResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SearchNewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.search_sources):
            request.search_sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.filter_not_null):
            body['FilterNotNull'] = request.filter_not_null
        if not UtilClient.is_unset(request.include_content):
            body['IncludeContent'] = request.include_content
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchNews',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SearchNewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_news_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SearchNewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SearchNewsResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SearchNewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.search_sources):
            request.search_sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.filter_not_null):
            body['FilterNotNull'] = request.filter_not_null
        if not UtilClient.is_unset(request.include_content):
            body['IncludeContent'] = request.include_content
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchNews',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SearchNewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_news(
        self,
        request: ai_miao_bi_20230801_models.SearchNewsRequest,
    ) -> ai_miao_bi_20230801_models.SearchNewsResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_news_with_options(request, runtime)

    async def search_news_async(
        self,
        request: ai_miao_bi_20230801_models.SearchNewsRequest,
    ) -> ai_miao_bi_20230801_models.SearchNewsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_news_with_options_async(request, runtime)

    def submit_async_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.SubmitAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitAsyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_code):
            body['TaskCode'] = request.task_code
        if not UtilClient.is_unset(request.task_execute_time):
            body['TaskExecuteTime'] = request.task_execute_time
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_param):
            body['TaskParam'] = request.task_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_async_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitAsyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.task_code):
            body['TaskCode'] = request.task_code
        if not UtilClient.is_unset(request.task_execute_time):
            body['TaskExecuteTime'] = request.task_execute_time
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_param):
            body['TaskParam'] = request.task_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitAsyncTask',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.SubmitAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_async_task(
        self,
        request: ai_miao_bi_20230801_models.SubmitAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_async_task_with_options(request, runtime)

    async def submit_async_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_async_task_with_options_async(request, runtime)

    def update_generated_content_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateGeneratedContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateGeneratedContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_text):
            body['ContentText'] = request.content_text
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_generated_content_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateGeneratedContentResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateGeneratedContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keywords):
            request.keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_text):
            body['ContentText'] = request.content_text
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGeneratedContent',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_generated_content(
        self,
        request: ai_miao_bi_20230801_models.UpdateGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateGeneratedContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_generated_content_with_options(request, runtime)

    async def update_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateGeneratedContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_generated_content_with_options_async(request, runtime)

    def update_material_document_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateMaterialDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateMaterialDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_keywords):
            request.doc_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.author):
            body['Author'] = request.author
        if not UtilClient.is_unset(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.html_content):
            body['HtmlContent'] = request.html_content
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.pub_time):
            body['PubTime'] = request.pub_time
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.src_from):
            body['SrcFrom'] = request.src_from
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.text_content):
            body['TextContent'] = request.text_content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMaterialDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_material_document_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateMaterialDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse:
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateMaterialDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_keywords):
            request.doc_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.author):
            body['Author'] = request.author
        if not UtilClient.is_unset(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.html_content):
            body['HtmlContent'] = request.html_content
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.pub_time):
            body['PubTime'] = request.pub_time
        if not UtilClient.is_unset(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not UtilClient.is_unset(request.src_from):
            body['SrcFrom'] = request.src_from
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.text_content):
            body['TextContent'] = request.text_content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMaterialDocument',
            version='2023-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_material_document(
        self,
        request: ai_miao_bi_20230801_models.UpdateMaterialDocumentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_material_document_with_options(request, runtime)

    async def update_material_document_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateMaterialDocumentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_material_document_with_options_async(request, runtime)
