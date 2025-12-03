# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rdsai20250507 import models as rds_ai_20250507_models
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
        self._endpoint = self.get_endpoint('rdsai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def chat_messages_with_options(
        self,
        tmp_req: rds_ai_20250507_models.ChatMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ChatMessagesResponse:
        """
        @summary 发送对话消息
        
        @param tmp_req: ChatMessagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatMessagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ChatMessagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.inputs_shrink):
            query['Inputs'] = request.inputs_shrink
        if not UtilClient.is_unset(request.parent_message_id):
            query['ParentMessageId'] = request.parent_message_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatMessages',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ChatMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_messages_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.ChatMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ChatMessagesResponse:
        """
        @summary 发送对话消息
        
        @param tmp_req: ChatMessagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatMessagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ChatMessagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.inputs_shrink):
            query['Inputs'] = request.inputs_shrink
        if not UtilClient.is_unset(request.parent_message_id):
            query['ParentMessageId'] = request.parent_message_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatMessages',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ChatMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_messages(
        self,
        request: rds_ai_20250507_models.ChatMessagesRequest,
    ) -> rds_ai_20250507_models.ChatMessagesResponse:
        """
        @summary 发送对话消息
        
        @param request: ChatMessagesRequest
        @return: ChatMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chat_messages_with_options(request, runtime)

    async def chat_messages_async(
        self,
        request: rds_ai_20250507_models.ChatMessagesRequest,
    ) -> rds_ai_20250507_models.ChatMessagesResponse:
        """
        @summary 发送对话消息
        
        @param request: ChatMessagesRequest
        @return: ChatMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chat_messages_with_options_async(request, runtime)

    def chat_messages_task_stop_with_options(
        self,
        request: rds_ai_20250507_models.ChatMessagesTaskStopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ChatMessagesTaskStopResponse:
        """
        @summary 停止对话
        
        @param request: ChatMessagesTaskStopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatMessagesTaskStopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatMessagesTaskStop',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ChatMessagesTaskStopResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_messages_task_stop_with_options_async(
        self,
        request: rds_ai_20250507_models.ChatMessagesTaskStopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ChatMessagesTaskStopResponse:
        """
        @summary 停止对话
        
        @param request: ChatMessagesTaskStopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatMessagesTaskStopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatMessagesTaskStop',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ChatMessagesTaskStopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_messages_task_stop(
        self,
        request: rds_ai_20250507_models.ChatMessagesTaskStopRequest,
    ) -> rds_ai_20250507_models.ChatMessagesTaskStopResponse:
        """
        @summary 停止对话
        
        @param request: ChatMessagesTaskStopRequest
        @return: ChatMessagesTaskStopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chat_messages_task_stop_with_options(request, runtime)

    async def chat_messages_task_stop_async(
        self,
        request: rds_ai_20250507_models.ChatMessagesTaskStopRequest,
    ) -> rds_ai_20250507_models.ChatMessagesTaskStopResponse:
        """
        @summary 停止对话
        
        @param request: ChatMessagesTaskStopRequest
        @return: ChatMessagesTaskStopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chat_messages_task_stop_with_options_async(request, runtime)

    def create_app_instance_with_options(
        self,
        tmp_req: rds_ai_20250507_models.CreateAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.CreateAppInstanceResponse:
        """
        @summary 创建应用服务实例
        
        @param tmp_req: CreateAppInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.CreateAppInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbinstance_config):
            request.dbinstance_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_config, 'DBInstanceConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_config_shrink):
            query['DBInstanceConfig'] = request.dbinstance_config_shrink
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not UtilClient.is_unset(request.dashboard_username):
            query['DashboardUsername'] = request.dashboard_username
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.public_endpoint_enabled):
            query['PublicEndpointEnabled'] = request.public_endpoint_enabled
        if not UtilClient.is_unset(request.public_network_access_enabled):
            query['PublicNetworkAccessEnabled'] = request.public_network_access_enabled
        if not UtilClient.is_unset(request.ragenabled):
            query['RAGEnabled'] = request.ragenabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.CreateAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_instance_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.CreateAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.CreateAppInstanceResponse:
        """
        @summary 创建应用服务实例
        
        @param tmp_req: CreateAppInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.CreateAppInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbinstance_config):
            request.dbinstance_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_config, 'DBInstanceConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_config_shrink):
            query['DBInstanceConfig'] = request.dbinstance_config_shrink
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not UtilClient.is_unset(request.dashboard_username):
            query['DashboardUsername'] = request.dashboard_username
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.public_endpoint_enabled):
            query['PublicEndpointEnabled'] = request.public_endpoint_enabled
        if not UtilClient.is_unset(request.public_network_access_enabled):
            query['PublicNetworkAccessEnabled'] = request.public_network_access_enabled
        if not UtilClient.is_unset(request.ragenabled):
            query['RAGEnabled'] = request.ragenabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.CreateAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_instance(
        self,
        request: rds_ai_20250507_models.CreateAppInstanceRequest,
    ) -> rds_ai_20250507_models.CreateAppInstanceResponse:
        """
        @summary 创建应用服务实例
        
        @param request: CreateAppInstanceRequest
        @return: CreateAppInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_instance_with_options(request, runtime)

    async def create_app_instance_async(
        self,
        request: rds_ai_20250507_models.CreateAppInstanceRequest,
    ) -> rds_ai_20250507_models.CreateAppInstanceResponse:
        """
        @summary 创建应用服务实例
        
        @param request: CreateAppInstanceRequest
        @return: CreateAppInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_instance_with_options_async(request, runtime)

    def create_custom_agent_with_options(
        self,
        tmp_req: rds_ai_20250507_models.CreateCustomAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.CreateCustomAgentResponse:
        """
        @summary 创建自定义agent
        
        @param tmp_req: CreateCustomAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomAgentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.CreateCustomAgentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tools):
            request.tools_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.system_prompt):
            query['SystemPrompt'] = request.system_prompt
        if not UtilClient.is_unset(request.tools_shrink):
            query['Tools'] = request.tools_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomAgent',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.CreateCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_agent_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.CreateCustomAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.CreateCustomAgentResponse:
        """
        @summary 创建自定义agent
        
        @param tmp_req: CreateCustomAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomAgentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.CreateCustomAgentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tools):
            request.tools_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.system_prompt):
            query['SystemPrompt'] = request.system_prompt
        if not UtilClient.is_unset(request.tools_shrink):
            query['Tools'] = request.tools_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomAgent',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.CreateCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_agent(
        self,
        request: rds_ai_20250507_models.CreateCustomAgentRequest,
    ) -> rds_ai_20250507_models.CreateCustomAgentResponse:
        """
        @summary 创建自定义agent
        
        @param request: CreateCustomAgentRequest
        @return: CreateCustomAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_agent_with_options(request, runtime)

    async def create_custom_agent_async(
        self,
        request: rds_ai_20250507_models.CreateCustomAgentRequest,
    ) -> rds_ai_20250507_models.CreateCustomAgentResponse:
        """
        @summary 创建自定义agent
        
        @param request: CreateCustomAgentRequest
        @return: CreateCustomAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_agent_with_options_async(request, runtime)

    def delete_app_instance_with_options(
        self,
        request: rds_ai_20250507_models.DeleteAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DeleteAppInstanceResponse:
        """
        @summary 删除应用服务实例
        
        @param request: DeleteAppInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DeleteAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_instance_with_options_async(
        self,
        request: rds_ai_20250507_models.DeleteAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DeleteAppInstanceResponse:
        """
        @summary 删除应用服务实例
        
        @param request: DeleteAppInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DeleteAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_instance(
        self,
        request: rds_ai_20250507_models.DeleteAppInstanceRequest,
    ) -> rds_ai_20250507_models.DeleteAppInstanceResponse:
        """
        @summary 删除应用服务实例
        
        @param request: DeleteAppInstanceRequest
        @return: DeleteAppInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_instance_with_options(request, runtime)

    async def delete_app_instance_async(
        self,
        request: rds_ai_20250507_models.DeleteAppInstanceRequest,
    ) -> rds_ai_20250507_models.DeleteAppInstanceResponse:
        """
        @summary 删除应用服务实例
        
        @param request: DeleteAppInstanceRequest
        @return: DeleteAppInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_instance_with_options_async(request, runtime)

    def delete_custom_agent_with_options(
        self,
        request: rds_ai_20250507_models.DeleteCustomAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DeleteCustomAgentResponse:
        """
        @summary 删除Custom Agent
        
        @param request: DeleteCustomAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomAgent',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DeleteCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_agent_with_options_async(
        self,
        request: rds_ai_20250507_models.DeleteCustomAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DeleteCustomAgentResponse:
        """
        @summary 删除Custom Agent
        
        @param request: DeleteCustomAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomAgent',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DeleteCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_agent(
        self,
        request: rds_ai_20250507_models.DeleteCustomAgentRequest,
    ) -> rds_ai_20250507_models.DeleteCustomAgentResponse:
        """
        @summary 删除Custom Agent
        
        @param request: DeleteCustomAgentRequest
        @return: DeleteCustomAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_agent_with_options(request, runtime)

    async def delete_custom_agent_async(
        self,
        request: rds_ai_20250507_models.DeleteCustomAgentRequest,
    ) -> rds_ai_20250507_models.DeleteCustomAgentResponse:
        """
        @summary 删除Custom Agent
        
        @param request: DeleteCustomAgentRequest
        @return: DeleteCustomAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_agent_with_options_async(request, runtime)

    def describe_app_instance_attribute_with_options(
        self,
        request: rds_ai_20250507_models.DescribeAppInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeAppInstanceAttributeResponse:
        """
        @summary 查询应用服务详情
        
        @param request: DescribeAppInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInstanceAttribute',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeAppInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_instance_attribute_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeAppInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeAppInstanceAttributeResponse:
        """
        @summary 查询应用服务详情
        
        @param request: DescribeAppInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInstanceAttribute',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeAppInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_instance_attribute(
        self,
        request: rds_ai_20250507_models.DescribeAppInstanceAttributeRequest,
    ) -> rds_ai_20250507_models.DescribeAppInstanceAttributeResponse:
        """
        @summary 查询应用服务详情
        
        @param request: DescribeAppInstanceAttributeRequest
        @return: DescribeAppInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_instance_attribute_with_options(request, runtime)

    async def describe_app_instance_attribute_async(
        self,
        request: rds_ai_20250507_models.DescribeAppInstanceAttributeRequest,
    ) -> rds_ai_20250507_models.DescribeAppInstanceAttributeResponse:
        """
        @summary 查询应用服务详情
        
        @param request: DescribeAppInstanceAttributeRequest
        @return: DescribeAppInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_instance_attribute_with_options_async(request, runtime)

    def describe_app_instances_with_options(
        self,
        request: rds_ai_20250507_models.DescribeAppInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeAppInstancesResponse:
        """
        @summary 查询应用服务列表
        
        @param request: DescribeAppInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInstances',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_instances_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeAppInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeAppInstancesResponse:
        """
        @summary 查询应用服务列表
        
        @param request: DescribeAppInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInstances',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_instances(
        self,
        request: rds_ai_20250507_models.DescribeAppInstancesRequest,
    ) -> rds_ai_20250507_models.DescribeAppInstancesResponse:
        """
        @summary 查询应用服务列表
        
        @param request: DescribeAppInstancesRequest
        @return: DescribeAppInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_instances_with_options(request, runtime)

    async def describe_app_instances_async(
        self,
        request: rds_ai_20250507_models.DescribeAppInstancesRequest,
    ) -> rds_ai_20250507_models.DescribeAppInstancesResponse:
        """
        @summary 查询应用服务列表
        
        @param request: DescribeAppInstancesRequest
        @return: DescribeAppInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_instances_with_options_async(request, runtime)

    def describe_events_list_with_options(
        self,
        request: rds_ai_20250507_models.DescribeEventsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeEventsListResponse:
        """
        @summary 查询事件信息列表
        
        @param request: DescribeEventsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventsList',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeEventsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_list_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeEventsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeEventsListResponse:
        """
        @summary 查询事件信息列表
        
        @param request: DescribeEventsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventsList',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeEventsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events_list(
        self,
        request: rds_ai_20250507_models.DescribeEventsListRequest,
    ) -> rds_ai_20250507_models.DescribeEventsListResponse:
        """
        @summary 查询事件信息列表
        
        @param request: DescribeEventsListRequest
        @return: DescribeEventsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_events_list_with_options(request, runtime)

    async def describe_events_list_async(
        self,
        request: rds_ai_20250507_models.DescribeEventsListRequest,
    ) -> rds_ai_20250507_models.DescribeEventsListResponse:
        """
        @summary 查询事件信息列表
        
        @param request: DescribeEventsListRequest
        @return: DescribeEventsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_events_list_with_options_async(request, runtime)

    def describe_instance_auth_info_with_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceAuthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceAuthInfoResponse:
        """
        @summary 查看实例认证信息
        
        @param request: DescribeInstanceAuthInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAuthInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAuthInfo',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceAuthInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_auth_info_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceAuthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceAuthInfoResponse:
        """
        @summary 查看实例认证信息
        
        @param request: DescribeInstanceAuthInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAuthInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAuthInfo',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceAuthInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_auth_info(
        self,
        request: rds_ai_20250507_models.DescribeInstanceAuthInfoRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceAuthInfoResponse:
        """
        @summary 查看实例认证信息
        
        @param request: DescribeInstanceAuthInfoRequest
        @return: DescribeInstanceAuthInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auth_info_with_options(request, runtime)

    async def describe_instance_auth_info_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceAuthInfoRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceAuthInfoResponse:
        """
        @summary 查看实例认证信息
        
        @param request: DescribeInstanceAuthInfoRequest
        @return: DescribeInstanceAuthInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auth_info_with_options_async(request, runtime)

    def describe_instance_endpoints_with_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceEndpointsResponse:
        """
        @summary 查看服务连接信息
        
        @param request: DescribeInstanceEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceEndpoints',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_endpoints_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceEndpointsResponse:
        """
        @summary 查看服务连接信息
        
        @param request: DescribeInstanceEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceEndpoints',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_endpoints(
        self,
        request: rds_ai_20250507_models.DescribeInstanceEndpointsRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceEndpointsResponse:
        """
        @summary 查看服务连接信息
        
        @param request: DescribeInstanceEndpointsRequest
        @return: DescribeInstanceEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_endpoints_with_options(request, runtime)

    async def describe_instance_endpoints_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceEndpointsRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceEndpointsResponse:
        """
        @summary 查看服务连接信息
        
        @param request: DescribeInstanceEndpointsRequest
        @return: DescribeInstanceEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_endpoints_with_options_async(request, runtime)

    def describe_instance_ip_whitelist_with_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse:
        """
        @summary 查询服务白名单
        
        @param request: DescribeInstanceIpWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIpWhitelist',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ip_whitelist_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse:
        """
        @summary 查询服务白名单
        
        @param request: DescribeInstanceIpWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIpWhitelist',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ip_whitelist(
        self,
        request: rds_ai_20250507_models.DescribeInstanceIpWhitelistRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse:
        """
        @summary 查询服务白名单
        
        @param request: DescribeInstanceIpWhitelistRequest
        @return: DescribeInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ip_whitelist_with_options(request, runtime)

    async def describe_instance_ip_whitelist_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceIpWhitelistRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse:
        """
        @summary 查询服务白名单
        
        @param request: DescribeInstanceIpWhitelistRequest
        @return: DescribeInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_ip_whitelist_with_options_async(request, runtime)

    def describe_instance_ragconfig_with_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceRAGConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceRAGConfigResponse:
        """
        @summary 查看实例RAG配置
        
        @param request: DescribeInstanceRAGConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceRAGConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRAGConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceRAGConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ragconfig_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceRAGConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceRAGConfigResponse:
        """
        @summary 查看实例RAG配置
        
        @param request: DescribeInstanceRAGConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceRAGConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRAGConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceRAGConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ragconfig(
        self,
        request: rds_ai_20250507_models.DescribeInstanceRAGConfigRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceRAGConfigResponse:
        """
        @summary 查看实例RAG配置
        
        @param request: DescribeInstanceRAGConfigRequest
        @return: DescribeInstanceRAGConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ragconfig_with_options(request, runtime)

    async def describe_instance_ragconfig_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceRAGConfigRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceRAGConfigResponse:
        """
        @summary 查看实例RAG配置
        
        @param request: DescribeInstanceRAGConfigRequest
        @return: DescribeInstanceRAGConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_ragconfig_with_options_async(request, runtime)

    def describe_instance_sslwith_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceSSLResponse:
        """
        @summary 查看实例SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSSL',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_sslwith_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceSSLResponse:
        """
        @summary 查看实例SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSSL',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ssl(
        self,
        request: rds_ai_20250507_models.DescribeInstanceSSLRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceSSLResponse:
        """
        @summary 查看实例SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @return: DescribeInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_sslwith_options(request, runtime)

    async def describe_instance_ssl_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceSSLRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceSSLResponse:
        """
        @summary 查看实例SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @return: DescribeInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_sslwith_options_async(request, runtime)

    def describe_instance_storage_config_with_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceStorageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceStorageConfigResponse:
        """
        @summary 查看实例存储配置
        
        @param request: DescribeInstanceStorageConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStorageConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStorageConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceStorageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_storage_config_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceStorageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceStorageConfigResponse:
        """
        @summary 查看实例存储配置
        
        @param request: DescribeInstanceStorageConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStorageConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStorageConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceStorageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_storage_config(
        self,
        request: rds_ai_20250507_models.DescribeInstanceStorageConfigRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceStorageConfigResponse:
        """
        @summary 查看实例存储配置
        
        @param request: DescribeInstanceStorageConfigRequest
        @return: DescribeInstanceStorageConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_storage_config_with_options(request, runtime)

    async def describe_instance_storage_config_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceStorageConfigRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceStorageConfigResponse:
        """
        @summary 查看实例存储配置
        
        @param request: DescribeInstanceStorageConfigRequest
        @return: DescribeInstanceStorageConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_storage_config_with_options_async(request, runtime)

    def get_conversations_with_options(
        self,
        request: rds_ai_20250507_models.GetConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.GetConversationsResponse:
        """
        @summary 获取会话列表
        
        @param request: GetConversationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConversationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.last_id):
            query['LastId'] = request.last_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.pinned):
            query['Pinned'] = request.pinned
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConversations',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.GetConversationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conversations_with_options_async(
        self,
        request: rds_ai_20250507_models.GetConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.GetConversationsResponse:
        """
        @summary 获取会话列表
        
        @param request: GetConversationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConversationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.last_id):
            query['LastId'] = request.last_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.pinned):
            query['Pinned'] = request.pinned
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConversations',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.GetConversationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conversations(
        self,
        request: rds_ai_20250507_models.GetConversationsRequest,
    ) -> rds_ai_20250507_models.GetConversationsResponse:
        """
        @summary 获取会话列表
        
        @param request: GetConversationsRequest
        @return: GetConversationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_conversations_with_options(request, runtime)

    async def get_conversations_async(
        self,
        request: rds_ai_20250507_models.GetConversationsRequest,
    ) -> rds_ai_20250507_models.GetConversationsResponse:
        """
        @summary 获取会话列表
        
        @param request: GetConversationsRequest
        @return: GetConversationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_conversations_with_options_async(request, runtime)

    def get_custom_agent_with_options(
        self,
        request: rds_ai_20250507_models.GetCustomAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.GetCustomAgentResponse:
        """
        @summary 查询CustomAgent
        
        @param request: GetCustomAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomAgent',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.GetCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_agent_with_options_async(
        self,
        request: rds_ai_20250507_models.GetCustomAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.GetCustomAgentResponse:
        """
        @summary 查询CustomAgent
        
        @param request: GetCustomAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomAgent',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.GetCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_agent(
        self,
        request: rds_ai_20250507_models.GetCustomAgentRequest,
    ) -> rds_ai_20250507_models.GetCustomAgentResponse:
        """
        @summary 查询CustomAgent
        
        @param request: GetCustomAgentRequest
        @return: GetCustomAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_custom_agent_with_options(request, runtime)

    async def get_custom_agent_async(
        self,
        request: rds_ai_20250507_models.GetCustomAgentRequest,
    ) -> rds_ai_20250507_models.GetCustomAgentResponse:
        """
        @summary 查询CustomAgent
        
        @param request: GetCustomAgentRequest
        @return: GetCustomAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_agent_with_options_async(request, runtime)

    def get_messages_with_options(
        self,
        request: rds_ai_20250507_models.GetMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.GetMessagesResponse:
        """
        @summary 获取会话历史消息
        
        @param request: GetMessagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMessagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.first_id):
            query['FirstId'] = request.first_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMessages',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.GetMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_messages_with_options_async(
        self,
        request: rds_ai_20250507_models.GetMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.GetMessagesResponse:
        """
        @summary 获取会话历史消息
        
        @param request: GetMessagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMessagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.first_id):
            query['FirstId'] = request.first_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMessages',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.GetMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_messages(
        self,
        request: rds_ai_20250507_models.GetMessagesRequest,
    ) -> rds_ai_20250507_models.GetMessagesResponse:
        """
        @summary 获取会话历史消息
        
        @param request: GetMessagesRequest
        @return: GetMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_messages_with_options(request, runtime)

    async def get_messages_async(
        self,
        request: rds_ai_20250507_models.GetMessagesRequest,
    ) -> rds_ai_20250507_models.GetMessagesResponse:
        """
        @summary 获取会话历史消息
        
        @param request: GetMessagesRequest
        @return: GetMessagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_messages_with_options_async(request, runtime)

    def list_custom_agent_with_options(
        self,
        request: rds_ai_20250507_models.ListCustomAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ListCustomAgentResponse:
        """
        @summary 获取Custom Agent列表
        
        @param request: ListCustomAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomAgent',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ListCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_agent_with_options_async(
        self,
        request: rds_ai_20250507_models.ListCustomAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ListCustomAgentResponse:
        """
        @summary 获取Custom Agent列表
        
        @param request: ListCustomAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomAgent',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ListCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_agent(
        self,
        request: rds_ai_20250507_models.ListCustomAgentRequest,
    ) -> rds_ai_20250507_models.ListCustomAgentResponse:
        """
        @summary 获取Custom Agent列表
        
        @param request: ListCustomAgentRequest
        @return: ListCustomAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_agent_with_options(request, runtime)

    async def list_custom_agent_async(
        self,
        request: rds_ai_20250507_models.ListCustomAgentRequest,
    ) -> rds_ai_20250507_models.ListCustomAgentResponse:
        """
        @summary 获取Custom Agent列表
        
        @param request: ListCustomAgentRequest
        @return: ListCustomAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_agent_with_options_async(request, runtime)

    def list_custom_agent_tools_with_options(
        self,
        request: rds_ai_20250507_models.ListCustomAgentToolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ListCustomAgentToolsResponse:
        """
        @summary 获取专属Agent可用工具
        
        @param request: ListCustomAgentToolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomAgentToolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomAgentTools',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ListCustomAgentToolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_agent_tools_with_options_async(
        self,
        request: rds_ai_20250507_models.ListCustomAgentToolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ListCustomAgentToolsResponse:
        """
        @summary 获取专属Agent可用工具
        
        @param request: ListCustomAgentToolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomAgentToolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomAgentTools',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ListCustomAgentToolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_agent_tools(
        self,
        request: rds_ai_20250507_models.ListCustomAgentToolsRequest,
    ) -> rds_ai_20250507_models.ListCustomAgentToolsResponse:
        """
        @summary 获取专属Agent可用工具
        
        @param request: ListCustomAgentToolsRequest
        @return: ListCustomAgentToolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_agent_tools_with_options(request, runtime)

    async def list_custom_agent_tools_async(
        self,
        request: rds_ai_20250507_models.ListCustomAgentToolsRequest,
    ) -> rds_ai_20250507_models.ListCustomAgentToolsResponse:
        """
        @summary 获取专属Agent可用工具
        
        @param request: ListCustomAgentToolsRequest
        @return: ListCustomAgentToolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_agent_tools_with_options_async(request, runtime)

    def modify_instance_auth_config_with_options(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceAuthConfigResponse:
        """
        @summary 修改Supabase Auth相关配置
        
        @param tmp_req: ModifyInstanceAuthConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAuthConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceAuthConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAuthConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_auth_config_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceAuthConfigResponse:
        """
        @summary 修改Supabase Auth相关配置
        
        @param tmp_req: ModifyInstanceAuthConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAuthConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceAuthConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAuthConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_auth_config(
        self,
        request: rds_ai_20250507_models.ModifyInstanceAuthConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceAuthConfigResponse:
        """
        @summary 修改Supabase Auth相关配置
        
        @param request: ModifyInstanceAuthConfigRequest
        @return: ModifyInstanceAuthConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auth_config_with_options(request, runtime)

    async def modify_instance_auth_config_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceAuthConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceAuthConfigResponse:
        """
        @summary 修改Supabase Auth相关配置
        
        @param request: ModifyInstanceAuthConfigRequest
        @return: ModifyInstanceAuthConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auth_config_with_options_async(request, runtime)

    def modify_instance_config_with_options(
        self,
        request: rds_ai_20250507_models.ModifyInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_config_with_options_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_config(
        self,
        request: rds_ai_20250507_models.ModifyInstanceConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceConfigRequest
        @return: ModifyInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_config_with_options(request, runtime)

    async def modify_instance_config_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceConfigRequest
        @return: ModifyInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_config_with_options_async(request, runtime)

    def modify_instance_ip_whitelist_with_options(
        self,
        request: rds_ai_20250507_models.ModifyInstanceIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse:
        """
        @summary 修改服务白名单
        
        @param request: ModifyInstanceIpWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceIpWhitelist',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_ip_whitelist_with_options_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse:
        """
        @summary 修改服务白名单
        
        @param request: ModifyInstanceIpWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceIpWhitelist',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ip_whitelist(
        self,
        request: rds_ai_20250507_models.ModifyInstanceIpWhitelistRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse:
        """
        @summary 修改服务白名单
        
        @param request: ModifyInstanceIpWhitelistRequest
        @return: ModifyInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_ip_whitelist_with_options(request, runtime)

    async def modify_instance_ip_whitelist_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceIpWhitelistRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse:
        """
        @summary 修改服务白名单
        
        @param request: ModifyInstanceIpWhitelistRequest
        @return: ModifyInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_ip_whitelist_with_options_async(request, runtime)

    def modify_instance_ragconfig_with_options(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceRAGConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceRAGConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param tmp_req: ModifyInstanceRAGConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceRAGConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceRAGConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRAGConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceRAGConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_ragconfig_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceRAGConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceRAGConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param tmp_req: ModifyInstanceRAGConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceRAGConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceRAGConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRAGConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceRAGConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ragconfig(
        self,
        request: rds_ai_20250507_models.ModifyInstanceRAGConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceRAGConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceRAGConfigRequest
        @return: ModifyInstanceRAGConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_ragconfig_with_options(request, runtime)

    async def modify_instance_ragconfig_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceRAGConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceRAGConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceRAGConfigRequest
        @return: ModifyInstanceRAGConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_ragconfig_with_options_async(request, runtime)

    def modify_instance_sslwith_options(
        self,
        request: rds_ai_20250507_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceSSLResponse:
        """
        @summary 修改实例SSL配置
        
        @param request: ModifyInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catype):
            query['CAType'] = request.catype
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not UtilClient.is_unset(request.server_cert):
            query['ServerCert'] = request.server_cert
        if not UtilClient.is_unset(request.server_key):
            query['ServerKey'] = request.server_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSSL',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_sslwith_options_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceSSLResponse:
        """
        @summary 修改实例SSL配置
        
        @param request: ModifyInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catype):
            query['CAType'] = request.catype
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not UtilClient.is_unset(request.server_cert):
            query['ServerCert'] = request.server_cert
        if not UtilClient.is_unset(request.server_key):
            query['ServerKey'] = request.server_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSSL',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ssl(
        self,
        request: rds_ai_20250507_models.ModifyInstanceSSLRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceSSLResponse:
        """
        @summary 修改实例SSL配置
        
        @param request: ModifyInstanceSSLRequest
        @return: ModifyInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_sslwith_options(request, runtime)

    async def modify_instance_ssl_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceSSLRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceSSLResponse:
        """
        @summary 修改实例SSL配置
        
        @param request: ModifyInstanceSSLRequest
        @return: ModifyInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_sslwith_options_async(request, runtime)

    def modify_instance_storage_config_with_options(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceStorageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceStorageConfigResponse:
        """
        @summary 修改实例存储配置
        
        @param tmp_req: ModifyInstanceStorageConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceStorageConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceStorageConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceStorageConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceStorageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_storage_config_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceStorageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceStorageConfigResponse:
        """
        @summary 修改实例存储配置
        
        @param tmp_req: ModifyInstanceStorageConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceStorageConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceStorageConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceStorageConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceStorageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_storage_config(
        self,
        request: rds_ai_20250507_models.ModifyInstanceStorageConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceStorageConfigResponse:
        """
        @summary 修改实例存储配置
        
        @param request: ModifyInstanceStorageConfigRequest
        @return: ModifyInstanceStorageConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_storage_config_with_options(request, runtime)

    async def modify_instance_storage_config_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceStorageConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceStorageConfigResponse:
        """
        @summary 修改实例存储配置
        
        @param request: ModifyInstanceStorageConfigRequest
        @return: ModifyInstanceStorageConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_storage_config_with_options_async(request, runtime)

    def modify_messages_feedbacks_with_options(
        self,
        request: rds_ai_20250507_models.ModifyMessagesFeedbacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyMessagesFeedbacksResponse:
        """
        @summary 消息终端用户反馈、点赞/点踩
        
        @param request: ModifyMessagesFeedbacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMessagesFeedbacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.rating):
            query['Rating'] = request.rating
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMessagesFeedbacks',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyMessagesFeedbacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_messages_feedbacks_with_options_async(
        self,
        request: rds_ai_20250507_models.ModifyMessagesFeedbacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyMessagesFeedbacksResponse:
        """
        @summary 消息终端用户反馈、点赞/点踩
        
        @param request: ModifyMessagesFeedbacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMessagesFeedbacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.rating):
            query['Rating'] = request.rating
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMessagesFeedbacks',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyMessagesFeedbacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_messages_feedbacks(
        self,
        request: rds_ai_20250507_models.ModifyMessagesFeedbacksRequest,
    ) -> rds_ai_20250507_models.ModifyMessagesFeedbacksResponse:
        """
        @summary 消息终端用户反馈、点赞/点踩
        
        @param request: ModifyMessagesFeedbacksRequest
        @return: ModifyMessagesFeedbacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_messages_feedbacks_with_options(request, runtime)

    async def modify_messages_feedbacks_async(
        self,
        request: rds_ai_20250507_models.ModifyMessagesFeedbacksRequest,
    ) -> rds_ai_20250507_models.ModifyMessagesFeedbacksResponse:
        """
        @summary 消息终端用户反馈、点赞/点踩
        
        @param request: ModifyMessagesFeedbacksRequest
        @return: ModifyMessagesFeedbacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_messages_feedbacks_with_options_async(request, runtime)

    def reset_instance_password_with_options(
        self,
        request: rds_ai_20250507_models.ResetInstancePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ResetInstancePasswordResponse:
        """
        @summary 重置实例密码
        
        @param request: ResetInstancePasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetInstancePasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetInstancePassword',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ResetInstancePasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_instance_password_with_options_async(
        self,
        request: rds_ai_20250507_models.ResetInstancePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ResetInstancePasswordResponse:
        """
        @summary 重置实例密码
        
        @param request: ResetInstancePasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetInstancePasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetInstancePassword',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ResetInstancePasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_instance_password(
        self,
        request: rds_ai_20250507_models.ResetInstancePasswordRequest,
    ) -> rds_ai_20250507_models.ResetInstancePasswordResponse:
        """
        @summary 重置实例密码
        
        @param request: ResetInstancePasswordRequest
        @return: ResetInstancePasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_instance_password_with_options(request, runtime)

    async def reset_instance_password_async(
        self,
        request: rds_ai_20250507_models.ResetInstancePasswordRequest,
    ) -> rds_ai_20250507_models.ResetInstancePasswordResponse:
        """
        @summary 重置实例密码
        
        @param request: ResetInstancePasswordRequest
        @return: ResetInstancePasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_instance_password_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: rds_ai_20250507_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: rds_ai_20250507_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: rds_ai_20250507_models.RestartInstanceRequest,
    ) -> rds_ai_20250507_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartInstanceRequest
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: rds_ai_20250507_models.RestartInstanceRequest,
    ) -> rds_ai_20250507_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartInstanceRequest
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: rds_ai_20250507_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: rds_ai_20250507_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        request: rds_ai_20250507_models.StartInstanceRequest,
    ) -> rds_ai_20250507_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: rds_ai_20250507_models.StartInstanceRequest,
    ) -> rds_ai_20250507_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: rds_ai_20250507_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: rds_ai_20250507_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: rds_ai_20250507_models.StopInstanceRequest,
    ) -> rds_ai_20250507_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: rds_ai_20250507_models.StopInstanceRequest,
    ) -> rds_ai_20250507_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def update_custom_agent_with_options(
        self,
        tmp_req: rds_ai_20250507_models.UpdateCustomAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.UpdateCustomAgentResponse:
        """
        @summary 更新Custom Agent
        
        @param tmp_req: UpdateCustomAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomAgentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.UpdateCustomAgentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tools):
            request.tools_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not UtilClient.is_unset(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.system_prompt):
            query['SystemPrompt'] = request.system_prompt
        if not UtilClient.is_unset(request.tools_shrink):
            query['Tools'] = request.tools_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomAgent',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.UpdateCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_agent_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.UpdateCustomAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.UpdateCustomAgentResponse:
        """
        @summary 更新Custom Agent
        
        @param tmp_req: UpdateCustomAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomAgentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.UpdateCustomAgentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tools):
            request.tools_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tools, 'Tools', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not UtilClient.is_unset(request.enable_tools):
            query['EnableTools'] = request.enable_tools
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.system_prompt):
            query['SystemPrompt'] = request.system_prompt
        if not UtilClient.is_unset(request.tools_shrink):
            query['Tools'] = request.tools_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomAgent',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.UpdateCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_agent(
        self,
        request: rds_ai_20250507_models.UpdateCustomAgentRequest,
    ) -> rds_ai_20250507_models.UpdateCustomAgentResponse:
        """
        @summary 更新Custom Agent
        
        @param request: UpdateCustomAgentRequest
        @return: UpdateCustomAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_agent_with_options(request, runtime)

    async def update_custom_agent_async(
        self,
        request: rds_ai_20250507_models.UpdateCustomAgentRequest,
    ) -> rds_ai_20250507_models.UpdateCustomAgentResponse:
        """
        @summary 更新Custom Agent
        
        @param request: UpdateCustomAgentRequest
        @return: UpdateCustomAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_agent_with_options_async(request, runtime)
