# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class GenerateVideoPlaylistRequest(DaraModel):
    def __init__(
        self,
        credential_config: main_models.CredentialConfig = None,
        master_uri: str = None,
        notification: main_models.Notification = None,
        overwrite_policy: str = None,
        project_name: str = None,
        source_duration: float = None,
        source_start_time: float = None,
        source_subtitles: List[main_models.GenerateVideoPlaylistRequestSourceSubtitles] = None,
        source_uri: str = None,
        tags: Dict[str, str] = None,
        targets: List[main_models.GenerateVideoPlaylistRequestTargets] = None,
        user_data: str = None,
    ):
        # **Leave this parameter empty unless you have specific requirements.**
        # 
        # The China authorization configuration. This parameter is optional. For more information, see [Use Chinese authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The OSS URI of the Master Playlist.
        # 
        # The OSS URI follows the format oss://${Bucket}/${Object}, where ${Bucket} is the name of the OSS bucket in the same region as the current project, and ${Object} is the full path of the file with the ".m3u8" extension.
        # > If the playlist has subtitle input or multiple Target outputs, MasterURI is required. The subtitle URI or Target URI must be in the same directory as or a subdirectory of MasterURI.
        self.master_uri = master_uri
        # The message notification configuration. Click Notification for details. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The overwrite policy when a Media Playlist already exists. Valid values:
        # 
        # - overwrite (default): overwrites the existing Media Playlist.
        # - skip-existing: skips generation and retains the existing Media Playlist.
        self.overwrite_policy = overwrite_policy
        # The project name. For information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The duration for generating the playlist. Unit: seconds. Valid values:
        # 
        # - 0 (default) or empty: continues until the end of the source video.
        # 
        # - A value greater than 0: continues for the specified duration from the start time of the playlist.
        # 
        # > If the time point corresponding to the specified parameter exceeds the end of the source video, the default value is used.
        self.source_duration = source_duration
        # The start time for generating the playlist. Unit: seconds. Valid values:
        # 
        # - 0 (default) or empty: starts from the beginning of the source video.
        # 
        # - A value greater than 0: starts from the specified time point in the source video.
        # 
        # > You can set this parameter together with **SourceDuration** to generate a playlist for a specific portion of the source video.
        self.source_start_time = source_start_time
        # The list of subtitles to add. This parameter is empty by default. A maximum of two subtitles are supported.
        self.source_subtitles = source_subtitles
        # The OSS URI of the video.
        # 
        # The OSS URI follows the format oss://${Bucket}/${Object}, where ${Bucket} is the name of the OSS bucket in the same region as the current project, and ${Object} is the full path of the file including the file name extension.
        # > Only OSS buckets with Standard storage class are supported.
        # > Buckets with hotlink protection whitelist configured are not supported.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The OSS object [tags](https://help.aliyun.com/document_detail/106678.html) to add to the generated TS files. You can use tags to control the lifecycle of OSS files.
        self.tags = tags
        # The array of just-in-time transcoding playlists. The maximum array length is 6. Each Target corresponds to at most one video Media Playlist and one or more subtitle Media Playlists.
        # > If more than one Target is configured, the **MasterURI** parameter must not be empty.
        # 
        # This parameter is required.
        self.targets = targets
        # The custom information, which is returned in asynchronous message notifications. This allows you to associate message notifications with specific processes in your system. Maximum length: 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.source_subtitles:
            for v1 in self.source_subtitles:
                 if v1:
                    v1.validate()
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.master_uri is not None:
            result['MasterURI'] = self.master_uri

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.overwrite_policy is not None:
            result['OverwritePolicy'] = self.overwrite_policy

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_duration is not None:
            result['SourceDuration'] = self.source_duration

        if self.source_start_time is not None:
            result['SourceStartTime'] = self.source_start_time

        result['SourceSubtitles'] = []
        if self.source_subtitles is not None:
            for k1 in self.source_subtitles:
                result['SourceSubtitles'].append(k1.to_map() if k1 else None)

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.tags is not None:
            result['Tags'] = self.tags

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('MasterURI') is not None:
            self.master_uri = m.get('MasterURI')

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('OverwritePolicy') is not None:
            self.overwrite_policy = m.get('OverwritePolicy')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceDuration') is not None:
            self.source_duration = m.get('SourceDuration')

        if m.get('SourceStartTime') is not None:
            self.source_start_time = m.get('SourceStartTime')

        self.source_subtitles = []
        if m.get('SourceSubtitles') is not None:
            for k1 in m.get('SourceSubtitles'):
                temp_model = main_models.GenerateVideoPlaylistRequestSourceSubtitles()
                self.source_subtitles.append(temp_model.from_map(k1))

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.GenerateVideoPlaylistRequestTargets()
                self.targets.append(temp_model.from_map(k1))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GenerateVideoPlaylistRequestTargets(DaraModel):
    def __init__(
        self,
        audio: main_models.TargetAudio = None,
        container: str = None,
        duration: float = None,
        initial_segments: List[float] = None,
        initial_transcode: float = None,
        subtitle: main_models.TargetSubtitle = None,
        tags: Dict[str, str] = None,
        transcode_ahead: int = None,
        uri: str = None,
        video: main_models.TargetVideo = None,
    ):
        # The audio processing parameter settings. An empty value (default) indicates that audio processing is disabled and the output TS files do not contain audio streams.
        # > The Audio and Subtitle fields within the same Target are mutually exclusive. If the Audio field is set, the Subtitle field is ignored. Audio and Video can be set simultaneously. Audio specifies the audio information in the output video. You can also set only Audio to generate audio-only output.
        self.audio = audio
        self.container = container
        # The playback duration of a single TS file. Unit: seconds. Default value: 10. Valid values: [5, 15].
        self.duration = duration
        # The array of initial transcoding TS file durations. The maximum array length is 6. This parameter is empty by default and is independent of the **Duration** parameter.
        self.initial_segments = initial_segments
        # The initial transcoding duration. Unit: seconds. Default value: 30.
        # 
        # - If the value is set to 0, no pre-transcoding is performed.
        # - If the value is less than 0 or exceeds the source video length, the entire video is initially transcoded.
        # - If the specified duration falls in the middle of a TS file, transcoding continues until the end of that TS file.
        # 
        # > This parameter is primarily used to reduce the wait time for initial video playback and improve the playback experience. If you want to replace traditional VOD business scenarios, try initially transcoding the entire video.
        self.initial_transcode = initial_transcode
        # The subtitle processing parameter settings.
        # > The Subtitle field is mutually exclusive with the Video or Audio fields within the same Target. Subtitles are generated only when Subtitle is set independently.
        self.subtitle = subtitle
        # The OSS object [tags](https://help.aliyun.com/document_detail/106678.html) to add to the generated TS files. You can use OSS tags to control the lifecycle of OSS files.
        # > The tag values at this level are merged with the Tags defined at the parent level to form the tag values for the current Target. If a tag with the same name exists, the value at this level takes precedence.
        self.tags = tags
        # The number of TS files to transcode ahead when just-in-time transcoding is triggered. By default, 2 minutes of video is transcoded ahead.
        # 
        # - Example: If **Duration** is 10, the default value of **TranscodeAhead** is 12. You can specify this parameter to control the number of asynchronous ahead-of-time transcoding files. Valid values: [10, 30].
        self.transcode_ahead = transcode_ahead
        # The OSS URI prefix of the just-in-time transcoding output files, including M3U8 files and TS files.
        # 
        # The OSS URI follows the format oss://${Bucket}/${Object}, where ${Bucket} is the name of the OSS bucket in the same region as the current project, and ${Object} is the full path prefix of the file without the file name extension.
        # 
        # - Example: If URI is oss://test-bucket/test-object/output-video, an oss://test-bucket/test-object/output-video.m3u8 file and multiple oss://test-bucket/test-object/output-video-${token}-${index}.ts files are generated. ${token} is a unique string generated based on the transcoding parameters and is included in the API response. ${index} is the sequence number of the TS file starting from 0.
        # 
        # > If the **MasterURI** parameter is not empty, the URI must be in the same directory as or a subdirectory of the **MasterURI** parameter.
        self.uri = uri
        # The video processing parameter settings. An empty value (default) indicates that video processing is disabled and the output TS files do not contain video streams.
        # > The Video and Subtitle fields within the same Target are mutually exclusive. If the Video field is set, the Subtitle field is ignored.
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.subtitle:
            self.subtitle.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()

        if self.container is not None:
            result['Container'] = self.container

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.initial_segments is not None:
            result['InitialSegments'] = self.initial_segments

        if self.initial_transcode is not None:
            result['InitialTranscode'] = self.initial_transcode

        if self.subtitle is not None:
            result['Subtitle'] = self.subtitle.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.transcode_ahead is not None:
            result['TranscodeAhead'] = self.transcode_ahead

        if self.uri is not None:
            result['URI'] = self.uri

        if self.video is not None:
            result['Video'] = self.video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = main_models.TargetAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            self.container = m.get('Container')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InitialSegments') is not None:
            self.initial_segments = m.get('InitialSegments')

        if m.get('InitialTranscode') is not None:
            self.initial_transcode = m.get('InitialTranscode')

        if m.get('Subtitle') is not None:
            temp_model = main_models.TargetSubtitle()
            self.subtitle = temp_model.from_map(m.get('Subtitle'))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TranscodeAhead') is not None:
            self.transcode_ahead = m.get('TranscodeAhead')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        if m.get('Video') is not None:
            temp_model = main_models.TargetVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class GenerateVideoPlaylistRequestSourceSubtitles(DaraModel):
    def __init__(
        self,
        language: str = None,
        uri: str = None,
    ):
        # The subtitle language. The value follows the ISO 639-2 standard. This parameter is empty by default.
        self.language = language
        # The OSS URI of the subtitle to embed.
        # 
        # The OSS URI follows the format oss://${Bucket}/${Object}, where ${Bucket} is the name of the OSS bucket in the same region as the current project, and ${Object} is the full path of the file.
        # > The **MasterURI** parameter must not be empty, and the OSS URI `oss://${Bucket}/${Object}` of the subtitle must be in the same directory as or a subdirectory of the **MasterURI** parameter.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

