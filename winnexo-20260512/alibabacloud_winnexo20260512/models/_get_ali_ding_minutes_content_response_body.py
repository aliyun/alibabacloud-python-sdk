# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetAliDingMinutesContentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        minutes_id: str = None,
        request_id: str = None,
        summary: str = None,
        title: str = None,
        todo_content: str = None,
        transcription: List[main_models.GetAliDingMinutesContentResponseBodyTranscription] = None,
    ):
        # The status code.
        self.code = code
        # The description of the status code.
        self.message = message
        # The DingTalk minutes ID.
        self.minutes_id = minutes_id
        # The request ID.
        self.request_id = request_id
        # The intelligent meeting summary content.
        self.summary = summary
        # The new session title.
        self.title = title
        # The to-do item details.
        self.todo_content = todo_content
        # The speech-type execution parameters.
        self.transcription = transcription

    def validate(self):
        if self.transcription:
            for v1 in self.transcription:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.minutes_id is not None:
            result['minutesId'] = self.minutes_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        if self.todo_content is not None:
            result['todoContent'] = self.todo_content

        result['transcription'] = []
        if self.transcription is not None:
            for k1 in self.transcription:
                result['transcription'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('minutesId') is not None:
            self.minutes_id = m.get('minutesId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('todoContent') is not None:
            self.todo_content = m.get('todoContent')

        self.transcription = []
        if m.get('transcription') is not None:
            for k1 in m.get('transcription'):
                temp_model = main_models.GetAliDingMinutesContentResponseBodyTranscription()
                self.transcription.append(temp_model.from_map(k1))

        return self

class GetAliDingMinutesContentResponseBodyTranscription(DaraModel):
    def __init__(
        self,
        content: str = None,
        speaker: str = None,
        speaker_avatar: str = None,
        time_end: int = None,
        time_start: int = None,
    ):
        # The returned content.
        self.content = content
        # The speaker.
        self.speaker = speaker
        # The avatar of the speaker. An empty string is returned if no avatar is available.
        self.speaker_avatar = speaker_avatar
        # The end time of the segment.
        self.time_end = time_end
        # The start time of the segment.
        self.time_start = time_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.speaker is not None:
            result['speaker'] = self.speaker

        if self.speaker_avatar is not None:
            result['speakerAvatar'] = self.speaker_avatar

        if self.time_end is not None:
            result['timeEnd'] = self.time_end

        if self.time_start is not None:
            result['timeStart'] = self.time_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('speaker') is not None:
            self.speaker = m.get('speaker')

        if m.get('speakerAvatar') is not None:
            self.speaker_avatar = m.get('speakerAvatar')

        if m.get('timeEnd') is not None:
            self.time_end = m.get('timeEnd')

        if m.get('timeStart') is not None:
            self.time_start = m.get('timeStart')

        return self

