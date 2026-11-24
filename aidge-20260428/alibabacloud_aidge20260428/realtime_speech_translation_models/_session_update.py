# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import realtime_speech_translation_models as main_models
from darabonba.model import DaraModel

class SessionUpdate(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session: main_models.SessionUpdateSession = None,
    ):
        # This parameter is required.
        self.type = type
        # 可省略；提供时必须为非空、非纯空白字符串。
        self.event_id = event_id
        # 仅填写当前模式适用字段。双向必须提供 session 对象，仅允许输入前更新；单向按 Qwen 3.5 原生契约可省略 session。
        # 双向不支持 glossary、声音复刻及单向平铺配置，模式、语言对、条件必填及能力校验由后端执行。网关不补默认值。
        # 单向手动提交、关闭转写：{"modalities":["text"],"sample_rate":16000,"input_audio_format":"pcm","input_audio_transcription":{"enabled":false},"translation":{"language":"en"},"turn_detection":null}
        # 单向 VAD、译音与转写：{"modalities":["text","audio"],"sample_rate":16000,"input_audio_format":"pcm","input_audio_transcription":{"enabled":true,"language":"auto"},"translation":{"language":"en"},"turn_detection":{"type":"server_vad","threshold":0.2,"silence_duration_ms":1000},"output_audio_format":"pcm","voice":"Tina","enable_voice_clone":false}
        # 双向手动提交、仅译文：{"input_audio":{"format":"pcm_s16le","sample_rate":16000,"channels":1},"output":{"modalities":["text"]},"transcription":{"enabled":false},"turn_detection":{"type":"manual"}}
        # 双向 VAD、译文与译音：{"input_audio":{"format":"pcm_s16le","sample_rate":16000,"channels":1},"output":{"modalities":["text","audio"],"audio":{"format":"pcm_s16le","sample_rate":24000,"channels":1,"voice":{"mode":"preset","id":"Tina"}}},"transcription":{"enabled":true},"turn_detection":{"type":"server_vad","threshold":0.2,"silence_duration_ms":1000}}
        # 单向扩展字段依据百炼 live-translator-client-events；新增原生字段须同步登记。显式 null 和热词动态键的映射保留行为仍需网关实测。
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

        if self.session is not None:
            result['session'] = self.session.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('session') is not None:
            temp_model = main_models.SessionUpdateSession()
            self.session = temp_model.from_map(m.get('session'))

        return self

