# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class RunHotTopicChatRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        generate_options: List[str] = None,
        hot_topic_version: str = None,
        hot_topics: List[str] = None,
        image_count: int = None,
        messages: List[main_models.RunHotTopicChatRequestMessages] = None,
        model_custom_prompt_template: str = None,
        model_id: str = None,
        original_session_id: str = None,
        prompt: str = None,
        step_for_broadcast_content_config: main_models.RunHotTopicChatRequestStepForBroadcastContentConfig = None,
        task_id: str = None,
    ):
        self.category = category
        self.generate_options = generate_options
        self.hot_topic_version = hot_topic_version
        self.hot_topics = hot_topics
        self.image_count = image_count
        self.messages = messages
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.prompt = prompt
        self.step_for_broadcast_content_config = step_for_broadcast_content_config
        self.task_id = task_id

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.step_for_broadcast_content_config:
            self.step_for_broadcast_content_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.generate_options is not None:
            result['generateOptions'] = self.generate_options

        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version

        if self.hot_topics is not None:
            result['hotTopics'] = self.hot_topics

        if self.image_count is not None:
            result['imageCount'] = self.image_count

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.original_session_id is not None:
            result['originalSessionId'] = self.original_session_id

        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.step_for_broadcast_content_config is not None:
            result['stepForBroadcastContentConfig'] = self.step_for_broadcast_content_config.to_map()

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('generateOptions') is not None:
            self.generate_options = m.get('generateOptions')

        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')

        if m.get('hotTopics') is not None:
            self.hot_topics = m.get('hotTopics')

        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.RunHotTopicChatRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('originalSessionId') is not None:
            self.original_session_id = m.get('originalSessionId')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('stepForBroadcastContentConfig') is not None:
            temp_model = main_models.RunHotTopicChatRequestStepForBroadcastContentConfig()
            self.step_for_broadcast_content_config = temp_model.from_map(m.get('stepForBroadcastContentConfig'))

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class RunHotTopicChatRequestStepForBroadcastContentConfig(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        custom_hot_value_weights: List[main_models.RunHotTopicChatRequestStepForBroadcastContentConfigCustomHotValueWeights] = None,
        topic_count: int = None,
    ):
        self.categories = categories
        self.custom_hot_value_weights = custom_hot_value_weights
        self.topic_count = topic_count

    def validate(self):
        if self.custom_hot_value_weights:
            for v1 in self.custom_hot_value_weights:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['categories'] = self.categories

        result['customHotValueWeights'] = []
        if self.custom_hot_value_weights is not None:
            for k1 in self.custom_hot_value_weights:
                result['customHotValueWeights'].append(k1.to_map() if k1 else None)

        if self.topic_count is not None:
            result['topicCount'] = self.topic_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categories') is not None:
            self.categories = m.get('categories')

        self.custom_hot_value_weights = []
        if m.get('customHotValueWeights') is not None:
            for k1 in m.get('customHotValueWeights'):
                temp_model = main_models.RunHotTopicChatRequestStepForBroadcastContentConfigCustomHotValueWeights()
                self.custom_hot_value_weights.append(temp_model.from_map(k1))

        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')

        return self

class RunHotTopicChatRequestStepForBroadcastContentConfigCustomHotValueWeights(DaraModel):
    def __init__(
        self,
        dimension: str = None,
        weight: int = None,
    ):
        self.dimension = dimension
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['dimension'] = self.dimension

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class RunHotTopicChatRequestMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        role: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

