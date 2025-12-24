# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveAudioAuditConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_audio_audit_config_list: main_models.DescribeLiveAudioAuditConfigResponseBodyLiveAudioAuditConfigList = None,
        request_id: str = None,
    ):
        # The list of audio moderation configurations.
        self.live_audio_audit_config_list = live_audio_audit_config_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_audio_audit_config_list:
            self.live_audio_audit_config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_audio_audit_config_list is not None:
            result['LiveAudioAuditConfigList'] = self.live_audio_audit_config_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveAudioAuditConfigList') is not None:
            temp_model = main_models.DescribeLiveAudioAuditConfigResponseBodyLiveAudioAuditConfigList()
            self.live_audio_audit_config_list = temp_model.from_map(m.get('LiveAudioAuditConfigList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveAudioAuditConfigResponseBodyLiveAudioAuditConfigList(DaraModel):
    def __init__(
        self,
        live_audio_audit_config: List[main_models.DescribeLiveAudioAuditConfigResponseBodyLiveAudioAuditConfigListLiveAudioAuditConfig] = None,
    ):
        self.live_audio_audit_config = live_audio_audit_config

    def validate(self):
        if self.live_audio_audit_config:
            for v1 in self.live_audio_audit_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveAudioAuditConfig'] = []
        if self.live_audio_audit_config is not None:
            for k1 in self.live_audio_audit_config:
                result['LiveAudioAuditConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_audio_audit_config = []
        if m.get('LiveAudioAuditConfig') is not None:
            for k1 in m.get('LiveAudioAuditConfig'):
                temp_model = main_models.DescribeLiveAudioAuditConfigResponseBodyLiveAudioAuditConfigListLiveAudioAuditConfig()
                self.live_audio_audit_config.append(temp_model.from_map(k1))

        return self

class DescribeLiveAudioAuditConfigResponseBodyLiveAudioAuditConfigListLiveAudioAuditConfig(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        biz_type: str = None,
        domain_name: str = None,
        scenes: main_models.DescribeLiveAudioAuditConfigResponseBodyLiveAudioAuditConfigListLiveAudioAuditConfigScenes = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The business type. You can specify a model. The default value is the domain name.
        self.biz_type = biz_type
        # The main streaming domain.
        self.domain_name = domain_name
        # The moderation scenarios.
        self.scenes = scenes
        # The name of the live stream.
        self.stream_name = stream_name

    def validate(self):
        if self.scenes:
            self.scenes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.scenes is not None:
            result['Scenes'] = self.scenes.to_map()

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Scenes') is not None:
            temp_model = main_models.DescribeLiveAudioAuditConfigResponseBodyLiveAudioAuditConfigListLiveAudioAuditConfigScenes()
            self.scenes = temp_model.from_map(m.get('Scenes'))

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

class DescribeLiveAudioAuditConfigResponseBodyLiveAudioAuditConfigListLiveAudioAuditConfigScenes(DaraModel):
    def __init__(
        self,
        scene: List[str] = None,
    ):
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene is not None:
            result['scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')

        return self

