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
        target_groups: List[main_models.CreateMediaConvertTaskRequestTargetGroups] = None,
        targets: List[main_models.CreateMediaConvertTaskRequestTargets] = None,
        user_data: str = None,
    ):
        # When concatenating media files, this specifies the index of the primary file in the Sources list. The default transcoding parameters (such as resolution and frame rate from the `Video` and `Audio` objects) are taken from this primary file. The default index is 0.
        self.alignment_index = alignment_index
        # **You can leave this parameter empty if you do not have special requirements.**
        # 
        # The chained authorization configuration. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The message notification settings. For more information, click Notification. For information about the format of asynchronous notifications, see [Asynchronous notification format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The name of the project. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # A list of media files. If you provide more than one file, they are concatenated in the order of their URIs.
        # 
        # This parameter is required.
        self.sources = sources
        # Custom tags for searching and filtering asynchronous tasks.
        self.tags = tags
        # A list of media packaging tasks to convert and package the input media into HLS outputs. Each TargetGroup corresponds to one HLS master playlist.
        self.target_groups = target_groups
        # A list of media processing tasks.
        self.targets = targets
        # The custom user data. This data is returned in the asynchronous notification, allowing you to associate the notification with your internal system. The maximum length is 2,048 bytes.
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
        if self.target_groups:
            for v1 in self.target_groups:
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

        result['TargetGroups'] = []
        if self.target_groups is not None:
            for k1 in self.target_groups:
                result['TargetGroups'].append(k1.to_map() if k1 else None)

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

        self.target_groups = []
        if m.get('TargetGroups') is not None:
            for k1 in m.get('TargetGroups'):
                temp_model = main_models.CreateMediaConvertTaskRequestTargetGroups()
                self.target_groups.append(temp_model.from_map(k1))

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
        attached_picture: main_models.CreateMediaConvertTaskRequestTargetsAttachedPicture = None,
        audio: main_models.TargetAudio = None,
        container: str = None,
        data: main_models.CreateMediaConvertTaskRequestTargetsData = None,
        image: main_models.TargetImage = None,
        segment: main_models.CreateMediaConvertTaskRequestTargetsSegment = None,
        speed: float = None,
        strip_metadata: bool = None,
        subtitle: main_models.TargetSubtitle = None,
        uri: str = None,
        video: main_models.TargetVideo = None,
    ):
        # Settings for retaining attached pictures.
        # >Notice: Retaining attached pictures is supported only when the `Container` parameter is set to `mp4` or `mkv`.
        self.attached_picture = attached_picture
        # The audio processing parameters.
        # >Notice: If this parameter is left empty, the first audio stream, if it exists, is copied directly to the output file.
        self.audio = audio
        # The media container type. Valid container types include:
        # 
        # - Audio/video containers: mp4, mkv, mov, asf, avi, mxf, ts, flv
        # 
        # - Audio-only containers: mp3, aac, flac, oga, ac3, opus
        # 
        # 
        #   >Notice: 
        # 
        #   The `Container` and `URI` parameters must be set together. To perform only subtitle extraction, frame capture, sprite generation, or animated image generation, leave both `Container` and `URI` empty. In this case, parameters such as `Segment`, `Video`, `Audio`, and `Speed` are ignored.
        self.container = container
        # Settings for retaining data streams.
        # >Notice: Retaining data streams is supported only when the `Container` parameter is set to `mp4`.
        self.data = data
        # The parameters for frame capture, sprite generation, and animated image generation.
        self.image = image
        # Settings for media segmentation.
        self.segment = segment
        # The playback speed of the output media. The value must be between 0.5 and 1.0, inclusive. The default value is 1.0.
        # 
        # > This parameter specifies the default playback speed of the output file as a ratio of the source file\\"s speed. It does not perform speed-up transcoding.
        self.speed = speed
        # If true, removes metadata such as `title` and `album` from the media file. The default is false.
        self.strip_metadata = strip_metadata
        # The subtitle processing parameters.
        # >Notice: If this parameter is left empty, the first subtitle stream, if it exists, is copied directly to the output file.
        self.subtitle = subtitle
        # The OSS URI of the output file for media transcoding.
        # 
        # The URI must be in the `oss://${Bucket}/${Object}` format. In this format, `${Bucket}` is the name of the OSS bucket, which must be in the same region as the project, and `${Object}` is the full path to the object, including the file extension.
        # 
        # - If the **URI** has a file extension, all output media files are saved to this **URI**. If multiple files are generated, they will overwrite each other.
        # 
        # - If the **URI** does not have a file extension, the final output URI is generated based on the **URI**, **Container**, and **Segment** parameters. For example, if the **URI** is `oss://examplebucket/outputVideo`:
        # 
        #   - If **Container** is `mp4` and **Segment** is empty, the OSS URI of the generated media file is `oss://examplebucket/outputVideo.mp4`.
        # 
        #   - If **Container** is `ts` and **Format** in **Segment** is `hls`, the process generates an m3u8 file with the OSS URI `oss://examplebucket/outputVideo.m3u8` and multiple TS files prefixed with `oss://examplebucket/outputVideo`.
        self.uri = uri
        # The video processing parameters.
        # >Notice: If this parameter is left empty, the first video stream, if it exists, is copied directly to the output file.
        self.video = video

    def validate(self):
        if self.attached_picture:
            self.attached_picture.validate()
        if self.audio:
            self.audio.validate()
        if self.data:
            self.data.validate()
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
        if self.attached_picture is not None:
            result['AttachedPicture'] = self.attached_picture.to_map()

        if self.audio is not None:
            result['Audio'] = self.audio.to_map()

        if self.container is not None:
            result['Container'] = self.container

        if self.data is not None:
            result['Data'] = self.data.to_map()

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
        if m.get('AttachedPicture') is not None:
            temp_model = main_models.CreateMediaConvertTaskRequestTargetsAttachedPicture()
            self.attached_picture = temp_model.from_map(m.get('AttachedPicture'))

        if m.get('Audio') is not None:
            temp_model = main_models.TargetAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            self.container = m.get('Container')

        if m.get('Data') is not None:
            temp_model = main_models.CreateMediaConvertTaskRequestTargetsData()
            self.data = temp_model.from_map(m.get('Data'))

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
        # The duration of each segment, in seconds.
        self.duration = duration
        # The segmentation method. Valid values include:
        # 
        # - hls
        # 
        # - dash
        self.format = format
        # The starting sequence number. This parameter is supported only for HLS. The default value is 0.
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

