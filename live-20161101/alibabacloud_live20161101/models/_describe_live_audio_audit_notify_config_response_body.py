# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveAudioAuditNotifyConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_audio_audit_notify_config_list: main_models.DescribeLiveAudioAuditNotifyConfigResponseBodyLiveAudioAuditNotifyConfigList = None,
        request_id: str = None,
    ):
        # The configuration of callbacks for audio moderation results.
        self.live_audio_audit_notify_config_list = live_audio_audit_notify_config_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_audio_audit_notify_config_list:
            self.live_audio_audit_notify_config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_audio_audit_notify_config_list is not None:
            result['LiveAudioAuditNotifyConfigList'] = self.live_audio_audit_notify_config_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveAudioAuditNotifyConfigList') is not None:
            temp_model = main_models.DescribeLiveAudioAuditNotifyConfigResponseBodyLiveAudioAuditNotifyConfigList()
            self.live_audio_audit_notify_config_list = temp_model.from_map(m.get('LiveAudioAuditNotifyConfigList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveAudioAuditNotifyConfigResponseBodyLiveAudioAuditNotifyConfigList(DaraModel):
    def __init__(
        self,
        live_audio_audit_notify_config: List[main_models.DescribeLiveAudioAuditNotifyConfigResponseBodyLiveAudioAuditNotifyConfigListLiveAudioAuditNotifyConfig] = None,
    ):
        self.live_audio_audit_notify_config = live_audio_audit_notify_config

    def validate(self):
        if self.live_audio_audit_notify_config:
            for v1 in self.live_audio_audit_notify_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveAudioAuditNotifyConfig'] = []
        if self.live_audio_audit_notify_config is not None:
            for k1 in self.live_audio_audit_notify_config:
                result['LiveAudioAuditNotifyConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_audio_audit_notify_config = []
        if m.get('LiveAudioAuditNotifyConfig') is not None:
            for k1 in m.get('LiveAudioAuditNotifyConfig'):
                temp_model = main_models.DescribeLiveAudioAuditNotifyConfigResponseBodyLiveAudioAuditNotifyConfigListLiveAudioAuditNotifyConfig()
                self.live_audio_audit_notify_config.append(temp_model.from_map(k1))

        return self

class DescribeLiveAudioAuditNotifyConfigResponseBodyLiveAudioAuditNotifyConfigListLiveAudioAuditNotifyConfig(DaraModel):
    def __init__(
        self,
        callback: str = None,
        callback_template: str = None,
        domain_name: str = None,
    ):
        # The callback URL.
        self.callback = callback
        # The callback template. The following fields are configured:
        # 
        # *   **{DomainName}**: the streaming domain.
        # *   **{AppName}**: the name of the application to which the live stream belongs.
        # *   **{StreamName}**: the name of the live stream.
        # *   **{Timestamp}**: the time when the callback is returned. The value of this field is a UNIX timestamp. Unit: seconds.
        # *   **{Result}**: the moderation results.
        self.callback_template = callback_template
        # The main streaming domain.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback is not None:
            result['Callback'] = self.callback

        if self.callback_template is not None:
            result['CallbackTemplate'] = self.callback_template

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('CallbackTemplate') is not None:
            self.callback_template = m.get('CallbackTemplate')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

