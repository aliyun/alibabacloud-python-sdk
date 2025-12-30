# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ForwardAIAgentCallRequest(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        caller_number: str = None,
        error_prompt: str = None,
        instance_id: str = None,
        transfer_prompt: str = None,
    ):
        self.called_number = called_number
        self.caller_number = caller_number
        self.error_prompt = error_prompt
        self.instance_id = instance_id
        self.transfer_prompt = transfer_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.error_prompt is not None:
            result['ErrorPrompt'] = self.error_prompt

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.transfer_prompt is not None:
            result['TransferPrompt'] = self.transfer_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('ErrorPrompt') is not None:
            self.error_prompt = m.get('ErrorPrompt')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TransferPrompt') is not None:
            self.transfer_prompt = m.get('TransferPrompt')

        return self

