# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_starops20260428 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL
from darabonba.utils.stream import Stream as DaraStream

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('starops', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_chat_with_sse(
        self,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.CreateChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.digital_employee_name):
            body['digitalEmployeeName'] = request.digital_employee_name
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.CreateChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def create_chat_with_sse_async(
        self,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.CreateChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.digital_employee_name):
            body['digitalEmployeeName'] = request.digital_employee_name
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.CreateChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def create_chat_with_options(
        self,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.digital_employee_name):
            body['digitalEmployeeName'] = request.digital_employee_name
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_with_options_async(
        self,
        request: main_models.CreateChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.digital_employee_name):
            body['digitalEmployeeName'] = request.digital_employee_name
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.thread_id):
            body['threadId'] = request.thread_id
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChat',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat(
        self,
        request: main_models.CreateChatRequest,
    ) -> main_models.CreateChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_chat_with_options(request, headers, runtime)

    async def create_chat_async(
        self,
        request: main_models.CreateChatRequest,
    ) -> main_models.CreateChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_chat_with_options_async(request, headers, runtime)

    def create_digital_employee_with_options(
        self,
        request: main_models.CreateDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDigitalEmployeeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default_rule):
            body['defaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.knowledges):
            body['knowledges'] = request.knowledges
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role_arn):
            body['roleArn'] = request.role_arn
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDigitalEmployee',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digital-employee',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDigitalEmployeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_digital_employee_with_options_async(
        self,
        request: main_models.CreateDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDigitalEmployeeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default_rule):
            body['defaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.knowledges):
            body['knowledges'] = request.knowledges
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role_arn):
            body['roleArn'] = request.role_arn
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDigitalEmployee',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digital-employee',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDigitalEmployeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_digital_employee(
        self,
        request: main_models.CreateDigitalEmployeeRequest,
    ) -> main_models.CreateDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_digital_employee_with_options(request, headers, runtime)

    async def create_digital_employee_async(
        self,
        request: main_models.CreateDigitalEmployeeRequest,
    ) -> main_models.CreateDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_digital_employee_with_options_async(request, headers, runtime)

    def create_digital_employee_skill_with_options(
        self,
        name: str,
        request: main_models.CreateDigitalEmployeeSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDigitalEmployeeSkillResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        if not DaraCore.is_null(request.skill_name):
            body['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDigitalEmployeeSkill',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skill',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDigitalEmployeeSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_digital_employee_skill_with_options_async(
        self,
        name: str,
        request: main_models.CreateDigitalEmployeeSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDigitalEmployeeSkillResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        if not DaraCore.is_null(request.skill_name):
            body['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDigitalEmployeeSkill',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skill',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDigitalEmployeeSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_digital_employee_skill(
        self,
        name: str,
        request: main_models.CreateDigitalEmployeeSkillRequest,
    ) -> main_models.CreateDigitalEmployeeSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_digital_employee_skill_with_options(name, request, headers, runtime)

    async def create_digital_employee_skill_async(
        self,
        name: str,
        request: main_models.CreateDigitalEmployeeSkillRequest,
    ) -> main_models.CreateDigitalEmployeeSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_digital_employee_skill_with_options_async(name, request, headers, runtime)

    def create_thread_with_options(
        self,
        name: str,
        request: main_models.CreateThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateThreadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attributes):
            body['attributes'] = request.attributes
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateThread',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateThreadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_thread_with_options_async(
        self,
        name: str,
        request: main_models.CreateThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateThreadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attributes):
            body['attributes'] = request.attributes
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateThread',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateThreadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_thread(
        self,
        name: str,
        request: main_models.CreateThreadRequest,
    ) -> main_models.CreateThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_thread_with_options(name, request, headers, runtime)

    async def create_thread_async(
        self,
        name: str,
        request: main_models.CreateThreadRequest,
    ) -> main_models.CreateThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_thread_with_options_async(name, request, headers, runtime)

    def create_ticket_with_options(
        self,
        request: main_models.CreateTicketRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token_expiration_time):
            query['accessTokenExpirationTime'] = request.access_token_expiration_time
        if not DaraCore.is_null(request.expiration_time):
            query['expirationTime'] = request.expiration_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/tickets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: main_models.CreateTicketRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token_expiration_time):
            query['accessTokenExpirationTime'] = request.access_token_expiration_time
        if not DaraCore.is_null(request.expiration_time):
            query['expirationTime'] = request.expiration_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/tickets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ticket(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_ticket_with_options(request, headers, runtime)

    async def create_ticket_async(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_ticket_with_options_async(request, headers, runtime)

    def delete_digital_employee_with_options(
        self,
        name: str,
        request: main_models.DeleteDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDigitalEmployeeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDigitalEmployee',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDigitalEmployeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_digital_employee_with_options_async(
        self,
        name: str,
        request: main_models.DeleteDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDigitalEmployeeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDigitalEmployee',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDigitalEmployeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_digital_employee(
        self,
        name: str,
        request: main_models.DeleteDigitalEmployeeRequest,
    ) -> main_models.DeleteDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_digital_employee_with_options(name, request, headers, runtime)

    async def delete_digital_employee_async(
        self,
        name: str,
        request: main_models.DeleteDigitalEmployeeRequest,
    ) -> main_models.DeleteDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_digital_employee_with_options_async(name, request, headers, runtime)

    def delete_digital_employee_skill_with_options(
        self,
        name: str,
        skill_name: str,
        request: main_models.DeleteDigitalEmployeeSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDigitalEmployeeSkillResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDigitalEmployeeSkill',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDigitalEmployeeSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_digital_employee_skill_with_options_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.DeleteDigitalEmployeeSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDigitalEmployeeSkillResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDigitalEmployeeSkill',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDigitalEmployeeSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_digital_employee_skill(
        self,
        name: str,
        skill_name: str,
        request: main_models.DeleteDigitalEmployeeSkillRequest,
    ) -> main_models.DeleteDigitalEmployeeSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_digital_employee_skill_with_options(name, skill_name, request, headers, runtime)

    async def delete_digital_employee_skill_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.DeleteDigitalEmployeeSkillRequest,
    ) -> main_models.DeleteDigitalEmployeeSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_digital_employee_skill_with_options_async(name, skill_name, request, headers, runtime)

    def delete_thread_with_options(
        self,
        name: str,
        thread_id: str,
        request: main_models.DeleteThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteThreadResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteThread',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteThreadResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_thread_with_options_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.DeleteThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteThreadResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteThread',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteThreadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_thread(
        self,
        name: str,
        thread_id: str,
        request: main_models.DeleteThreadRequest,
    ) -> main_models.DeleteThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_thread_with_options(name, thread_id, request, headers, runtime)

    async def delete_thread_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.DeleteThreadRequest,
    ) -> main_models.DeleteThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_thread_with_options_async(name, thread_id, request, headers, runtime)

    def get_artifact_with_options(
        self,
        name: str,
        request: main_models.GetArtifactRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_path):
            query['artifactPath'] = request.artifact_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifact',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/artifact',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'binary'
        )
        res = main_models.GetArtifactResponse()
        tmp = self.call_api(params, req, runtime)
        if not DaraCore.is_null(tmp.get("body")):
            resp_body = DaraStream.to_readable(tmp.get("body"))
            res.body = resp_body
        if not DaraCore.is_null(tmp.get("headers")):
            resp_headers = tmp.get("headers")
            res.headers = Utils.stringify_map_value(resp_headers)
        if not DaraCore.is_null(tmp.get("statusCode")):
            status_code = int(tmp.get("statusCode"))
            res.status_code = status_code
        return res

    async def get_artifact_with_options_async(
        self,
        name: str,
        request: main_models.GetArtifactRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_path):
            query['artifactPath'] = request.artifact_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifact',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/artifact',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'binary'
        )
        res = main_models.GetArtifactResponse()
        tmp = await self.call_api_async(params, req, runtime)
        if not DaraCore.is_null(tmp.get("body")):
            resp_body = DaraStream.to_readable(tmp.get("body"))
            res.body = resp_body
        if not DaraCore.is_null(tmp.get("headers")):
            resp_headers = tmp.get("headers")
            res.headers = Utils.stringify_map_value(resp_headers)
        if not DaraCore.is_null(tmp.get("statusCode")):
            status_code = int(tmp.get("statusCode"))
            res.status_code = status_code
        return res

    def get_artifact(
        self,
        name: str,
        request: main_models.GetArtifactRequest,
    ) -> main_models.GetArtifactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_artifact_with_options(name, request, headers, runtime)

    async def get_artifact_async(
        self,
        name: str,
        request: main_models.GetArtifactRequest,
    ) -> main_models.GetArtifactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_artifact_with_options_async(name, request, headers, runtime)

    def get_digital_employee_with_options(
        self,
        name: str,
        request: main_models.GetDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDigitalEmployeeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDigitalEmployee',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDigitalEmployeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_digital_employee_with_options_async(
        self,
        name: str,
        request: main_models.GetDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDigitalEmployeeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDigitalEmployee',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDigitalEmployeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_digital_employee(
        self,
        name: str,
        request: main_models.GetDigitalEmployeeRequest,
    ) -> main_models.GetDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_digital_employee_with_options(name, request, headers, runtime)

    async def get_digital_employee_async(
        self,
        name: str,
        request: main_models.GetDigitalEmployeeRequest,
    ) -> main_models.GetDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_digital_employee_with_options_async(name, request, headers, runtime)

    def get_digital_employee_skill_with_options(
        self,
        name: str,
        skill_name: str,
        request: main_models.GetDigitalEmployeeSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDigitalEmployeeSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDigitalEmployeeSkill',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDigitalEmployeeSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_digital_employee_skill_with_options_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.GetDigitalEmployeeSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDigitalEmployeeSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDigitalEmployeeSkill',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDigitalEmployeeSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_digital_employee_skill(
        self,
        name: str,
        skill_name: str,
        request: main_models.GetDigitalEmployeeSkillRequest,
    ) -> main_models.GetDigitalEmployeeSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_digital_employee_skill_with_options(name, skill_name, request, headers, runtime)

    async def get_digital_employee_skill_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.GetDigitalEmployeeSkillRequest,
    ) -> main_models.GetDigitalEmployeeSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_digital_employee_skill_with_options_async(name, skill_name, request, headers, runtime)

    def get_thread_with_options(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetThreadResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetThread',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetThreadResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_thread_with_options_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetThreadResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetThread',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetThreadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_thread(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadRequest,
    ) -> main_models.GetThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_thread_with_options(name, thread_id, request, headers, runtime)

    async def get_thread_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadRequest,
    ) -> main_models.GetThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_thread_with_options_async(name, thread_id, request, headers, runtime)

    def get_thread_data_with_options(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetThreadDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetThreadData',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}/data',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetThreadDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_thread_data_with_options_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetThreadDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetThreadData',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}/data',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetThreadDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_thread_data(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadDataRequest,
    ) -> main_models.GetThreadDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_thread_data_with_options(name, thread_id, request, headers, runtime)

    async def get_thread_data_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.GetThreadDataRequest,
    ) -> main_models.GetThreadDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_thread_data_with_options_async(name, thread_id, request, headers, runtime)

    def list_artifacts_with_options(
        self,
        name: str,
        request: main_models.ListArtifactsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_path):
            query['artifactPath'] = request.artifact_path
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifacts',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/artifacts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifacts_with_options_async(
        self,
        name: str,
        request: main_models.ListArtifactsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_path):
            query['artifactPath'] = request.artifact_path
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifacts',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/artifacts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifacts(
        self,
        name: str,
        request: main_models.ListArtifactsRequest,
    ) -> main_models.ListArtifactsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_artifacts_with_options(name, request, headers, runtime)

    async def list_artifacts_async(
        self,
        name: str,
        request: main_models.ListArtifactsRequest,
    ) -> main_models.ListArtifactsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_artifacts_with_options_async(name, request, headers, runtime)

    def list_digital_employee_skill_versions_with_options(
        self,
        name: str,
        skill_name: str,
        request: main_models.ListDigitalEmployeeSkillVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDigitalEmployeeSkillVersionsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListDigitalEmployeeSkillVersions',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDigitalEmployeeSkillVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_digital_employee_skill_versions_with_options_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.ListDigitalEmployeeSkillVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDigitalEmployeeSkillVersionsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListDigitalEmployeeSkillVersions',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDigitalEmployeeSkillVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_digital_employee_skill_versions(
        self,
        name: str,
        skill_name: str,
        request: main_models.ListDigitalEmployeeSkillVersionsRequest,
    ) -> main_models.ListDigitalEmployeeSkillVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_digital_employee_skill_versions_with_options(name, skill_name, request, headers, runtime)

    async def list_digital_employee_skill_versions_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.ListDigitalEmployeeSkillVersionsRequest,
    ) -> main_models.ListDigitalEmployeeSkillVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_digital_employee_skill_versions_with_options_async(name, skill_name, request, headers, runtime)

    def list_digital_employee_skills_with_options(
        self,
        name: str,
        request: main_models.ListDigitalEmployeeSkillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDigitalEmployeeSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.skill_name):
            query['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDigitalEmployeeSkills',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skills',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDigitalEmployeeSkillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_digital_employee_skills_with_options_async(
        self,
        name: str,
        request: main_models.ListDigitalEmployeeSkillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDigitalEmployeeSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.skill_name):
            query['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDigitalEmployeeSkills',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skills',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDigitalEmployeeSkillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_digital_employee_skills(
        self,
        name: str,
        request: main_models.ListDigitalEmployeeSkillsRequest,
    ) -> main_models.ListDigitalEmployeeSkillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_digital_employee_skills_with_options(name, request, headers, runtime)

    async def list_digital_employee_skills_async(
        self,
        name: str,
        request: main_models.ListDigitalEmployeeSkillsRequest,
    ) -> main_models.ListDigitalEmployeeSkillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_digital_employee_skills_with_options_async(name, request, headers, runtime)

    def list_digital_employees_with_options(
        self,
        tmp_req: main_models.ListDigitalEmployeesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDigitalEmployeesResponse:
        tmp_req.validate()
        request = main_models.ListDigitalEmployeesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['displayName'] = request.display_name
        if not DaraCore.is_null(request.employee_type):
            query['employeeType'] = request.employee_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDigitalEmployees',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digital-employee',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDigitalEmployeesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_digital_employees_with_options_async(
        self,
        tmp_req: main_models.ListDigitalEmployeesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDigitalEmployeesResponse:
        tmp_req.validate()
        request = main_models.ListDigitalEmployeesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['displayName'] = request.display_name
        if not DaraCore.is_null(request.employee_type):
            query['employeeType'] = request.employee_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDigitalEmployees',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digital-employee',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDigitalEmployeesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_digital_employees(
        self,
        request: main_models.ListDigitalEmployeesRequest,
    ) -> main_models.ListDigitalEmployeesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_digital_employees_with_options(request, headers, runtime)

    async def list_digital_employees_async(
        self,
        request: main_models.ListDigitalEmployeesRequest,
    ) -> main_models.ListDigitalEmployeesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_digital_employees_with_options_async(request, headers, runtime)

    def list_threads_with_options(
        self,
        name: str,
        tmp_req: main_models.ListThreadsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListThreadsResponse:
        tmp_req.validate()
        request = main_models.ListThreadsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.thread_id):
            query['threadId'] = request.thread_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListThreads',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/threads',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListThreadsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_threads_with_options_async(
        self,
        name: str,
        tmp_req: main_models.ListThreadsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListThreadsResponse:
        tmp_req.validate()
        request = main_models.ListThreadsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.thread_id):
            query['threadId'] = request.thread_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListThreads',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/threads',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListThreadsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_threads(
        self,
        name: str,
        request: main_models.ListThreadsRequest,
    ) -> main_models.ListThreadsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_threads_with_options(name, request, headers, runtime)

    async def list_threads_async(
        self,
        name: str,
        request: main_models.ListThreadsRequest,
    ) -> main_models.ListThreadsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_threads_with_options_async(name, request, headers, runtime)

    def update_digital_employee_with_options(
        self,
        name: str,
        request: main_models.UpdateDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDigitalEmployeeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default_rule):
            body['defaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.knowledges):
            body['knowledges'] = request.knowledges
        if not DaraCore.is_null(request.role_arn):
            body['roleArn'] = request.role_arn
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDigitalEmployee',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDigitalEmployeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_digital_employee_with_options_async(
        self,
        name: str,
        request: main_models.UpdateDigitalEmployeeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDigitalEmployeeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default_rule):
            body['defaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.knowledges):
            body['knowledges'] = request.knowledges
        if not DaraCore.is_null(request.role_arn):
            body['roleArn'] = request.role_arn
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDigitalEmployee',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digital-employee/{DaraURL.percent_encode(name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDigitalEmployeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_digital_employee(
        self,
        name: str,
        request: main_models.UpdateDigitalEmployeeRequest,
    ) -> main_models.UpdateDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_digital_employee_with_options(name, request, headers, runtime)

    async def update_digital_employee_async(
        self,
        name: str,
        request: main_models.UpdateDigitalEmployeeRequest,
    ) -> main_models.UpdateDigitalEmployeeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_digital_employee_with_options_async(name, request, headers, runtime)

    def update_digital_employee_skill_with_options(
        self,
        name: str,
        skill_name: str,
        request: main_models.UpdateDigitalEmployeeSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDigitalEmployeeSkillResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDigitalEmployeeSkill',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDigitalEmployeeSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_digital_employee_skill_with_options_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.UpdateDigitalEmployeeSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDigitalEmployeeSkillResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDigitalEmployeeSkill',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/skill/{DaraURL.percent_encode(skill_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDigitalEmployeeSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_digital_employee_skill(
        self,
        name: str,
        skill_name: str,
        request: main_models.UpdateDigitalEmployeeSkillRequest,
    ) -> main_models.UpdateDigitalEmployeeSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_digital_employee_skill_with_options(name, skill_name, request, headers, runtime)

    async def update_digital_employee_skill_async(
        self,
        name: str,
        skill_name: str,
        request: main_models.UpdateDigitalEmployeeSkillRequest,
    ) -> main_models.UpdateDigitalEmployeeSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_digital_employee_skill_with_options_async(name, skill_name, request, headers, runtime)

    def update_thread_with_options(
        self,
        name: str,
        thread_id: str,
        request: main_models.UpdateThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateThreadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attributes):
            body['attributes'] = request.attributes
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateThread',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateThreadResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_thread_with_options_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.UpdateThreadRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateThreadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attributes):
            body['attributes'] = request.attributes
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateThread',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = f'/digitalEmployee/{DaraURL.percent_encode(name)}/thread/{DaraURL.percent_encode(thread_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateThreadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_thread(
        self,
        name: str,
        thread_id: str,
        request: main_models.UpdateThreadRequest,
    ) -> main_models.UpdateThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_thread_with_options(name, thread_id, request, headers, runtime)

    async def update_thread_async(
        self,
        name: str,
        thread_id: str,
        request: main_models.UpdateThreadRequest,
    ) -> main_models.UpdateThreadResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_thread_with_options_async(name, thread_id, request, headers, runtime)
