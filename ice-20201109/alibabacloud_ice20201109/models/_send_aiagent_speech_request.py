# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendAIAgentSpeechRequest(DaraModel):
    def __init__(
        self,
        enable_interrupt: bool = None,
        instance_id: str = None,
        text: str = None,
        type: str = None,
    ):
        # Specifies whether the broadcast can interrupt the ongoing speech. Default value: true
        self.enable_interrupt = enable_interrupt
        # Agent instance ID.
        # 
        # > The InstanceId is the unique ID returned after successfully starting an agent instance. For details about starting an agent instance, see [StartAIAgentInstance](https://help.aliyun.com/document_detail/2846201.html) and [GenerateAIAgentCall](https://help.aliyun.com/document_detail/2846209.html).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The text content to be played back. The supported input format varies based on the Type parameter. The length cannot exceed 1024 characters.
        # 
        # This parameter is required.
        self.text = text
        # Input type. Valid values:
        # 
        # - Text: Input is plain text.
        # 
        # - AudioUrl: Input is an audio URL.
        # 
        # Default value: Text.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_interrupt is not None:
            result['EnableInterrupt'] = self.enable_interrupt

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInterrupt') is not None:
            self.enable_interrupt = m.get('EnableInterrupt')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

