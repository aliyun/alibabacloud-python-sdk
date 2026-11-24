# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import realtime_speech_translation_models as main_models
from darabonba.model import DaraModel

class SessionUpdated(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session_id: str = None,
        caused_by: str = None,
        warnings: List[str] = None,
        session: main_models.SessionUpdatedSession = None,
    ):
        self.type = type
        self.event_id = event_id
        self.session_id = session_id
        self.caused_by = caused_by
        self.warnings = warnings
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

        if self.warnings is not None:
            result['warnings'] = self.warnings

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

        if m.get('warnings') is not None:
            self.warnings = m.get('warnings')

        if m.get('session') is not None:
            temp_model = main_models.SessionUpdatedSession()
            self.session = temp_model.from_map(m.get('session'))

        return self

class SessionUpdatedSession(DaraModel):
    def __init__(
        self,
        mode: str = None,
        language_pair: List[str] = None,
        input_audio: main_models.SessionUpdatedSessionInputAudio = None,
        output: main_models.SessionUpdatedSessionOutput = None,
        transcription: main_models.SessionUpdatedSessionTranscription = None,
        turn_detection: main_models.SessionUpdatedSessionTurnDetection = None,
        id: str = None,
        object: str = None,
        modalities: List[str] = None,
        voice: str = None,
        input_audio_format: str = None,
        sample_rate: int = None,
        output_audio_format: str = None,
        translation: main_models.SessionUpdatedSessionTranslation = None,
        enable_voice_clone: bool = None,
        voice_clone_options: main_models.SessionUpdatedSessionVoiceCloneOptions = None,
        input_audio_transcription: main_models.SessionUpdatedSessionInputAudioTranscription = None,
    ):
        self.mode = mode
        self.language_pair = language_pair
        self.input_audio = input_audio
        self.output = output
        self.transcription = transcription
        self.turn_detection = turn_detection
        self.id = id
        self.object = object
        self.modalities = modalities
        self.voice = voice
        self.input_audio_format = input_audio_format
        self.sample_rate = sample_rate
        self.output_audio_format = output_audio_format
        self.translation = translation
        self.enable_voice_clone = enable_voice_clone
        self.voice_clone_options = voice_clone_options
        # 单向回执固定包含 enabled、language；双向使用 transcription 字段。内部转写 model 不对客回显。
        self.input_audio_transcription = input_audio_transcription

    def validate(self):
        if self.input_audio:
            self.input_audio.validate()
        if self.output:
            self.output.validate()
        if self.transcription:
            self.transcription.validate()
        if self.turn_detection:
            self.turn_detection.validate()
        if self.translation:
            self.translation.validate()
        if self.voice_clone_options:
            self.voice_clone_options.validate()
        if self.input_audio_transcription:
            self.input_audio_transcription.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['mode'] = self.mode

        if self.language_pair is not None:
            result['language_pair'] = self.language_pair

        if self.input_audio is not None:
            result['input_audio'] = self.input_audio.to_map()

        if self.output is not None:
            result['output'] = self.output.to_map()

        if self.transcription is not None:
            result['transcription'] = self.transcription.to_map()

        if self.turn_detection is not None:
            result['turn_detection'] = self.turn_detection.to_map()

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

        if self.translation is not None:
            result['translation'] = self.translation.to_map()

        if self.enable_voice_clone is not None:
            result['enable_voice_clone'] = self.enable_voice_clone

        if self.voice_clone_options is not None:
            result['voice_clone_options'] = self.voice_clone_options.to_map()

        if self.input_audio_transcription is not None:
            result['input_audio_transcription'] = self.input_audio_transcription.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('language_pair') is not None:
            self.language_pair = m.get('language_pair')

        if m.get('input_audio') is not None:
            temp_model = main_models.SessionUpdatedSessionInputAudio()
            self.input_audio = temp_model.from_map(m.get('input_audio'))

        if m.get('output') is not None:
            temp_model = main_models.SessionUpdatedSessionOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('transcription') is not None:
            temp_model = main_models.SessionUpdatedSessionTranscription()
            self.transcription = temp_model.from_map(m.get('transcription'))

        if m.get('turn_detection') is not None:
            temp_model = main_models.SessionUpdatedSessionTurnDetection()
            self.turn_detection = temp_model.from_map(m.get('turn_detection'))

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

        if m.get('translation') is not None:
            temp_model = main_models.SessionUpdatedSessionTranslation()
            self.translation = temp_model.from_map(m.get('translation'))

        if m.get('enable_voice_clone') is not None:
            self.enable_voice_clone = m.get('enable_voice_clone')

        if m.get('voice_clone_options') is not None:
            temp_model = main_models.SessionUpdatedSessionVoiceCloneOptions()
            self.voice_clone_options = temp_model.from_map(m.get('voice_clone_options'))

        if m.get('input_audio_transcription') is not None:
            temp_model = main_models.SessionUpdatedSessionInputAudioTranscription()
            self.input_audio_transcription = temp_model.from_map(m.get('input_audio_transcription'))

        return self

