# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateHighlightTaskRequest(DaraModel):
    def __init__(
        self,
        credential_config: main_models.CredentialConfig = None,
        edit: main_models.CreateHighlightTaskRequestEdit = None,
        highlight: main_models.CreateHighlightTaskRequestHighlight = None,
        mode: str = None,
        notification: main_models.Notification = None,
        output: main_models.CreateHighlightTaskRequestOutput = None,
        project_name: str = None,
        sources: List[main_models.CreateHighlightTaskRequestSources] = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        user_data: str = None,
    ):
        # The chained authorization configuration. **Leave this parameter empty unless otherwise required.**
        self.credential_config = credential_config
        # The editing configuration.
        self.edit = edit
        # The highlight configuration.
        self.highlight = highlight
        # The highlight recognition mode. Valid values:
        # - Scene: scene and frame recognition
        # - Average: average clip recognition
        # Default value: Average.
        self.mode = mode
        # The message notification configuration. For more information, see Notification. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://www.alibabacloud.com/help/en/imm/developer-reference/asynchronous-notification-message-examples).
        self.notification = notification
        # The output configuration.
        # 
        # This parameter is required.
        self.output = output
        # The name of the project.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The list of media resources to be processed. You can specify up to 10 videos.
        # 
        # This parameter is required.
        self.sources = sources
        # The custom tags used to search and filter asynchronous tasks.
        self.tags = tags
        # The processing type. Valid values:
        # - Retrieval: highlight extraction
        # - Concat: video composition
        # - Compose: one-click video creation
        # 
        # This parameter is required.
        self.type = type
        # The custom user data, which is returned in asynchronous message notifications.
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.edit:
            self.edit.validate()
        if self.highlight:
            self.highlight.validate()
        if self.notification:
            self.notification.validate()
        if self.output:
            self.output.validate()
        if self.sources:
            for v1 in self.sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.edit is not None:
            result['Edit'] = self.edit.to_map()

        if self.highlight is not None:
            result['Highlight'] = self.highlight.to_map()

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('Edit') is not None:
            temp_model = main_models.CreateHighlightTaskRequestEdit()
            self.edit = temp_model.from_map(m.get('Edit'))

        if m.get('Highlight') is not None:
            temp_model = main_models.CreateHighlightTaskRequestHighlight()
            self.highlight = temp_model.from_map(m.get('Highlight'))

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('Output') is not None:
            temp_model = main_models.CreateHighlightTaskRequestOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.CreateHighlightTaskRequestSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class CreateHighlightTaskRequestSources(DaraModel):
    def __init__(
        self,
        duration: float = None,
        start_time: float = None,
        uri: str = None,
    ):
        # The duration of the media clip. Unit: seconds. Default value: 0, which indicates the end time of the video. This parameter is valid only when Type is set to Concat.
        self.duration = duration
        # The start time of the media resource. Valid values: [0, video duration]. This parameter is valid only when Type is set to Concat. Unit: seconds.
        self.start_time = start_time
        # The URI of the media resource, which is an OSS URI. Only videos are supported.
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
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

