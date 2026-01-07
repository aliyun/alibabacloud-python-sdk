# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class RealtimeDialogAssistRequest(DaraModel):
    def __init__(
        self,
        analysis: bool = None,
        biz_type: str = None,
        conversation_model: List[main_models.RealtimeDialogAssistRequestConversationModel] = None,
        dialog_memory_turns: int = None,
        hang_up_dialog: bool = None,
        meta_data: Dict[str, Any] = None,
        request_id: str = None,
        script_content_played: str = None,
        session_id: str = None,
        user_vad: bool = None,
    ):
        self.analysis = analysis
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.conversation_model = conversation_model
        self.dialog_memory_turns = dialog_memory_turns
        self.hang_up_dialog = hang_up_dialog
        # metaData
        self.meta_data = meta_data
        # This parameter is required.
        self.request_id = request_id
        self.script_content_played = script_content_played
        # This parameter is required.
        self.session_id = session_id
        self.user_vad = user_vad

    def validate(self):
        if self.conversation_model:
            for v1 in self.conversation_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis is not None:
            result['analysis'] = self.analysis

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        result['conversationModel'] = []
        if self.conversation_model is not None:
            for k1 in self.conversation_model:
                result['conversationModel'].append(k1.to_map() if k1 else None)

        if self.dialog_memory_turns is not None:
            result['dialogMemoryTurns'] = self.dialog_memory_turns

        if self.hang_up_dialog is not None:
            result['hangUpDialog'] = self.hang_up_dialog

        if self.meta_data is not None:
            result['metaData'] = self.meta_data

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.script_content_played is not None:
            result['scriptContentPlayed'] = self.script_content_played

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.user_vad is not None:
            result['userVad'] = self.user_vad

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis') is not None:
            self.analysis = m.get('analysis')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        self.conversation_model = []
        if m.get('conversationModel') is not None:
            for k1 in m.get('conversationModel'):
                temp_model = main_models.RealtimeDialogAssistRequestConversationModel()
                self.conversation_model.append(temp_model.from_map(k1))

        if m.get('dialogMemoryTurns') is not None:
            self.dialog_memory_turns = m.get('dialogMemoryTurns')

        if m.get('hangUpDialog') is not None:
            self.hang_up_dialog = m.get('hangUpDialog')

        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scriptContentPlayed') is not None:
            self.script_content_played = m.get('scriptContentPlayed')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('userVad') is not None:
            self.user_vad = m.get('userVad')

        return self

class RealtimeDialogAssistRequestConversationModel(DaraModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        end: int = None,
        role: int = None,
        type: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        # This parameter is required.
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.end = end
        # This parameter is required.
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['begin'] = self.begin

        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.content is not None:
            result['content'] = self.content

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id

        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type

        if self.end is not None:
            result['end'] = self.end

        if self.role is not None:
            result['role'] = self.role

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('begin') is not None:
            self.begin = m.get('begin')

        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')

        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

