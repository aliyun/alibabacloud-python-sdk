# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class VodPackagingConfig(DaraModel):
    def __init__(
        self,
        drm_provider: main_models.VodPackagingConfigDrmProvider = None,
        manifest_name: str = None,
        segment_duration: int = None,
        stream_selection: main_models.VodPackagingConfigStreamSelection = None,
    ):
        self.drm_provider = drm_provider
        self.manifest_name = manifest_name
        self.segment_duration = segment_duration
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
            temp_model = main_models.VodPackagingConfigDrmProvider()
            self.drm_provider = temp_model.from_map(m.get('DrmProvider'))

        if m.get('ManifestName') is not None:
            self.manifest_name = m.get('ManifestName')

        if m.get('SegmentDuration') is not None:
            self.segment_duration = m.get('SegmentDuration')

        if m.get('StreamSelection') is not None:
            temp_model = main_models.VodPackagingConfigStreamSelection()
            self.stream_selection = temp_model.from_map(m.get('StreamSelection'))

        return self

class VodPackagingConfigStreamSelection(DaraModel):
    def __init__(
        self,
        max_video_bits_per_second: int = None,
        min_video_bits_per_second: int = None,
        stream_order: str = None,
    ):
        self.max_video_bits_per_second = max_video_bits_per_second
        self.min_video_bits_per_second = min_video_bits_per_second
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

class VodPackagingConfigDrmProvider(DaraModel):
    def __init__(
        self,
        encryption_method: str = None,
        iv: str = None,
        system_ids: List[str] = None,
        url: str = None,
    ):
        self.encryption_method = encryption_method
        self.iv = iv
        self.system_ids = system_ids
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

