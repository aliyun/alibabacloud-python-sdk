# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitEditMediaManifestJobRequest(DaraModel):
    def __init__(
        self,
        audio_tracks: str = None,
        auto_stream_job_id: str = None,
        output_config: str = None,
        remove_tracks: str = None,
        subtitles: str = None,
        template_id: str = None,
        user_data: str = None,
        video_id: str = None,
        video_tracks: str = None,
    ):
        # The list of audio tracks to be added. The value is a JSON string array. Each element contains the following fields:
        # - **Language**: the language identifier of the audio track.
        # - **Name**: the display name of the track. If this field is not specified, the default value is audio-{Language}.
        # - **AudioUrl**: the URL of the audio file, which is an OSS object URL.
        self.audio_tracks = audio_tracks
        # The job ID of the target AUTO stream.
        # 
        # This parameter is required.
        self.auto_stream_job_id = auto_stream_job_id
        # The output configuration. The value is a JSON string. It contains the following fields:
        # - **OutputDir**: the output directory. By default, this field is set to the same directory as the source manifest.
        # - **ManifestName**: the file name of the output master playlist. Default value: master. The .m3u8 extension is not allowed.
        self.output_config = output_config
        # The configuration of tracks to be removed. The value is a JSON string. It contains the following fields:
        # - **AudioLanguages**: the list of audio language identifiers for which the entire audio tracks are to be removed.
        # - **SubtitleLanguages**: the list of subtitle language identifiers for which the entire subtitle tracks are to be removed.
        self.remove_tracks = remove_tracks
        # The list of subtitle tracks to be added. The value is a JSON string array. Each element contains the following fields:
        # - **Language**: the language identifier of the subtitle track. If this field is not specified, the subtitle track is ignored.
        # - **SubtitleUrl**: the URL of the subtitle file in WebVTT format, which is an OSS object URL.
        self.subtitles = subtitles
        # The manifest editing template ID, which is returned after the AddManifestEditTemplate operation is called. If this parameter is specified, the output tracks are orchestrated based on the fixed video, audio, and subtitle item configurations in the template.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The custom pass-through data.
        self.user_data = user_data
        # **The target video ID**, used for authentication isolation and consistency verification.
        # 
        # This parameter is required.
        self.video_id = video_id
        # The list of video tracks to be added. The value is a JSON string array. Each element contains the following fields:
        # - **Name**: the display name of the track. If this field is not specified, the video track is ignored.
        # - **VideoUrl**: the URL of the video stream manifest file, which is an OSS object URL.
        self.video_tracks = video_tracks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_tracks is not None:
            result['AudioTracks'] = self.audio_tracks

        if self.auto_stream_job_id is not None:
            result['AutoStreamJobId'] = self.auto_stream_job_id

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.remove_tracks is not None:
            result['RemoveTracks'] = self.remove_tracks

        if self.subtitles is not None:
            result['Subtitles'] = self.subtitles

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        if self.video_tracks is not None:
            result['VideoTracks'] = self.video_tracks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioTracks') is not None:
            self.audio_tracks = m.get('AudioTracks')

        if m.get('AutoStreamJobId') is not None:
            self.auto_stream_job_id = m.get('AutoStreamJobId')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('RemoveTracks') is not None:
            self.remove_tracks = m.get('RemoveTracks')

        if m.get('Subtitles') is not None:
            self.subtitles = m.get('Subtitles')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        if m.get('VideoTracks') is not None:
            self.video_tracks = m.get('VideoTracks')

        return self