class CreateHighlightTaskRequestOutput(DaraModel):
    def __init__(
        self,
        audio: main_models.TargetAudio = None,
        container: str = None,
        max_duration: float = None,
        segment: main_models.CreateHighlightTaskRequestOutputSegment = None,
        speed: float = None,
        target_duration: float = None,
        uri: str = None,
        video: main_models.TargetVideo = None,
    ):
        # The audio processing parameter settings. >Notice: If Audio is empty, the first audio stream (if any) is directly copied to the output file.</notice>
        self.audio = audio
        # The media container type. This parameter is required when Type is set to Concat or Compose. Valid values:
        # - Audio and video containers: mp4, mkv, mov, asf, avi, mxf, ts, and flv
        # 
        # >Notice: You must specify both Container and URI.</notice>
        self.container = container
        # The maximum duration of the edited video. Unit: seconds.
        self.max_duration = max_duration
        # The media segmentation settings. By default, segmentation is not performed.
        self.segment = segment
        # The playback speed multiplier for the media. Valid values: [0.5, 1.0]. Default value: 1.0.
        # 
        # > The ratio of the default playback speed of the transcoded media file to that of the source media file. This is not speed-adjusted transcoding.
        self.speed = speed
        # The target duration of the video. Unit: seconds.
        self.target_duration = target_duration
        # The URI of the output file.
        # 
        # This parameter is required.
        self.uri = uri
        # The video processing parameter settings. >Notice: If Video is empty, the first video stream (if any) is directly copied to the output file.</notice>
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.segment:
            self.segment.validate()
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

        if self.max_duration is not None:
            result['MaxDuration'] = self.max_duration

        if self.segment is not None:
            result['Segment'] = self.segment.to_map()

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.target_duration is not None:
            result['TargetDuration'] = self.target_duration

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

        if m.get('MaxDuration') is not None:
            self.max_duration = m.get('MaxDuration')

        if m.get('Segment') is not None:
            temp_model = main_models.CreateHighlightTaskRequestOutputSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('TargetDuration') is not None:
            self.target_duration = m.get('TargetDuration')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        if m.get('Video') is not None:
            temp_model = main_models.TargetVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class CreateHighlightTaskRequestOutputSegment(DaraModel):
    def __init__(
        self,
        duration: float = None,
        format: str = None,
        start_number: int = None,
    ):
        # The length of each segment. Unit: seconds.
        self.duration = duration
        # The media segmentation format. Valid values:
        # - hls
        # - dash
        self.format = format
        # The start number. This parameter is supported only for hls. Default value: 0.
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

class CreateHighlightTaskRequestHighlight(DaraModel):
    def __init__(
        self,
        content: str = None,
    ):
        # The highlight content. Valid values:
        # - Pet
        # - Person
        # - Sports
        # - Meeting
        # 
        # The value cannot exceed 100 characters in length.
        # 
        # This parameter is required.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        return self

