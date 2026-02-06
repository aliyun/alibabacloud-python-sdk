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
        # Specifies the resolutions of the media streams you want to refresh or prefetch. You can specify multiple resolutions. Separate multiple resolutions with commas (,). If you leave this parameter empty, media streams in all resolutions are refreshed or prefetched by default.
        # 
        # >  The value must be supported in the **Definition** section in [Parameters for media assets](https://help.aliyun.com/document_detail/124671.html).
        self.definitions = definitions
        # The formats of the media streams you want to refresh or prefetch. You can specify multiple formats. Separate multiple formats with commas (,). If you leave this parameter empty, media streams in all formats are refreshed or prefetched by default. Valid values:
        # 
        # *   **mp4**
        # *   **m3u8**
        # *   **mp3**
        # *   **flv**
        # *   **webm**
        # *   **ts**
        self.formats = formats
        # The IDs of the media files that you want to refresh or prefetch. You can specify a maximum of 20 IDs. Separate multiple IDs with commas (,). You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD](https://vod.console.aliyun.com) console. In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, view the ID of the audio or video file. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of VideoId from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you call to upload media files.
        # *   Obtain the value of VideoId from the response to the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation that you call to query the media ID after the media file is uploaded.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # Specifies the type of the refresh or prefetch operation. Default value: Single. Valid values:
        # 
        # *   **Single**: Only one latest transcoded stream is refreshed or prefetched for each resolution and format.
        # *   **Multiple**: All transcoded streams are refreshed or prefetched for each resolution and format.
        self.result_type = result_type
        # Specifies the number of the playback URLs of the TS files for the M3U8 media stream you want to refresh or prefetch. After you set this parameter, only the playback URLs of the first N TS files will be refreshed or prefetched. Valid values: 1 to 20. Default value: 5.
        self.slice_count = slice_count
        # Specifies whether to refresh or prefetch the playback URLs of the TS files of the M3U8 media stream. Default value: false. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.slice_flag = slice_flag
        # Specifies the types of media streams you want to refresh or prefetch. You can specify multiple types. Separate multiple types with commas (,). If you leave this parameter empty, media streams in all types are refreshed or prefetched by default. Valid values:
        # 
        # *   **video**
        # *   **audio**
        self.stream_type = stream_type
        # The type of the task that you want to create. Valid values:
        # 
        # *   **Refresh**
        # *   **Preload**
        # 
        # This parameter is required.
        self.task_type = task_type
        # The custom configurations such as callback configurations and upload acceleration configurations. The value must be a JSON string. For more information, see the "UserData: specifies the custom configurations for media upload" section in the [Request parameter](https://help.aliyun.com/document_detail/86952.html) topic.
        # 
        # >*   The callback configurations take effect only after you specify the HTTP callback URL and select specific callback events in the ApsaraVideo VOD console. For more information about how to configure HTTP callback settings in the ApsaraVideo VOD console, see [Configure callback settings](https://help.aliyun.com/document_detail/86071.html).
        # >*   To enable the upload acceleration feature, submit a ticket. For more information, see [Overview](https://help.aliyun.com/document_detail/55396.html). For more information about how to submit a ticket, see [Contact us](https://help.aliyun.com/document_detail/464625.html).
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

