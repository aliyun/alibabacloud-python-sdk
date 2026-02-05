# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyScriptVoiceConfigRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        script_voice_config_id: str = None,
        script_waveform_relation: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.script_id = script_id
        # This parameter is required.
        self.script_voice_config_id = script_voice_config_id
        self.script_waveform_relation = script_waveform_relation
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_voice_config_id is not None:
            result['ScriptVoiceConfigId'] = self.script_voice_config_id

        if self.script_waveform_relation is not None:
            result['ScriptWaveformRelation'] = self.script_waveform_relation

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptVoiceConfigId') is not None:
            self.script_voice_config_id = m.get('ScriptVoiceConfigId')

        if m.get('ScriptWaveformRelation') is not None:
            self.script_waveform_relation = m.get('ScriptWaveformRelation')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

