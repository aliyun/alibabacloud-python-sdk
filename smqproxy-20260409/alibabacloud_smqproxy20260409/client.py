# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_gateway_mns.client import Client as GatewayClientClient
from alibabacloud_smqproxy20260409 import models as main_models
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
        self._product_id = 'SMQProxy'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'mns.cn-hangzhou.aliyuncs.com'
        }

    def batch_delete_message_with_options(
        self,
        queue_name: str,
        request: main_models.BatchDeleteMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.receipt_handles):
            body['ReceiptHandles'] = request.receipt_handles
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteMessageResponse(),
            self.execute(params, req, runtime)
        )

    async def batch_delete_message_with_options_async(
        self,
        queue_name: str,
        request: main_models.BatchDeleteMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.receipt_handles):
            body['ReceiptHandles'] = request.receipt_handles
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteMessageResponse(),
            await self.execute_async(params, req, runtime)
        )

    def batch_delete_message(
        self,
        queue_name: str,
        request: main_models.BatchDeleteMessageRequest,
    ) -> main_models.BatchDeleteMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_delete_message_with_options(queue_name, request, headers, runtime)

    async def batch_delete_message_async(
        self,
        queue_name: str,
        request: main_models.BatchDeleteMessageRequest,
    ) -> main_models.BatchDeleteMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_delete_message_with_options_async(queue_name, request, headers, runtime)

    def batch_peek_message_with_options(
        self,
        queue_name: str,
        request: main_models.BatchPeekMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchPeekMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.num_of_messages):
            query['numOfMessages'] = request.num_of_messages
        if not DaraCore.is_null(request.peekonly):
            query['peekonly'] = request.peekonly
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchPeekMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchPeekMessageResponse(),
            self.execute(params, req, runtime)
        )

    async def batch_peek_message_with_options_async(
        self,
        queue_name: str,
        request: main_models.BatchPeekMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchPeekMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.num_of_messages):
            query['numOfMessages'] = request.num_of_messages
        if not DaraCore.is_null(request.peekonly):
            query['peekonly'] = request.peekonly
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchPeekMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchPeekMessageResponse(),
            await self.execute_async(params, req, runtime)
        )

    def batch_peek_message(
        self,
        queue_name: str,
        request: main_models.BatchPeekMessageRequest,
    ) -> main_models.BatchPeekMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_peek_message_with_options(queue_name, request, headers, runtime)

    async def batch_peek_message_async(
        self,
        queue_name: str,
        request: main_models.BatchPeekMessageRequest,
    ) -> main_models.BatchPeekMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_peek_message_with_options_async(queue_name, request, headers, runtime)

    def batch_receive_message_with_options(
        self,
        queue_name: str,
        request: main_models.BatchReceiveMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchReceiveMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.num_of_messages):
            query['numOfMessages'] = request.num_of_messages
        if not DaraCore.is_null(request.waitseconds):
            query['waitseconds'] = request.waitseconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchReceiveMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchReceiveMessageResponse(),
            self.execute(params, req, runtime)
        )

    async def batch_receive_message_with_options_async(
        self,
        queue_name: str,
        request: main_models.BatchReceiveMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchReceiveMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.num_of_messages):
            query['numOfMessages'] = request.num_of_messages
        if not DaraCore.is_null(request.waitseconds):
            query['waitseconds'] = request.waitseconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchReceiveMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchReceiveMessageResponse(),
            await self.execute_async(params, req, runtime)
        )

    def batch_receive_message(
        self,
        queue_name: str,
        request: main_models.BatchReceiveMessageRequest,
    ) -> main_models.BatchReceiveMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_receive_message_with_options(queue_name, request, headers, runtime)

    async def batch_receive_message_async(
        self,
        queue_name: str,
        request: main_models.BatchReceiveMessageRequest,
    ) -> main_models.BatchReceiveMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_receive_message_with_options_async(queue_name, request, headers, runtime)

    def batch_send_message_with_options(
        self,
        queue_name: str,
        request: main_models.BatchSendMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchSendMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchSendMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSendMessageResponse(),
            self.execute(params, req, runtime)
        )

    async def batch_send_message_with_options_async(
        self,
        queue_name: str,
        request: main_models.BatchSendMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchSendMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchSendMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSendMessageResponse(),
            await self.execute_async(params, req, runtime)
        )

    def batch_send_message(
        self,
        queue_name: str,
        request: main_models.BatchSendMessageRequest,
    ) -> main_models.BatchSendMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_send_message_with_options(queue_name, request, headers, runtime)

    async def batch_send_message_async(
        self,
        queue_name: str,
        request: main_models.BatchSendMessageRequest,
    ) -> main_models.BatchSendMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_send_message_with_options_async(queue_name, request, headers, runtime)

    def change_message_visibility_with_options(
        self,
        queue_name: str,
        request: main_models.ChangeMessageVisibilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMessageVisibilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.receipt_handle):
            query['receiptHandle'] = request.receipt_handle
        if not DaraCore.is_null(request.visibility_timeout):
            query['visibilityTimeout'] = request.visibility_timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMessageVisibility',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMessageVisibilityResponse(),
            self.execute(params, req, runtime)
        )

    async def change_message_visibility_with_options_async(
        self,
        queue_name: str,
        request: main_models.ChangeMessageVisibilityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMessageVisibilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.receipt_handle):
            query['receiptHandle'] = request.receipt_handle
        if not DaraCore.is_null(request.visibility_timeout):
            query['visibilityTimeout'] = request.visibility_timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMessageVisibility',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMessageVisibilityResponse(),
            await self.execute_async(params, req, runtime)
        )

    def change_message_visibility(
        self,
        queue_name: str,
        request: main_models.ChangeMessageVisibilityRequest,
    ) -> main_models.ChangeMessageVisibilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.change_message_visibility_with_options(queue_name, request, headers, runtime)

    async def change_message_visibility_async(
        self,
        queue_name: str,
        request: main_models.ChangeMessageVisibilityRequest,
    ) -> main_models.ChangeMessageVisibilityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_message_visibility_with_options_async(queue_name, request, headers, runtime)

    def delete_message_with_options(
        self,
        queue_name: str,
        request: main_models.DeleteMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.receipt_handle):
            query['ReceiptHandle'] = request.receipt_handle
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessageResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_message_with_options_async(
        self,
        queue_name: str,
        request: main_models.DeleteMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.receipt_handle):
            query['ReceiptHandle'] = request.receipt_handle
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessageResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_message(
        self,
        queue_name: str,
        request: main_models.DeleteMessageRequest,
    ) -> main_models.DeleteMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_message_with_options(queue_name, request, headers, runtime)

    async def delete_message_async(
        self,
        queue_name: str,
        request: main_models.DeleteMessageRequest,
    ) -> main_models.DeleteMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_message_with_options_async(queue_name, request, headers, runtime)

    def peek_message_with_options(
        self,
        queue_name: str,
        request: main_models.PeekMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PeekMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.peekonly):
            query['peekonly'] = request.peekonly
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PeekMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PeekMessageResponse(),
            self.execute(params, req, runtime)
        )

    async def peek_message_with_options_async(
        self,
        queue_name: str,
        request: main_models.PeekMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PeekMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.peekonly):
            query['peekonly'] = request.peekonly
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PeekMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PeekMessageResponse(),
            await self.execute_async(params, req, runtime)
        )

    def peek_message(
        self,
        queue_name: str,
        request: main_models.PeekMessageRequest,
    ) -> main_models.PeekMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.peek_message_with_options(queue_name, request, headers, runtime)

    async def peek_message_async(
        self,
        queue_name: str,
        request: main_models.PeekMessageRequest,
    ) -> main_models.PeekMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.peek_message_with_options_async(queue_name, request, headers, runtime)

    def publish_message_with_options(
        self,
        topic_name: str,
        request: main_models.PublishMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.message_attributes):
            body['MessageAttributes'] = request.message_attributes
        if not DaraCore.is_null(request.message_body):
            body['MessageBody'] = request.message_body
        if not DaraCore.is_null(request.message_tag):
            body['MessageTag'] = request.message_tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/topics/{topic_name}/messages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishMessageResponse(),
            self.execute(params, req, runtime)
        )

    async def publish_message_with_options_async(
        self,
        topic_name: str,
        request: main_models.PublishMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.message_attributes):
            body['MessageAttributes'] = request.message_attributes
        if not DaraCore.is_null(request.message_body):
            body['MessageBody'] = request.message_body
        if not DaraCore.is_null(request.message_tag):
            body['MessageTag'] = request.message_tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/topics/{topic_name}/messages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishMessageResponse(),
            await self.execute_async(params, req, runtime)
        )

    def publish_message(
        self,
        topic_name: str,
        request: main_models.PublishMessageRequest,
    ) -> main_models.PublishMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_message_with_options(topic_name, request, headers, runtime)

    async def publish_message_async(
        self,
        topic_name: str,
        request: main_models.PublishMessageRequest,
    ) -> main_models.PublishMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_message_with_options_async(topic_name, request, headers, runtime)

    def receive_message_with_options(
        self,
        queue_name: str,
        request: main_models.ReceiveMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReceiveMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.waitseconds):
            query['waitseconds'] = request.waitseconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReceiveMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReceiveMessageResponse(),
            self.execute(params, req, runtime)
        )

    async def receive_message_with_options_async(
        self,
        queue_name: str,
        request: main_models.ReceiveMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReceiveMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.waitseconds):
            query['waitseconds'] = request.waitseconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReceiveMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReceiveMessageResponse(),
            await self.execute_async(params, req, runtime)
        )

    def receive_message(
        self,
        queue_name: str,
        request: main_models.ReceiveMessageRequest,
    ) -> main_models.ReceiveMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.receive_message_with_options(queue_name, request, headers, runtime)

    async def receive_message_async(
        self,
        queue_name: str,
        request: main_models.ReceiveMessageRequest,
    ) -> main_models.ReceiveMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.receive_message_with_options_async(queue_name, request, headers, runtime)

    def send_message_with_options(
        self,
        queue_name: str,
        request: main_models.SendMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.delay_seconds):
            body['DelaySeconds'] = request.delay_seconds
        if not DaraCore.is_null(request.message_body):
            body['MessageBody'] = request.message_body
        if not DaraCore.is_null(request.message_group_id):
            body['MessageGroupId'] = request.message_group_id
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.user_properties):
            body['UserProperties'] = request.user_properties
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMessageResponse(),
            self.execute(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        queue_name: str,
        request: main_models.SendMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.delay_seconds):
            body['DelaySeconds'] = request.delay_seconds
        if not DaraCore.is_null(request.message_body):
            body['MessageBody'] = request.message_body
        if not DaraCore.is_null(request.message_group_id):
            body['MessageGroupId'] = request.message_group_id
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.user_properties):
            body['UserProperties'] = request.user_properties
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = '2026-04-09',
            protocol = 'HTTPS',
            pathname = f'/queues/{queue_name}/messages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMessageResponse(),
            await self.execute_async(params, req, runtime)
        )

    def send_message(
        self,
        queue_name: str,
        request: main_models.SendMessageRequest,
    ) -> main_models.SendMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_message_with_options(queue_name, request, headers, runtime)

    async def send_message_async(
        self,
        queue_name: str,
        request: main_models.SendMessageRequest,
    ) -> main_models.SendMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_message_with_options_async(queue_name, request, headers, runtime)
