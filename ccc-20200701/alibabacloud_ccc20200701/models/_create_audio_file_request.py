# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAudioFileRequest(DaraModel):
    def __init__(
        self,
        audio_file_name: str = None,
        instance_id: str = None,
        name: str = None,
        oss_file_key: str = None,
        usage: str = None,
    ):
        # This parameter is required.
        self.audio_file_name = audio_file_name
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.oss_file_key = oss_file_key
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_file_name is not None:
            result['AudioFileName'] = self.audio_file_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_file_key is not None:
            result['OssFileKey'] = self.oss_file_key

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioFileName') is not None:
            self.audio_file_name = m.get('AudioFileName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssFileKey') is not None:
            self.oss_file_key = m.get('OssFileKey')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

