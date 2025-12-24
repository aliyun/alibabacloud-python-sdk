# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartRtcCloudRecordingShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        max_idle_time: int = None,
        mix_layout_params_shrink: str = None,
        mix_transcode_params_shrink: str = None,
        notify_auth_key: str = None,
        notify_file_uploaded_format: List[str] = None,
        notify_url: str = None,
        record_params_shrink: str = None,
        storage_params_shrink: str = None,
        subscribe_params_shrink: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        self.max_idle_time = max_idle_time
        self.mix_layout_params_shrink = mix_layout_params_shrink
        self.mix_transcode_params_shrink = mix_transcode_params_shrink
        self.notify_auth_key = notify_auth_key
        self.notify_file_uploaded_format = notify_file_uploaded_format
        self.notify_url = notify_url
        # This parameter is required.
        self.record_params_shrink = record_params_shrink
        # This parameter is required.
        self.storage_params_shrink = storage_params_shrink
        # This parameter is required.
        self.subscribe_params_shrink = subscribe_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.max_idle_time is not None:
            result['MaxIdleTime'] = self.max_idle_time

        if self.mix_layout_params_shrink is not None:
            result['MixLayoutParams'] = self.mix_layout_params_shrink

        if self.mix_transcode_params_shrink is not None:
            result['MixTranscodeParams'] = self.mix_transcode_params_shrink

        if self.notify_auth_key is not None:
            result['NotifyAuthKey'] = self.notify_auth_key

        if self.notify_file_uploaded_format is not None:
            result['NotifyFileUploadedFormat'] = self.notify_file_uploaded_format

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.record_params_shrink is not None:
            result['RecordParams'] = self.record_params_shrink

        if self.storage_params_shrink is not None:
            result['StorageParams'] = self.storage_params_shrink

        if self.subscribe_params_shrink is not None:
            result['SubscribeParams'] = self.subscribe_params_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('MixLayoutParams') is not None:
            self.mix_layout_params_shrink = m.get('MixLayoutParams')

        if m.get('MixTranscodeParams') is not None:
            self.mix_transcode_params_shrink = m.get('MixTranscodeParams')

        if m.get('NotifyAuthKey') is not None:
            self.notify_auth_key = m.get('NotifyAuthKey')

        if m.get('NotifyFileUploadedFormat') is not None:
            self.notify_file_uploaded_format = m.get('NotifyFileUploadedFormat')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('RecordParams') is not None:
            self.record_params_shrink = m.get('RecordParams')

        if m.get('StorageParams') is not None:
            self.storage_params_shrink = m.get('StorageParams')

        if m.get('SubscribeParams') is not None:
            self.subscribe_params_shrink = m.get('SubscribeParams')

        return self

