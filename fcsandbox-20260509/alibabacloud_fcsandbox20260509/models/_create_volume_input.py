# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class CreateVolumeInput(DaraModel):
    def __init__(
        self,
        agentic_fsvolume_config: main_models.AgenticFSVolumeConfig = None,
        oss_volume_config: main_models.OSSVolumeConfig = None,
        team_id: str = None,
        volume_name: str = None,
    ):
        self.agentic_fsvolume_config = agentic_fsvolume_config
        self.oss_volume_config = oss_volume_config
        self.team_id = team_id
        self.volume_name = volume_name

    def validate(self):
        if self.agentic_fsvolume_config:
            self.agentic_fsvolume_config.validate()
        if self.oss_volume_config:
            self.oss_volume_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentic_fsvolume_config is not None:
            result['agenticFSVolumeConfig'] = self.agentic_fsvolume_config.to_map()

        if self.oss_volume_config is not None:
            result['ossVolumeConfig'] = self.oss_volume_config.to_map()

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.volume_name is not None:
            result['volumeName'] = self.volume_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agenticFSVolumeConfig') is not None:
            temp_model = main_models.AgenticFSVolumeConfig()
            self.agentic_fsvolume_config = temp_model.from_map(m.get('agenticFSVolumeConfig'))

        if m.get('ossVolumeConfig') is not None:
            temp_model = main_models.OSSVolumeConfig()
            self.oss_volume_config = temp_model.from_map(m.get('ossVolumeConfig'))

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')

        return self

