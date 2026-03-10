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
        self.credential_config = credential_config
        self.edit = edit
        self.highlight = highlight
        self.mode = mode
        self.notification = notification
        # This parameter is required.
        self.output = output
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.sources = sources
        self.tags = tags
        # This parameter is required.
        self.type = type
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
        self.duration = duration
        self.start_time = start_time
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
        uri: str = None,
        video: main_models.TargetVideo = None,
    ):
        self.audio = audio
        self.container = container
        self.max_duration = max_duration
        self.segment = segment
        self.speed = speed
        # This parameter is required.
        self.uri = uri
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
        self.duration = duration
        self.format = format
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
        self.background_music_mode = background_music_mode
        self.background_musics = background_musics
        # This parameter is required.
        self.mode = mode
        self.transition_mode = transition_mode
        self.transitions = transitions
        self.vfx_effect_mode = vfx_effect_mode
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
        # This parameter is required.
        self.vfx_effect = vfx_effect
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
        self.duration = duration
        # This parameter is required.
        self.transition = transition
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
        # This parameter is required.
        self.uri = uri
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

