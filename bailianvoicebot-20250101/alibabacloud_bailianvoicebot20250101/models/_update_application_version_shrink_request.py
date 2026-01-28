# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationVersionShrinkRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        business_unit_id: str = None,
        interaction_config_shrink: str = None,
        script_profile_shrink: str = None,
        synthesizer_config_shrink: str = None,
        transcriber_config_shrink: str = None,
        version_id: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.business_unit_id = business_unit_id
        self.interaction_config_shrink = interaction_config_shrink
        # This parameter is required.
        self.script_profile_shrink = script_profile_shrink
        self.synthesizer_config_shrink = synthesizer_config_shrink
        self.transcriber_config_shrink = transcriber_config_shrink
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.interaction_config_shrink is not None:
            result['InteractionConfig'] = self.interaction_config_shrink

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
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('InteractionConfig') is not None:
            self.interaction_config_shrink = m.get('InteractionConfig')

        if m.get('ScriptProfile') is not None:
            self.script_profile_shrink = m.get('ScriptProfile')

        if m.get('SynthesizerConfig') is not None:
            self.synthesizer_config_shrink = m.get('SynthesizerConfig')

        if m.get('TranscriberConfig') is not None:
            self.transcriber_config_shrink = m.get('TranscriberConfig')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

