# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateMediaConvertTaskRequest(DaraModel):
    def __init__(
        self,
        alignment_index: int = None,
        credential_config: main_models.CredentialConfig = None,
        notification: main_models.Notification = None,
        project_name: str = None,
        sources: List[main_models.CreateMediaConvertTaskRequestSources] = None,
        tags: Dict[str, Any] = None,
        targets: List[main_models.CreateMediaConvertTaskRequestTargets] = None,
        user_data: str = None,
    ):
        # When performing media concatenation, the index of the primary media file (which provides the default transcoding parameters for `Video` and `Audio`, including resolution, frame rate, etc.) in the concatenation list. The default value is 0 (aligning with the first media file in the concatenation list).
        self.alignment_index = alignment_index
        # **If there are no special requirements, please leave this blank.**
        # 
        # Chain authorization configuration. For more information, see [Using Chain Authorization to Access Other Entity Resources](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # Notification configuration. For details, click Notification. The format of asynchronous notification messages can be found in [Asynchronous Notification Message Format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The name of the project. For how to obtain it, see [Creating a Project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # A list of media files. If the list contains more than one element, it indicates that the Concat (concatenation) function is enabled. The Concat order follows the sequence of the input video file URIs.
        # 
        # This parameter is required.
        self.sources = sources
        # Custom tags used for searching and filtering asynchronous tasks.
        self.tags = tags
        # List of media processing tasks, supporting multiple task configurations.
        # 
        # This parameter is required.
        self.targets = targets
        # User-defined information that will be returned in asynchronous message notifications, used for convenient association and processing within your system. The maximum length is 2048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for v1 in self.sources:
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
        if self.alignment_index is not None:
            result['AlignmentIndex'] = self.alignment_index

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

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
        if m.get('AlignmentIndex') is not None:
            self.alignment_index = m.get('AlignmentIndex')

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.CreateMediaConvertTaskRequestSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.CreateMediaConvertTaskRequestTargets()
                self.targets.append(temp_model.from_map(k1))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class CreateMediaConvertTaskRequestTargets(DaraModel):
    def __init__(
        self,
        audio: main_models.TargetAudio = None,
        container: str = None,
        image: main_models.TargetImage = None,
        segment: main_models.CreateMediaConvertTaskRequestTargetsSegment = None,
        speed: float = None,
        strip_metadata: bool = None,
        subtitle: main_models.TargetSubtitle = None,
        uri: str = None,
        video: main_models.TargetVideo = None,
    ):
        # Audio processing parameter configuration.
        # >Notice: If Audio is null, the first audio stream (if present) will be directly copied to the output file.</notice>
        self.audio = audio
        # Media container type. Available container types are as follows:
        # - Audio and video containers: mp4, mkv, mov, asf, avi, mxf, ts, flv
        # - Audio containers: mp3, aac, flac, oga, ac3, opus
        # >Notice: Both Container and URI parameters need to be set. If only subtitle extraction, frame capture, sprite image capture, or media-to-gif conversion is performed, both Container and URI should be set to null, making the Segment, Video, Audio, and Speed parameters meaningless.</notice>
        self.container = container
        # Configuration for frame capture, sprite image capture, and media to animated image conversion.
        self.image = image
        # Media segment settings, no segmentation by default.
        self.segment = segment
        # Media playback speed setting, with a value range of [0.5,1.0], default is 1.0.
        # > The ratio of the playback speed of the transcoded media file to the original media file, not a speed-up transcoding.
        self.speed = speed
        # Removes metadata from the media file, such as `title`, `album`, etc. The default value is false.
        self.strip_metadata = strip_metadata
        # Subtitle processing parameter configuration.
        # >Notice: If Subtitle is null, the first subtitle stream (if present) will be directly copied to the output file.</notice>
        self.subtitle = subtitle
        # OSS address for the output file of media transcoding.
        # 
        # The OSS address rule is `oss://${Bucket}/${Object}`, where `${Bucket}` is the name of the OSS Bucket in the same region (Region) as the current project, and `${Object}` is the complete path of the file including the file extension.
        # - When **URI** has an extension, the OSS address for the transcoded media file will be **URI**. If there are multiple output files, they may overwrite each other.
        # - When **URI** does not have an extension, the OSS address for the transcoded media file is determined by the **URI**, **Container**, and **Segment** parameters. For example, if **URI** is `oss://examplebucket/outputVideo`:
        #    -  When **Container** is `mp4` and **Segment** is empty, the generated media file\\"s OSS address will be `oss://examplebucket/outputVideo.mp4`.
        #    -  When **Container** is `ts` and **Segment**\\"s **Format** is `hls`, it will generate an m3u8 file with the OSS address `oss://examplebucket/outputVideo.m3u8` and multiple ts files with the prefix `oss://examplebucket/outputVideo`.
        self.uri = uri
        # Video processing parameter configuration.
        # >Notice: If Video is null, the first video stream (if present) will be directly copied to the output file.</notice>
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.image:
            self.image.validate()
        if self.segment:
            self.segment.validate()
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

        if self.image is not None:
            result['Image'] = self.image.to_map()

        if self.segment is not None:
            result['Segment'] = self.segment.to_map()

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.strip_metadata is not None:
            result['StripMetadata'] = self.strip_metadata

        if self.subtitle is not None:
            result['Subtitle'] = self.subtitle.to_map()

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

        if m.get('Image') is not None:
            temp_model = main_models.TargetImage()
            self.image = temp_model.from_map(m.get('Image'))

        if m.get('Segment') is not None:
            temp_model = main_models.CreateMediaConvertTaskRequestTargetsSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('StripMetadata') is not None:
            self.strip_metadata = m.get('StripMetadata')

        if m.get('Subtitle') is not None:
            temp_model = main_models.TargetSubtitle()
            self.subtitle = temp_model.from_map(m.get('Subtitle'))

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        if m.get('Video') is not None:
            temp_model = main_models.TargetVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class CreateMediaConvertTaskRequestTargetsSegment(DaraModel):
    def __init__(
        self,
        duration: float = None,
        format: str = None,
        start_number: int = None,
    ):
        # Segment length. Unit: seconds.
        self.duration = duration
        # Media slicing method. The value range is as follows:
        # - hls
        # - dash
        self.format = format
        # Starting sequence number, supported only for hls, default is 0.
        self.start_number = start_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.format is not None:
            result['Format'] = self.format

        if self.start_number is not None:
            result['StartNumber'] = self.start_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('StartNumber') is not None:
            self.start_number = m.get('StartNumber')

        return self

