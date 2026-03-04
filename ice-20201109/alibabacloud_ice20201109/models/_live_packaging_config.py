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
        # Configuration for the DRM provider. To disable DRM, leave all fields in this object empty.
        self.drm_config = drm_config
        # Live stream manifest configuration. Only one configuration is supported.
        self.live_manifest_configs = live_manifest_configs
        # The duration of each output segment, in seconds. If not set, this defaults to the channel\\"s configured segment duration. The final segment duration is a multiple of the source segment duration that is closest to and not less than this value. Valid values: 1 to 30.
        self.segment_duration = segment_duration
        # Specifies whether to create separate audio rendition groups for TS segments.
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
        # The content ID in the DRM system. The maximum length is 256 characters. Letters, digits, underscores (_), and hyphens (-) are supported. You must ensure this ID is unique to prevent playback failures.
        self.content_id = content_id
        # The encryption method. Valid value:
        # 
        # *   SAMPLE_AES
        # 
        # If not specified, encryption is disabled.
        self.encryption_method = encryption_method
        # A 128-bit, 16-byte hex value represented by a 32-character string that is used with the key for encrypting data blocks. If you leave this parameter empty, MediaPackage creates a constant initialization vector (IV). If it is specified, the value is passed to the DRM service.
        self.iv = iv
        # The key rotation interval for DRM, in seconds. The default value of 0 disables key rotation.
        self.rotate_period = rotate_period
        # The ID of the DRM system. The supported systems depend on the protocol.
        # 
        # *   DASH: Supports Google Widevine and Microsoft PlayReady.
        # *   HLS: DRM is not supported.
        # *   HLS-CMAF: Supports Apple FairPlay, Google Widevine, and Microsoft PlayReady.
        # 
        # The corresponding System IDs are:
        # 
        # *   Apple FairPlay: 94ce86fb-07ff-4f43-adb8-93d2fa968ca2
        # *   Google Widevine: edef8ba9-79d6-4ace-a3c8-27dcd51d21ed
        # *   Microsoft PlayReady: 9a04f079-9840-4286-ab92-e65be0885f95
        self.system_ids = system_ids
        # The URL of the DRM key provider.
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

