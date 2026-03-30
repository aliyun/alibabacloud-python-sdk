# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCloneVoiceRequest(DaraModel):
    def __init__(
        self,
        clone_voice_id: str = None,
        instance_id: str = None,
    ):
        self.clone_voice_id = clone_voice_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clone_voice_id is not None:
            result['CloneVoiceId'] = self.clone_voice_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloneVoiceId') is not None:
            self.clone_voice_id = m.get('CloneVoiceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

