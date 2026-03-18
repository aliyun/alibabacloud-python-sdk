# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ExecuteAITeacherExpansionDialogueRefineRequest(DaraModel):
    def __init__(
        self,
        background: str = None,
        dialogue_tasks: List[main_models.ExecuteAITeacherExpansionDialogueRefineRequestDialogueTasks] = None,
        language_code: str = None,
        records: List[main_models.ExecuteAITeacherExpansionDialogueRefineRequestRecords] = None,
        role_info: main_models.ExecuteAITeacherExpansionDialogueRefineRequestRoleInfo = None,
        start_sentence: str = None,
        topic: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.background = background
        # This parameter is required.
        self.dialogue_tasks = dialogue_tasks
        self.language_code = language_code
        # This parameter is required.
        self.records = records
        # This parameter is required.
        self.role_info = role_info
        self.start_sentence = start_sentence
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.dialogue_tasks:
            for v1 in self.dialogue_tasks:
                 if v1:
                    v1.validate()
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()
        if self.role_info:
            self.role_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background is not None:
            result['background'] = self.background

        result['dialogueTasks'] = []
        if self.dialogue_tasks is not None:
            for k1 in self.dialogue_tasks:
                result['dialogueTasks'].append(k1.to_map() if k1 else None)

        if self.language_code is not None:
            result['languageCode'] = self.language_code

        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        if self.role_info is not None:
            result['roleInfo'] = self.role_info.to_map()

        if self.start_sentence is not None:
            result['startSentence'] = self.start_sentence

        if self.topic is not None:
            result['topic'] = self.topic

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('background') is not None:
            self.background = m.get('background')

        self.dialogue_tasks = []
        if m.get('dialogueTasks') is not None:
            for k1 in m.get('dialogueTasks'):
                temp_model = main_models.ExecuteAITeacherExpansionDialogueRefineRequestDialogueTasks()
                self.dialogue_tasks.append(temp_model.from_map(k1))

        if m.get('languageCode') is not None:
            self.language_code = m.get('languageCode')

        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.ExecuteAITeacherExpansionDialogueRefineRequestRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('roleInfo') is not None:
            temp_model = main_models.ExecuteAITeacherExpansionDialogueRefineRequestRoleInfo()
            self.role_info = temp_model.from_map(m.get('roleInfo'))

        if m.get('startSentence') is not None:
            self.start_sentence = m.get('startSentence')

        if m.get('topic') is not None:
            self.topic = m.get('topic')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class ExecuteAITeacherExpansionDialogueRefineRequestRoleInfo(DaraModel):
    def __init__(
        self,
        assistant: str = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assistant is not None:
            result['assistant'] = self.assistant

        if self.user is not None:
            result['user'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')

        if m.get('user') is not None:
            self.user = m.get('user')

        return self

class ExecuteAITeacherExpansionDialogueRefineRequestRecords(DaraModel):
    def __init__(
        self,
        content: str = None,
        is_off_topic_control: bool = None,
        is_on_topic: bool = None,
        order: int = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.is_off_topic_control = is_off_topic_control
        self.is_on_topic = is_on_topic
        # This parameter is required.
        self.order = order
        # This parameter is required.
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

        if self.is_off_topic_control is not None:
            result['isOffTopicControl'] = self.is_off_topic_control

        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic

        if self.order is not None:
            result['order'] = self.order

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('isOffTopicControl') is not None:
            self.is_off_topic_control = m.get('isOffTopicControl')

        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

class ExecuteAITeacherExpansionDialogueRefineRequestDialogueTasks(DaraModel):
    def __init__(
        self,
        assistant: str = None,
        assistant_translate: str = None,
        order: int = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        self.assistant_translate = assistant_translate
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assistant is not None:
            result['assistant'] = self.assistant

        if self.assistant_translate is not None:
            result['assistantTranslate'] = self.assistant_translate

        if self.order is not None:
            result['order'] = self.order

        if self.user is not None:
            result['user'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')

        if m.get('assistantTranslate') is not None:
            self.assistant_translate = m.get('assistantTranslate')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('user') is not None:
            self.user = m.get('user')

        return self