class SessionUpdatedSessionInputAudioTranscription(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        language: str = None,
    ):
        # This parameter is required.
        self.enabled = enabled
        # 开启时回显指定语种，自动识别回显 auto；关闭时统一回显 auto。
        # 
        # This parameter is required.
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.language is not None:
            result['language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('language') is not None:
            self.language = m.get('language')

        return self

class SessionUpdatedSessionVoiceCloneOptions(DaraModel):
    def __init__(
        self,
        frequency: str = None,
    ):
        self.frequency = frequency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frequency is not None:
            result['frequency'] = self.frequency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('frequency') is not None:
            self.frequency = m.get('frequency')

        return self

class SessionUpdatedSessionTranslation(DaraModel):
    def __init__(
        self,
        language: str = None,
        corpus: main_models.SessionUpdatedSessionTranslationCorpus = None,
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
            temp_model = main_models.SessionUpdatedSessionTranslationCorpus()
            self.corpus = temp_model.from_map(m.get('corpus'))

        return self

class SessionUpdatedSessionTranslationCorpus(DaraModel):
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

class SessionUpdatedSessionTurnDetection(DaraModel):
    def __init__(
        self,
        type: str = None,
        threshold: float = None,
        silence_duration_ms: int = None,
        prefix_padding_ms: int = None,
        create_response: bool = None,
        interrupt_response: bool = None,
    ):
        self.type = type
        self.threshold = threshold
        self.silence_duration_ms = silence_duration_ms
        self.prefix_padding_ms = prefix_padding_ms
        self.create_response = create_response
        self.interrupt_response = interrupt_response

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

        if self.prefix_padding_ms is not None:
            result['prefix_padding_ms'] = self.prefix_padding_ms

        if self.create_response is not None:
            result['create_response'] = self.create_response

        if self.interrupt_response is not None:
            result['interrupt_response'] = self.interrupt_response

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('silence_duration_ms') is not None:
            self.silence_duration_ms = m.get('silence_duration_ms')

        if m.get('prefix_padding_ms') is not None:
            self.prefix_padding_ms = m.get('prefix_padding_ms')

        if m.get('create_response') is not None:
            self.create_response = m.get('create_response')

        if m.get('interrupt_response') is not None:
            self.interrupt_response = m.get('interrupt_response')

        return self

class SessionUpdatedSessionTranscription(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class SessionUpdatedSessionOutput(DaraModel):
    def __init__(
        self,
        modalities: List[str] = None,
        audio: main_models.SessionUpdatedSessionOutputAudio = None,
    ):
        self.modalities = modalities
        self.audio = audio

    def validate(self):
        if self.audio:
            self.audio.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modalities is not None:
            result['modalities'] = self.modalities

        if self.audio is not None:
            result['audio'] = self.audio.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modalities') is not None:
            self.modalities = m.get('modalities')

        if m.get('audio') is not None:
            temp_model = main_models.SessionUpdatedSessionOutputAudio()
            self.audio = temp_model.from_map(m.get('audio'))

        return self

class SessionUpdatedSessionOutputAudio(DaraModel):
    def __init__(
        self,
        format: str = None,
        sample_rate: int = None,
        channels: int = None,
        voice: main_models.SessionUpdatedSessionOutputAudioVoice = None,
    ):
        self.format = format
        self.sample_rate = sample_rate
        self.channels = channels
        self.voice = voice

    def validate(self):
        if self.voice:
            self.voice.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['format'] = self.format

        if self.sample_rate is not None:
            result['sample_rate'] = self.sample_rate

        if self.channels is not None:
            result['channels'] = self.channels

        if self.voice is not None:
            result['voice'] = self.voice.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('sample_rate') is not None:
            self.sample_rate = m.get('sample_rate')

        if m.get('channels') is not None:
            self.channels = m.get('channels')

        if m.get('voice') is not None:
            temp_model = main_models.SessionUpdatedSessionOutputAudioVoice()
            self.voice = temp_model.from_map(m.get('voice'))

        return self

class SessionUpdatedSessionOutputAudioVoice(DaraModel):
    def __init__(
        self,
        mode: str = None,
        id: str = None,
    ):
        self.mode = mode
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['mode'] = self.mode

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

class SessionUpdatedSessionInputAudio(DaraModel):
    def __init__(
        self,
        format: str = None,
        sample_rate: int = None,
        channels: int = None,
    ):
        self.format = format
        self.sample_rate = sample_rate
        self.channels = channels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['format'] = self.format

        if self.sample_rate is not None:
            result['sample_rate'] = self.sample_rate

        if self.channels is not None:
            result['channels'] = self.channels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('sample_rate') is not None:
            self.sample_rate = m.get('sample_rate')

        if m.get('channels') is not None:
            self.channels = m.get('channels')

        return self

