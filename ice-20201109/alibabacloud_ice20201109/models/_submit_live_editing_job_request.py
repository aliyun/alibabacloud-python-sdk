# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitLiveEditingJobRequest(DaraModel):
    def __init__(
        self,
        clips: str = None,
        live_stream_config: str = None,
        media_produce_config: str = None,
        output_media_config: str = None,
        output_media_target: str = None,
        project_id: str = None,
        user_data: str = None,
    ):
        # A JSON array that specifies the clips to edit. The job creates the output file by concatenating these clips in the specified order.
        # 
        # Each clip includes a start and end time. If live stream parameters are not specified for a clip, the system uses the global `LiveStreamConfig` settings. The start and end timestamps must be in UTC. For more details, see the Clip data structure below.
        # 
        # This parameter is required.
        self.clips = clips
        # The configuration of the source live stream, specified as a JSON object. It includes the following parameters:
        # 
        # - `AppName`: The name of the application to which the stream belongs.
        # 
        # - `DomainName`: The domain name of the stream.
        # 
        # - `StreamName`: The name of the live stream.
        self.live_stream_config = live_stream_config
        # The production configuration for the output file, specified as a JSON object. The `Mode` parameter specifies the editing mode. Valid values are:
        # 
        # - **AccurateFast** (Default): Fast and precise editing. It offers faster processing compared to the `Accurate` mode. The output file has the same resolution as the source stream. You cannot specify a custom width and height for the output file.
        # 
        # - **Accurate**: Precise editing. This mode lets you specify a custom width and height for the output file.
        # 
        # - **Rough**: Rough editing with a precision of a single TS segment. The output file includes all segments between the specified start and end times. You can specify a custom width and height for the output file.
        # 
        # - **RoughFast**: Fast rough-cut editing, which is faster than the `Accurate` mode. It has a precision of a single TS segment, and the output file includes all segments between the specified start and end times. The output file has the same resolution as the source stream. You cannot specify a custom width and height for the output file.
        self.media_produce_config = media_produce_config
        # The destination configuration for the output file, specified as a JSON object. You can specify either a URL on OSS or a storage location in a VOD bucket.
        # 
        # - To output to OSS, the `MediaURL` parameter is required.
        # 
        # - To output to VOD, the `StorageLocation` and `FileName` parameters are required.
        self.output_media_config = output_media_config
        # The destination type for the output file. Valid values:
        # 
        # - `oss-object`: An object in an Alibaba Cloud OSS bucket.
        # 
        # - `vod-media`: A media asset in Alibaba Cloud VOD.
        self.output_media_target = output_media_target
        # The ID of the live editing project. If you specify this parameter, the system uses the storage settings from the project. If left empty, the system uses the storage settings provided in the request instead.
        self.project_id = project_id
        # Custom user data, provided as a JSON object. The maximum length is 512 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clips is not None:
            result['Clips'] = self.clips

        if self.live_stream_config is not None:
            result['LiveStreamConfig'] = self.live_stream_config

        if self.media_produce_config is not None:
            result['MediaProduceConfig'] = self.media_produce_config

        if self.output_media_config is not None:
            result['OutputMediaConfig'] = self.output_media_config

        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clips') is not None:
            self.clips = m.get('Clips')

        if m.get('LiveStreamConfig') is not None:
            self.live_stream_config = m.get('LiveStreamConfig')

        if m.get('MediaProduceConfig') is not None:
            self.media_produce_config = m.get('MediaProduceConfig')

        if m.get('OutputMediaConfig') is not None:
            self.output_media_config = m.get('OutputMediaConfig')

        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

