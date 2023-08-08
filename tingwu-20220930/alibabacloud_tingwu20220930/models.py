# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any


class CreateFileTransRequest(TeaModel):
    def __init__(
        self,
        ability_params: Dict[str, Any] = None,
        app_key: str = None,
        asr_params: Dict[str, Any] = None,
        audio_language: str = None,
        audio_oss_bucket: str = None,
        audio_oss_path: str = None,
        audio_output_enabled: bool = None,
        audio_output_oss_bucket: str = None,
        audio_output_oss_path: str = None,
        audio_role_num: str = None,
        audio_segments_enabled: bool = None,
        lab_params: Dict[str, Any] = None,
        tags: Dict[str, Any] = None,
        trans_key: str = None,
        trans_result_oss_bucket: str = None,
        trans_result_oss_path: str = None,
        video_output_enabled: bool = None,
        video_output_oss_bucket: str = None,
        video_output_oss_path: str = None,
    ):
        self.ability_params = ability_params
        self.app_key = app_key
        self.asr_params = asr_params
        self.audio_language = audio_language
        self.audio_oss_bucket = audio_oss_bucket
        self.audio_oss_path = audio_oss_path
        self.audio_output_enabled = audio_output_enabled
        self.audio_output_oss_bucket = audio_output_oss_bucket
        self.audio_output_oss_path = audio_output_oss_path
        self.audio_role_num = audio_role_num
        self.audio_segments_enabled = audio_segments_enabled
        self.lab_params = lab_params
        self.tags = tags
        self.trans_key = trans_key
        self.trans_result_oss_bucket = trans_result_oss_bucket
        self.trans_result_oss_path = trans_result_oss_path
        self.video_output_enabled = video_output_enabled
        self.video_output_oss_bucket = video_output_oss_bucket
        self.video_output_oss_path = video_output_oss_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ability_params is not None:
            result['AbilityParams'] = self.ability_params
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.asr_params is not None:
            result['AsrParams'] = self.asr_params
        if self.audio_language is not None:
            result['AudioLanguage'] = self.audio_language
        if self.audio_oss_bucket is not None:
            result['AudioOssBucket'] = self.audio_oss_bucket
        if self.audio_oss_path is not None:
            result['AudioOssPath'] = self.audio_oss_path
        if self.audio_output_enabled is not None:
            result['AudioOutputEnabled'] = self.audio_output_enabled
        if self.audio_output_oss_bucket is not None:
            result['AudioOutputOssBucket'] = self.audio_output_oss_bucket
        if self.audio_output_oss_path is not None:
            result['AudioOutputOssPath'] = self.audio_output_oss_path
        if self.audio_role_num is not None:
            result['AudioRoleNum'] = self.audio_role_num
        if self.audio_segments_enabled is not None:
            result['AudioSegmentsEnabled'] = self.audio_segments_enabled
        if self.lab_params is not None:
            result['LabParams'] = self.lab_params
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.trans_key is not None:
            result['TransKey'] = self.trans_key
        if self.trans_result_oss_bucket is not None:
            result['TransResultOssBucket'] = self.trans_result_oss_bucket
        if self.trans_result_oss_path is not None:
            result['TransResultOssPath'] = self.trans_result_oss_path
        if self.video_output_enabled is not None:
            result['VideoOutputEnabled'] = self.video_output_enabled
        if self.video_output_oss_bucket is not None:
            result['VideoOutputOssBucket'] = self.video_output_oss_bucket
        if self.video_output_oss_path is not None:
            result['VideoOutputOssPath'] = self.video_output_oss_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbilityParams') is not None:
            self.ability_params = m.get('AbilityParams')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AsrParams') is not None:
            self.asr_params = m.get('AsrParams')
        if m.get('AudioLanguage') is not None:
            self.audio_language = m.get('AudioLanguage')
        if m.get('AudioOssBucket') is not None:
            self.audio_oss_bucket = m.get('AudioOssBucket')
        if m.get('AudioOssPath') is not None:
            self.audio_oss_path = m.get('AudioOssPath')
        if m.get('AudioOutputEnabled') is not None:
            self.audio_output_enabled = m.get('AudioOutputEnabled')
        if m.get('AudioOutputOssBucket') is not None:
            self.audio_output_oss_bucket = m.get('AudioOutputOssBucket')
        if m.get('AudioOutputOssPath') is not None:
            self.audio_output_oss_path = m.get('AudioOutputOssPath')
        if m.get('AudioRoleNum') is not None:
            self.audio_role_num = m.get('AudioRoleNum')
        if m.get('AudioSegmentsEnabled') is not None:
            self.audio_segments_enabled = m.get('AudioSegmentsEnabled')
        if m.get('LabParams') is not None:
            self.lab_params = m.get('LabParams')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TransKey') is not None:
            self.trans_key = m.get('TransKey')
        if m.get('TransResultOssBucket') is not None:
            self.trans_result_oss_bucket = m.get('TransResultOssBucket')
        if m.get('TransResultOssPath') is not None:
            self.trans_result_oss_path = m.get('TransResultOssPath')
        if m.get('VideoOutputEnabled') is not None:
            self.video_output_enabled = m.get('VideoOutputEnabled')
        if m.get('VideoOutputOssBucket') is not None:
            self.video_output_oss_bucket = m.get('VideoOutputOssBucket')
        if m.get('VideoOutputOssPath') is not None:
            self.video_output_oss_path = m.get('VideoOutputOssPath')
        return self


