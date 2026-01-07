# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunHotTopicChatShrinkRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        generate_options_shrink: str = None,
        hot_topic_version: str = None,
        hot_topics_shrink: str = None,
        image_count: int = None,
        messages_shrink: str = None,
        model_custom_prompt_template: str = None,
        model_id: str = None,
        original_session_id: str = None,
        prompt: str = None,
        step_for_broadcast_content_config_shrink: str = None,
        task_id: str = None,
    ):
        self.category = category
        self.generate_options_shrink = generate_options_shrink
        self.hot_topic_version = hot_topic_version
        self.hot_topics_shrink = hot_topics_shrink
        self.image_count = image_count
        self.messages_shrink = messages_shrink
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.prompt = prompt
        self.step_for_broadcast_content_config_shrink = step_for_broadcast_content_config_shrink
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.generate_options_shrink is not None:
            result['generateOptions'] = self.generate_options_shrink

        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version

        if self.hot_topics_shrink is not None:
            result['hotTopics'] = self.hot_topics_shrink

        if self.image_count is not None:
            result['imageCount'] = self.image_count

        if self.messages_shrink is not None:
            result['messages'] = self.messages_shrink

        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.original_session_id is not None:
            result['originalSessionId'] = self.original_session_id

        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.step_for_broadcast_content_config_shrink is not None:
            result['stepForBroadcastContentConfig'] = self.step_for_broadcast_content_config_shrink

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('generateOptions') is not None:
            self.generate_options_shrink = m.get('generateOptions')

        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')

        if m.get('hotTopics') is not None:
            self.hot_topics_shrink = m.get('hotTopics')

        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')

        if m.get('messages') is not None:
            self.messages_shrink = m.get('messages')

        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('originalSessionId') is not None:
            self.original_session_id = m.get('originalSessionId')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('stepForBroadcastContentConfig') is not None:
            self.step_for_broadcast_content_config_shrink = m.get('stepForBroadcastContentConfig')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

