# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScriptVersionShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        interaction_config_shrink: str = None,
        label_config_shrink: str = None,
        script_id: str = None,
        script_profile_shrink: str = None,
        source_version_id: str = None,
        synthesizer_config_shrink: str = None,
        transcriber_config_shrink: str = None,
    ):
        self.instance_id = instance_id
        self.interaction_config_shrink = interaction_config_shrink
        self.label_config_shrink = label_config_shrink
        self.script_id = script_id
        self.script_profile_shrink = script_profile_shrink
        self.source_version_id = source_version_id
        self.synthesizer_config_shrink = synthesizer_config_shrink
        self.transcriber_config_shrink = transcriber_config_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interaction_config_shrink is not None:
            result['InteractionConfig'] = self.interaction_config_shrink

        if self.label_config_shrink is not None:
            result['LabelConfig'] = self.label_config_shrink

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_profile_shrink is not None:
            result['ScriptProfile'] = self.script_profile_shrink

        if self.source_version_id is not None:
            result['SourceVersionId'] = self.source_version_id

        if self.synthesizer_config_shrink is not None:
            result['SynthesizerConfig'] = self.synthesizer_config_shrink

        if self.transcriber_config_shrink is not None:
            result['TranscriberConfig'] = self.transcriber_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InteractionConfig') is not None:
            self.interaction_config_shrink = m.get('InteractionConfig')

        if m.get('LabelConfig') is not None:
            self.label_config_shrink = m.get('LabelConfig')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptProfile') is not None:
            self.script_profile_shrink = m.get('ScriptProfile')

        if m.get('SourceVersionId') is not None:
            self.source_version_id = m.get('SourceVersionId')

        if m.get('SynthesizerConfig') is not None:
            self.synthesizer_config_shrink = m.get('SynthesizerConfig')

        if m.get('TranscriberConfig') is not None:
            self.transcriber_config_shrink = m.get('TranscriberConfig')

        return self

