# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class TongyiChatDebugInfoResponseBody(DaraModel):
    def __init__(
        self,
        message_id: str = None,
        pipeline: List[main_models.TongyiChatDebugInfoResponseBodyPipeline] = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.pipeline = pipeline
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.pipeline:
            for v1 in self.pipeline:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['MessageId'] = self.message_id

        result['Pipeline'] = []
        if self.pipeline is not None:
            for k1 in self.pipeline:
                result['Pipeline'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        self.pipeline = []
        if m.get('Pipeline') is not None:
            for k1 in m.get('Pipeline'):
                temp_model = main_models.TongyiChatDebugInfoResponseBodyPipeline()
                self.pipeline.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TongyiChatDebugInfoResponseBodyPipeline(DaraModel):
    def __init__(
        self,
        input: Any = None,
        name: str = None,
        node_type: str = None,
        output: Any = None,
    ):
        self.input = input
        self.name = name
        self.node_type = node_type
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input

        if self.name is not None:
            result['Name'] = self.name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.output is not None:
            result['Output'] = self.output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        return self

