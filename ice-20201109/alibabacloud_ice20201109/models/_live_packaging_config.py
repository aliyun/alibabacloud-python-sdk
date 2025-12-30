# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class LivePackagingConfig(DaraModel):
    def __init__(
        self,
        drm_config: main_models.LivePackagingConfigDrmConfig = None,
        live_manifest_configs: List[main_models.LiveManifestConfig] = None,
        segment_duration: int = None,
        use_audio_rendition_groups: bool = None,
    ):
        self.drm_config = drm_config
        self.live_manifest_configs = live_manifest_configs
        self.segment_duration = segment_duration
        self.use_audio_rendition_groups = use_audio_rendition_groups

    def validate(self):
        if self.drm_config:
            self.drm_config.validate()
        if self.live_manifest_configs:
            for v1 in self.live_manifest_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drm_config is not None:
            result['DrmConfig'] = self.drm_config.to_map()

        result['LiveManifestConfigs'] = []
        if self.live_manifest_configs is not None:
            for k1 in self.live_manifest_configs:
                result['LiveManifestConfigs'].append(k1.to_map() if k1 else None)

        if self.segment_duration is not None:
            result['SegmentDuration'] = self.segment_duration

        if self.use_audio_rendition_groups is not None:
            result['UseAudioRenditionGroups'] = self.use_audio_rendition_groups

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DrmConfig') is not None:
            temp_model = main_models.LivePackagingConfigDrmConfig()
            self.drm_config = temp_model.from_map(m.get('DrmConfig'))

        self.live_manifest_configs = []
        if m.get('LiveManifestConfigs') is not None:
            for k1 in m.get('LiveManifestConfigs'):
                temp_model = main_models.LiveManifestConfig()
                self.live_manifest_configs.append(temp_model.from_map(k1))

        if m.get('SegmentDuration') is not None:
            self.segment_duration = m.get('SegmentDuration')

        if m.get('UseAudioRenditionGroups') is not None:
            self.use_audio_rendition_groups = m.get('UseAudioRenditionGroups')

        return self

class LivePackagingConfigDrmConfig(DaraModel):
    def __init__(
        self,
        content_id: str = None,
        encryption_method: str = None,
        iv: str = None,
        rotate_period: int = None,
        system_ids: List[str] = None,
        url: str = None,
    ):
        self.content_id = content_id
        self.encryption_method = encryption_method
        self.iv = iv
        self.rotate_period = rotate_period
        self.system_ids = system_ids
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_id is not None:
            result['ContentId'] = self.content_id

        if self.encryption_method is not None:
            result['EncryptionMethod'] = self.encryption_method

        if self.iv is not None:
            result['IV'] = self.iv

        if self.rotate_period is not None:
            result['RotatePeriod'] = self.rotate_period

        if self.system_ids is not None:
            result['SystemIds'] = self.system_ids

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')

        if m.get('EncryptionMethod') is not None:
            self.encryption_method = m.get('EncryptionMethod')

        if m.get('IV') is not None:
            self.iv = m.get('IV')

        if m.get('RotatePeriod') is not None:
            self.rotate_period = m.get('RotatePeriod')

        if m.get('SystemIds') is not None:
            self.system_ids = m.get('SystemIds')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

