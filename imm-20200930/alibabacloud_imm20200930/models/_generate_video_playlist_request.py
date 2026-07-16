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
        # **If you do not have special requirements, leave this parameter empty.**
        # 
        # The chained authorization configuration. This parameter is not required. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The OSS URI of the Master Playlist.
        # 
        # The OSS URI must be in the format of oss\\://${Bucket}/${Object}. ${Bucket} is the name of the OSS bucket that is in the same region as the current project. ${Object} is the full path of the file with the .m3u8 file name extension.
        # 
        # > If the playlist has subtitle inputs or multiple target outputs, MasterURI is required. The subtitle URI or target URI must be in the same directory as or a subdirectory of the directory specified by MasterURI.
        self.master_uri = master_uri
        # The message notification configuration. For more information, click Notification. For more information about the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The policy to overwrite an existing Media Playlist. Valid values:
        # 
        # - overwrite (default): Overwrites the existing Media Playlist.
        # 
        # - skip-existing: Skips the generation and retains the existing Media Playlist.
        self.overwrite_policy = overwrite_policy
        # The project name. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The duration for which the playlist is generated. Unit: seconds (s). Valid values:
        # 
        # - 0 (default) or empty: continues to the end of the source video.
        # 
        # - Greater than 0: lasts for the specified duration from the start time.
        # 
        # > If the specified duration extends beyond the end of the source video, the default value is used.
        self.source_duration = source_duration
        # The start time for generating the playlist. Unit: seconds (s). Valid values:
        # 
        # - 0 (default) or empty: starts from the beginning of the source video.
        # 
        # - Greater than 0: starts from the specified time point in the source video.
        # 
        # > You can set this parameter together with the **SourceDuration** parameter to generate a playlist for a specific part of the source video.
        self.source_start_time = source_start_time
        # The list of subtitles to add. The default value is empty. You can add up to two subtitles.
        self.source_subtitles = source_subtitles
        # The OSS URI of the video.
        # 
        # The OSS URI must be in the format of oss\\://${Bucket}/${Object}. ${Bucket} is the name of the OSS bucket that is in the same region as the current project. ${Object} is the full path of the file, including the file name extension.
        # 
        # > Only OSS Standard storage buckets are supported. Buckets with hotlink protection whitelists are not supported.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # Adds OSS object [tags](https://help.aliyun.com/document_detail/106678.html) to the generated TS files. You can use tags to control the lifecycle of OSS files.
        self.tags = tags
        # An array of live transcoding playlists. The maximum array length is 6. Each target corresponds to a maximum of one video Media Playlist and one or more subtitle Media Playlists.
        # 
        # > If you configure more than one target, the **MasterURI** parameter must not be empty.
        # 
        # This parameter is required.
        self.targets = targets
        # The custom information. This information is returned in the asynchronous notification message to help you associate the message with your services. The maximum length is 2,048 bytes.
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
        duration: float = None,
        initial_segments: List[float] = None,
        initial_transcode: float = None,
        subtitle: main_models.TargetSubtitle = None,
        tags: Dict[str, str] = None,
        transcode_ahead: int = None,
        uri: str = None,
        video: main_models.TargetVideo = None,
    ):
        # The parameter settings for audio processing. An empty value (default) disables audio processing. The output TS file will not contain an audio stream.
        # 
        # > The Audio and Subtitle fields within the same target are mutually exclusive. If the Audio field is set, the Subtitle field is ignored. You can set both Audio and Video. Audio specifies the audio information in the output video. You can also set only Audio to generate only audio information.
        self.audio = audio
        # The playback duration of a single TS file. Unit: seconds (s). Default value: 10. Value range: [5, 15].
        self.duration = duration
        # An array of durations for the initial transcoded TS files. The maximum array length is 6. The default value is empty. This parameter is independent of the **Duration** parameter.
        self.initial_segments = initial_segments
        # The initial transcoding duration. Unit: seconds (s). Default value: 30.
        # 
        # - If you set this parameter to 0, pre-transcoding is not performed.
        # 
        # - If you set this parameter to a value less than 0 or a value that exceeds the source video length, the entire video is initially transcoded.
        # 
        # - If the specified duration ends in the middle of a TS file, transcoding continues to the end of that TS file.
        # 
        # > This parameter is mainly used to reduce the waiting time for the first playback and improve the user experience. To replace a traditional VOD scenario, you can try initially transcoding the entire video.
        self.initial_transcode = initial_transcode
        # The parameter settings for subtitle processing.
        # 
        # > The Subtitle field is mutually exclusive with the Video and Audio fields within the same target. Subtitles can be generated only when the Subtitle field is set independently.
        self.subtitle = subtitle
        # Adds OSS object [tags](https://help.aliyun.com/document_detail/106678.html) to the generated TS files. You can use OSS tags to control the lifecycle of OSS files.
        # 
        # > The tags for the current target are the union of the tags defined at this level and the tags defined at the parent level. If a tag has the same name, the value at the current level is used.
        self.tags = tags
        # The number of TS files to transcode ahead when live transcoding is triggered. By default, 2 minutes of video is transcoded ahead.
        # 
        # - Example: If **Duration** is 10, the default value of **TranscodeAhead** is 12. You can specify this parameter to control the number of asynchronous forward transcodes. The value must be in the range of [10, 30].
        self.transcode_ahead = transcode_ahead
        # The OSS URI prefix for the output files of live transcoding. The output files include M3U8 files and TS files.
        # 
        # The OSS URI must be in the format of oss\\://${Bucket}/${Object}. ${Bucket} is the name of the OSS bucket that is in the same region as the current project. ${Object} is the prefix of the full path of the file, without the file name extension.
        # 
        # - Example: If URI is oss\\://test-bucket/test-object/output-video, one oss\\://test-bucket/test-object/output-video.m3u8 file and multiple oss\\://test-bucket/test-object/output-video-${token}-${index}.ts files are generated. ${token} is a unique string generated based on the transcoding parameters and is included in the API response. ${index} is the sequence number of the generated TS file, starting from 0.
        # 
        # > If the **MasterURI** parameter is not empty, the URI must be in the same directory as or a subdirectory of the directory specified by **MasterURI**.
        self.uri = uri
        # The parameter settings for video processing. An empty value (default) disables video processing. The output TS file will not contain a video stream.
        # 
        # > The Video and Subtitle fields within the same target are mutually exclusive. If the Video field is set, the Subtitle field is ignored.
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
        # The language of the subtitle. The value must comply with the ISO 639-2 standard. The default value is empty.
        self.language = language
        # The OSS URI of the subtitle file to embed.
        # 
        # The OSS URI must be in the format of oss\\://${Bucket}/${Object}. ${Bucket} is the name of the OSS bucket that is in the same region as the current project. ${Object} is the full path of the file.
        # 
        # > The **MasterURI** parameter must not be empty. The OSS URI of the subtitle file to embed, `oss://${Bucket}/${Object}`, must be in the same directory as or a subdirectory of the directory specified by **MasterURI**.
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

