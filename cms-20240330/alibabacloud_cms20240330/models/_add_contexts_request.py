# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AddContextsRequest(DaraModel):
    def __init__(
        self,
        context_type: str = None,
        items: List[main_models.AddContextsRequestItems] = None,
        memory_type: str = None,
    ):
        # The context type.
        # 
        # This parameter is required.
        self.context_type = context_type
        # An array of context items.
        # 
        # This parameter is required.
        self.items = items
        # The memory type.
        self.memory_type = memory_type

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_type is not None:
            result['contextType'] = self.context_type

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.memory_type is not None:
            result['memoryType'] = self.memory_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contextType') is not None:
            self.context_type = m.get('contextType')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.AddContextsRequestItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('memoryType') is not None:
            self.memory_type = m.get('memoryType')

        return self

class AddContextsRequestItems(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        app_id: str = None,
        categories: List[str] = None,
        content: str = None,
        custom_instructions: str = None,
        experience: Dict[str, Any] = None,
        expiration_date: str = None,
        immutable: bool = None,
        infer: bool = None,
        labels: Dict[str, str] = None,
        messages: List[Dict[str, Any]] = None,
        metadata: Dict[str, Any] = None,
        run_id: str = None,
        timestamp: int = None,
        trigger_condition: str = None,
        user_id: str = None,
    ):
        # The unique agent ID.
        self.agent_id = agent_id
        # The application ID.
        self.app_id = app_id
        # A list of categories to apply to the context item.
        self.categories = categories
        # The content of the context item.
        self.content = content
        # The custom instructions for processing the context.
        self.custom_instructions = custom_instructions
        # An object containing experience information for the context.
        self.experience = experience
        # The expiration timestamp for the context item.
        self.expiration_date = expiration_date
        # Specifies whether the context item is immutable. If set to `true`, the item cannot be changed after it is created. The default value is `false`.
        self.immutable = immutable
        # Specifies whether to perform inference based on the context. The default value is `false`.
        self.infer = infer
        # A map of key-value pairs to apply as labels.
        self.labels = labels
        # An array of message objects.
        self.messages = messages
        # Key-value pairs to store as metadata.
        self.metadata = metadata
        # The run ID.
        self.run_id = run_id
        # The timestamp of the context item.
        self.timestamp = timestamp
        # The condition that triggers the context.
        self.trigger_condition = trigger_condition
        # The unique user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.categories is not None:
            result['categories'] = self.categories

        if self.content is not None:
            result['content'] = self.content

        if self.custom_instructions is not None:
            result['customInstructions'] = self.custom_instructions

        if self.experience is not None:
            result['experience'] = self.experience

        if self.expiration_date is not None:
            result['expirationDate'] = self.expiration_date

        if self.immutable is not None:
            result['immutable'] = self.immutable

        if self.infer is not None:
            result['infer'] = self.infer

        if self.labels is not None:
            result['labels'] = self.labels

        if self.messages is not None:
            result['messages'] = self.messages

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.trigger_condition is not None:
            result['triggerCondition'] = self.trigger_condition

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('categories') is not None:
            self.categories = m.get('categories')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('customInstructions') is not None:
            self.custom_instructions = m.get('customInstructions')

        if m.get('experience') is not None:
            self.experience = m.get('experience')

        if m.get('expirationDate') is not None:
            self.expiration_date = m.get('expirationDate')

        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')

        if m.get('infer') is not None:
            self.infer = m.get('infer')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('messages') is not None:
            self.messages = m.get('messages')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('triggerCondition') is not None:
            self.trigger_condition = m.get('triggerCondition')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

