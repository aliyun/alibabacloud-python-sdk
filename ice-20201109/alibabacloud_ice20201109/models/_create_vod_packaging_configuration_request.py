# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateVodPackagingConfigurationRequest(DaraModel):
    def __init__(
        self,
        configuration_name: str = None,
        description: str = None,
        group_name: str = None,
        package_config: main_models.CreateVodPackagingConfigurationRequestPackageConfig = None,
        protocol: str = None,
    ):
        # The name of the packaging configuration. The name must be unique in an account and can be up to 128 characters in length. Letters, digits, underscores (_), and hyphens (-) are supported.
        self.configuration_name = configuration_name
        # The description of the packaging configuration.
        self.description = description
        # The name of the packaging group. The name can be up to 128 characters in length. Letters, digits, underscores (_), and hyphens (-) are supported.
        self.group_name = group_name
        # The packaging configuration.
        self.package_config = package_config
        # The package type.
        # 
        # *   HLS: packages content into TS segments for delivery over the HLS protocol.
        # *   HLS_CMAF: packages content into CMAF segments for delivery over the HLS protocol.
        # *   DASH: packages content for delivery over the DASH protocol.
        self.protocol = protocol

    def validate(self):
        if self.package_config:
            self.package_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_name is not None:
            result['ConfigurationName'] = self.configuration_name

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.package_config is not None:
            result['PackageConfig'] = self.package_config.to_map()

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationName') is not None:
            self.configuration_name = m.get('ConfigurationName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('PackageConfig') is not None:
            temp_model = main_models.CreateVodPackagingConfigurationRequestPackageConfig()
            self.package_config = temp_model.from_map(m.get('PackageConfig'))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class CreateVodPackagingConfigurationRequestPackageConfig(DaraModel):
    def __init__(
        self,
        drm_provider: main_models.CreateVodPackagingConfigurationRequestPackageConfigDrmProvider = None,
        manifest_name: str = None,
        segment_duration: int = None,
        stream_selection: main_models.CreateVodPackagingConfigurationRequestPackageConfigStreamSelection = None,
    ):
        # The settings of digital rights management (DRM) encryption.
        self.drm_provider = drm_provider
        # The manifest name. The name can be up to 128 characters in length. Letters, digits, underscores (_), and hyphens (-) are supported.
        self.manifest_name = manifest_name
        # The duration of each segment in a packaged stream. Unit: seconds. MediaPackage rounds segments to the nearest multiple of the input segment duration. Valid values: 1 to 30.
        self.segment_duration = segment_duration
        # The settings of stream selection.
        self.stream_selection = stream_selection

    def validate(self):
        if self.drm_provider:
            self.drm_provider.validate()
        if self.stream_selection:
            self.stream_selection.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drm_provider is not None:
            result['DrmProvider'] = self.drm_provider.to_map()

        if self.manifest_name is not None:
            result['ManifestName'] = self.manifest_name

        if self.segment_duration is not None:
            result['SegmentDuration'] = self.segment_duration

        if self.stream_selection is not None:
            result['StreamSelection'] = self.stream_selection.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DrmProvider') is not None:
            temp_model = main_models.CreateVodPackagingConfigurationRequestPackageConfigDrmProvider()
            self.drm_provider = temp_model.from_map(m.get('DrmProvider'))

        if m.get('ManifestName') is not None:
            self.manifest_name = m.get('ManifestName')

        if m.get('SegmentDuration') is not None:
            self.segment_duration = m.get('SegmentDuration')

        if m.get('StreamSelection') is not None:
            temp_model = main_models.CreateVodPackagingConfigurationRequestPackageConfigStreamSelection()
            self.stream_selection = temp_model.from_map(m.get('StreamSelection'))

        return self

class CreateVodPackagingConfigurationRequestPackageConfigStreamSelection(DaraModel):
    def __init__(
        self,
        max_video_bits_per_second: int = None,
        min_video_bits_per_second: int = None,
        stream_order: str = None,
    ):
        # The maximum bitrate of the video stream. Unit: bit/s.
        self.max_video_bits_per_second = max_video_bits_per_second
        # The minimum bitrate of the video stream. Unit: bit/s.
        self.min_video_bits_per_second = min_video_bits_per_second
        # The order of manifest files in the master playlist. Valid values:
        # 
        # *   ORIGINAL: sorts the manifest files in the same order as the source.
        # *   VIDEO_BITRATE_ASCENDING: sorts the manifest files in ascending order of bitrates, from lowest to highest.
        # *   VIDEO_BITRATE_DESCENDING: sorts the manifest files in descending order of bitrates, from highest to lowest.
        self.stream_order = stream_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_video_bits_per_second is not None:
            result['MaxVideoBitsPerSecond'] = self.max_video_bits_per_second

        if self.min_video_bits_per_second is not None:
            result['MinVideoBitsPerSecond'] = self.min_video_bits_per_second

        if self.stream_order is not None:
            result['StreamOrder'] = self.stream_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxVideoBitsPerSecond') is not None:
            self.max_video_bits_per_second = m.get('MaxVideoBitsPerSecond')

        if m.get('MinVideoBitsPerSecond') is not None:
            self.min_video_bits_per_second = m.get('MinVideoBitsPerSecond')

        if m.get('StreamOrder') is not None:
            self.stream_order = m.get('StreamOrder')

        return self

class CreateVodPackagingConfigurationRequestPackageConfigDrmProvider(DaraModel):
    def __init__(
        self,
        encryption_method: str = None,
        iv: str = None,
        system_ids: List[str] = None,
        url: str = None,
    ):
        # The encryption method. Valid values:
        # 
        # *   AES_128: Advanced Encryption Standard (AES) with 128-bit key length.
        # *   SAMPLE_AES: an encryption method that encrypts individual media samples.
        self.encryption_method = encryption_method
        # A 128-bit, 16-byte hex value represented by a 32-character string that is used with the key for encrypting data blocks. If you leave this parameter empty, MediaPackage creates a constant initialization vector (IV). If it is specified, the value is passed to the DRM service.
        self.iv = iv
        # The ID of the DRM system. The maximum number of system IDs allowed is determined by the protocol type. Limits:
        # 
        # *   DASH: 2
        # *   HLS: 1
        # *   HLS_CMAF: 2
        # 
        # Apple FairPlay, Google Widevine, and Microsoft PlayReady are supported. Their system IDs are as follows:
        # 
        # *   Apple FairPlay: 94ce86fb-07ff-4f43-adb8-93d2fa968ca2
        # *   Google Widevine: edef8ba9-79d6-4ace-a3c8-27dcd51d21e
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
        if self.encryption_method is not None:
            result['EncryptionMethod'] = self.encryption_method

        if self.iv is not None:
            result['IV'] = self.iv

        if self.system_ids is not None:
            result['SystemIds'] = self.system_ids

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionMethod') is not None:
            self.encryption_method = m.get('EncryptionMethod')

        if m.get('IV') is not None:
            self.iv = m.get('IV')

        if m.get('SystemIds') is not None:
            self.system_ids = m.get('SystemIds')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

