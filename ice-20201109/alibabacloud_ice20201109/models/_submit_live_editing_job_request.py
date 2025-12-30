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
        # The clips in the JSON array format. The output video is created by merging these clips sequentially.
        # 
        # Each clip has a start time and an end time. If no live stream parameters are specified, the outer live stream configurations apply. The start and end timestamps are in UTC. For more information about the parameters, see the "Clip" section of this topic.
        # 
        # This parameter is required.
        self.clips = clips
        # The live stream configurations, in the JSON format. The configurations must include the following parameters:
        # 
        # *   AppName: the name of the application to which the live stream belongs.
        # *   DomainName: the domain name of the application.
        # *   StreamName: the name of the live stream.
        self.live_stream_config = live_stream_config
        # The production configurations, in the JSON format. Mode specifies the editing mode. Valid values:
        # 
        # *   **AccurateFast** (default): fast editing. It is faster than the Accurate mode. The resolution of the output file is the same as that of the source stream. You cannot specify the width and height of the output file.
        # *   **Accurate**: accurate editing. In this mode, you can specify the width and height of the output file.
        # *   **Rough**: rough editing. The minimum precision is one TS segment. The output file comprises all segments within the specified time range. You can specify the width and height of the output file.
        # *   **RoughFast**: fast rough editing. It is faster than the Accurate mode. The minimum precision is one TS segment. The output file comprises all segments within the specified time range. The resolution of the output file is the same as that of the source stream. You cannot specify the width and height of the output file.
        self.media_produce_config = media_produce_config
        # The configurations of the output file, in the JSON format. You can specify an OSS URL or a storage location in a storage bucket of ApsaraVideo VOD.
        # 
        # *   To store the output file in OSS, you must specify MediaURL.
        # *   To store the output file in ApsaraVideo VOD, you must specify StorageLocation and FileName.
        self.output_media_config = output_media_config
        # The type of the output file. Valid values:
        # 
        # *   oss-object: OSS object in an OSS bucket.
        # *   vod-media: media asset in Alibaba Cloud VOD.
        self.output_media_target = output_media_target
        # The ID of the live editing project. If this parameter is specified, the system reads the storage configurations of the project. If this parameter is not specified, the specified storage configurations take precedence.
        self.project_id = project_id
        # The user-defined data in the JSON format, which can be up to 512 bytes in length.
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

