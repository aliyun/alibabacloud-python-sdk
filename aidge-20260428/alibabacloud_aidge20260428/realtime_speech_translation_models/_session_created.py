# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import realtime_speech_translation_models as main_models
from darabonba.model import DaraModel

class SessionCreated(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session_id: str = None,
        caused_by: str = None,
        created_at: int = None,
        expires_at: int = None,
        session: main_models.SessionCreatedSession = None,
    ):
        self.type = type
        self.event_id = event_id
        self.session_id = session_id
        self.caused_by = caused_by
        self.created_at = created_at
        self.expires_at = expires_at
        self.session = session

    def validate(self):
        if self.session:
            self.session.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.event_id is not None:
            result['event_id'] = self.event_id

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.caused_by is not None:
            result['caused_by'] = self.caused_by

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.expires_at is not None:
            result['expires_at'] = self.expires_at

        if self.session is not None:
            result['session'] = self.session.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('caused_by') is not None:
            self.caused_by = m.get('caused_by')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('expires_at') is not None:
            self.expires_at = m.get('expires_at')

        if m.get('session') is not None:
            temp_model = main_models.SessionCreatedSession()
            self.session = temp_model.from_map(m.get('session'))

        return self

class SessionCreatedSession(DaraModel):
    def __init__(
        self,
        id: str = None,
        object: str = None,
        modalities: List[str] = None,
        voice: str = None,
        input_audio_format: str = None,
        sample_rate: int = None,
        output_audio_format: str = None,
        turn_detection: main_models.SessionCreatedSessionTurnDetection = None,
        translation: main_models.SessionCreatedSessionTranslation = None,
    ):
        self.id = id
        self.object = object
        self.modalities = modalities
        self.voice = voice
        self.input_audio_format = input_audio_format
        self.sample_rate = sample_rate
        self.output_audio_format = output_audio_format
        self.turn_detection = turn_detection
        self.translation = translation

    def validate(self):
        if self.turn_detection:
            self.turn_detection.validate()
        if self.translation:
            self.translation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.object is not None:
            result['object'] = self.object

        if self.modalities is not None:
            result['modalities'] = self.modalities

        if self.voice is not None:
            result['voice'] = self.voice

        if self.input_audio_format is not None:
            result['input_audio_format'] = self.input_audio_format

        if self.sample_rate is not None:
            result['sample_rate'] = self.sample_rate

        if self.output_audio_format is not None:
            result['output_audio_format'] = self.output_audio_format

        if self.turn_detection is not None:
            result['turn_detection'] = self.turn_detection.to_map()

        if self.translation is not None:
            result['translation'] = self.translation.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('object') is not None:
            self.object = m.get('object')

        if m.get('modalities') is not None:
            self.modalities = m.get('modalities')

        if m.get('voice') is not None:
            self.voice = m.get('voice')

        if m.get('input_audio_format') is not None:
            self.input_audio_format = m.get('input_audio_format')

        if m.get('sample_rate') is not None:
            self.sample_rate = m.get('sample_rate')

        if m.get('output_audio_format') is not None:
            self.output_audio_format = m.get('output_audio_format')

        if m.get('turn_detection') is not None:
            temp_model = main_models.SessionCreatedSessionTurnDetection()
            self.turn_detection = temp_model.from_map(m.get('turn_detection'))

        if m.get('translation') is not None:
            temp_model = main_models.SessionCreatedSessionTranslation()
            self.translation = temp_model.from_map(m.get('translation'))

        return self

class SessionCreatedSessionTranslation(DaraModel):
    def __init__(
        self,
        language: str = None,
        corpus: main_models.SessionCreatedSessionTranslationCorpus = None,
    ):
        self.language = language
        self.corpus = corpus

    def validate(self):
        if self.corpus:
            self.corpus.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['language'] = self.language

        if self.corpus is not None:
            result['corpus'] = self.corpus.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('corpus') is not None:
            temp_model = main_models.SessionCreatedSessionTranslationCorpus()
            self.corpus = temp_model.from_map(m.get('corpus'))

        return self

class SessionCreatedSessionTranslationCorpus(DaraModel):
    def __init__(
        self,
        phrases: Dict[str, str] = None,
    ):
        self.phrases = phrases

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phrases is not None:
            result['phrases'] = self.phrases

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phrases') is not None:
            self.phrases = m.get('phrases')

        return self

class SessionCreatedSessionTurnDetection(DaraModel):
    def __init__(
        self,
        type: str = None,
        threshold: float = None,
        silence_duration_ms: int = None,
    ):
        self.type = type
        self.threshold = threshold
        self.silence_duration_ms = silence_duration_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.threshold is not None:
            result['threshold'] = self.threshold

        if self.silence_duration_ms is not None:
            result['silence_duration_ms'] = self.silence_duration_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('silence_duration_ms') is not None:
            self.silence_duration_ms = m.get('silence_duration_ms')

        return self

