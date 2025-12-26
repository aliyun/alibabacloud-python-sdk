# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lingmou20250527 import models as main_models
from darabonba.model import DaraModel

class GetTTSVoiceByIdCustomResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTTSVoiceByIdCustomResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetTTSVoiceByIdCustomResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetTTSVoiceByIdCustomResponseBodyData(DaraModel):
    def __init__(
        self,
        audio_url: str = None,
        censor_status: str = None,
        common: bool = None,
        create_time: str = None,
        description: str = None,
        error_detail: str = None,
        gender: str = None,
        id: str = None,
        language: str = None,
        modified_time: str = None,
        name: str = None,
        remain_seconds: int = None,
        status: str = None,
        text: str = None,
        voice_key: str = None,
    ):
        self.audio_url = audio_url
        self.censor_status = censor_status
        self.common = common
        self.create_time = create_time
        self.description = description
        self.error_detail = error_detail
        self.gender = gender
        self.id = id
        self.language = language
        self.modified_time = modified_time
        self.name = name
        self.remain_seconds = remain_seconds
        self.status = status
        self.text = text
        self.voice_key = voice_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_url is not None:
            result['audioURL'] = self.audio_url

        if self.censor_status is not None:
            result['censorStatus'] = self.censor_status

        if self.common is not None:
            result['common'] = self.common

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.error_detail is not None:
            result['errorDetail'] = self.error_detail

        if self.gender is not None:
            result['gender'] = self.gender

        if self.id is not None:
            result['id'] = self.id

        if self.language is not None:
            result['language'] = self.language

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.name is not None:
            result['name'] = self.name

        if self.remain_seconds is not None:
            result['remainSeconds'] = self.remain_seconds

        if self.status is not None:
            result['status'] = self.status

        if self.text is not None:
            result['text'] = self.text

        if self.voice_key is not None:
            result['voiceKey'] = self.voice_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioURL') is not None:
            self.audio_url = m.get('audioURL')

        if m.get('censorStatus') is not None:
            self.censor_status = m.get('censorStatus')

        if m.get('common') is not None:
            self.common = m.get('common')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('errorDetail') is not None:
            self.error_detail = m.get('errorDetail')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('remainSeconds') is not None:
            self.remain_seconds = m.get('remainSeconds')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('voiceKey') is not None:
            self.voice_key = m.get('voiceKey')

        return self

