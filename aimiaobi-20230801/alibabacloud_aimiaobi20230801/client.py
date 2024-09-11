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
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAsyncTaskResponse
        """
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
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAsyncTaskResponse
        """
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
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @return: CancelAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_async_task_with_options(request, runtime)

    async def cancel_async_task_async(
        self,
        request: ai_miao_bi_20230801_models.CancelAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.CancelAsyncTaskResponse:
        """
        @summary 取消异步任务
        
        @param request: CancelAsyncTaskRequest
        @return: CancelAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_async_task_with_options_async(request, runtime)

    def clear_intervenes_with_options(
        self,
        request: ai_miao_bi_20230801_models.ClearIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ClearIntervenesResponse:
        """
        @summary 清除所有干预内容
        
        @param request: ClearIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearIntervenesResponse
        """
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
        """
        @summary 清除所有干预内容
        
        @param request: ClearIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearIntervenesResponse
        """
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
        """
        @summary 清除所有干预内容
        
        @param request: ClearIntervenesRequest
        @return: ClearIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.clear_intervenes_with_options(request, runtime)

    async def clear_intervenes_async(
        self,
        request: ai_miao_bi_20230801_models.ClearIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ClearIntervenesResponse:
        """
        @summary 清除所有干预内容
        
        @param request: ClearIntervenesRequest
        @return: ClearIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.clear_intervenes_with_options_async(request, runtime)

    def create_generated_content_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.CreateGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateGeneratedContentResponse:
        """
        @summary 文档管理-创建
        
        @param tmp_req: CreateGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGeneratedContentResponse
        """
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
        """
        @summary 文档管理-创建
        
        @param tmp_req: CreateGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGeneratedContentResponse
        """
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
        """
        @summary 文档管理-创建
        
        @param request: CreateGeneratedContentRequest
        @return: CreateGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_generated_content_with_options(request, runtime)

    async def create_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.CreateGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.CreateGeneratedContentResponse:
        """
        @summary 文档管理-创建
        
        @param request: CreateGeneratedContentRequest
        @return: CreateGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_generated_content_with_options_async(request, runtime)

    def create_token_with_options(
        self,
        request: ai_miao_bi_20230801_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.CreateTokenResponse:
        """
        @summary 获取授权token
        
        @param request: CreateTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTokenResponse
        """
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
        """
        @summary 获取授权token
        
        @param request: CreateTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTokenResponse
        """
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
        """
        @summary 获取授权token
        
        @param request: CreateTokenRequest
        @return: CreateTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_token_with_options(request, runtime)

    async def create_token_async(
        self,
        request: ai_miao_bi_20230801_models.CreateTokenRequest,
    ) -> ai_miao_bi_20230801_models.CreateTokenResponse:
        """
        @summary 获取授权token
        
        @param request: CreateTokenRequest
        @return: CreateTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_token_with_options_async(request, runtime)

    def delete_custom_text_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTextResponse:
        """
        @summary 删除自定义文本
        
        @param request: DeleteCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomText',
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
            ai_miao_bi_20230801_models.DeleteCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_text_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTextResponse:
        """
        @summary 删除自定义文本
        
        @param request: DeleteCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomText',
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
            ai_miao_bi_20230801_models.DeleteCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_text(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTextResponse:
        """
        @summary 删除自定义文本
        
        @param request: DeleteCustomTextRequest
        @return: DeleteCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_text_with_options(request, runtime)

    async def delete_custom_text_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTextResponse:
        """
        @summary 删除自定义文本
        
        @param request: DeleteCustomTextRequest
        @return: DeleteCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_text_with_options_async(request, runtime)

    def delete_custom_topic_by_topic_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse:
        """
        @summary 根据主题删除自定义主题事件
        
        @param request: DeleteCustomTopicByTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTopicByTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomTopicByTopic',
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
            ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_topic_by_topic_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse:
        """
        @summary 根据主题删除自定义主题事件
        
        @param request: DeleteCustomTopicByTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTopicByTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomTopicByTopic',
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
            ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_topic_by_topic(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicByTopicRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse:
        """
        @summary 根据主题删除自定义主题事件
        
        @param request: DeleteCustomTopicByTopicRequest
        @return: DeleteCustomTopicByTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_topic_by_topic_with_options(request, runtime)

    async def delete_custom_topic_by_topic_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicByTopicRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicByTopicResponse:
        """
        @summary 根据主题删除自定义主题事件
        
        @param request: DeleteCustomTopicByTopicRequest
        @return: DeleteCustomTopicByTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_topic_by_topic_with_options_async(request, runtime)

    def delete_custom_topic_view_point_by_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse:
        """
        @summary 根据自定义观点ID删除自定义观点
        
        @param request: DeleteCustomTopicViewPointByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTopicViewPointByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomTopicViewPointById',
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
            ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_topic_view_point_by_id_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse:
        """
        @summary 根据自定义观点ID删除自定义观点
        
        @param request: DeleteCustomTopicViewPointByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomTopicViewPointByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomTopicViewPointById',
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
            ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_topic_view_point_by_id(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse:
        """
        @summary 根据自定义观点ID删除自定义观点
        
        @param request: DeleteCustomTopicViewPointByIdRequest
        @return: DeleteCustomTopicViewPointByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_topic_view_point_by_id_with_options(request, runtime)

    async def delete_custom_topic_view_point_by_id_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdRequest,
    ) -> ai_miao_bi_20230801_models.DeleteCustomTopicViewPointByIdResponse:
        """
        @summary 根据自定义观点ID删除自定义观点
        
        @param request: DeleteCustomTopicViewPointByIdRequest
        @return: DeleteCustomTopicViewPointByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_topic_view_point_by_id_with_options_async(request, runtime)

    def delete_generated_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteGeneratedContentResponse:
        """
        @summary 文档管理-删除。
        
        @param request: DeleteGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGeneratedContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        """
        @summary 文档管理-删除。
        
        @param request: DeleteGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGeneratedContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        """
        @summary 文档管理-删除。
        
        @param request: DeleteGeneratedContentRequest
        @return: DeleteGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_generated_content_with_options(request, runtime)

    async def delete_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.DeleteGeneratedContentResponse:
        """
        @summary 文档管理-删除。
        
        @param request: DeleteGeneratedContentRequest
        @return: DeleteGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_generated_content_with_options_async(request, runtime)

    def delete_intervene_rule_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteInterveneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteInterveneRuleResponse:
        """
        @summary 删除干预规则
        
        @param request: DeleteInterveneRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInterveneRuleResponse
        """
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
        """
        @summary 删除干预规则
        
        @param request: DeleteInterveneRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInterveneRuleResponse
        """
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
        """
        @summary 删除干预规则
        
        @param request: DeleteInterveneRuleRequest
        @return: DeleteInterveneRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_intervene_rule_with_options(request, runtime)

    async def delete_intervene_rule_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteInterveneRuleRequest,
    ) -> ai_miao_bi_20230801_models.DeleteInterveneRuleResponse:
        """
        @summary 删除干预规则
        
        @param request: DeleteInterveneRuleRequest
        @return: DeleteInterveneRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_intervene_rule_with_options_async(request, runtime)

    def delete_material_by_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.DeleteMaterialByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DeleteMaterialByIdResponse:
        """
        @summary 根据ID删除素材
        
        @param request: DeleteMaterialByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMaterialByIdResponse
        """
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
        """
        @summary 根据ID删除素材
        
        @param request: DeleteMaterialByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMaterialByIdResponse
        """
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
        """
        @summary 根据ID删除素材
        
        @param request: DeleteMaterialByIdRequest
        @return: DeleteMaterialByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_material_by_id_with_options(request, runtime)

    async def delete_material_by_id_async(
        self,
        request: ai_miao_bi_20230801_models.DeleteMaterialByIdRequest,
    ) -> ai_miao_bi_20230801_models.DeleteMaterialByIdResponse:
        """
        @summary 根据ID删除素材
        
        @param request: DeleteMaterialByIdRequest
        @return: DeleteMaterialByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_material_by_id_with_options_async(request, runtime)

    def document_extraction_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.DocumentExtractionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DocumentExtractionResponse:
        """
        @summary 从链接中提取文档内容
        
        @param tmp_req: DocumentExtractionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DocumentExtractionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.DocumentExtractionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.urls):
            request.urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.urls, 'Urls', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.urls_shrink):
            body['Urls'] = request.urls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DocumentExtraction',
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
            ai_miao_bi_20230801_models.DocumentExtractionResponse(),
            self.call_api(params, req, runtime)
        )

    async def document_extraction_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.DocumentExtractionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.DocumentExtractionResponse:
        """
        @summary 从链接中提取文档内容
        
        @param tmp_req: DocumentExtractionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DocumentExtractionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.DocumentExtractionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.urls):
            request.urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.urls, 'Urls', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.urls_shrink):
            body['Urls'] = request.urls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DocumentExtraction',
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
            ai_miao_bi_20230801_models.DocumentExtractionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def document_extraction(
        self,
        request: ai_miao_bi_20230801_models.DocumentExtractionRequest,
    ) -> ai_miao_bi_20230801_models.DocumentExtractionResponse:
        """
        @summary 从链接中提取文档内容
        
        @param request: DocumentExtractionRequest
        @return: DocumentExtractionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.document_extraction_with_options(request, runtime)

    async def document_extraction_async(
        self,
        request: ai_miao_bi_20230801_models.DocumentExtractionRequest,
    ) -> ai_miao_bi_20230801_models.DocumentExtractionResponse:
        """
        @summary 从链接中提取文档内容
        
        @param request: DocumentExtractionRequest
        @return: DocumentExtractionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.document_extraction_with_options_async(request, runtime)

    def export_generated_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.ExportGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportGeneratedContentResponse:
        """
        @summary 文档管理-导出。
        
        @param request: ExportGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportGeneratedContentResponse
        """
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
        """
        @summary 文档管理-导出。
        
        @param request: ExportGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportGeneratedContentResponse
        """
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
        """
        @summary 文档管理-导出。
        
        @param request: ExportGeneratedContentRequest
        @return: ExportGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_generated_content_with_options(request, runtime)

    async def export_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.ExportGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.ExportGeneratedContentResponse:
        """
        @summary 文档管理-导出。
        
        @param request: ExportGeneratedContentRequest
        @return: ExportGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_generated_content_with_options_async(request, runtime)

    def export_hot_topic_planning_proposals_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse:
        """
        @summary 导出选题策划文档，响应为一个可公开访问的URL。一小时后失效
        
        @param tmp_req: ExportHotTopicPlanningProposalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportHotTopicPlanningProposalsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not UtilClient.is_unset(tmp_req.titles):
            request.titles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.export_type):
            body['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportHotTopicPlanningProposals',
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
            ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_hot_topic_planning_proposals_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse:
        """
        @summary 导出选题策划文档，响应为一个可公开访问的URL。一小时后失效
        
        @param tmp_req: ExportHotTopicPlanningProposalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportHotTopicPlanningProposalsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not UtilClient.is_unset(tmp_req.titles):
            request.titles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.export_type):
            body['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportHotTopicPlanningProposals',
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
            ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_hot_topic_planning_proposals(
        self,
        request: ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsRequest,
    ) -> ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse:
        """
        @summary 导出选题策划文档，响应为一个可公开访问的URL。一小时后失效
        
        @param request: ExportHotTopicPlanningProposalsRequest
        @return: ExportHotTopicPlanningProposalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_hot_topic_planning_proposals_with_options(request, runtime)

    async def export_hot_topic_planning_proposals_async(
        self,
        request: ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsRequest,
    ) -> ai_miao_bi_20230801_models.ExportHotTopicPlanningProposalsResponse:
        """
        @summary 导出选题策划文档，响应为一个可公开访问的URL。一小时后失效
        
        @param request: ExportHotTopicPlanningProposalsRequest
        @return: ExportHotTopicPlanningProposalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_hot_topic_planning_proposals_with_options_async(request, runtime)

    def export_intervenes_with_options(
        self,
        request: ai_miao_bi_20230801_models.ExportIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ExportIntervenesResponse:
        """
        @summary 导出所有干预内容
        
        @param request: ExportIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportIntervenesResponse
        """
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
        """
        @summary 导出所有干预内容
        
        @param request: ExportIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportIntervenesResponse
        """
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
        """
        @summary 导出所有干预内容
        
        @param request: ExportIntervenesRequest
        @return: ExportIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_intervenes_with_options(request, runtime)

    async def export_intervenes_async(
        self,
        request: ai_miao_bi_20230801_models.ExportIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ExportIntervenesResponse:
        """
        @summary 导出所有干预内容
        
        @param request: ExportIntervenesRequest
        @return: ExportIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_intervenes_with_options_async(request, runtime)

    def feedback_dialogue_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.FeedbackDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.FeedbackDialogueResponse:
        """
        @summary 反馈某次生成的结果
        
        @param tmp_req: FeedbackDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FeedbackDialogueResponse
        """
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
        """
        @summary 反馈某次生成的结果
        
        @param tmp_req: FeedbackDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FeedbackDialogueResponse
        """
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
        """
        @summary 反馈某次生成的结果
        
        @param request: FeedbackDialogueRequest
        @return: FeedbackDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.feedback_dialogue_with_options(request, runtime)

    async def feedback_dialogue_async(
        self,
        request: ai_miao_bi_20230801_models.FeedbackDialogueRequest,
    ) -> ai_miao_bi_20230801_models.FeedbackDialogueResponse:
        """
        @summary 反馈某次生成的结果
        
        @param request: FeedbackDialogueRequest
        @return: FeedbackDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.feedback_dialogue_with_options_async(request, runtime)

    def fetch_image_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.FetchImageTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.FetchImageTaskResponse:
        """
        @summary 获取图片任务执行结果
        
        @param tmp_req: FetchImageTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchImageTaskResponse
        """
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
        """
        @summary 获取图片任务执行结果
        
        @param tmp_req: FetchImageTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchImageTaskResponse
        """
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
        """
        @summary 获取图片任务执行结果
        
        @param request: FetchImageTaskRequest
        @return: FetchImageTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fetch_image_task_with_options(request, runtime)

    async def fetch_image_task_async(
        self,
        request: ai_miao_bi_20230801_models.FetchImageTaskRequest,
    ) -> ai_miao_bi_20230801_models.FetchImageTaskResponse:
        """
        @summary 获取图片任务执行结果
        
        @param request: FetchImageTaskRequest
        @return: FetchImageTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fetch_image_task_with_options_async(request, runtime)

    def generate_file_url_by_key_with_options(
        self,
        request: ai_miao_bi_20230801_models.GenerateFileUrlByKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse:
        """
        @summary 生成临时可访问的公开url
        
        @param request: GenerateFileUrlByKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateFileUrlByKeyResponse
        """
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
        """
        @summary 生成临时可访问的公开url
        
        @param request: GenerateFileUrlByKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateFileUrlByKeyResponse
        """
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
        """
        @summary 生成临时可访问的公开url
        
        @param request: GenerateFileUrlByKeyRequest
        @return: GenerateFileUrlByKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_file_url_by_key_with_options(request, runtime)

    async def generate_file_url_by_key_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateFileUrlByKeyRequest,
    ) -> ai_miao_bi_20230801_models.GenerateFileUrlByKeyResponse:
        """
        @summary 生成临时可访问的公开url
        
        @param request: GenerateFileUrlByKeyRequest
        @return: GenerateFileUrlByKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_file_url_by_key_with_options_async(request, runtime)

    def generate_image_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.GenerateImageTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateImageTaskResponse:
        """
        @summary 智能配图，图片生成任务
        
        @param tmp_req: GenerateImageTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateImageTaskResponse
        """
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
        """
        @summary 智能配图，图片生成任务
        
        @param tmp_req: GenerateImageTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateImageTaskResponse
        """
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
        """
        @summary 智能配图，图片生成任务
        
        @param request: GenerateImageTaskRequest
        @return: GenerateImageTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_image_task_with_options(request, runtime)

    async def generate_image_task_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateImageTaskRequest,
    ) -> ai_miao_bi_20230801_models.GenerateImageTaskResponse:
        """
        @summary 智能配图，图片生成任务
        
        @param request: GenerateImageTaskRequest
        @return: GenerateImageTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_image_task_with_options_async(request, runtime)

    def generate_upload_config_with_options(
        self,
        request: ai_miao_bi_20230801_models.GenerateUploadConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateUploadConfigResponse:
        """
        @summary 生成上传配置
        
        @param request: GenerateUploadConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUploadConfigResponse
        """
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
        """
        @summary 生成上传配置
        
        @param request: GenerateUploadConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUploadConfigResponse
        """
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
        """
        @summary 生成上传配置
        
        @param request: GenerateUploadConfigRequest
        @return: GenerateUploadConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_config_with_options(request, runtime)

    async def generate_upload_config_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateUploadConfigRequest,
    ) -> ai_miao_bi_20230801_models.GenerateUploadConfigResponse:
        """
        @summary 生成上传配置
        
        @param request: GenerateUploadConfigRequest
        @return: GenerateUploadConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_upload_config_with_options_async(request, runtime)

    def generate_view_point_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.GenerateViewPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GenerateViewPointResponse:
        """
        @summary 视角生成
        
        @param tmp_req: GenerateViewPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateViewPointResponse
        """
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
        """
        @summary 视角生成
        
        @param tmp_req: GenerateViewPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateViewPointResponse
        """
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
        """
        @summary 视角生成
        
        @param request: GenerateViewPointRequest
        @return: GenerateViewPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_view_point_with_options(request, runtime)

    async def generate_view_point_async(
        self,
        request: ai_miao_bi_20230801_models.GenerateViewPointRequest,
    ) -> ai_miao_bi_20230801_models.GenerateViewPointResponse:
        """
        @summary 视角生成
        
        @param request: GenerateViewPointRequest
        @return: GenerateViewPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_view_point_with_options_async(request, runtime)

    def get_custom_text_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCustomTextResponse:
        """
        @summary 获取自定义文本
        
        @param request: GetCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCustomText',
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
            ai_miao_bi_20230801_models.GetCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_text_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCustomTextResponse:
        """
        @summary 获取自定义文本
        
        @param request: GetCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCustomText',
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
            ai_miao_bi_20230801_models.GetCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_text(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.GetCustomTextResponse:
        """
        @summary 获取自定义文本
        
        @param request: GetCustomTextRequest
        @return: GetCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_custom_text_with_options(request, runtime)

    async def get_custom_text_async(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.GetCustomTextResponse:
        """
        @summary 获取自定义文本
        
        @param request: GetCustomTextRequest
        @return: GetCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_text_with_options_async(request, runtime)

    def get_custom_topic_selection_perspective_analysis_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取自定义选题视角分析任务结果
        
        @param request: GetCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
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
            action='GetCustomTopicSelectionPerspectiveAnalysisTask',
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
            ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_topic_selection_perspective_analysis_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取自定义选题视角分析任务结果
        
        @param request: GetCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
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
            action='GetCustomTopicSelectionPerspectiveAnalysisTask',
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
            ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_topic_selection_perspective_analysis_task(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取自定义选题视角分析任务结果
        
        @param request: GetCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @return: GetCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_custom_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def get_custom_topic_selection_perspective_analysis_task_async(
        self,
        request: ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取自定义选题视角分析任务结果
        
        @param request: GetCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @return: GetCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def get_data_source_order_config_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetDataSourceOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse:
        """
        @summary 获取系统数据源配置和个人配置
        
        @param request: GetDataSourceOrderConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataSourceOrderConfigResponse
        """
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
        """
        @summary 获取系统数据源配置和个人配置
        
        @param request: GetDataSourceOrderConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataSourceOrderConfigResponse
        """
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
        """
        @summary 获取系统数据源配置和个人配置
        
        @param request: GetDataSourceOrderConfigRequest
        @return: GetDataSourceOrderConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_order_config_with_options(request, runtime)

    async def get_data_source_order_config_async(
        self,
        request: ai_miao_bi_20230801_models.GetDataSourceOrderConfigRequest,
    ) -> ai_miao_bi_20230801_models.GetDataSourceOrderConfigResponse:
        """
        @summary 获取系统数据源配置和个人配置
        
        @param request: GetDataSourceOrderConfigRequest
        @return: GetDataSourceOrderConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_source_order_config_with_options_async(request, runtime)

    def get_doc_cluster_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetDocClusterTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDocClusterTaskResponse:
        """
        @summary 获取文档聚合任务结果
        
        @param request: GetDocClusterTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocClusterTaskResponse
        """
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
            action='GetDocClusterTask',
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
            ai_miao_bi_20230801_models.GetDocClusterTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_cluster_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetDocClusterTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetDocClusterTaskResponse:
        """
        @summary 获取文档聚合任务结果
        
        @param request: GetDocClusterTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocClusterTaskResponse
        """
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
            action='GetDocClusterTask',
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
            ai_miao_bi_20230801_models.GetDocClusterTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_cluster_task(
        self,
        request: ai_miao_bi_20230801_models.GetDocClusterTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetDocClusterTaskResponse:
        """
        @summary 获取文档聚合任务结果
        
        @param request: GetDocClusterTaskRequest
        @return: GetDocClusterTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doc_cluster_task_with_options(request, runtime)

    async def get_doc_cluster_task_async(
        self,
        request: ai_miao_bi_20230801_models.GetDocClusterTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetDocClusterTaskResponse:
        """
        @summary 获取文档聚合任务结果
        
        @param request: GetDocClusterTaskRequest
        @return: GetDocClusterTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doc_cluster_task_with_options_async(request, runtime)

    def get_generated_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetGeneratedContentResponse:
        """
        @summary 文档管理-查询详情。
        
        @param request: GetGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGeneratedContentResponse
        """
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
        """
        @summary 文档管理-查询详情。
        
        @param request: GetGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGeneratedContentResponse
        """
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
        """
        @summary 文档管理-查询详情。
        
        @param request: GetGeneratedContentRequest
        @return: GetGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_generated_content_with_options(request, runtime)

    async def get_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.GetGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.GetGeneratedContentResponse:
        """
        @summary 文档管理-查询详情。
        
        @param request: GetGeneratedContentRequest
        @return: GetGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_generated_content_with_options_async(request, runtime)

    def get_intervene_global_reply_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneGlobalReplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse:
        """
        @summary 获得干预全局回复
        
        @param request: GetInterveneGlobalReplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneGlobalReplyResponse
        """
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
        """
        @summary 获得干预全局回复
        
        @param request: GetInterveneGlobalReplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneGlobalReplyResponse
        """
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
        """
        @summary 获得干预全局回复
        
        @param request: GetInterveneGlobalReplyRequest
        @return: GetInterveneGlobalReplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_global_reply_with_options(request, runtime)

    async def get_intervene_global_reply_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneGlobalReplyRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneGlobalReplyResponse:
        """
        @summary 获得干预全局回复
        
        @param request: GetInterveneGlobalReplyRequest
        @return: GetInterveneGlobalReplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_global_reply_with_options_async(request, runtime)

    def get_intervene_import_task_info_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneImportTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse:
        """
        @summary 获得导入任务信息
        
        @param request: GetInterveneImportTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneImportTaskInfoResponse
        """
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
        """
        @summary 获得导入任务信息
        
        @param request: GetInterveneImportTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneImportTaskInfoResponse
        """
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
        """
        @summary 获得导入任务信息
        
        @param request: GetInterveneImportTaskInfoRequest
        @return: GetInterveneImportTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_import_task_info_with_options(request, runtime)

    async def get_intervene_import_task_info_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneImportTaskInfoRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneImportTaskInfoResponse:
        """
        @summary 获得导入任务信息
        
        @param request: GetInterveneImportTaskInfoRequest
        @return: GetInterveneImportTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_import_task_info_with_options_async(request, runtime)

    def get_intervene_rule_detail_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse:
        """
        @summary 获得干预项规则详情
        
        @param request: GetInterveneRuleDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneRuleDetailResponse
        """
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
        """
        @summary 获得干预项规则详情
        
        @param request: GetInterveneRuleDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneRuleDetailResponse
        """
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
        """
        @summary 获得干预项规则详情
        
        @param request: GetInterveneRuleDetailRequest
        @return: GetInterveneRuleDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_rule_detail_with_options(request, runtime)

    async def get_intervene_rule_detail_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneRuleDetailRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneRuleDetailResponse:
        """
        @summary 获得干预项规则详情
        
        @param request: GetInterveneRuleDetailRequest
        @return: GetInterveneRuleDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_rule_detail_with_options_async(request, runtime)

    def get_intervene_template_file_url_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse:
        """
        @summary 获得干预导入模版文件下载地址
        
        @param request: GetInterveneTemplateFileUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneTemplateFileUrlResponse
        """
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
        """
        @summary 获得干预导入模版文件下载地址
        
        @param request: GetInterveneTemplateFileUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInterveneTemplateFileUrlResponse
        """
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
        """
        @summary 获得干预导入模版文件下载地址
        
        @param request: GetInterveneTemplateFileUrlRequest
        @return: GetInterveneTemplateFileUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_intervene_template_file_url_with_options(request, runtime)

    async def get_intervene_template_file_url_async(
        self,
        request: ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlRequest,
    ) -> ai_miao_bi_20230801_models.GetInterveneTemplateFileUrlResponse:
        """
        @summary 获得干预导入模版文件下载地址
        
        @param request: GetInterveneTemplateFileUrlRequest
        @return: GetInterveneTemplateFileUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_intervene_template_file_url_with_options_async(request, runtime)

    def get_material_by_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetMaterialByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetMaterialByIdResponse:
        """
        @summary 根据ID获取素材内容
        
        @param request: GetMaterialByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMaterialByIdResponse
        """
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
        """
        @summary 根据ID获取素材内容
        
        @param request: GetMaterialByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMaterialByIdResponse
        """
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
        """
        @summary 根据ID获取素材内容
        
        @param request: GetMaterialByIdRequest
        @return: GetMaterialByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_material_by_id_with_options(request, runtime)

    async def get_material_by_id_async(
        self,
        request: ai_miao_bi_20230801_models.GetMaterialByIdRequest,
    ) -> ai_miao_bi_20230801_models.GetMaterialByIdResponse:
        """
        @summary 根据ID获取素材内容
        
        @param request: GetMaterialByIdRequest
        @return: GetMaterialByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_material_by_id_with_options_async(request, runtime)

    def get_properties_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetPropertiesResponse:
        """
        @summary 获取当前用户的配置
        
        @param request: GetPropertiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPropertiesResponse
        """
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
        """
        @summary 获取当前用户的配置
        
        @param request: GetPropertiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPropertiesResponse
        """
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
        """
        @summary 获取当前用户的配置
        
        @param request: GetPropertiesRequest
        @return: GetPropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_properties_with_options(request, runtime)

    async def get_properties_async(
        self,
        request: ai_miao_bi_20230801_models.GetPropertiesRequest,
    ) -> ai_miao_bi_20230801_models.GetPropertiesResponse:
        """
        @summary 获取当前用户的配置
        
        @param request: GetPropertiesRequest
        @return: GetPropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_properties_with_options_async(request, runtime)

    def get_topic_by_id_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetTopicByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetTopicByIdResponse:
        """
        @summary 根据ID获取热点事件信息
        
        @param request: GetTopicByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicByIdResponse
        """
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
            action='GetTopicById',
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
            ai_miao_bi_20230801_models.GetTopicByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_by_id_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetTopicByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetTopicByIdResponse:
        """
        @summary 根据ID获取热点事件信息
        
        @param request: GetTopicByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicByIdResponse
        """
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
            action='GetTopicById',
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
            ai_miao_bi_20230801_models.GetTopicByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_by_id(
        self,
        request: ai_miao_bi_20230801_models.GetTopicByIdRequest,
    ) -> ai_miao_bi_20230801_models.GetTopicByIdResponse:
        """
        @summary 根据ID获取热点事件信息
        
        @param request: GetTopicByIdRequest
        @return: GetTopicByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_by_id_with_options(request, runtime)

    async def get_topic_by_id_async(
        self,
        request: ai_miao_bi_20230801_models.GetTopicByIdRequest,
    ) -> ai_miao_bi_20230801_models.GetTopicByIdResponse:
        """
        @summary 根据ID获取热点事件信息
        
        @param request: GetTopicByIdRequest
        @return: GetTopicByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_by_id_with_options_async(request, runtime)

    def get_topic_selection_perspective_analysis_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取选题视角分析任务结果
        
        @param request: GetTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicSelectionPerspectiveAnalysisTaskResponse
        """
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
            action='GetTopicSelectionPerspectiveAnalysisTask',
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
            ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_selection_perspective_analysis_task_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取选题视角分析任务结果
        
        @param request: GetTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicSelectionPerspectiveAnalysisTaskResponse
        """
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
            action='GetTopicSelectionPerspectiveAnalysisTask',
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
            ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_selection_perspective_analysis_task(
        self,
        request: ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取选题视角分析任务结果
        
        @param request: GetTopicSelectionPerspectiveAnalysisTaskRequest
        @return: GetTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def get_topic_selection_perspective_analysis_task_async(
        self,
        request: ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 获取选题视角分析任务结果
        
        @param request: GetTopicSelectionPerspectiveAnalysisTaskRequest
        @return: GetTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def import_intervene_file_with_options(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileResponse:
        """
        @summary 导入干预文件
        
        @param request: ImportInterveneFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportInterveneFileResponse
        """
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
        """
        @summary 导入干预文件
        
        @param request: ImportInterveneFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportInterveneFileResponse
        """
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
        """
        @summary 导入干预文件
        
        @param request: ImportInterveneFileRequest
        @return: ImportInterveneFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_intervene_file_with_options(request, runtime)

    async def import_intervene_file_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileRequest,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileResponse:
        """
        @summary 导入干预文件
        
        @param request: ImportInterveneFileRequest
        @return: ImportInterveneFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_intervene_file_with_options_async(request, runtime)

    def import_intervene_file_async_with_options(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse:
        """
        @summary 异步导入干预文件
        
        @param request: ImportInterveneFileAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportInterveneFileAsyncResponse
        """
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
        """
        @summary 异步导入干预文件
        
        @param request: ImportInterveneFileAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportInterveneFileAsyncResponse
        """
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
        """
        @summary 异步导入干预文件
        
        @param request: ImportInterveneFileAsyncRequest
        @return: ImportInterveneFileAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_intervene_file_async_with_options(request, runtime)

    async def import_intervene_file_async_async(
        self,
        request: ai_miao_bi_20230801_models.ImportInterveneFileAsyncRequest,
    ) -> ai_miao_bi_20230801_models.ImportInterveneFileAsyncResponse:
        """
        @summary 异步导入干预文件
        
        @param request: ImportInterveneFileAsyncRequest
        @return: ImportInterveneFileAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_intervene_file_async_with_options_async(request, runtime)

    def insert_intervene_global_reply_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.InsertInterveneGlobalReplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse:
        """
        @summary 设置干预全局回复
        
        @param tmp_req: InsertInterveneGlobalReplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertInterveneGlobalReplyResponse
        """
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
        """
        @summary 设置干预全局回复
        
        @param tmp_req: InsertInterveneGlobalReplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertInterveneGlobalReplyResponse
        """
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
        """
        @summary 设置干预全局回复
        
        @param request: InsertInterveneGlobalReplyRequest
        @return: InsertInterveneGlobalReplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.insert_intervene_global_reply_with_options(request, runtime)

    async def insert_intervene_global_reply_async(
        self,
        request: ai_miao_bi_20230801_models.InsertInterveneGlobalReplyRequest,
    ) -> ai_miao_bi_20230801_models.InsertInterveneGlobalReplyResponse:
        """
        @summary 设置干预全局回复
        
        @param request: InsertInterveneGlobalReplyRequest
        @return: InsertInterveneGlobalReplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.insert_intervene_global_reply_with_options_async(request, runtime)

    def insert_intervene_rule_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.InsertInterveneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.InsertInterveneRuleResponse:
        """
        @summary 插入干预规则
        
        @param tmp_req: InsertInterveneRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertInterveneRuleResponse
        """
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
        """
        @summary 插入干预规则
        
        @param tmp_req: InsertInterveneRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertInterveneRuleResponse
        """
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
        """
        @summary 插入干预规则
        
        @param request: InsertInterveneRuleRequest
        @return: InsertInterveneRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.insert_intervene_rule_with_options(request, runtime)

    async def insert_intervene_rule_async(
        self,
        request: ai_miao_bi_20230801_models.InsertInterveneRuleRequest,
    ) -> ai_miao_bi_20230801_models.InsertInterveneRuleResponse:
        """
        @summary 插入干预规则
        
        @param request: InsertInterveneRuleRequest
        @return: InsertInterveneRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.insert_intervene_rule_with_options_async(request, runtime)

    def list_async_tasks_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListAsyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListAsyncTasksResponse:
        """
        @summary 查询任务列表
        
        @param tmp_req: ListAsyncTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsyncTasksResponse
        """
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
        """
        @summary 查询任务列表
        
        @param tmp_req: ListAsyncTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsyncTasksResponse
        """
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
        """
        @summary 查询任务列表
        
        @param request: ListAsyncTasksRequest
        @return: ListAsyncTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_async_tasks_with_options(request, runtime)

    async def list_async_tasks_async(
        self,
        request: ai_miao_bi_20230801_models.ListAsyncTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListAsyncTasksResponse:
        """
        @summary 查询任务列表
        
        @param request: ListAsyncTasksRequest
        @return: ListAsyncTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_async_tasks_with_options_async(request, runtime)

    def list_build_configs_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListBuildConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListBuildConfigsResponse:
        """
        @summary 获取系统自定义预设
        
        @param request: ListBuildConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBuildConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        """
        @summary 获取系统自定义预设
        
        @param request: ListBuildConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBuildConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        """
        @summary 获取系统自定义预设
        
        @param request: ListBuildConfigsRequest
        @return: ListBuildConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_build_configs_with_options(request, runtime)

    async def list_build_configs_async(
        self,
        request: ai_miao_bi_20230801_models.ListBuildConfigsRequest,
    ) -> ai_miao_bi_20230801_models.ListBuildConfigsResponse:
        """
        @summary 获取系统自定义预设
        
        @param request: ListBuildConfigsRequest
        @return: ListBuildConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_build_configs_with_options_async(request, runtime)

    def list_custom_text_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListCustomTextResponse:
        """
        @summary 自定义文本列表
        
        @param request: ListCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomText',
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
            ai_miao_bi_20230801_models.ListCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_text_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListCustomTextResponse:
        """
        @summary 自定义文本列表
        
        @param request: ListCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomText',
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
            ai_miao_bi_20230801_models.ListCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_text(
        self,
        request: ai_miao_bi_20230801_models.ListCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.ListCustomTextResponse:
        """
        @summary 自定义文本列表
        
        @param request: ListCustomTextRequest
        @return: ListCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_text_with_options(request, runtime)

    async def list_custom_text_async(
        self,
        request: ai_miao_bi_20230801_models.ListCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.ListCustomTextResponse:
        """
        @summary 自定义文本列表
        
        @param request: ListCustomTextRequest
        @return: ListCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_text_with_options_async(request, runtime)

    def list_custom_view_points_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListCustomViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListCustomViewPointsResponse:
        """
        @summary 自定义视角列表
        
        @param tmp_req: ListCustomViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomViewPointsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListCustomViewPointsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attitudes):
            request.attitudes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attitudes, 'Attitudes', 'json')
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.attitude):
            body['Attitude'] = request.attitude
        if not UtilClient.is_unset(request.attitudes_shrink):
            body['Attitudes'] = request.attitudes_shrink
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomViewPoints',
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
            ai_miao_bi_20230801_models.ListCustomViewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_view_points_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListCustomViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListCustomViewPointsResponse:
        """
        @summary 自定义视角列表
        
        @param tmp_req: ListCustomViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomViewPointsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListCustomViewPointsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attitudes):
            request.attitudes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attitudes, 'Attitudes', 'json')
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.attitude):
            body['Attitude'] = request.attitude
        if not UtilClient.is_unset(request.attitudes_shrink):
            body['Attitudes'] = request.attitudes_shrink
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomViewPoints',
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
            ai_miao_bi_20230801_models.ListCustomViewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_view_points(
        self,
        request: ai_miao_bi_20230801_models.ListCustomViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListCustomViewPointsResponse:
        """
        @summary 自定义视角列表
        
        @param request: ListCustomViewPointsRequest
        @return: ListCustomViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_view_points_with_options(request, runtime)

    async def list_custom_view_points_async(
        self,
        request: ai_miao_bi_20230801_models.ListCustomViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListCustomViewPointsResponse:
        """
        @summary 自定义视角列表
        
        @param request: ListCustomViewPointsRequest
        @return: ListCustomViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_view_points_with_options_async(request, runtime)

    def list_dialogues_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListDialoguesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListDialoguesResponse:
        """
        @summary 生成历史列表
        
        @param request: ListDialoguesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDialoguesResponse
        """
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
        """
        @summary 生成历史列表
        
        @param request: ListDialoguesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDialoguesResponse
        """
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
        """
        @summary 生成历史列表
        
        @param request: ListDialoguesRequest
        @return: ListDialoguesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dialogues_with_options(request, runtime)

    async def list_dialogues_async(
        self,
        request: ai_miao_bi_20230801_models.ListDialoguesRequest,
    ) -> ai_miao_bi_20230801_models.ListDialoguesResponse:
        """
        @summary 生成历史列表
        
        @param request: ListDialoguesRequest
        @return: ListDialoguesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dialogues_with_options_async(request, runtime)

    def list_fresh_view_points_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListFreshViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListFreshViewPointsResponse:
        """
        @summary 新颖视角列表
        
        @param request: ListFreshViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFreshViewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFreshViewPoints',
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
            ai_miao_bi_20230801_models.ListFreshViewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fresh_view_points_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListFreshViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListFreshViewPointsResponse:
        """
        @summary 新颖视角列表
        
        @param request: ListFreshViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFreshViewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFreshViewPoints',
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
            ai_miao_bi_20230801_models.ListFreshViewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fresh_view_points(
        self,
        request: ai_miao_bi_20230801_models.ListFreshViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListFreshViewPointsResponse:
        """
        @summary 新颖视角列表
        
        @param request: ListFreshViewPointsRequest
        @return: ListFreshViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fresh_view_points_with_options(request, runtime)

    async def list_fresh_view_points_async(
        self,
        request: ai_miao_bi_20230801_models.ListFreshViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListFreshViewPointsResponse:
        """
        @summary 新颖视角列表
        
        @param request: ListFreshViewPointsRequest
        @return: ListFreshViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fresh_view_points_with_options_async(request, runtime)

    def list_generated_contents_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListGeneratedContentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListGeneratedContentsResponse:
        """
        @summary 文档管理-列表。
        
        @param request: ListGeneratedContentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGeneratedContentsResponse
        """
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
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
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
        """
        @summary 文档管理-列表。
        
        @param request: ListGeneratedContentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGeneratedContentsResponse
        """
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
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
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
        """
        @summary 文档管理-列表。
        
        @param request: ListGeneratedContentsRequest
        @return: ListGeneratedContentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_generated_contents_with_options(request, runtime)

    async def list_generated_contents_async(
        self,
        request: ai_miao_bi_20230801_models.ListGeneratedContentsRequest,
    ) -> ai_miao_bi_20230801_models.ListGeneratedContentsResponse:
        """
        @summary 文档管理-列表。
        
        @param request: ListGeneratedContentsRequest
        @return: ListGeneratedContentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_generated_contents_with_options_async(request, runtime)

    def list_hot_news_with_type_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListHotNewsWithTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse:
        """
        @summary 获取分类的热点新闻
        
        @param tmp_req: ListHotNewsWithTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotNewsWithTypeResponse
        """
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
        """
        @summary 获取分类的热点新闻
        
        @param tmp_req: ListHotNewsWithTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotNewsWithTypeResponse
        """
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
        """
        @summary 获取分类的热点新闻
        
        @param request: ListHotNewsWithTypeRequest
        @return: ListHotNewsWithTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hot_news_with_type_with_options(request, runtime)

    async def list_hot_news_with_type_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotNewsWithTypeRequest,
    ) -> ai_miao_bi_20230801_models.ListHotNewsWithTypeResponse:
        """
        @summary 获取分类的热点新闻
        
        @param request: ListHotNewsWithTypeRequest
        @return: ListHotNewsWithTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_news_with_type_with_options_async(request, runtime)

    def list_hot_sources_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListHotSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotSourcesResponse:
        """
        @summary 获取所有平台热榜源列表
        
        @param request: ListHotSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotSources',
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
            ai_miao_bi_20230801_models.ListHotSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_sources_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotSourcesResponse:
        """
        @summary 获取所有平台热榜源列表
        
        @param request: ListHotSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotSources',
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
            ai_miao_bi_20230801_models.ListHotSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_sources(
        self,
        request: ai_miao_bi_20230801_models.ListHotSourcesRequest,
    ) -> ai_miao_bi_20230801_models.ListHotSourcesResponse:
        """
        @summary 获取所有平台热榜源列表
        
        @param request: ListHotSourcesRequest
        @return: ListHotSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hot_sources_with_options(request, runtime)

    async def list_hot_sources_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotSourcesRequest,
    ) -> ai_miao_bi_20230801_models.ListHotSourcesResponse:
        """
        @summary 获取所有平台热榜源列表
        
        @param request: ListHotSourcesRequest
        @return: ListHotSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_sources_with_options_async(request, runtime)

    def list_hot_topics_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListHotTopicsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotTopicsResponse:
        """
        @summary 获取热点事件列表
        
        @param tmp_req: ListHotTopicsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotTopicsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListHotTopicsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.topic_ids):
            request.topic_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_ids, 'TopicIds', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic_ids_shrink):
            body['TopicIds'] = request.topic_ids_shrink
        if not UtilClient.is_unset(request.topic_query):
            body['TopicQuery'] = request.topic_query
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not UtilClient.is_unset(request.with_news):
            body['WithNews'] = request.with_news
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotTopics',
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
            ai_miao_bi_20230801_models.ListHotTopicsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_topics_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListHotTopicsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotTopicsResponse:
        """
        @summary 获取热点事件列表
        
        @param tmp_req: ListHotTopicsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotTopicsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListHotTopicsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.topic_ids):
            request.topic_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_ids, 'TopicIds', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic_ids_shrink):
            body['TopicIds'] = request.topic_ids_shrink
        if not UtilClient.is_unset(request.topic_query):
            body['TopicQuery'] = request.topic_query
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not UtilClient.is_unset(request.with_news):
            body['WithNews'] = request.with_news
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotTopics',
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
            ai_miao_bi_20230801_models.ListHotTopicsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_topics(
        self,
        request: ai_miao_bi_20230801_models.ListHotTopicsRequest,
    ) -> ai_miao_bi_20230801_models.ListHotTopicsResponse:
        """
        @summary 获取热点事件列表
        
        @param request: ListHotTopicsRequest
        @return: ListHotTopicsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hot_topics_with_options(request, runtime)

    async def list_hot_topics_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotTopicsRequest,
    ) -> ai_miao_bi_20230801_models.ListHotTopicsResponse:
        """
        @summary 获取热点事件列表
        
        @param request: ListHotTopicsRequest
        @return: ListHotTopicsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_topics_with_options_async(request, runtime)

    def list_hot_view_points_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListHotViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotViewPointsResponse:
        """
        @summary 热门视角列表
        
        @param request: ListHotViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotViewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotViewPoints',
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
            ai_miao_bi_20230801_models.ListHotViewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_view_points_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotViewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListHotViewPointsResponse:
        """
        @summary 热门视角列表
        
        @param request: ListHotViewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHotViewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotViewPoints',
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
            ai_miao_bi_20230801_models.ListHotViewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_view_points(
        self,
        request: ai_miao_bi_20230801_models.ListHotViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListHotViewPointsResponse:
        """
        @summary 热门视角列表
        
        @param request: ListHotViewPointsRequest
        @return: ListHotViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hot_view_points_with_options(request, runtime)

    async def list_hot_view_points_async(
        self,
        request: ai_miao_bi_20230801_models.ListHotViewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListHotViewPointsResponse:
        """
        @summary 热门视角列表
        
        @param request: ListHotViewPointsRequest
        @return: ListHotViewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_view_points_with_options_async(request, runtime)

    def list_intervene_cnt_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneCntRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneCntResponse:
        """
        @summary 获得干预项目数量列表
        
        @param request: ListInterveneCntRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneCntResponse
        """
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
        """
        @summary 获得干预项目数量列表
        
        @param request: ListInterveneCntRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneCntResponse
        """
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
        """
        @summary 获得干预项目数量列表
        
        @param request: ListInterveneCntRequest
        @return: ListInterveneCntResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intervene_cnt_with_options(request, runtime)

    async def list_intervene_cnt_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneCntRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneCntResponse:
        """
        @summary 获得干预项目数量列表
        
        @param request: ListInterveneCntRequest
        @return: ListInterveneCntResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intervene_cnt_with_options_async(request, runtime)

    def list_intervene_import_tasks_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneImportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneImportTasksResponse:
        """
        @summary 获得导入任务列表
        
        @param request: ListInterveneImportTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneImportTasksResponse
        """
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
        """
        @summary 获得导入任务列表
        
        @param request: ListInterveneImportTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneImportTasksResponse
        """
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
        """
        @summary 获得导入任务列表
        
        @param request: ListInterveneImportTasksRequest
        @return: ListInterveneImportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intervene_import_tasks_with_options(request, runtime)

    async def list_intervene_import_tasks_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneImportTasksRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneImportTasksResponse:
        """
        @summary 获得导入任务列表
        
        @param request: ListInterveneImportTasksRequest
        @return: ListInterveneImportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intervene_import_tasks_with_options_async(request, runtime)

    def list_intervene_rules_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListInterveneRulesResponse:
        """
        @summary 获得干预规则列表
        
        @param request: ListInterveneRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneRulesResponse
        """
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
        """
        @summary 获得干预规则列表
        
        @param request: ListInterveneRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterveneRulesResponse
        """
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
        """
        @summary 获得干预规则列表
        
        @param request: ListInterveneRulesRequest
        @return: ListInterveneRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intervene_rules_with_options(request, runtime)

    async def list_intervene_rules_async(
        self,
        request: ai_miao_bi_20230801_models.ListInterveneRulesRequest,
    ) -> ai_miao_bi_20230801_models.ListInterveneRulesResponse:
        """
        @summary 获得干预规则列表
        
        @param request: ListInterveneRulesRequest
        @return: ListInterveneRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intervene_rules_with_options_async(request, runtime)

    def list_intervenes_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListIntervenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListIntervenesResponse:
        """
        @summary 获得干预项列表
        
        @param request: ListIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervenesResponse
        """
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
        """
        @summary 获得干预项列表
        
        @param request: ListIntervenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntervenesResponse
        """
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
        """
        @summary 获得干预项列表
        
        @param request: ListIntervenesRequest
        @return: ListIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intervenes_with_options(request, runtime)

    async def list_intervenes_async(
        self,
        request: ai_miao_bi_20230801_models.ListIntervenesRequest,
    ) -> ai_miao_bi_20230801_models.ListIntervenesResponse:
        """
        @summary 获得干预项列表
        
        @param request: ListIntervenesRequest
        @return: ListIntervenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intervenes_with_options_async(request, runtime)

    def list_material_documents_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListMaterialDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListMaterialDocumentsResponse:
        """
        @summary 查询素材列表
        
        @param tmp_req: ListMaterialDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMaterialDocumentsResponse
        """
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
        """
        @summary 查询素材列表
        
        @param tmp_req: ListMaterialDocumentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMaterialDocumentsResponse
        """
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
        """
        @summary 查询素材列表
        
        @param request: ListMaterialDocumentsRequest
        @return: ListMaterialDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_material_documents_with_options(request, runtime)

    async def list_material_documents_async(
        self,
        request: ai_miao_bi_20230801_models.ListMaterialDocumentsRequest,
    ) -> ai_miao_bi_20230801_models.ListMaterialDocumentsResponse:
        """
        @summary 查询素材列表
        
        @param request: ListMaterialDocumentsRequest
        @return: ListMaterialDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_material_documents_with_options_async(request, runtime)

    def list_planning_proposal_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListPlanningProposalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListPlanningProposalResponse:
        """
        @summary 获取选题策划列表
        
        @param tmp_req: ListPlanningProposalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPlanningProposalResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListPlanningProposalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not UtilClient.is_unset(tmp_req.titles):
            request.titles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPlanningProposal',
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
            ai_miao_bi_20230801_models.ListPlanningProposalResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_planning_proposal_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.ListPlanningProposalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListPlanningProposalResponse:
        """
        @summary 获取选题策划列表
        
        @param tmp_req: ListPlanningProposalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPlanningProposalResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.ListPlanningProposalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not UtilClient.is_unset(tmp_req.titles):
            request.titles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not UtilClient.is_unset(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPlanningProposal',
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
            ai_miao_bi_20230801_models.ListPlanningProposalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_planning_proposal(
        self,
        request: ai_miao_bi_20230801_models.ListPlanningProposalRequest,
    ) -> ai_miao_bi_20230801_models.ListPlanningProposalResponse:
        """
        @summary 获取选题策划列表
        
        @param request: ListPlanningProposalRequest
        @return: ListPlanningProposalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_planning_proposal_with_options(request, runtime)

    async def list_planning_proposal_async(
        self,
        request: ai_miao_bi_20230801_models.ListPlanningProposalRequest,
    ) -> ai_miao_bi_20230801_models.ListPlanningProposalResponse:
        """
        @summary 获取选题策划列表
        
        @param request: ListPlanningProposalRequest
        @return: ListPlanningProposalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_planning_proposal_with_options_async(request, runtime)

    def list_timed_view_attitude_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListTimedViewAttitudeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse:
        """
        @summary 时效性视角列表
        
        @param request: ListTimedViewAttitudeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTimedViewAttitudeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTimedViewAttitude',
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
            ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_timed_view_attitude_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListTimedViewAttitudeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse:
        """
        @summary 时效性视角列表
        
        @param request: ListTimedViewAttitudeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTimedViewAttitudeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTimedViewAttitude',
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
            ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_timed_view_attitude(
        self,
        request: ai_miao_bi_20230801_models.ListTimedViewAttitudeRequest,
    ) -> ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse:
        """
        @summary 时效性视角列表
        
        @param request: ListTimedViewAttitudeRequest
        @return: ListTimedViewAttitudeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_timed_view_attitude_with_options(request, runtime)

    async def list_timed_view_attitude_async(
        self,
        request: ai_miao_bi_20230801_models.ListTimedViewAttitudeRequest,
    ) -> ai_miao_bi_20230801_models.ListTimedViewAttitudeResponse:
        """
        @summary 时效性视角列表
        
        @param request: ListTimedViewAttitudeRequest
        @return: ListTimedViewAttitudeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_timed_view_attitude_with_options_async(request, runtime)

    def list_topic_recommend_event_list_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListTopicRecommendEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse:
        """
        @summary 获取热点推荐事件
        
        @param request: ListTopicRecommendEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicRecommendEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTopicRecommendEventList',
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
            ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topic_recommend_event_list_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListTopicRecommendEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse:
        """
        @summary 获取热点推荐事件
        
        @param request: ListTopicRecommendEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicRecommendEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTopicRecommendEventList',
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
            ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topic_recommend_event_list(
        self,
        request: ai_miao_bi_20230801_models.ListTopicRecommendEventListRequest,
    ) -> ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse:
        """
        @summary 获取热点推荐事件
        
        @param request: ListTopicRecommendEventListRequest
        @return: ListTopicRecommendEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_topic_recommend_event_list_with_options(request, runtime)

    async def list_topic_recommend_event_list_async(
        self,
        request: ai_miao_bi_20230801_models.ListTopicRecommendEventListRequest,
    ) -> ai_miao_bi_20230801_models.ListTopicRecommendEventListResponse:
        """
        @summary 获取热点推荐事件
        
        @param request: ListTopicRecommendEventListRequest
        @return: ListTopicRecommendEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_topic_recommend_event_list_with_options_async(request, runtime)

    def list_topic_view_point_recommend_event_list_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse:
        """
        @summary 获取主题事件推荐观点列表
        
        @param request: ListTopicViewPointRecommendEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicViewPointRecommendEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTopicViewPointRecommendEventList',
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
            ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topic_view_point_recommend_event_list_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse:
        """
        @summary 获取主题事件推荐观点列表
        
        @param request: ListTopicViewPointRecommendEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicViewPointRecommendEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTopicViewPointRecommendEventList',
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
            ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topic_view_point_recommend_event_list(
        self,
        request: ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListRequest,
    ) -> ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse:
        """
        @summary 获取主题事件推荐观点列表
        
        @param request: ListTopicViewPointRecommendEventListRequest
        @return: ListTopicViewPointRecommendEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_topic_view_point_recommend_event_list_with_options(request, runtime)

    async def list_topic_view_point_recommend_event_list_async(
        self,
        request: ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListRequest,
    ) -> ai_miao_bi_20230801_models.ListTopicViewPointRecommendEventListResponse:
        """
        @summary 获取主题事件推荐观点列表
        
        @param request: ListTopicViewPointRecommendEventListRequest
        @return: ListTopicViewPointRecommendEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_topic_view_point_recommend_event_list_with_options_async(request, runtime)

    def list_versions_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListVersionsResponse:
        """
        @summary 获取系统所有实例信息
        
        @param request: ListVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVersionsResponse
        """
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
        """
        @summary 获取系统所有实例信息
        
        @param request: ListVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVersionsResponse
        """
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
        """
        @summary 获取系统所有实例信息
        
        @param request: ListVersionsRequest
        @return: ListVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_versions_with_options(request, runtime)

    async def list_versions_async(
        self,
        request: ai_miao_bi_20230801_models.ListVersionsRequest,
    ) -> ai_miao_bi_20230801_models.ListVersionsResponse:
        """
        @summary 获取系统所有实例信息
        
        @param request: ListVersionsRequest
        @return: ListVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_versions_with_options_async(request, runtime)

    def list_web_review_points_with_options(
        self,
        request: ai_miao_bi_20230801_models.ListWebReviewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListWebReviewPointsResponse:
        """
        @summary 网友视角列表
        
        @param request: ListWebReviewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebReviewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWebReviewPoints',
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
            ai_miao_bi_20230801_models.ListWebReviewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_review_points_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.ListWebReviewPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.ListWebReviewPointsResponse:
        """
        @summary 网友视角列表
        
        @param request: ListWebReviewPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebReviewPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWebReviewPoints',
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
            ai_miao_bi_20230801_models.ListWebReviewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_review_points(
        self,
        request: ai_miao_bi_20230801_models.ListWebReviewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListWebReviewPointsResponse:
        """
        @summary 网友视角列表
        
        @param request: ListWebReviewPointsRequest
        @return: ListWebReviewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_web_review_points_with_options(request, runtime)

    async def list_web_review_points_async(
        self,
        request: ai_miao_bi_20230801_models.ListWebReviewPointsRequest,
    ) -> ai_miao_bi_20230801_models.ListWebReviewPointsResponse:
        """
        @summary 网友视角列表
        
        @param request: ListWebReviewPointsRequest
        @return: ListWebReviewPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_web_review_points_with_options_async(request, runtime)

    def query_async_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.QueryAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.QueryAsyncTaskResponse:
        """
        @summary 根据taskId查询异步任务状态
        
        @param request: QueryAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAsyncTaskResponse
        """
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
        """
        @summary 根据taskId查询异步任务状态
        
        @param request: QueryAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAsyncTaskResponse
        """
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
        """
        @summary 根据taskId查询异步任务状态
        
        @param request: QueryAsyncTaskRequest
        @return: QueryAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_async_task_with_options(request, runtime)

    async def query_async_task_async(
        self,
        request: ai_miao_bi_20230801_models.QueryAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.QueryAsyncTaskResponse:
        """
        @summary 根据taskId查询异步任务状态
        
        @param request: QueryAsyncTaskRequest
        @return: QueryAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_async_task_with_options_async(request, runtime)

    def run_abbreviation_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunAbbreviationContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunAbbreviationContentResponse:
        """
        @summary 内容缩写
        
        @param request: RunAbbreviationContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunAbbreviationContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunAbbreviationContent',
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
            ai_miao_bi_20230801_models.RunAbbreviationContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_abbreviation_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunAbbreviationContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunAbbreviationContentResponse:
        """
        @summary 内容缩写
        
        @param request: RunAbbreviationContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunAbbreviationContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunAbbreviationContent',
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
            ai_miao_bi_20230801_models.RunAbbreviationContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_abbreviation_content(
        self,
        request: ai_miao_bi_20230801_models.RunAbbreviationContentRequest,
    ) -> ai_miao_bi_20230801_models.RunAbbreviationContentResponse:
        """
        @summary 内容缩写
        
        @param request: RunAbbreviationContentRequest
        @return: RunAbbreviationContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_abbreviation_content_with_options(request, runtime)

    async def run_abbreviation_content_async(
        self,
        request: ai_miao_bi_20230801_models.RunAbbreviationContentRequest,
    ) -> ai_miao_bi_20230801_models.RunAbbreviationContentResponse:
        """
        @summary 内容缩写
        
        @param request: RunAbbreviationContentRequest
        @return: RunAbbreviationContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_abbreviation_content_with_options_async(request, runtime)

    def run_continue_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunContinueContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunContinueContentResponse:
        """
        @summary 内容续写
        
        @param request: RunContinueContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunContinueContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunContinueContent',
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
            ai_miao_bi_20230801_models.RunContinueContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_continue_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunContinueContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunContinueContentResponse:
        """
        @summary 内容续写
        
        @param request: RunContinueContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunContinueContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunContinueContent',
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
            ai_miao_bi_20230801_models.RunContinueContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_continue_content(
        self,
        request: ai_miao_bi_20230801_models.RunContinueContentRequest,
    ) -> ai_miao_bi_20230801_models.RunContinueContentResponse:
        """
        @summary 内容续写
        
        @param request: RunContinueContentRequest
        @return: RunContinueContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_continue_content_with_options(request, runtime)

    async def run_continue_content_async(
        self,
        request: ai_miao_bi_20230801_models.RunContinueContentRequest,
    ) -> ai_miao_bi_20230801_models.RunContinueContentResponse:
        """
        @summary 内容续写
        
        @param request: RunContinueContentRequest
        @return: RunContinueContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_continue_content_with_options_async(request, runtime)

    def run_custom_hot_topic_analysis_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse:
        """
        @summary 自定义热点话题分析
        
        @param request: RunCustomHotTopicAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCustomHotTopicAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ask_user):
            body['AskUser'] = request.ask_user
        if not UtilClient.is_unset(request.force_analysis_exists_topic):
            body['ForceAnalysisExistsTopic'] = request.force_analysis_exists_topic
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.user_back):
            body['UserBack'] = request.user_back
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCustomHotTopicAnalysis',
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
            ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_custom_hot_topic_analysis_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse:
        """
        @summary 自定义热点话题分析
        
        @param request: RunCustomHotTopicAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCustomHotTopicAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ask_user):
            body['AskUser'] = request.ask_user
        if not UtilClient.is_unset(request.force_analysis_exists_topic):
            body['ForceAnalysisExistsTopic'] = request.force_analysis_exists_topic
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.user_back):
            body['UserBack'] = request.user_back
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCustomHotTopicAnalysis',
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
            ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_custom_hot_topic_analysis(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse:
        """
        @summary 自定义热点话题分析
        
        @param request: RunCustomHotTopicAnalysisRequest
        @return: RunCustomHotTopicAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_custom_hot_topic_analysis_with_options(request, runtime)

    async def run_custom_hot_topic_analysis_async(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicAnalysisResponse:
        """
        @summary 自定义热点话题分析
        
        @param request: RunCustomHotTopicAnalysisRequest
        @return: RunCustomHotTopicAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_custom_hot_topic_analysis_with_options_async(request, runtime)

    def run_custom_hot_topic_view_point_analysis_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse:
        """
        @summary 自定义选题视角分析
        
        @param request: RunCustomHotTopicViewPointAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCustomHotTopicViewPointAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ask_user):
            body['AskUser'] = request.ask_user
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.search_query):
            body['SearchQuery'] = request.search_query
        if not UtilClient.is_unset(request.skip_ask_user):
            body['SkipAskUser'] = request.skip_ask_user
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.user_back):
            body['UserBack'] = request.user_back
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCustomHotTopicViewPointAnalysis',
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
            ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_custom_hot_topic_view_point_analysis_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse:
        """
        @summary 自定义选题视角分析
        
        @param request: RunCustomHotTopicViewPointAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCustomHotTopicViewPointAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ask_user):
            body['AskUser'] = request.ask_user
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.search_query):
            body['SearchQuery'] = request.search_query
        if not UtilClient.is_unset(request.skip_ask_user):
            body['SkipAskUser'] = request.skip_ask_user
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_id):
            body['TopicId'] = request.topic_id
        if not UtilClient.is_unset(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not UtilClient.is_unset(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not UtilClient.is_unset(request.user_back):
            body['UserBack'] = request.user_back
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCustomHotTopicViewPointAnalysis',
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
            ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_custom_hot_topic_view_point_analysis(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse:
        """
        @summary 自定义选题视角分析
        
        @param request: RunCustomHotTopicViewPointAnalysisRequest
        @return: RunCustomHotTopicViewPointAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_custom_hot_topic_view_point_analysis_with_options(request, runtime)

    async def run_custom_hot_topic_view_point_analysis_async(
        self,
        request: ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunCustomHotTopicViewPointAnalysisResponse:
        """
        @summary 自定义选题视角分析
        
        @param request: RunCustomHotTopicViewPointAnalysisRequest
        @return: RunCustomHotTopicViewPointAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_custom_hot_topic_view_point_analysis_with_options_async(request, runtime)

    def run_expand_content_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunExpandContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunExpandContentResponse:
        """
        @summary 内容扩写
        
        @param request: RunExpandContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunExpandContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunExpandContent',
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
            ai_miao_bi_20230801_models.RunExpandContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_expand_content_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunExpandContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunExpandContentResponse:
        """
        @summary 内容扩写
        
        @param request: RunExpandContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunExpandContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunExpandContent',
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
            ai_miao_bi_20230801_models.RunExpandContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_expand_content(
        self,
        request: ai_miao_bi_20230801_models.RunExpandContentRequest,
    ) -> ai_miao_bi_20230801_models.RunExpandContentResponse:
        """
        @summary 内容扩写
        
        @param request: RunExpandContentRequest
        @return: RunExpandContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_expand_content_with_options(request, runtime)

    async def run_expand_content_async(
        self,
        request: ai_miao_bi_20230801_models.RunExpandContentRequest,
    ) -> ai_miao_bi_20230801_models.RunExpandContentResponse:
        """
        @summary 内容扩写
        
        @param request: RunExpandContentRequest
        @return: RunExpandContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_expand_content_with_options_async(request, runtime)

    def run_keywords_extraction_generation_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse:
        """
        @summary AI妙笔-创作-抽取关键词
        
        @param tmp_req: RunKeywordsExtractionGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunKeywordsExtractionGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunKeywordsExtractionGeneration',
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
            ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_keywords_extraction_generation_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse:
        """
        @summary AI妙笔-创作-抽取关键词
        
        @param tmp_req: RunKeywordsExtractionGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunKeywordsExtractionGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunKeywordsExtractionGeneration',
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
            ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_keywords_extraction_generation(
        self,
        request: ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse:
        """
        @summary AI妙笔-创作-抽取关键词
        
        @param request: RunKeywordsExtractionGenerationRequest
        @return: RunKeywordsExtractionGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_keywords_extraction_generation_with_options(request, runtime)

    async def run_keywords_extraction_generation_async(
        self,
        request: ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunKeywordsExtractionGenerationResponse:
        """
        @summary AI妙笔-创作-抽取关键词
        
        @param request: RunKeywordsExtractionGenerationRequest
        @return: RunKeywordsExtractionGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_keywords_extraction_generation_with_options_async(request, runtime)

    def run_step_by_step_writing_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunStepByStepWritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunStepByStepWritingResponse:
        """
        @summary 创作-分步骤写作
        
        @param tmp_req: RunStepByStepWritingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunStepByStepWritingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunStepByStepWritingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not UtilClient.is_unset(tmp_req.writing_config):
            request.writing_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunStepByStepWriting',
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
            ai_miao_bi_20230801_models.RunStepByStepWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_step_by_step_writing_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunStepByStepWritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunStepByStepWritingResponse:
        """
        @summary 创作-分步骤写作
        
        @param tmp_req: RunStepByStepWritingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunStepByStepWritingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunStepByStepWritingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not UtilClient.is_unset(tmp_req.writing_config):
            request.writing_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunStepByStepWriting',
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
            ai_miao_bi_20230801_models.RunStepByStepWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_step_by_step_writing(
        self,
        request: ai_miao_bi_20230801_models.RunStepByStepWritingRequest,
    ) -> ai_miao_bi_20230801_models.RunStepByStepWritingResponse:
        """
        @summary 创作-分步骤写作
        
        @param request: RunStepByStepWritingRequest
        @return: RunStepByStepWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_step_by_step_writing_with_options(request, runtime)

    async def run_step_by_step_writing_async(
        self,
        request: ai_miao_bi_20230801_models.RunStepByStepWritingRequest,
    ) -> ai_miao_bi_20230801_models.RunStepByStepWritingResponse:
        """
        @summary 创作-分步骤写作
        
        @param request: RunStepByStepWritingRequest
        @return: RunStepByStepWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_step_by_step_writing_with_options_async(request, runtime)

    def run_style_feature_analysis_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunStyleFeatureAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse:
        """
        @summary 内容特点分析
        
        @param tmp_req: RunStyleFeatureAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunStyleFeatureAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunStyleFeatureAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.material_ids):
            request.material_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.material_ids, 'MaterialIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.material_ids_shrink):
            body['MaterialIds'] = request.material_ids_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunStyleFeatureAnalysis',
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
            ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_style_feature_analysis_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunStyleFeatureAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse:
        """
        @summary 内容特点分析
        
        @param tmp_req: RunStyleFeatureAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunStyleFeatureAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunStyleFeatureAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.material_ids):
            request.material_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.material_ids, 'MaterialIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.material_ids_shrink):
            body['MaterialIds'] = request.material_ids_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunStyleFeatureAnalysis',
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
            ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_style_feature_analysis(
        self,
        request: ai_miao_bi_20230801_models.RunStyleFeatureAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse:
        """
        @summary 内容特点分析
        
        @param request: RunStyleFeatureAnalysisRequest
        @return: RunStyleFeatureAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_style_feature_analysis_with_options(request, runtime)

    async def run_style_feature_analysis_async(
        self,
        request: ai_miao_bi_20230801_models.RunStyleFeatureAnalysisRequest,
    ) -> ai_miao_bi_20230801_models.RunStyleFeatureAnalysisResponse:
        """
        @summary 内容特点分析
        
        @param request: RunStyleFeatureAnalysisRequest
        @return: RunStyleFeatureAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_style_feature_analysis_with_options_async(request, runtime)

    def run_summary_generate_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunSummaryGenerateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunSummaryGenerateResponse:
        """
        @summary 内容摘要生成
        
        @param request: RunSummaryGenerateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSummaryGenerateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSummaryGenerate',
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
            ai_miao_bi_20230801_models.RunSummaryGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_summary_generate_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunSummaryGenerateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunSummaryGenerateResponse:
        """
        @summary 内容摘要生成
        
        @param request: RunSummaryGenerateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSummaryGenerateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSummaryGenerate',
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
            ai_miao_bi_20230801_models.RunSummaryGenerateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_summary_generate(
        self,
        request: ai_miao_bi_20230801_models.RunSummaryGenerateRequest,
    ) -> ai_miao_bi_20230801_models.RunSummaryGenerateResponse:
        """
        @summary 内容摘要生成
        
        @param request: RunSummaryGenerateRequest
        @return: RunSummaryGenerateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_summary_generate_with_options(request, runtime)

    async def run_summary_generate_async(
        self,
        request: ai_miao_bi_20230801_models.RunSummaryGenerateRequest,
    ) -> ai_miao_bi_20230801_models.RunSummaryGenerateResponse:
        """
        @summary 内容摘要生成
        
        @param request: RunSummaryGenerateRequest
        @return: RunSummaryGenerateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_summary_generate_with_options_async(request, runtime)

    def run_text_polishing_with_options(
        self,
        request: ai_miao_bi_20230801_models.RunTextPolishingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTextPolishingResponse:
        """
        @summary 创作-文本润色
        
        @param request: RunTextPolishingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTextPolishingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTextPolishing',
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
            ai_miao_bi_20230801_models.RunTextPolishingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_text_polishing_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.RunTextPolishingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTextPolishingResponse:
        """
        @summary 创作-文本润色
        
        @param request: RunTextPolishingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTextPolishingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTextPolishing',
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
            ai_miao_bi_20230801_models.RunTextPolishingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_text_polishing(
        self,
        request: ai_miao_bi_20230801_models.RunTextPolishingRequest,
    ) -> ai_miao_bi_20230801_models.RunTextPolishingResponse:
        """
        @summary 创作-文本润色
        
        @param request: RunTextPolishingRequest
        @return: RunTextPolishingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_text_polishing_with_options(request, runtime)

    async def run_text_polishing_async(
        self,
        request: ai_miao_bi_20230801_models.RunTextPolishingRequest,
    ) -> ai_miao_bi_20230801_models.RunTextPolishingResponse:
        """
        @summary 创作-文本润色
        
        @param request: RunTextPolishingRequest
        @return: RunTextPolishingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_text_polishing_with_options_async(request, runtime)

    def run_title_generation_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunTitleGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTitleGenerationResponse:
        """
        @summary 妙笔：标题生成
        
        @param tmp_req: RunTitleGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTitleGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunTitleGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTitleGeneration',
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
            ai_miao_bi_20230801_models.RunTitleGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_title_generation_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunTitleGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTitleGenerationResponse:
        """
        @summary 妙笔：标题生成
        
        @param tmp_req: RunTitleGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTitleGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunTitleGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTitleGeneration',
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
            ai_miao_bi_20230801_models.RunTitleGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_title_generation(
        self,
        request: ai_miao_bi_20230801_models.RunTitleGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunTitleGenerationResponse:
        """
        @summary 妙笔：标题生成
        
        @param request: RunTitleGenerationRequest
        @return: RunTitleGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_title_generation_with_options(request, runtime)

    async def run_title_generation_async(
        self,
        request: ai_miao_bi_20230801_models.RunTitleGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunTitleGenerationResponse:
        """
        @summary 妙笔：标题生成
        
        @param request: RunTitleGenerationRequest
        @return: RunTitleGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_title_generation_with_options_async(request, runtime)

    def run_translate_generation_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunTranslateGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTranslateGenerationResponse:
        """
        @summary AI妙笔-创作-中英文翻译
        
        @param tmp_req: RunTranslateGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTranslateGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunTranslateGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTranslateGeneration',
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
            ai_miao_bi_20230801_models.RunTranslateGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_translate_generation_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunTranslateGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunTranslateGenerationResponse:
        """
        @summary AI妙笔-创作-中英文翻译
        
        @param tmp_req: RunTranslateGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunTranslateGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunTranslateGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunTranslateGeneration',
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
            ai_miao_bi_20230801_models.RunTranslateGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_translate_generation(
        self,
        request: ai_miao_bi_20230801_models.RunTranslateGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunTranslateGenerationResponse:
        """
        @summary AI妙笔-创作-中英文翻译
        
        @param request: RunTranslateGenerationRequest
        @return: RunTranslateGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_translate_generation_with_options(request, runtime)

    async def run_translate_generation_async(
        self,
        request: ai_miao_bi_20230801_models.RunTranslateGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunTranslateGenerationResponse:
        """
        @summary AI妙笔-创作-中英文翻译
        
        @param request: RunTranslateGenerationRequest
        @return: RunTranslateGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_translate_generation_with_options_async(request, runtime)

    def run_write_tone_generation_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunWriteToneGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunWriteToneGenerationResponse:
        """
        @summary AI妙笔-创作-文风改写
        
        @param tmp_req: RunWriteToneGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunWriteToneGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunWriteToneGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunWriteToneGeneration',
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
            ai_miao_bi_20230801_models.RunWriteToneGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_write_tone_generation_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunWriteToneGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunWriteToneGenerationResponse:
        """
        @summary AI妙笔-创作-文风改写
        
        @param tmp_req: RunWriteToneGenerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunWriteToneGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunWriteToneGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunWriteToneGeneration',
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
            ai_miao_bi_20230801_models.RunWriteToneGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_write_tone_generation(
        self,
        request: ai_miao_bi_20230801_models.RunWriteToneGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunWriteToneGenerationResponse:
        """
        @summary AI妙笔-创作-文风改写
        
        @param request: RunWriteToneGenerationRequest
        @return: RunWriteToneGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_write_tone_generation_with_options(request, runtime)

    async def run_write_tone_generation_async(
        self,
        request: ai_miao_bi_20230801_models.RunWriteToneGenerationRequest,
    ) -> ai_miao_bi_20230801_models.RunWriteToneGenerationResponse:
        """
        @summary AI妙笔-创作-文风改写
        
        @param request: RunWriteToneGenerationRequest
        @return: RunWriteToneGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_write_tone_generation_with_options_async(request, runtime)

    def run_writing_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunWritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunWritingResponse:
        """
        @summary 直接写作
        
        @param tmp_req: RunWritingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunWritingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunWritingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not UtilClient.is_unset(tmp_req.writing_config):
            request.writing_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunWriting',
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
            ai_miao_bi_20230801_models.RunWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_writing_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.RunWritingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.RunWritingResponse:
        """
        @summary 直接写作
        
        @param tmp_req: RunWritingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunWritingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.RunWritingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reference_data):
            request.reference_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not UtilClient.is_unset(tmp_req.writing_config):
            request.writing_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunWriting',
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
            ai_miao_bi_20230801_models.RunWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_writing(
        self,
        request: ai_miao_bi_20230801_models.RunWritingRequest,
    ) -> ai_miao_bi_20230801_models.RunWritingResponse:
        """
        @summary 直接写作
        
        @param request: RunWritingRequest
        @return: RunWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_writing_with_options(request, runtime)

    async def run_writing_async(
        self,
        request: ai_miao_bi_20230801_models.RunWritingRequest,
    ) -> ai_miao_bi_20230801_models.RunWritingResponse:
        """
        @summary 直接写作
        
        @param request: RunWritingRequest
        @return: RunWritingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_writing_with_options_async(request, runtime)

    def save_custom_text_with_options(
        self,
        request: ai_miao_bi_20230801_models.SaveCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveCustomTextResponse:
        """
        @summary 保存自定义文本
        
        @param request: SaveCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveCustomText',
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
            ai_miao_bi_20230801_models.SaveCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_custom_text_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.SaveCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveCustomTextResponse:
        """
        @summary 保存自定义文本
        
        @param request: SaveCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveCustomText',
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
            ai_miao_bi_20230801_models.SaveCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_custom_text(
        self,
        request: ai_miao_bi_20230801_models.SaveCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.SaveCustomTextResponse:
        """
        @summary 保存自定义文本
        
        @param request: SaveCustomTextRequest
        @return: SaveCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_custom_text_with_options(request, runtime)

    async def save_custom_text_async(
        self,
        request: ai_miao_bi_20230801_models.SaveCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.SaveCustomTextResponse:
        """
        @summary 保存自定义文本
        
        @param request: SaveCustomTextRequest
        @return: SaveCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_custom_text_with_options_async(request, runtime)

    def save_data_source_order_config_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveDataSourceOrderConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse:
        """
        @summary 保存用户的信源配置
        
        @param tmp_req: SaveDataSourceOrderConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveDataSourceOrderConfigResponse
        """
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
        """
        @summary 保存用户的信源配置
        
        @param tmp_req: SaveDataSourceOrderConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveDataSourceOrderConfigResponse
        """
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
        """
        @summary 保存用户的信源配置
        
        @param request: SaveDataSourceOrderConfigRequest
        @return: SaveDataSourceOrderConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_data_source_order_config_with_options(request, runtime)

    async def save_data_source_order_config_async(
        self,
        request: ai_miao_bi_20230801_models.SaveDataSourceOrderConfigRequest,
    ) -> ai_miao_bi_20230801_models.SaveDataSourceOrderConfigResponse:
        """
        @summary 保存用户的信源配置
        
        @param request: SaveDataSourceOrderConfigRequest
        @return: SaveDataSourceOrderConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_data_source_order_config_with_options_async(request, runtime)

    def save_material_document_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SaveMaterialDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SaveMaterialDocumentResponse:
        """
        @summary 保存素材
        
        @param tmp_req: SaveMaterialDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveMaterialDocumentResponse
        """
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
        """
        @summary 保存素材
        
        @param tmp_req: SaveMaterialDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveMaterialDocumentResponse
        """
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
        """
        @summary 保存素材
        
        @param request: SaveMaterialDocumentRequest
        @return: SaveMaterialDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_material_document_with_options(request, runtime)

    async def save_material_document_async(
        self,
        request: ai_miao_bi_20230801_models.SaveMaterialDocumentRequest,
    ) -> ai_miao_bi_20230801_models.SaveMaterialDocumentResponse:
        """
        @summary 保存素材
        
        @param request: SaveMaterialDocumentRequest
        @return: SaveMaterialDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_material_document_with_options_async(request, runtime)

    def search_news_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SearchNewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SearchNewsResponse:
        """
        @summary 新闻检索
        
        @param tmp_req: SearchNewsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchNewsResponse
        """
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
        """
        @summary 新闻检索
        
        @param tmp_req: SearchNewsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchNewsResponse
        """
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
        """
        @summary 新闻检索
        
        @param request: SearchNewsRequest
        @return: SearchNewsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_news_with_options(request, runtime)

    async def search_news_async(
        self,
        request: ai_miao_bi_20230801_models.SearchNewsRequest,
    ) -> ai_miao_bi_20230801_models.SearchNewsResponse:
        """
        @summary 新闻检索
        
        @param request: SearchNewsRequest
        @return: SearchNewsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_news_with_options_async(request, runtime)

    def submit_async_task_with_options(
        self,
        request: ai_miao_bi_20230801_models.SubmitAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitAsyncTaskResponse:
        """
        @summary 提交异步任务
        
        @param request: SubmitAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitAsyncTaskResponse
        """
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
        """
        @summary 提交异步任务
        
        @param request: SubmitAsyncTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitAsyncTaskResponse
        """
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
        """
        @summary 提交异步任务
        
        @param request: SubmitAsyncTaskRequest
        @return: SubmitAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_async_task_with_options(request, runtime)

    async def submit_async_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitAsyncTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitAsyncTaskResponse:
        """
        @summary 提交异步任务
        
        @param request: SubmitAsyncTaskRequest
        @return: SubmitAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_async_task_with_options_async(request, runtime)

    def submit_custom_topic_selection_perspective_analysis_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交自定义热点选题视角分析任务
        
        @param tmp_req: SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitCustomTopicSelectionPerspectiveAnalysisTask',
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
            ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_custom_topic_selection_perspective_analysis_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交自定义热点选题视角分析任务
        
        @param tmp_req: SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitCustomTopicSelectionPerspectiveAnalysisTask',
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
            ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_custom_topic_selection_perspective_analysis_task(
        self,
        request: ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交自定义热点选题视角分析任务
        
        @param request: SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @return: SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_custom_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def submit_custom_topic_selection_perspective_analysis_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交自定义热点选题视角分析任务
        
        @param request: SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest
        @return: SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_custom_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def submit_doc_cluster_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitDocClusterTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse:
        """
        @summary 提交文档聚合任务
        
        @param tmp_req: SubmitDocClusterTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocClusterTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitDocClusterTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.summary_length):
            body['SummaryLength'] = request.summary_length
        if not UtilClient.is_unset(request.title_length):
            body['TitleLength'] = request.title_length
        if not UtilClient.is_unset(request.topic_count):
            body['TopicCount'] = request.topic_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDocClusterTask',
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
            ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_cluster_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitDocClusterTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse:
        """
        @summary 提交文档聚合任务
        
        @param tmp_req: SubmitDocClusterTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocClusterTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitDocClusterTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.summary_length):
            body['SummaryLength'] = request.summary_length
        if not UtilClient.is_unset(request.title_length):
            body['TitleLength'] = request.title_length
        if not UtilClient.is_unset(request.topic_count):
            body['TopicCount'] = request.topic_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDocClusterTask',
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
            ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_cluster_task(
        self,
        request: ai_miao_bi_20230801_models.SubmitDocClusterTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse:
        """
        @summary 提交文档聚合任务
        
        @param request: SubmitDocClusterTaskRequest
        @return: SubmitDocClusterTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_doc_cluster_task_with_options(request, runtime)

    async def submit_doc_cluster_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitDocClusterTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitDocClusterTaskResponse:
        """
        @summary 提交文档聚合任务
        
        @param request: SubmitDocClusterTaskRequest
        @return: SubmitDocClusterTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_doc_cluster_task_with_options_async(request, runtime)

    def submit_topic_selection_perspective_analysis_task_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交选题热点分析任务
        
        @param tmp_req: SubmitTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        if not UtilClient.is_unset(tmp_req.perspective_types):
            request.perspective_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective_types, 'PerspectiveTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.perspective_types_shrink):
            body['PerspectiveTypes'] = request.perspective_types_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitTopicSelectionPerspectiveAnalysisTask',
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
            ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_topic_selection_perspective_analysis_task_with_options_async(
        self,
        tmp_req: ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交选题热点分析任务
        
        @param tmp_req: SubmitTopicSelectionPerspectiveAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitTopicSelectionPerspectiveAnalysisTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        if not UtilClient.is_unset(tmp_req.perspective_types):
            request.perspective_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective_types, 'PerspectiveTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.perspective_types_shrink):
            body['PerspectiveTypes'] = request.perspective_types_shrink
        if not UtilClient.is_unset(request.topic):
            body['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitTopicSelectionPerspectiveAnalysisTask',
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
            ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_topic_selection_perspective_analysis_task(
        self,
        request: ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交选题热点分析任务
        
        @param request: SubmitTopicSelectionPerspectiveAnalysisTaskRequest
        @return: SubmitTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def submit_topic_selection_perspective_analysis_task_async(
        self,
        request: ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> ai_miao_bi_20230801_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        """
        @summary 提交选题热点分析任务
        
        @param request: SubmitTopicSelectionPerspectiveAnalysisTaskRequest
        @return: SubmitTopicSelectionPerspectiveAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def update_custom_text_with_options(
        self,
        request: ai_miao_bi_20230801_models.UpdateCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateCustomTextResponse:
        """
        @summary 更新自定义文本
        
        @param request: UpdateCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomText',
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
            ai_miao_bi_20230801_models.UpdateCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_text_with_options_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateCustomTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateCustomTextResponse:
        """
        @summary 更新自定义文本
        
        @param request: UpdateCustomTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomTextResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCustomText',
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
            ai_miao_bi_20230801_models.UpdateCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_text(
        self,
        request: ai_miao_bi_20230801_models.UpdateCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.UpdateCustomTextResponse:
        """
        @summary 更新自定义文本
        
        @param request: UpdateCustomTextRequest
        @return: UpdateCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_text_with_options(request, runtime)

    async def update_custom_text_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateCustomTextRequest,
    ) -> ai_miao_bi_20230801_models.UpdateCustomTextResponse:
        """
        @summary 更新自定义文本
        
        @param request: UpdateCustomTextRequest
        @return: UpdateCustomTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_text_with_options_async(request, runtime)

    def update_generated_content_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateGeneratedContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateGeneratedContentResponse:
        """
        @summary 文档管理-更新。
        
        @param tmp_req: UpdateGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGeneratedContentResponse
        """
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
        """
        @summary 文档管理-更新。
        
        @param tmp_req: UpdateGeneratedContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGeneratedContentResponse
        """
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
        """
        @summary 文档管理-更新。
        
        @param request: UpdateGeneratedContentRequest
        @return: UpdateGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_generated_content_with_options(request, runtime)

    async def update_generated_content_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateGeneratedContentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateGeneratedContentResponse:
        """
        @summary 文档管理-更新。
        
        @param request: UpdateGeneratedContentRequest
        @return: UpdateGeneratedContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_generated_content_with_options_async(request, runtime)

    def update_material_document_with_options(
        self,
        tmp_req: ai_miao_bi_20230801_models.UpdateMaterialDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse:
        """
        @summary 根据ID更新素材
        
        @param tmp_req: UpdateMaterialDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMaterialDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateMaterialDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_keywords):
            request.doc_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        """
        @summary 根据ID更新素材
        
        @param tmp_req: UpdateMaterialDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMaterialDocumentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ai_miao_bi_20230801_models.UpdateMaterialDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_keywords):
            request.doc_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        """
        @summary 根据ID更新素材
        
        @param request: UpdateMaterialDocumentRequest
        @return: UpdateMaterialDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_material_document_with_options(request, runtime)

    async def update_material_document_async(
        self,
        request: ai_miao_bi_20230801_models.UpdateMaterialDocumentRequest,
    ) -> ai_miao_bi_20230801_models.UpdateMaterialDocumentResponse:
        """
        @summary 根据ID更新素材
        
        @param request: UpdateMaterialDocumentRequest
        @return: UpdateMaterialDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_material_document_with_options_async(request, runtime)
