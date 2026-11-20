# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetSecretAsrDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSecretAsrDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The ASR details.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSecretAsrDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSecretAsrDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_duration: int = None,
        business_id: str = None,
        business_key: str = None,
        code: str = None,
        msg: str = None,
        request_id: str = None,
        sentences: List[main_models.GetSecretAsrDetailResponseBodyDataSentences] = None,
        type: str = None,
    ):
        # The total duration of the audio file that was recognized. Unit: milliseconds.
        self.biz_duration = biz_duration
        # The ID of the business process.
        self.business_id = business_id
        # The business keyword.
        self.business_key = business_key
        # The status code. The status code 21050000 indicates that the request was successful.
        self.code = code
        # The description.
        self.msg = msg
        # The request ID.
        self.request_id = request_id
        # The ASR result.
        self.sentences = sentences
        # The type.
        self.type = type

    def validate(self):
        if self.sentences:
            for v1 in self.sentences:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_duration is not None:
            result['BizDuration'] = self.biz_duration

        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.business_key is not None:
            result['BusinessKey'] = self.business_key

        if self.code is not None:
            result['Code'] = self.code

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Sentences'] = []
        if self.sentences is not None:
            for k1 in self.sentences:
                result['Sentences'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDuration') is not None:
            self.biz_duration = m.get('BizDuration')

        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('BusinessKey') is not None:
            self.business_key = m.get('BusinessKey')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sentences = []
        if m.get('Sentences') is not None:
            for k1 in m.get('Sentences'):
                temp_model = main_models.GetSecretAsrDetailResponseBodyDataSentences()
                self.sentences.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetSecretAsrDetailResponseBodyDataSentences(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        channel_id: int = None,
        emotion_value: str = None,
        end_time: int = None,
        silence_duration: int = None,
        speech_rate: int = None,
        text: str = None,
    ):
        # The start time offset of the sentence. Unit: milliseconds.
        self.begin_time = begin_time
        # The ID of the audio track to which the sentence belongs.
        self.channel_id = channel_id
        # The emotion value. Value range: 1 to 10. The higher the value, the stronger the emotion.
        self.emotion_value = emotion_value
        # The end time offset of the sentence. Unit: milliseconds.
        self.end_time = end_time
        # The silence duration between the current sentence and the previous sentence. Unit: seconds.
        self.silence_duration = silence_duration
        # The average speech rate of the sentence. Unit: number of words per minute.
        self.speech_rate = speech_rate
        # The recognition result of the sentence.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

