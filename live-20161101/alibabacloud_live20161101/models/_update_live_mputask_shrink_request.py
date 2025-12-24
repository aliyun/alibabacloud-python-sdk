# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveMPUTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        mix_mode: str = None,
        multi_stream_urlshrink: str = None,
        sei_params_shrink: str = None,
        single_sub_params_shrink: str = None,
        stream_url: str = None,
        task_id: str = None,
        transcode_params_shrink: str = None,
    ):
        # The application ID. You can specify only one application ID. The ID can be up to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The channel ID. You can specify only one channel ID. The ID can be up to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The stream mixing mode. Valid values:
        # 
        # *   **0**: the single-stream relay mode. In this mode, the service only relays the original single stream, but does not transcode mixed streams. You do not need to set parameters for mixed-stream transcoding.
        # *   **1** (default): the mixed-stream relay mode.
        self.mix_mode = mix_mode
        # The multiple ingest URLs to relay. This parameter allows you to specify multiple ingest URLs.
        self.multi_stream_urlshrink = multi_stream_urlshrink
        # The supplemental enhancement information (SEI) parameters.
        self.sei_params_shrink = sei_params_shrink
        # The single-stream relay parameters. These parameters are required if you set MixMode to 0.
        self.single_sub_params_shrink = single_sub_params_shrink
        # The ingest URL. You can specify only one ingest URL in the Real-Time Messaging Protocol (RTMP) format. The URL can be up to 2,048 characters in length. For information about the generation rules of ingest URLs, see [Ingest and streaming URLs](https://help.aliyun.com/document_detail/199339.html).
        # 
        # > 
        # 
        # *   If the ingest URL is under a domain name for which hotlink protection is enabled, you must include an access token in the URL.
        # *   You cannot use the same ingest URL in different tasks.
        # *   You cannot use the same ingest URL within 10 seconds after a task is stopped.
        self.stream_url = stream_url
        # The task ID. You can specify only one task ID. The ID can be up to 55 characters in length and can contain letters, digits, underscores (_), and hyphens (-). The ID must be unique.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The mixed-stream relay parameters. These parameters are required if you set MixMode to 1.
        self.transcode_params_shrink = transcode_params_shrink

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

        if self.mix_mode is not None:
            result['MixMode'] = self.mix_mode

        if self.multi_stream_urlshrink is not None:
            result['MultiStreamURL'] = self.multi_stream_urlshrink

        if self.sei_params_shrink is not None:
            result['SeiParams'] = self.sei_params_shrink

        if self.single_sub_params_shrink is not None:
            result['SingleSubParams'] = self.single_sub_params_shrink

        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.transcode_params_shrink is not None:
            result['TranscodeParams'] = self.transcode_params_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('MixMode') is not None:
            self.mix_mode = m.get('MixMode')

        if m.get('MultiStreamURL') is not None:
            self.multi_stream_urlshrink = m.get('MultiStreamURL')

        if m.get('SeiParams') is not None:
            self.sei_params_shrink = m.get('SeiParams')

        if m.get('SingleSubParams') is not None:
            self.single_sub_params_shrink = m.get('SingleSubParams')

        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TranscodeParams') is not None:
            self.transcode_params_shrink = m.get('TranscodeParams')

        return self