class SessionUpdateSession(DaraModel):
    def __init__(
        self,
        mode: str = None,
        language_pair: List[str] = None,
        input_audio: main_models.SessionUpdateSessionInputAudio = None,
        output: main_models.SessionUpdateSessionOutput = None,
        transcription: main_models.SessionUpdateSessionTranscription = None,
        turn_detection: main_models.SessionUpdateSessionTurnDetection = None,
        modalities: List[str] = None,
        sample_rate: int = None,
        input_audio_format: str = None,
        input_audio_transcription: main_models.SessionUpdateSessionInputAudioTranscription = None,
        translation: main_models.SessionUpdateSessionTranslation = None,
        output_audio_format: str = None,
        voice: str = None,
        enable_voice_clone: bool = None,
        voice_clone_options: main_models.SessionUpdateSessionVoiceCloneOptions = None,
    ):
        # 仅双向使用；可省略，提供时必须为 bidirectional，不能切换模式。
        self.mode = mode
        # 仅双向使用；可省略，提供时必须与创建时内容及顺序一致。
        self.language_pair = language_pair
        # 仅双向使用；省略时后端使用 pcm_s16le、16000Hz、单声道，不接受 null。
        self.input_audio = input_audio
        # 仅双向使用；省略时后端输出 text 和 audio。
        self.output = output
        self.transcription = transcription
        # 单向 manual 必须显式传 null，VAD 使用 server_vad 对象。双向不接受 null，manual 使用对象；省略时后端为 server_vad。nullable 仅兼容单向，模式约束交后端校验。
        self.turn_detection = turn_detection
        # 仅单向使用；支持 text 或 text 与 audio，省略时模型默认 text 与 audio。双向使用 output.modalities。
        self.modalities = modalities
        # 仅单向使用；须与输入音频一致，支持8000或16000。
        self.sample_rate = sample_rate
        # 仅单向原生协议使用；现有冒烟客户端使用 pcm，opus 尚未在本次实测。双向仅支持 pcm_s16le。
        self.input_audio_format = input_audio_format
        # 仅单向使用，仅支持 enabled、language。对象省略或为空时默认开启、自动识别。enabled=false 时忽略 language，关闭原文转写；model 不再接受。默认值由后端补齐，网关不注入。
        self.input_audio_transcription = input_audio_transcription
        # 仅单向原生协议使用；双向目标语言来自创建时的语言对，不接受本字段。
        self.translation = translation
        # 仅单向译音使用，当前原生协议只支持 pcm。
        self.output_audio_format = output_audio_format
        # 未启用复刻时使用预设音色，模型缺省为 Tina。启用复刻且 frequency 为 once/always 时必须为 default；never 时须为已有复刻音色ID。双向使用 output.audio.voice.id。
        self.voice = voice
        # 仅单向原生协议使用，模型默认 false；开启时联动 voice 和 voice_clone_options，实际可用性由上游校验。本次未实测复刻，双向不支持。
        self.enable_voice_clone = enable_voice_clone
        # 仅 enable_voice_clone=true 时生效；双向不支持本字段。
        self.voice_clone_options = voice_clone_options

    def validate(self):
        if self.input_audio:
            self.input_audio.validate()
        if self.output:
            self.output.validate()
        if self.transcription:
            self.transcription.validate()
        if self.turn_detection:
            self.turn_detection.validate()
        if self.input_audio_transcription:
            self.input_audio_transcription.validate()
        if self.translation:
            self.translation.validate()
        if self.voice_clone_options:
            self.voice_clone_options.validate()

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

        if self.modalities is not None:
            result['modalities'] = self.modalities

        if self.sample_rate is not None:
            result['sample_rate'] = self.sample_rate

        if self.input_audio_format is not None:
            result['input_audio_format'] = self.input_audio_format

        if self.input_audio_transcription is not None:
            result['input_audio_transcription'] = self.input_audio_transcription.to_map()

        if self.translation is not None:
            result['translation'] = self.translation.to_map()

        if self.output_audio_format is not None:
            result['output_audio_format'] = self.output_audio_format

        if self.voice is not None:
            result['voice'] = self.voice

        if self.enable_voice_clone is not None:
            result['enable_voice_clone'] = self.enable_voice_clone

        if self.voice_clone_options is not None:
            result['voice_clone_options'] = self.voice_clone_options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('language_pair') is not None:
            self.language_pair = m.get('language_pair')

        if m.get('input_audio') is not None:
            temp_model = main_models.SessionUpdateSessionInputAudio()
            self.input_audio = temp_model.from_map(m.get('input_audio'))

        if m.get('output') is not None:
            temp_model = main_models.SessionUpdateSessionOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('transcription') is not None:
            temp_model = main_models.SessionUpdateSessionTranscription()
            self.transcription = temp_model.from_map(m.get('transcription'))

        if m.get('turn_detection') is not None:
            temp_model = main_models.SessionUpdateSessionTurnDetection()
            self.turn_detection = temp_model.from_map(m.get('turn_detection'))

        if m.get('modalities') is not None:
            self.modalities = m.get('modalities')

        if m.get('sample_rate') is not None:
            self.sample_rate = m.get('sample_rate')

        if m.get('input_audio_format') is not None:
            self.input_audio_format = m.get('input_audio_format')

        if m.get('input_audio_transcription') is not None:
            temp_model = main_models.SessionUpdateSessionInputAudioTranscription()
            self.input_audio_transcription = temp_model.from_map(m.get('input_audio_transcription'))

        if m.get('translation') is not None:
            temp_model = main_models.SessionUpdateSessionTranslation()
            self.translation = temp_model.from_map(m.get('translation'))

        if m.get('output_audio_format') is not None:
            self.output_audio_format = m.get('output_audio_format')

        if m.get('voice') is not None:
            self.voice = m.get('voice')

        if m.get('enable_voice_clone') is not None:
            self.enable_voice_clone = m.get('enable_voice_clone')

        if m.get('voice_clone_options') is not None:
            temp_model = main_models.SessionUpdateSessionVoiceCloneOptions()
            self.voice_clone_options = temp_model.from_map(m.get('voice_clone_options'))

        return self

class SessionUpdateSessionVoiceCloneOptions(DaraModel):
    def __init__(
        self,
        frequency: str = None,
    ):
        # never 使用已有复刻音色；once 会话开始时复刻一次；always 每次输出前复刻。once/always 必须设置 voice=default。
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

