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
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The OSS path of the master playlist.
        # 
        # The OSS path must be in the oss://${Bucket}/${Object} format. ${Bucket} specifies the name of the OSS bucket that is in the same region as the current project. ${Object} specifies the full path of the file that is suffixed with .m3u8.
        # 
        # >  If a playlist contains subtitles or multiple outputs, the MasterURI parameter is required and the URI of subtitle files or outputs must be in the directory specified by the MasterURI parameter or its subdirectory.
        self.master_uri = master_uri
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The overwrite policy when the media playlist exists. Valid values:
        # 
        # *   overwrite (default): overwrites an existing media playlist.
        # *   skip-existing: skips generation and retains the existing media playlist.
        self.overwrite_policy = overwrite_policy
        # The project name.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The period of time during which the playlist is generated. Unit: seconds.
        # 
        # *   If you set this parameter to 0 (default) or leave this parameter empty, a playlist is generated until the end time of the source video.
        # *   If you set this parameter to a value greater than 0, a playlist is generated for the specified period of time from the start time that you specify.
        # 
        # >  If you set this parameter to a value that exceeds the end time of a source video, use the default value.
        self.source_duration = source_duration
        # The time when the playlist starts to generate. Unit: seconds.
        # 
        # *   If you set this parameter to 0 (default) or leave this parameter empty, the start time of the source video is used as the time when a playlist starts to generate.
        # *   If you set this parameter to a value greater than 0, the time when a playlist starts to generate is the specified point in time.
        # 
        # >  If you use this parameter together with the **SourceDuration** parameter, a playlist can be generated based on the partial content of a source video.
        self.source_start_time = source_start_time
        # The subtitle files. By default, this parameter is left empty. Up to two subtitle files are supported.
        self.source_subtitles = source_subtitles
        # The OSS path of the video file.
        # 
        # The OSS path must be in the oss://${Bucket}/${Object} format. ${Bucket} specifies the name of the OSS bucket that is in the same region as the current project. ${Object} specifies the full path of the file that contains the file name extension.
        # 
        # >  Only OSS buckets of the Standard storage class are supported. OSS buckets for which hotlink protection whitelists are configured are not supported.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The [tags](https://help.aliyun.com/document_detail/106678.html) that you want to add to a TS file in OSS. You can use tags to manage the lifecycles of TS files in OSS.
        self.tags = tags
        # The array of live transcoding playlists. The maximum length of the array is 6. Each element corresponds to at most one video media playlist and one or more subtitle media playlists.
        # 
        # >  If the array contains more than one element, the **MasterURI** parameter cannot be left empty.
        # 
        # This parameter is required.
        self.targets = targets
        # The custom user information, which is returned in asynchronous notifications to help you handle the notifications in the system. The maximum length of a notification is 2048 bytes.
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
        # The audio processing configuration. If you set this parameter to null (default), audio processing is disabled. The generated TS files do not contain audio streams.
        # 
        # >  The Audio and Subtitle parameters in the same element are mutually exclusive. If the Audio parameter is configured, the Subtitle parameter is ignored. The Audio and Video parameters can be configured at the same time. You can also configure only the Audio parameter to generate only audio.
        self.audio = audio
        # The playback duration of a single TS file. Unit: seconds. Default value: 10. Valid values: 5 to 15.
        self.duration = duration
        # The array of the durations of the pre-transcoded TS files. The maximum length of the array is 6. By default, this parameter is left empty. This parameter is independent of the **Duration** parameter.
        self.initial_segments = initial_segments
        # The pre-transcoding duration. Unit: seconds. Default value: 30.
        # 
        # *   If you set this parameter to 0, pre-transcoding is disabled.
        # *   If you set this parameter to a value that is less than 0 or greater than the duration of a source video, the entire video is pre-transcoded.
        # *   If you set this parameter to a value that is within the middle of the playback duration of a TS file, the transcoding continues until the end of the playback duration.
        # 
        # >  This parameter reduces the time required to start the first playback, which enhances the viewing experience. If you want to use live transcoding in traditional video-on-demand scenarios, you can pre-transcode entire videos.
        self.initial_transcode = initial_transcode
        # The subtitle processing configuration.
        # 
        # >  The Subtitle and Video or Audio parameters in the same element are mutually exclusive. You must configure the Subtitle parameter independently to generate subtitles.
        self.subtitle = subtitle
        # The [tags](https://help.aliyun.com/document_detail/106678.html) that you want to add to a TS file in OSS. You can use tags to manage the lifecycles of TS files in OSS.
        # 
        # >  The combination of the value of the Tags parameter and the value of the Tags parameter in the upper level is used as the tag value of the current output. If the value of the Tags parameter in the current level is the same as the value of the Tags parameter in the upper level, the value of the Tags parameter in the current level is used.
        self.tags = tags
        # The number of TS files that are pre-transcoded when the live transcoding is triggered. By default, a 2-minute video is pre-transcoded.
        # 
        # *   Example: If you set the **Duration** parameter to 10, the value of the **TranscodeAhead** parameter is 12 by default. You can configure this parameter to manage the number of pre-transcoded files. Valid values: 10 to 30.
        self.transcode_ahead = transcode_ahead
        # The prefix of the OSS path that is used to store the live transcoding files. The live transcoding files include a M3U8 file and multiple TS files.
        # 
        # The OSS path must be in the oss://${Bucket}/${Object} format. ${Bucket} specifies the name of the OSS bucket that is in the same region as the current project. ${Object} specifies the prefix of the full path that does not contain the file name extension.
        # 
        # *   Example: If the URI is oss://test-bucket/test-object/output-video, the output-video.m3u8 file and multiple output-video-${token}-${index}.ts files are generated in the oss://test-bucket/test-object/ directory. ${token} is a unique string generated based on the transcoding parameters. The ${token} parameter is included in the response of the operation. ${index} is the serial number of the generated TS files that are numbered starting from 0.
        # 
        # >  If the **MasterURI** parameter is not left empty, the path specified by this parameter must be in the directory specified by the **MasterURI** parameter or its subdirectory.
        self.uri = uri
        # The video processing configuration. If you set this parameter to null (default), video processing is disabled. The generated TS files do not contain video streams.
        # 
        # >  The Video and Subtitle parameters in the same element are mutually exclusive. If the Video parameter is configured, the Subtitle parameter is ignored.
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
        # The subtitle language. If you configure this parameter, the value must comply with the ISO 639-2 standard. By default, this parameter is left empty.
        self.language = language
        # The OSS path of the subtitle file.
        # 
        # The OSS path must be in the oss://${Bucket}/${Object} format. ${Bucket} specifies the name of the OSS bucket that is in the same region as the current project. ${Object} specifies the full path of the file.
        # 
        # >  The **MasterURI** parameter cannot be left empty, and the OSS path `oss://${Bucket}/${Object}` of a subtitle file must be in the directory specified by the **MasterURI** parameter or its subdirectory.
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

