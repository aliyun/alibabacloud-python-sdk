# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class CreateDialogAnalysisTaskRequest(DaraModel):
    def __init__(
        self,
        analysis_nodes: List[str] = None,
        conversation_list: List[main_models.CreateDialogAnalysisTaskRequestConversationList] = None,
        meta_data: Dict[str, Any] = None,
        play_code: str = None,
        request_id: str = None,
    ):
        self.analysis_nodes = analysis_nodes
        # This parameter is required.
        self.conversation_list = conversation_list
        self.meta_data = meta_data
        # This parameter is required.
        self.play_code = play_code
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.conversation_list:
            for v1 in self.conversation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_nodes is not None:
            result['analysisNodes'] = self.analysis_nodes

        result['conversationList'] = []
        if self.conversation_list is not None:
            for k1 in self.conversation_list:
                result['conversationList'].append(k1.to_map() if k1 else None)

        if self.meta_data is not None:
            result['metaData'] = self.meta_data

        if self.play_code is not None:
            result['playCode'] = self.play_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisNodes') is not None:
            self.analysis_nodes = m.get('analysisNodes')

        self.conversation_list = []
        if m.get('conversationList') is not None:
            for k1 in m.get('conversationList'):
                temp_model = main_models.CreateDialogAnalysisTaskRequestConversationList()
                self.conversation_list.append(temp_model.from_map(k1))

        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')

        if m.get('playCode') is not None:
            self.play_code = m.get('playCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateDialogAnalysisTaskRequestConversationList(DaraModel):
    def __init__(
        self,
        dialogue_list: List[main_models.CreateDialogAnalysisTaskRequestConversationListDialogueList] = None,
    ):
        # This parameter is required.
        self.dialogue_list = dialogue_list

    def validate(self):
        if self.dialogue_list:
            for v1 in self.dialogue_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k1 in self.dialogue_list:
                result['dialogueList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k1 in m.get('dialogueList'):
                temp_model = main_models.CreateDialogAnalysisTaskRequestConversationListDialogueList()
                self.dialogue_list.append(temp_model.from_map(k1))

        return self

class CreateDialogAnalysisTaskRequestConversationListDialogueList(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
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

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