class SessionUpdateSessionTranslation(DaraModel):
    def __init__(
        self,
        language: str = None,
        same_language_skip_options: main_models.SessionUpdateSessionTranslationSameLanguageSkipOptions = None,
        corpus: main_models.SessionUpdateSessionTranslationCorpus = None,
    ):
        # 例如 en，缺省时模型默认 en；具体支持范围由模型校验。
        self.language = language
        # 仅单向 Qwen 3.5 使用，目标语种为 zh 或 en 时生效；源语种等于目标语种时按设置跳过输出。
        self.same_language_skip_options = same_language_skip_options
        # 仅单向原生协议使用；与双向不支持的 glossary 字段不同。
        self.corpus = corpus

    def validate(self):
        if self.same_language_skip_options:
            self.same_language_skip_options.validate()
        if self.corpus:
            self.corpus.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['language'] = self.language

        if self.same_language_skip_options is not None:
            result['same_language_skip_options'] = self.same_language_skip_options.to_map()

        if self.corpus is not None:
            result['corpus'] = self.corpus.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('same_language_skip_options') is not None:
            temp_model = main_models.SessionUpdateSessionTranslationSameLanguageSkipOptions()
            self.same_language_skip_options = temp_model.from_map(m.get('same_language_skip_options'))

        if m.get('corpus') is not None:
            temp_model = main_models.SessionUpdateSessionTranslationCorpus()
            self.corpus = temp_model.from_map(m.get('corpus'))

        return self

class SessionUpdateSessionTranslationCorpus(DaraModel):
    def __init__(
        self,
        phrases: Dict[str, str] = None,
    ):
        # 动态 key 为源语言词汇，value 为目标语言译词；不固定热词名称，动态键映射保留需网关实测。
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

class SessionUpdateSessionTranslationSameLanguageSkipOptions(DaraModel):
    def __init__(
        self,
        skip_text: bool = None,
        skip_audio: bool = None,
    ):
        self.skip_text = skip_text
        self.skip_audio = skip_audio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skip_text is not None:
            result['skip_text'] = self.skip_text

        if self.skip_audio is not None:
            result['skip_audio'] = self.skip_audio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skip_text') is not None:
            self.skip_text = m.get('skip_text')

        if m.get('skip_audio') is not None:
            self.skip_audio = m.get('skip_audio')

        return self

class SessionUpdateSessionInputAudioTranscription(DaraModel):
    def __init__(
        self,
        language: str = None,
        enabled: bool = None,
    ):
        # 默认 auto，省略或 auto 表示自动识别。开启时保留指定的受支持语种；关闭时忽略本字段。此字段不是翻译目标语言。
        self.language = language
        # 默认 true。false 时忽略 language，不影响译文和译音。
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['language'] = self.language

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class SessionUpdateSessionTurnDetection(DaraModel):
    def __init__(
        self,
        type: str = None,
        threshold: float = None,
        silence_duration_ms: int = None,
    ):
        # manual 对象仅用于双向；单向手动模式使用整个 turn_detection 为 null。
        self.type = type
        # 范围 -1 到 1，后端缺省0.2。
        self.threshold = threshold
        # 范围200到6000，后端缺省1000。
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

class SessionUpdateSessionTranscription(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # 省略时后端为 true；关闭输出不会关闭内部语种识别。
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

class SessionUpdateSessionOutput(DaraModel):
    def __init__(
        self,
        modalities: List[str] = None,
        audio: main_models.SessionUpdateSessionOutputAudio = None,
    ):
        # 必须包含 text，可加 audio；不可重复，不能只有 audio。允许顺序反转，后端规范化为 text、audio。
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
            temp_model = main_models.SessionUpdateSessionOutputAudio()
            self.audio = temp_model.from_map(m.get('audio'))

        return self

class SessionUpdateSessionOutputAudio(DaraModel):
    def __init__(
        self,
        format: str = None,
        sample_rate: int = None,
        channels: int = None,
        voice: main_models.SessionUpdateSessionOutputAudioVoice = None,
    ):
        self.format = format
        self.sample_rate = sample_rate
        self.channels = channels
        # 仅支持 preset；不支持 clone_frequency。id 省略或为 default 时后端使用 Tina。
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
            temp_model = main_models.SessionUpdateSessionOutputAudioVoice()
            self.voice = temp_model.from_map(m.get('voice'))

        return self

class SessionUpdateSessionOutputAudioVoice(DaraModel):
    def __init__(
        self,
        mode: str = None,
        id: str = None,
    ):
        self.mode = mode
        # 非空且不能含控制字符，最长128字符；具体音色支持范围由模型校验。
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

class SessionUpdateSessionInputAudio(DaraModel):
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

