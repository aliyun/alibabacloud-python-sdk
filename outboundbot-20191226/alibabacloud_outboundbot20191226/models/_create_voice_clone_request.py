# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVoiceCloneRequest(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        instance_id: str = None,
        model: str = None,
        voice_name: str = None,
    ):
        # The Folder field returned after a file is uploaded by calling the GetJobDataUploadParams operation.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The model used for voice cloning.
        self.model = model
        # The name of the cloned voice. The names of enabled voices within the same instance must be unique.
        # 
        # This parameter is required.
        self.voice_name = voice_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.voice_name is not None:
            result['VoiceName'] = self.voice_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('VoiceName') is not None:
            self.voice_name = m.get('VoiceName')

        return self

