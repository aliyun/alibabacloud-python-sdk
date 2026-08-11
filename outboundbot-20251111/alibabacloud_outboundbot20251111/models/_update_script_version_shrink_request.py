# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateScriptVersionShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        interaction_config_shrink: str = None,
        label_configs_shrink: str = None,
        script_id: str = None,
        script_profile_shrink: str = None,
        synthesizer_config_shrink: str = None,
        transcriber_config_shrink: str = None,
        version_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 交互配置
        self.interaction_config_shrink = interaction_config_shrink
        # 草稿版本的标签配置（JSON字符串）
        self.label_configs_shrink = label_configs_shrink
        # 场景ID
        self.script_id = script_id
        # 话术配置
        self.script_profile_shrink = script_profile_shrink
        # 语音合成配置
        self.synthesizer_config_shrink = synthesizer_config_shrink
        # 语音识别配置
        self.transcriber_config_shrink = transcriber_config_shrink
        # 版本ID
        self.version_id = version_id

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

        if self.label_configs_shrink is not None:
            result['LabelConfigs'] = self.label_configs_shrink

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_profile_shrink is not None:
            result['ScriptProfile'] = self.script_profile_shrink

        if self.synthesizer_config_shrink is not None:
            result['SynthesizerConfig'] = self.synthesizer_config_shrink

        if self.transcriber_config_shrink is not None:
            result['TranscriberConfig'] = self.transcriber_config_shrink

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InteractionConfig') is not None:
            self.interaction_config_shrink = m.get('InteractionConfig')

        if m.get('LabelConfigs') is not None:
            self.label_configs_shrink = m.get('LabelConfigs')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptProfile') is not None:
            self.script_profile_shrink = m.get('ScriptProfile')

        if m.get('SynthesizerConfig') is not None:
            self.synthesizer_config_shrink = m.get('SynthesizerConfig')

        if m.get('TranscriberConfig') is not None:
            self.transcriber_config_shrink = m.get('TranscriberConfig')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

