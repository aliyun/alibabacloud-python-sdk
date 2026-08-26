# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartLiveMPUTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        max_idle_time: str = None,
        mix_mode: str = None,
        multi_stream_urlshrink: str = None,
        region: str = None,
        sei_params_shrink: str = None,
        single_sub_params_shrink: str = None,
        stream_url: str = None,
        task_id: str = None,
        transcode_params_shrink: str = None,
    ):
        # The application ID. Only one ID is supported. It can contain uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-). The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The channel ID. Only one ID is supported. It can contain uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-). The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The idle timeout period. Unit: seconds. The value must be in the range of [10, 86400].
        # 
        # > If you set this parameter, the task is automatically stopped when it has been idle for a period longer than MaxIdleTime. If you do not set this parameter, the task is stopped immediately after the channel is closed.
        self.max_idle_time = max_idle_time
        # The stream mixing mode. Valid values:
        # 
        # - **0**: Single-stream ingest. The original single stream is ingested without stream mixing or transcoding. You do not need to configure stream mixing and transcoding parameters.
        # 
        # - **1** (default): Stream mixing and transcoding.
        # 
        # This parameter is required.
        self.mix_mode = mix_mode
        # The parameters for ingesting to multiple URLs. You can specify multiple live ingest URLs.
        # 
        # > When you set the ingest URL for a task, you must configure either the StreamURL parameter or the MultiStreamURL parameter, but not both.
        self.multi_stream_urlshrink = multi_stream_urlshrink
        # The region where the stream mixing service is located. Valid values:
        # 
        # - **CN-Shanghai<props="china">(default)**: Shanghai.
        # 
        # - **AP-Singapore<props="intl">(default)**: Singapore.
        # 
        # - **EMAA-Saudi**: Saudi Arabia.
        self.region = region
        # The SEI configuration parameters.
        self.sei_params_shrink = sei_params_shrink
        # The parameters for single-stream ingest. This parameter is required when MixMode is set to 0. Do not set this parameter for stream mixing and transcoding.
        self.single_sub_params_shrink = single_sub_params_shrink
        # The live ingest URL. Only the RTMP protocol is supported. Only one URL is supported. The maximum length is 2048 characters. For information about how to generate the URL, see [Ingest URLs and playback URLs](https://help.aliyun.com/document_detail/199339.html).
        # 
        # > - For domain names with hotlink protection enabled, the ingest URL must include an access token.
        # 
        # - Do not use the same StreamURL in different tasks at the same time.
        # 
        # - Do not use the same StreamURL within 10 seconds after a task stops.
        self.stream_url = stream_url
        # The task ID. Only one ID is supported. It can contain uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-). The maximum length is 55 characters. This ID is the unique identifier for the bypass ingest task.
        # If a task with the same ID still exists and has not been cleared when you start a new task, \\`InvalidParam\\` is returned.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The parameters for stream mixing and transcoding. This parameter is required when MixMode is set to 1. Do not set this parameter for single-stream ingest.
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

        if self.max_idle_time is not None:
            result['MaxIdleTime'] = self.max_idle_time

        if self.mix_mode is not None:
            result['MixMode'] = self.mix_mode

        if self.multi_stream_urlshrink is not None:
            result['MultiStreamURL'] = self.multi_stream_urlshrink

        if self.region is not None:
            result['Region'] = self.region

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

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('MixMode') is not None:
            self.mix_mode = m.get('MixMode')

        if m.get('MultiStreamURL') is not None:
            self.multi_stream_urlshrink = m.get('MultiStreamURL')

        if m.get('Region') is not None:
            self.region = m.get('Region')

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

