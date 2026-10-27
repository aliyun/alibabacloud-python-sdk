# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateMemoryStoreResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateMemoryStoreResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The MemoryStore details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.UpdateMemoryStoreResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class UpdateMemoryStoreResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        extract_instructions: str = None,
        memory_store_id: str = None,
        memory_store_name: str = None,
        status: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The creation time.
        self.created_at = created_at
        # The MemoryStore description.
        self.description = description
        # The custom extraction instructions.
        self.extract_instructions = extract_instructions
        # The MemoryStore ID.
        self.memory_store_id = memory_store_id
        # The MemoryStore name. It cannot be modified after creation.
        self.memory_store_name = memory_store_name
        # The lifecycle status of the MemoryStore.
        self.status = status
        # The last updated time.
        self.updated_at = updated_at
        # The AgentCore workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.extract_instructions is not None:
            result['extractInstructions'] = self.extract_instructions

        if self.memory_store_id is not None:
            result['memoryStoreId'] = self.memory_store_id

        if self.memory_store_name is not None:
            result['memoryStoreName'] = self.memory_store_name

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('extractInstructions') is not None:
            self.extract_instructions = m.get('extractInstructions')

        if m.get('memoryStoreId') is not None:
            self.memory_store_id = m.get('memoryStoreId')

        if m.get('memoryStoreName') is not None:
            self.memory_store_name = m.get('memoryStoreName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

