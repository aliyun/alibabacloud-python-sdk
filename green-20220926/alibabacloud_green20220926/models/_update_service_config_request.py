# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceConfigRequest(DaraModel):
    def __init__(
        self,
        file_config: str = None,
        keyword_filter_libs: str = None,
        keyword_hit_libs: str = None,
        manual_machine_config: str = None,
        region_id: str = None,
        resource_type: str = None,
        scene: str = None,
        scene_config: str = None,
        service_code: str = None,
        service_config: str = None,
        video_config: str = None,
    ):
        self.file_config = file_config
        self.keyword_filter_libs = keyword_filter_libs
        self.keyword_hit_libs = keyword_hit_libs
        self.manual_machine_config = manual_machine_config
        self.region_id = region_id
        self.resource_type = resource_type
        self.scene = scene
        self.scene_config = scene_config
        self.service_code = service_code
        self.service_config = service_config
        self.video_config = video_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_config is not None:
            result['FileConfig'] = self.file_config

        if self.keyword_filter_libs is not None:
            result['KeywordFilterLibs'] = self.keyword_filter_libs

        if self.keyword_hit_libs is not None:
            result['KeywordHitLibs'] = self.keyword_hit_libs

        if self.manual_machine_config is not None:
            result['ManualMachineConfig'] = self.manual_machine_config

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.scene_config is not None:
            result['SceneConfig'] = self.scene_config

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config

        if self.video_config is not None:
            result['VideoConfig'] = self.video_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileConfig') is not None:
            self.file_config = m.get('FileConfig')

        if m.get('KeywordFilterLibs') is not None:
            self.keyword_filter_libs = m.get('KeywordFilterLibs')

        if m.get('KeywordHitLibs') is not None:
            self.keyword_hit_libs = m.get('KeywordHitLibs')

        if m.get('ManualMachineConfig') is not None:
            self.manual_machine_config = m.get('ManualMachineConfig')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SceneConfig') is not None:
            self.scene_config = m.get('SceneConfig')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')

        if m.get('VideoConfig') is not None:
            self.video_config = m.get('VideoConfig')

        return self