class CreateHighlightTaskRequestEdit(DaraModel):
    def __init__(
        self,
        background_music_mode: str = None,
        background_musics: List[main_models.CreateHighlightTaskRequestEditBackgroundMusics] = None,
        mode: str = None,
        transition_mode: str = None,
        transitions: List[main_models.CreateHighlightTaskRequestEditTransitions] = None,
        vfx_effect_mode: str = None,
        vfx_effects: List[main_models.CreateHighlightTaskRequestEditVfxEffects] = None,
    ):
        # The background music mode. Valid values:
        # - Random: custom background music, randomly selected based on weights
        # - Sequential: custom background music, applied in sequence
        # - Closed: no background music
        # Default value: Closed.
        self.background_music_mode = background_music_mode
        # The background music. This parameter is valid only when BackgroundMusicMode is set to Random or Sequential. **The current maximum number of background music tracks is 1.**
        self.background_musics = background_musics
        # The editing mode. Valid values:
        # - Sequential: sequential mode
        # 
        # This parameter is required.
        self.mode = mode
        # The transition mode. Valid values:
        # - Auto: automatic transition
        # - Random: custom transition, randomly selected based on weights
        # - Sequential: custom transition, applied in sequence
        # - Closed: no transition
        # Default value: Closed.
        self.transition_mode = transition_mode
        # The transition effects. This parameter is valid only when TransitionMode is set to Random or Sequential. You can specify up to 10 transition effects.
        self.transitions = transitions
        # The visual effect mode. Valid values:
        # - Auto: automatic visual effect
        # - Random: custom visual effect, randomly selected based on weights
        # - Sequential: custom visual effect, applied in sequence
        # - Closed: no visual effect
        # Default value: Closed.
        self.vfx_effect_mode = vfx_effect_mode
        # The visual effects. This parameter is valid only when VfxEffectMode is set to Random or Sequential. You can specify up to 10 visual effects.
        self.vfx_effects = vfx_effects

    def validate(self):
        if self.background_musics:
            for v1 in self.background_musics:
                 if v1:
                    v1.validate()
        if self.transitions:
            for v1 in self.transitions:
                 if v1:
                    v1.validate()
        if self.vfx_effects:
            for v1 in self.vfx_effects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_music_mode is not None:
            result['BackgroundMusicMode'] = self.background_music_mode

        result['BackgroundMusics'] = []
        if self.background_musics is not None:
            for k1 in self.background_musics:
                result['BackgroundMusics'].append(k1.to_map() if k1 else None)

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.transition_mode is not None:
            result['TransitionMode'] = self.transition_mode

        result['Transitions'] = []
        if self.transitions is not None:
            for k1 in self.transitions:
                result['Transitions'].append(k1.to_map() if k1 else None)

        if self.vfx_effect_mode is not None:
            result['VfxEffectMode'] = self.vfx_effect_mode

        result['VfxEffects'] = []
        if self.vfx_effects is not None:
            for k1 in self.vfx_effects:
                result['VfxEffects'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundMusicMode') is not None:
            self.background_music_mode = m.get('BackgroundMusicMode')

        self.background_musics = []
        if m.get('BackgroundMusics') is not None:
            for k1 in m.get('BackgroundMusics'):
                temp_model = main_models.CreateHighlightTaskRequestEditBackgroundMusics()
                self.background_musics.append(temp_model.from_map(k1))

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('TransitionMode') is not None:
            self.transition_mode = m.get('TransitionMode')

        self.transitions = []
        if m.get('Transitions') is not None:
            for k1 in m.get('Transitions'):
                temp_model = main_models.CreateHighlightTaskRequestEditTransitions()
                self.transitions.append(temp_model.from_map(k1))

        if m.get('VfxEffectMode') is not None:
            self.vfx_effect_mode = m.get('VfxEffectMode')

        self.vfx_effects = []
        if m.get('VfxEffects') is not None:
            for k1 in m.get('VfxEffects'):
                temp_model = main_models.CreateHighlightTaskRequestEditVfxEffects()
                self.vfx_effects.append(temp_model.from_map(k1))

        return self

class CreateHighlightTaskRequestEditVfxEffects(DaraModel):
    def __init__(
        self,
        vfx_effect: str = None,
        weight: int = None,
    ):
        # The visual effect. For more information, see [Visual effects](https://www.alibabacloud.com/help/en/imm/developer-reference/effects).
        # 
        # This parameter is required.
        self.vfx_effect = vfx_effect
        # The weight of the visual effect. Valid values: [1, 100]. Default value: 50. This parameter is valid only when VfxEffectMode is set to Random.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vfx_effect is not None:
            result['VfxEffect'] = self.vfx_effect

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VfxEffect') is not None:
            self.vfx_effect = m.get('VfxEffect')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class CreateHighlightTaskRequestEditTransitions(DaraModel):
    def __init__(
        self,
        duration: float = None,
        transition: str = None,
        weight: int = None,
    ):
        # The duration of the transition. Unit: seconds. If the transition duration is greater than the clip duration minus 1, the transition effect on the clip does not take effect. Valid values: [0, 5].
        self.duration = duration
        # The transition effect. For more information, see [Transition effects](https://www.alibabacloud.com/help/en/imm/developer-reference/transition-effect).
        # 
        # This parameter is required.
        self.transition = transition
        # The weight of the transition. Valid values: [1, 100]. Default value: 50. This parameter is valid only when TransitionMode is set to Random.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.transition is not None:
            result['Transition'] = self.transition

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Transition') is not None:
            self.transition = m.get('Transition')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class CreateHighlightTaskRequestEditBackgroundMusics(DaraModel):
    def __init__(
        self,
        uri: str = None,
        volume: float = None,
    ):
        # The URI of the background music, which is an OSS URI. Only audio files are supported.
        # 
        # This parameter is required.
        self.uri = uri
        # The volume of the background music. Valid values: [0, 10]. Default value: 0.2. A value of 1 indicates the original volume.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uri is not None:
            result['URI'] = self.uri

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