class CreateMediaConvertTaskRequestTargetsData(DaraModel):
    def __init__(
        self,
        stream: List[int] = None,
    ):
        # A list of indexes of the data streams in the source file to process. An empty list (default) indicates that no data streams are retained. An index of -1 indicates that all data streams are retained.
        # 
        # - Example: `[0,1]` processes the data streams with index 0 and 1; `[1]` processes the data stream with index 1; `[-1]` processes all data streams.
        # 
        # > If a specified index does not correspond to an existing data stream, it is ignored.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

class CreateMediaConvertTaskRequestTargetsAttachedPicture(DaraModel):
    def __init__(
        self,
        stream: List[int] = None,
    ):
        # A list of indexes of the attached pictures in the source file to process. An empty list (default) indicates that no attached pictures are retained. An index of -1 indicates that all attached pictures are retained.
        # 
        # - Example: `[0,1]` processes the attached pictures with index 0 and 1; `[1]` processes the attached picture with index 1; `[-1]` processes all attached pictures.
        # 
        # > If a specified index does not correspond to an existing attached picture, it is ignored.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

class CreateMediaConvertTaskRequestTargetGroups(DaraModel):
    def __init__(
        self,
        targets: List[main_models.CreateMediaConvertTaskRequestTargetGroupsTargets] = None,
        uri: str = None,
    ):
        # A list of media packaging subtasks. Each `Target` corresponds to a variant stream (`#EXT-X-STREAM-INF`) in the HLS master playlist and generates a corresponding HLS media playlist.
        self.targets = targets
        # The OSS URI of the output HLS master playlist file for the packaging task.
        self.uri = uri

    def validate(self):
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.CreateMediaConvertTaskRequestTargetGroupsTargets()
                self.targets.append(temp_model.from_map(k1))

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

