# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ListTongyiConversationLogsResponseBody(DaraModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
        session_flow_debug_info: main_models.ListTongyiConversationLogsResponseBodySessionFlowDebugInfo = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id
        self.session_flow_debug_info = session_flow_debug_info

    def validate(self):
        if self.session_flow_debug_info:
            self.session_flow_debug_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time

        if self.datas is not None:
            result['Datas'] = self.datas

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_flow_debug_info is not None:
            result['SessionFlowDebugInfo'] = self.session_flow_debug_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')

        if m.get('Datas') is not None:
            self.datas = m.get('Datas')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionFlowDebugInfo') is not None:
            temp_model = main_models.ListTongyiConversationLogsResponseBodySessionFlowDebugInfo()
            self.session_flow_debug_info = temp_model.from_map(m.get('SessionFlowDebugInfo'))

        return self

class ListTongyiConversationLogsResponseBodySessionFlowDebugInfo(DaraModel):
    def __init__(
        self,
        api_params: Dict[str, Any] = None,
        slot_params: Dict[str, Any] = None,
    ):
        self.api_params = api_params
        self.slot_params = slot_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_params is not None:
            result['ApiParams'] = self.api_params

        if self.slot_params is not None:
            result['SlotParams'] = self.slot_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParams') is not None:
            self.api_params = m.get('ApiParams')

        if m.get('SlotParams') is not None:
            self.slot_params = m.get('SlotParams')

        return self

