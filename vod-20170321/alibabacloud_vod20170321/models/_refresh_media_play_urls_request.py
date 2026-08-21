# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshMediaPlayUrlsRequest(DaraModel):
    def __init__(
        self,
        definitions: str = None,
        formats: str = None,
        media_ids: str = None,
        result_type: str = None,
        slice_count: int = None,
        slice_flag: bool = None,
        stream_type: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        # Specifies the definitions of the streams that you want to purge or prefetch. You can specify multiple definitions. Separate multiple definitions with commas (,). If you do not specify this parameter, **streams in all definitions are purged or prefetched by default**.
        # > The value must be one of the values defined in **Definition** in [Metric description for media assets](https://help.aliyun.com/document_detail/124671.html).
        self.definitions = definitions
        # The streaming formats that you want to refresh or prefetch. You can specify multiple formats. Separate multiple formats with commas (,). If you do not specify this parameter, **streams in all formats are refreshed or prefetched by default**. Valid values:
        # - **mp4**
        # - **m3u8**
        # - **mp3**
        # - **flv**
        # - **webm**
        # - **ts**
        self.formats = formats
        # The IDs of the audio or video files that you want to refresh or prefetch. You can specify one or more IDs. Separate multiple IDs with commas (,). You can specify up to 20 IDs.
        # You can obtain audio or video IDs by using the following methods:
        # - For audio or video files uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - When you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential, the audio or video ID is the value of the VideoId response parameter.
        # - After the audio or video file is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of the VideoId response parameter.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The result type of the refresh or prefetch task. Valid values:
        # - **Single** (default): Only the latest transcoded stream for each definition and format is refreshed or prefetched.
        # - **Multiple**: All transcoded streams for each definition and format are refreshed or prefetched.
        self.result_type = result_type
        # The number of TS file playback URLs to refresh or prefetch for M3U8 streams. Only the first N TS file playback URLs of each M3U8 stream are refreshed or prefetched. Valid values: 1 to 20. **Default value: 5**.
        self.slice_count = slice_count
        # Specifies whether to refresh or prefetch the playback URLs of TS files in M3U8 streams. Valid values:
        # - **false** (default): No.
        # - **true**: Yes.
        self.slice_flag = slice_flag
        # The types of the streams that you want to refresh or prefetch. You can specify multiple stream types. Separate multiple stream types with commas (,). If you do not specify this parameter, **all stream types are refreshed or prefetched by default**. Valid values:
        # - **video**: video.
        # - **audio**: audio.
        self.stream_type = stream_type
        # The type of the task. Valid values:
        # - **Refresh**: purge.
        # - **Preload**: prefetch.
        # 
        # This parameter is required.
        self.task_type = task_type
        # The custom settings. The value is a JSON string that supports settings such as message callbacks and upload acceleration. For more information, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        # > - To use message callbacks in this parameter, configure an HTTP callback URL and select the corresponding callback event types in the console. Otherwise, the callback settings do not take effect. For information about how to configure HTTP callbacks in the console, see [Callback settings](https://help.aliyun.com/document_detail/86071.html).
        # > - To use the upload acceleration feature, submit a ticket to activate it. For more information, see [Upload instructions](https://help.aliyun.com/document_detail/55396.html). For information about how to submit a ticket, see [Contact us](https://help.aliyun.com/document_detail/464625.html).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definitions is not None:
            result['Definitions'] = self.definitions

        if self.formats is not None:
            result['Formats'] = self.formats

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        if self.slice_count is not None:
            result['SliceCount'] = self.slice_count

        if self.slice_flag is not None:
            result['SliceFlag'] = self.slice_flag

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definitions') is not None:
            self.definitions = m.get('Definitions')

        if m.get('Formats') is not None:
            self.formats = m.get('Formats')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('SliceCount') is not None:
            self.slice_count = m.get('SliceCount')

        if m.get('SliceFlag') is not None:
            self.slice_flag = m.get('SliceFlag')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

