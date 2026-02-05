# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListDialogueFlowsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        dialogue_flows: List[main_models.ListDialogueFlowsResponseBodyDialogueFlows] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dialogue_flows = dialogue_flows
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.dialogue_flows:
            for v1 in self.dialogue_flows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['DialogueFlows'] = []
        if self.dialogue_flows is not None:
            for k1 in self.dialogue_flows:
                result['DialogueFlows'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.dialogue_flows = []
        if m.get('DialogueFlows') is not None:
            for k1 in m.get('DialogueFlows'):
                temp_model = main_models.ListDialogueFlowsResponseBodyDialogueFlows()
                self.dialogue_flows.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDialogueFlowsResponseBodyDialogueFlows(DaraModel):
    def __init__(
        self,
        dialogue_flow_definition: str = None,
        dialogue_flow_id: str = None,
        dialogue_flow_name: str = None,
        dialogue_flow_type: str = None,
        script_id: str = None,
        script_version: str = None,
    ):
        self.dialogue_flow_definition = dialogue_flow_definition
        self.dialogue_flow_id = dialogue_flow_id
        self.dialogue_flow_name = dialogue_flow_name
        self.dialogue_flow_type = dialogue_flow_type
        self.script_id = script_id
        self.script_version = script_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialogue_flow_definition is not None:
            result['DialogueFlowDefinition'] = self.dialogue_flow_definition

        if self.dialogue_flow_id is not None:
            result['DialogueFlowId'] = self.dialogue_flow_id

        if self.dialogue_flow_name is not None:
            result['DialogueFlowName'] = self.dialogue_flow_name

        if self.dialogue_flow_type is not None:
            result['DialogueFlowType'] = self.dialogue_flow_type

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_version is not None:
            result['ScriptVersion'] = self.script_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogueFlowDefinition') is not None:
            self.dialogue_flow_definition = m.get('DialogueFlowDefinition')

        if m.get('DialogueFlowId') is not None:
            self.dialogue_flow_id = m.get('DialogueFlowId')

        if m.get('DialogueFlowName') is not None:
            self.dialogue_flow_name = m.get('DialogueFlowName')

        if m.get('DialogueFlowType') is not None:
            self.dialogue_flow_type = m.get('DialogueFlowType')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptVersion') is not None:
            self.script_version = m.get('ScriptVersion')

        return self