class CreateMediaConvertTaskRequestTargetGroupsTargets(DaraModel):
    def __init__(
        self,
        audio: main_models.TargetAudio = None,
        container: str = None,
        segment: main_models.CreateMediaConvertTaskRequestTargetGroupsTargetsSegment = None,
        speed: float = None,
        strip_metadata: bool = None,
        subtitle: main_models.TargetSubtitle = None,
        uri: str = None,
        video: main_models.TargetVideo = None,
    ):
        # The audio processing parameters.
        # >Notice: If this parameter is left empty, the first audio stream, if it exists, is copied directly to the output file.
        self.audio = audio
        # The packaging container type. Only `mp4` and `ts` are supported.
        self.container = container
        # The media packaging settings.
        self.segment = segment
        # The playback speed of the output media. The value must be between 0.5 and 1.0, inclusive. The default value is 1.0.
        # 
        # > This parameter specifies the default playback speed of the output file as a ratio of the source file\\"s speed. It does not perform speed-up transcoding.
        self.speed = speed
        # If true, removes metadata from the output file. The default is false.
        self.strip_metadata = strip_metadata
        # The subtitle processing parameters.
        # >Notice: You must use the `Subtitle.ExtractSubtitle` parameter to package subtitle streams. The `URI` in `Subtitle.ExtractSubtitle` must be in the same directory as or a subdirectory of `TargetGroups.URI`. The `Format` in `Subtitle.ExtractSubtitle` must be `vtt`. You only need to configure this parameter in one `Target` to package all subtitle streams.
        self.subtitle = subtitle
        # The OSS URI of the output HLS media playlist file for the subtask.
        # >Notice: This URI must be in the same directory as or a subdirectory of `TargetGroups.URI`.
        self.uri = uri
        # The video processing parameters.
        # >Notice: If this parameter is left empty, the first video stream, if it exists, is copied directly to the output file.
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
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

        if m.get('Segment') is not None:
            temp_model = main_models.CreateMediaConvertTaskRequestTargetGroupsTargetsSegment()
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

class CreateMediaConvertTaskRequestTargetGroupsTargetsSegment(DaraModel):
    def __init__(
        self,
        duration: float = None,
        format: str = None,
        start_number: int = None,
    ):
        # The duration of each segment, in seconds.
        self.duration = duration
        # The media packaging format. Only `hls` is supported.
        self.format = format
        # The starting sequence number for segments. The default is 0.
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
        # The alignment mode for the added audio and video streams. Valid values include:
        # 
        # - false (default): No alignment is performed.
        # 
        # - loop: Aligns content by looping the audio or video.
        # 
        # - pad: Aligns content by padding with silent frames or black frames.
        # 
        # > * This parameter only takes effect if Attached is set to true.
        self.align_mode = align_mode
        # If true, adds the current source media file to the output as a synchronized audio stream or video stream. The default is false.
        # 
        # > - You cannot set Attached to true for the source media file referenced by AlignmentIndex.
        self.attached = attached
        # Specifies whether to disable the audio from the source media file. Valid values include:
        # 
        # - true: Disables the audio.
        # 
        # - false (default): Includes the audio.
        self.disable_audio = disable_audio
        # Specifies whether to disable the video from the source media file. Valid values include:
        # 
        # - true: Disables the video.
        # 
        # - false (default): Includes the video.
        self.disable_video = disable_video
        # The duration of media transcoding in seconds. The default value, 0, transcodes the media until its end.
        self.duration = duration
        # The start time of media transcoding, in seconds. Valid values include:
        # 
        # - 0 (default): Transcoding starts from the beginning of the media file.
        # 
        # - n (a value greater than 0): Transcoding starts n seconds into the media file.
        self.start_time = start_time
        # A list of subtitles to add.
        self.subtitles = subtitles
        # The OSS URI of the object. The URI must use the `oss://${Bucket}/${Object}` format, where `${Bucket}` is the name of an OSS bucket in the same region as the project, and `${Object}` is the full path to the object, including its file extension.
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
        # The language of the subtitle. The value must comply with the ISO 639-2 standard.
        self.language = language
        # The subtitle delay, in seconds. The default value is 0.
        self.time_offset = time_offset
        # The OSS URI of the object. The URI must use the `oss://${Bucket}/${Object}` format, where `${Bucket}` is the name of an OSS bucket in the same region as the project, and `${Object}` is the full path to the object, including its file extension.
        # Supported subtitle formats include: srt, vtt, mov_text, ass, dvd_sub, and pgs.
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

