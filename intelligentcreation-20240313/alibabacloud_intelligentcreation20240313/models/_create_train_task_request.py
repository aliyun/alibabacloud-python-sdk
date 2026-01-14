# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTrainTaskRequest(DaraModel):
    def __init__(
        self,
        aliyun_main_id: str = None,
        res_spec_type: str = None,
        task_type: str = None,
        use_scene: str = None,
        voice_gender: str = None,
        voice_language: str = None,
        voice_name: str = None,
        voice_path: str = None,
    ):
        self.aliyun_main_id = aliyun_main_id
        self.res_spec_type = res_spec_type
        self.task_type = task_type
        self.use_scene = use_scene
        self.voice_gender = voice_gender
        self.voice_language = voice_language
        self.voice_name = voice_name
        self.voice_path = voice_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_main_id is not None:
            result['aliyunMainId'] = self.aliyun_main_id

        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type

        if self.task_type is not None:
            result['taskType'] = self.task_type

        if self.use_scene is not None:
            result['useScene'] = self.use_scene

        if self.voice_gender is not None:
            result['voiceGender'] = self.voice_gender

        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language

        if self.voice_name is not None:
            result['voiceName'] = self.voice_name

        if self.voice_path is not None:
            result['voicePath'] = self.voice_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunMainId') is not None:
            self.aliyun_main_id = m.get('aliyunMainId')

        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')

        if m.get('voiceGender') is not None:
            self.voice_gender = m.get('voiceGender')

        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')

        if m.get('voiceName') is not None:
            self.voice_name = m.get('voiceName')

        if m.get('voicePath') is not None:
            self.voice_path = m.get('voicePath')

        return self