class CreateFileTransResponseBodyData(TeaModel):
    def __init__(
        self,
        trans_id: str = None,
        trans_key: str = None,
    ):
        self.trans_id = trans_id
        self.trans_key = trans_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trans_id is not None:
            result['TransId'] = self.trans_id
        if self.trans_key is not None:
            result['TransKey'] = self.trans_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransId') is not None:
            self.trans_id = m.get('TransId')
        if m.get('TransKey') is not None:
            self.trans_key = m.get('TransKey')
        return self


class CreateFileTransResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateFileTransResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateFileTransResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFileTransResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFileTransResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFileTransResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMeetingTransRequest(TeaModel):
    def __init__(
        self,
        ability_params: Dict[str, Any] = None,
        app_key: str = None,
        asr_params: Dict[str, Any] = None,
        audio_bit_rate: int = None,
        audio_format: str = None,
        audio_language: str = None,
        audio_output_enabled: bool = None,
        audio_output_oss_bucket: str = None,
        audio_output_oss_path: str = None,
        audio_package: str = None,
        audio_sample_rate: int = None,
        audio_segments_enabled: bool = None,
        doc_result_enabled: bool = None,
        lab_params: Dict[str, Any] = None,
        meeting_key: str = None,
        meeting_result_enabled: bool = None,
        meeting_result_oss_bucket: str = None,
        meeting_result_oss_path: str = None,
        realtime_active_result_level: int = None,
        realtime_result_enabled: bool = None,
        realtime_result_level: int = None,
        realtime_result_meeting_info_enabled: bool = None,
        realtime_result_words_enabled: bool = None,
        tags: Dict[str, Any] = None,
        translate_active_result_level: int = None,
        translate_languages: str = None,
        translate_result_enabled: bool = None,
        translate_result_level: int = None,
    ):
        self.ability_params = ability_params
        self.app_key = app_key
        self.asr_params = asr_params
        self.audio_bit_rate = audio_bit_rate
        self.audio_format = audio_format
        self.audio_language = audio_language
        self.audio_output_enabled = audio_output_enabled
        self.audio_output_oss_bucket = audio_output_oss_bucket
        self.audio_output_oss_path = audio_output_oss_path
        self.audio_package = audio_package
        self.audio_sample_rate = audio_sample_rate
        self.audio_segments_enabled = audio_segments_enabled
        self.doc_result_enabled = doc_result_enabled
        self.lab_params = lab_params
        self.meeting_key = meeting_key
        self.meeting_result_enabled = meeting_result_enabled
        self.meeting_result_oss_bucket = meeting_result_oss_bucket
        self.meeting_result_oss_path = meeting_result_oss_path
        self.realtime_active_result_level = realtime_active_result_level
        self.realtime_result_enabled = realtime_result_enabled
        self.realtime_result_level = realtime_result_level
        self.realtime_result_meeting_info_enabled = realtime_result_meeting_info_enabled
        self.realtime_result_words_enabled = realtime_result_words_enabled
        self.tags = tags
        self.translate_active_result_level = translate_active_result_level
        self.translate_languages = translate_languages
        self.translate_result_enabled = translate_result_enabled
        self.translate_result_level = translate_result_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ability_params is not None:
            result['AbilityParams'] = self.ability_params
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.asr_params is not None:
            result['AsrParams'] = self.asr_params
        if self.audio_bit_rate is not None:
            result['AudioBitRate'] = self.audio_bit_rate
        if self.audio_format is not None:
            result['AudioFormat'] = self.audio_format
        if self.audio_language is not None:
            result['AudioLanguage'] = self.audio_language
        if self.audio_output_enabled is not None:
            result['AudioOutputEnabled'] = self.audio_output_enabled
        if self.audio_output_oss_bucket is not None:
            result['AudioOutputOssBucket'] = self.audio_output_oss_bucket
        if self.audio_output_oss_path is not None:
            result['AudioOutputOssPath'] = self.audio_output_oss_path
        if self.audio_package is not None:
            result['AudioPackage'] = self.audio_package
        if self.audio_sample_rate is not None:
            result['AudioSampleRate'] = self.audio_sample_rate
        if self.audio_segments_enabled is not None:
            result['AudioSegmentsEnabled'] = self.audio_segments_enabled
        if self.doc_result_enabled is not None:
            result['DocResultEnabled'] = self.doc_result_enabled
        if self.lab_params is not None:
            result['LabParams'] = self.lab_params
        if self.meeting_key is not None:
            result['MeetingKey'] = self.meeting_key
        if self.meeting_result_enabled is not None:
            result['MeetingResultEnabled'] = self.meeting_result_enabled
        if self.meeting_result_oss_bucket is not None:
            result['MeetingResultOssBucket'] = self.meeting_result_oss_bucket
        if self.meeting_result_oss_path is not None:
            result['MeetingResultOssPath'] = self.meeting_result_oss_path
        if self.realtime_active_result_level is not None:
            result['RealtimeActiveResultLevel'] = self.realtime_active_result_level
        if self.realtime_result_enabled is not None:
            result['RealtimeResultEnabled'] = self.realtime_result_enabled
        if self.realtime_result_level is not None:
            result['RealtimeResultLevel'] = self.realtime_result_level
        if self.realtime_result_meeting_info_enabled is not None:
            result['RealtimeResultMeetingInfoEnabled'] = self.realtime_result_meeting_info_enabled
        if self.realtime_result_words_enabled is not None:
            result['RealtimeResultWordsEnabled'] = self.realtime_result_words_enabled
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.translate_active_result_level is not None:
            result['TranslateActiveResultLevel'] = self.translate_active_result_level
        if self.translate_languages is not None:
            result['TranslateLanguages'] = self.translate_languages
        if self.translate_result_enabled is not None:
            result['TranslateResultEnabled'] = self.translate_result_enabled
        if self.translate_result_level is not None:
            result['TranslateResultLevel'] = self.translate_result_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbilityParams') is not None:
            self.ability_params = m.get('AbilityParams')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AsrParams') is not None:
            self.asr_params = m.get('AsrParams')
        if m.get('AudioBitRate') is not None:
            self.audio_bit_rate = m.get('AudioBitRate')
        if m.get('AudioFormat') is not None:
            self.audio_format = m.get('AudioFormat')
        if m.get('AudioLanguage') is not None:
            self.audio_language = m.get('AudioLanguage')
        if m.get('AudioOutputEnabled') is not None:
            self.audio_output_enabled = m.get('AudioOutputEnabled')
        if m.get('AudioOutputOssBucket') is not None:
            self.audio_output_oss_bucket = m.get('AudioOutputOssBucket')
        if m.get('AudioOutputOssPath') is not None:
            self.audio_output_oss_path = m.get('AudioOutputOssPath')
        if m.get('AudioPackage') is not None:
            self.audio_package = m.get('AudioPackage')
        if m.get('AudioSampleRate') is not None:
            self.audio_sample_rate = m.get('AudioSampleRate')
        if m.get('AudioSegmentsEnabled') is not None:
            self.audio_segments_enabled = m.get('AudioSegmentsEnabled')
        if m.get('DocResultEnabled') is not None:
            self.doc_result_enabled = m.get('DocResultEnabled')
        if m.get('LabParams') is not None:
            self.lab_params = m.get('LabParams')
        if m.get('MeetingKey') is not None:
            self.meeting_key = m.get('MeetingKey')
        if m.get('MeetingResultEnabled') is not None:
            self.meeting_result_enabled = m.get('MeetingResultEnabled')
        if m.get('MeetingResultOssBucket') is not None:
            self.meeting_result_oss_bucket = m.get('MeetingResultOssBucket')
        if m.get('MeetingResultOssPath') is not None:
            self.meeting_result_oss_path = m.get('MeetingResultOssPath')
        if m.get('RealtimeActiveResultLevel') is not None:
            self.realtime_active_result_level = m.get('RealtimeActiveResultLevel')
        if m.get('RealtimeResultEnabled') is not None:
            self.realtime_result_enabled = m.get('RealtimeResultEnabled')
        if m.get('RealtimeResultLevel') is not None:
            self.realtime_result_level = m.get('RealtimeResultLevel')
        if m.get('RealtimeResultMeetingInfoEnabled') is not None:
            self.realtime_result_meeting_info_enabled = m.get('RealtimeResultMeetingInfoEnabled')
        if m.get('RealtimeResultWordsEnabled') is not None:
            self.realtime_result_words_enabled = m.get('RealtimeResultWordsEnabled')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TranslateActiveResultLevel') is not None:
            self.translate_active_result_level = m.get('TranslateActiveResultLevel')
        if m.get('TranslateLanguages') is not None:
            self.translate_languages = m.get('TranslateLanguages')
        if m.get('TranslateResultEnabled') is not None:
            self.translate_result_enabled = m.get('TranslateResultEnabled')
        if m.get('TranslateResultLevel') is not None:
            self.translate_result_level = m.get('TranslateResultLevel')
        return self