class CreateMediaConvertTaskRequestSources(DaraModel):
    def __init__(
        self,
        align_mode: str = None,
        attached: bool = None,
        disable_audio: bool = None,
        disable_video: bool = None,
        duration: float = None,
        start_time: float = None,
        subtitles: List[main_models.CreateMediaConvertTaskRequestSourcesSubtitles] = None,
        uri: str = None,
    ):
        # The alignment strategy for adding audio and video streams, with the following value range:
        # - false (default): No alignment.
        # - loop: Loop the audio and video content to align.
        # - pad: Align by padding silent frames and black video frames.
        # > - Only valid when the Attached parameter is true.
        self.align_mode = align_mode
        # Add the current source media file as a synchronized audio or video stream to the output media file, with a default value of false.
        # 
        # > - The AlignmentIndex parameter pointing to the Attached parameter of the Source cannot be true.
        self.attached = attached
        # Whether to disable the audio in the source media file. The value range is as follows:
        # 
        # - true: Disable.
        # - false (default): Do not disable.
        self.disable_audio = disable_audio
        # Whether to disable the video in the source media file. The value range is as follows:
        # 
        # - true: Disable.
        # - false (default): Do not disable.
        self.disable_video = disable_video
        # The duration of media transcoding, in seconds. The default value is 0, indicating until the end of the video.
        self.duration = duration
        # The start time for media transcoding, in seconds. The value range is as follows:
        # - 0 (default): Start transcoding from the beginning of the media.
        # - n (greater than 0): Start transcoding n seconds after the beginning of the media.
        self.start_time = start_time
        # A list of subtitles to add, which is empty by default.
        self.subtitles = subtitles
        # The OSS address rule is `oss://${Bucket}/${Object}`, where `${Bucket}` is the name of the OSS Bucket in the same region (Region) as the current project, and `${Object}` is the complete path of the file including the file extension.
        self.uri = uri

    def validate(self):
        if self.subtitles:
            for v1 in self.subtitles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.align_mode is not None:
            result['AlignMode'] = self.align_mode

        if self.attached is not None:
            result['Attached'] = self.attached

        if self.disable_audio is not None:
            result['DisableAudio'] = self.disable_audio

        if self.disable_video is not None:
            result['DisableVideo'] = self.disable_video

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['Subtitles'] = []
        if self.subtitles is not None:
            for k1 in self.subtitles:
                result['Subtitles'].append(k1.to_map() if k1 else None)

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlignMode') is not None:
            self.align_mode = m.get('AlignMode')

        if m.get('Attached') is not None:
            self.attached = m.get('Attached')

        if m.get('DisableAudio') is not None:
            self.disable_audio = m.get('DisableAudio')

        if m.get('DisableVideo') is not None:
            self.disable_video = m.get('DisableVideo')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k1 in m.get('Subtitles'):
                temp_model = main_models.CreateMediaConvertTaskRequestSourcesSubtitles()
                self.subtitles.append(temp_model.from_map(k1))

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

class CreateMediaConvertTaskRequestSourcesSubtitles(DaraModel):
    def __init__(
        self,
        language: str = None,
        time_offset: float = None,
        uri: str = None,
    ):
        # The language of the subtitle, referenced by ISO 639-2, with a default value of empty.
        self.language = language
        # The subtitle delay time, in seconds, with a default value of 0.
        self.time_offset = time_offset
        # The OSS address rule is `oss://${Bucket}/${Object}`, where `${Bucket}` is the name of the OSS Bucket in the same region (Region) as the current project, and `${Object}` is the complete path of the file including the file extension.
        # Supported subtitle formats include: srt, vtt, mov_text, ass, dvd_sub, pgs.
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

        if self.time_offset is not None:
            result['TimeOffset'] = self.time_offset

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('TimeOffset') is not None:
            self.time_offset = m.get('TimeOffset')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

