# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetNextResultToVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetNextResultToVerifyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetNextResultToVerifyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetNextResultToVerifyResponseBodyData(DaraModel):
    def __init__(
        self,
        audio_scheme: str = None,
        audio_url: str = None,
        dialogues: main_models.GetNextResultToVerifyResponseBodyDataDialogues = None,
        duration: int = None,
        file_id: str = None,
        file_name: str = None,
        incorrect_words: int = None,
        index: int = None,
        precision: float = None,
        status: int = None,
        total_count: int = None,
        update_time: str = None,
        verified: bool = None,
        verified_count: int = None,
    ):
        self.audio_scheme = audio_scheme
        self.audio_url = audio_url
        self.dialogues = dialogues
        self.duration = duration
        self.file_id = file_id
        self.file_name = file_name
        self.incorrect_words = incorrect_words
        self.index = index
        self.precision = precision
        self.status = status
        self.total_count = total_count
        self.update_time = update_time
        self.verified = verified
        self.verified_count = verified_count

    def validate(self):
        if self.dialogues:
            self.dialogues.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_scheme is not None:
            result['AudioScheme'] = self.audio_scheme

        if self.audio_url is not None:
            result['AudioURL'] = self.audio_url

        if self.dialogues is not None:
            result['Dialogues'] = self.dialogues.to_map()

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words

        if self.index is not None:
            result['Index'] = self.index

        if self.precision is not None:
            result['Precision'] = self.precision

        if self.status is not None:
            result['Status'] = self.status

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.verified is not None:
            result['Verified'] = self.verified

        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioScheme') is not None:
            self.audio_scheme = m.get('AudioScheme')

        if m.get('AudioURL') is not None:
            self.audio_url = m.get('AudioURL')

        if m.get('Dialogues') is not None:
            temp_model = main_models.GetNextResultToVerifyResponseBodyDataDialogues()
            self.dialogues = temp_model.from_map(m.get('Dialogues'))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Precision') is not None:
            self.precision = m.get('Precision')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Verified') is not None:
            self.verified = m.get('Verified')

        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')

        return self

class GetNextResultToVerifyResponseBodyDataDialogues(DaraModel):
    def __init__(
        self,
        dialogue: List[main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogue] = None,
    ):
        self.dialogue = dialogue

    def validate(self):
        if self.dialogue:
            for v1 in self.dialogue:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dialogue'] = []
        if self.dialogue is not None:
            for k1 in self.dialogue:
                result['Dialogue'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue = []
        if m.get('Dialogue') is not None:
            for k1 in m.get('Dialogue'):
                temp_model = main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogue()
                self.dialogue.append(temp_model.from_map(k1))

        return self

class GetNextResultToVerifyResponseBodyDataDialoguesDialogue(DaraModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        deltas: main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas = None,
        emotion_value: int = None,
        end: int = None,
        hour_min_sec: str = None,
        identity: str = None,
        incorrect_words: int = None,
        role: str = None,
        silence_duration: int = None,
        source_role: str = None,
        source_words: str = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.deltas = deltas
        self.emotion_value = emotion_value
        self.end = end
        self.hour_min_sec = hour_min_sec
        self.identity = identity
        self.incorrect_words = incorrect_words
        self.role = role
        self.silence_duration = silence_duration
        self.source_role = source_role
        self.source_words = source_words
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        if self.deltas:
            self.deltas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.deltas is not None:
            result['Deltas'] = self.deltas.to_map()

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end is not None:
            result['End'] = self.end

        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words

        if self.role is not None:
            result['Role'] = self.role

        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration

        if self.source_role is not None:
            result['SourceRole'] = self.source_role

        if self.source_words is not None:
            result['SourceWords'] = self.source_words

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('Deltas') is not None:
            temp_model = main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas()
            self.deltas = temp_model.from_map(m.get('Deltas'))

        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')

        if m.get('SourceRole') is not None:
            self.source_role = m.get('SourceRole')

        if m.get('SourceWords') is not None:
            self.source_words = m.get('SourceWords')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas(DaraModel):
    def __init__(
        self,
        delta: List[main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDelta] = None,
    ):
        self.delta = delta

    def validate(self):
        if self.delta:
            for v1 in self.delta:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Delta'] = []
        if self.delta is not None:
            for k1 in self.delta:
                result['Delta'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delta = []
        if m.get('Delta') is not None:
            for k1 in m.get('Delta'):
                temp_model = main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDelta()
                self.delta.append(temp_model.from_map(k1))

        return self

class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDelta(DaraModel):
    def __init__(
        self,
        source: main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource = None,
        target: main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget = None,
        type: str = None,
    ):
        self.source = source
        self.target = target
        self.type = type

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['Source'] = self.source.to_map()

        if self.target is not None:
            result['Target'] = self.target.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            temp_model = main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource()
            self.source = temp_model.from_map(m.get('Source'))

        if m.get('Target') is not None:
            temp_model = main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget(DaraModel):
    def __init__(
        self,
        line: main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTargetLine = None,
        position: int = None,
    ):
        self.line = line
        self.position = position

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line.to_map()

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTargetLine()
            self.line = temp_model.from_map(m.get('Line'))

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTargetLine(DaraModel):
    def __init__(
        self,
        line: List[str] = None,
    ):
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')

        return self

class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource(DaraModel):
    def __init__(
        self,
        line: main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine = None,
        position: int = None,
    ):
        self.line = line
        self.position = position

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line.to_map()

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = main_models.GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine()
            self.line = temp_model.from_map(m.get('Line'))

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine(DaraModel):
    def __init__(
        self,
        line: List[str] = None,
    ):
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')

        return self

