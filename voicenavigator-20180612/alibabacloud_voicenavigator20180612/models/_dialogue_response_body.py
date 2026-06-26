# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DialogueResponseBody(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        interruptible: bool = None,
        request_id: str = None,
        text_response: str = None,
    ):
        # The action to be performed.
        self.action = action
        # The action parameters.
        self.action_params = action_params
        # Indicates whether the IVR greeting can be interrupted.
        self.interruptible = interruptible
        # The request ID.
        self.request_id = request_id
        # The text to be broadcasted.
        self.text_response = text_response

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_params is not None:
            result['ActionParams'] = self.action_params

        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.text_response is not None:
            result['TextResponse'] = self.text_response

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')

        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TextResponse') is not None:
            self.text_response = m.get('TextResponse')

        return self