class CreateMeetingTransResponseBodyData(TeaModel):
    def __init__(
        self,
        meeting_id: str = None,
        meeting_join_url: str = None,
        meeting_key: str = None,
    ):
        self.meeting_id = meeting_id
        self.meeting_join_url = meeting_join_url
        self.meeting_key = meeting_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meeting_id is not None:
            result['MeetingId'] = self.meeting_id
        if self.meeting_join_url is not None:
            result['MeetingJoinUrl'] = self.meeting_join_url
        if self.meeting_key is not None:
            result['MeetingKey'] = self.meeting_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeetingId') is not None:
            self.meeting_id = m.get('MeetingId')
        if m.get('MeetingJoinUrl') is not None:
            self.meeting_join_url = m.get('MeetingJoinUrl')
        if m.get('MeetingKey') is not None:
            self.meeting_key = m.get('MeetingKey')
        return self


class CreateMeetingTransResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateMeetingTransResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateMeetingTransResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMeetingTransResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMeetingTransResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMeetingTransResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileTransResponseBodyData(TeaModel):
    def __init__(
        self,
        trans_id: str = None,
        trans_key: str = None,
        trans_status: str = None,
    ):
        self.trans_id = trans_id
        self.trans_key = trans_key
        self.trans_status = trans_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trans_id is not None:
            result['TransId'] = self.trans_id
        if self.trans_key is not None:
            result['TransKey'] = self.trans_key
        if self.trans_status is not None:
            result['TransStatus'] = self.trans_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransId') is not None:
            self.trans_id = m.get('TransId')
        if m.get('TransKey') is not None:
            self.trans_key = m.get('TransKey')
        if m.get('TransStatus') is not None:
            self.trans_status = m.get('TransStatus')
        return self


class GetFileTransResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetFileTransResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetFileTransResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFileTransResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFileTransResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFileTransResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMeetingTransResponseBodyData(TeaModel):
    def __init__(
        self,
        meeting_id: str = None,
        meeting_key: str = None,
        meeting_status: str = None,
    ):
        self.meeting_id = meeting_id
        self.meeting_key = meeting_key
        self.meeting_status = meeting_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meeting_id is not None:
            result['MeetingId'] = self.meeting_id
        if self.meeting_key is not None:
            result['MeetingKey'] = self.meeting_key
        if self.meeting_status is not None:
            result['MeetingStatus'] = self.meeting_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeetingId') is not None:
            self.meeting_id = m.get('MeetingId')
        if m.get('MeetingKey') is not None:
            self.meeting_key = m.get('MeetingKey')
        if m.get('MeetingStatus') is not None:
            self.meeting_status = m.get('MeetingStatus')
        return self


class GetMeetingTransResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetMeetingTransResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetMeetingTransResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMeetingTransResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMeetingTransResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMeetingTransResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMeetingTransRequest(TeaModel):
    def __init__(
        self,
        meeting_role_num: int = None,
        only_role_split_result: bool = None,
    ):
        self.meeting_role_num = meeting_role_num
        self.only_role_split_result = only_role_split_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meeting_role_num is not None:
            result['MeetingRoleNum'] = self.meeting_role_num
        if self.only_role_split_result is not None:
            result['OnlyRoleSplitResult'] = self.only_role_split_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeetingRoleNum') is not None:
            self.meeting_role_num = m.get('MeetingRoleNum')
        if m.get('OnlyRoleSplitResult') is not None:
            self.only_role_split_result = m.get('OnlyRoleSplitResult')
        return self


class StopMeetingTransResponseBodyData(TeaModel):
    def __init__(
        self,
        meeting_id: str = None,
        meeting_key: str = None,
        meeting_status: str = None,
    ):
        self.meeting_id = meeting_id
        self.meeting_key = meeting_key
        self.meeting_status = meeting_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meeting_id is not None:
            result['MeetingId'] = self.meeting_id
        if self.meeting_key is not None:
            result['MeetingKey'] = self.meeting_key
        if self.meeting_status is not None:
            result['MeetingStatus'] = self.meeting_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeetingId') is not None:
            self.meeting_id = m.get('MeetingId')
        if m.get('MeetingKey') is not None:
            self.meeting_key = m.get('MeetingKey')
        if m.get('MeetingStatus') is not None:
            self.meeting_status = m.get('MeetingStatus')
        return self


class StopMeetingTransResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StopMeetingTransResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = StopMeetingTransResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopMeetingTransResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopMeetingTransResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopMeetingTransResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


