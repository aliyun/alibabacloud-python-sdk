# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddCartoonHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddCartoonRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        start_video_md_5: str = None,
        start_video_url: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.start_video_md_5 = start_video_md_5
        # This parameter is required.
        self.start_video_url = start_video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.start_video_md_5 is not None:
            result['StartVideoMd5'] = self.start_video_md_5
        if self.start_video_url is not None:
            result['StartVideoUrl'] = self.start_video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('StartVideoMd5') is not None:
            self.start_video_md_5 = m.get('StartVideoMd5')
        if m.get('StartVideoUrl') is not None:
            self.start_video_url = m.get('StartVideoUrl')
        return self


class AddCartoonResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddCartoonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCartoonResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddCartoonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCustomQAHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddCustomQARequest(TeaModel):
    def __init__(
        self,
        answers: List[str] = None,
        hotel_id: str = None,
        key_words: List[str] = None,
        major_question: str = None,
        supplementary_questions: List[str] = None,
    ):
        self.answers = answers
        # This parameter is required.
        self.hotel_id = hotel_id
        self.key_words = key_words
        self.major_question = major_question
        self.supplementary_questions = supplementary_questions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers is not None:
            result['Answers'] = self.answers
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.supplementary_questions is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions = m.get('SupplementaryQuestions')
        return self


class AddCustomQAShrinkRequest(TeaModel):
    def __init__(
        self,
        answers_shrink: str = None,
        hotel_id: str = None,
        key_words_shrink: str = None,
        major_question: str = None,
        supplementary_questions_shrink: str = None,
    ):
        self.answers_shrink = answers_shrink
        # This parameter is required.
        self.hotel_id = hotel_id
        self.key_words_shrink = key_words_shrink
        self.major_question = major_question
        self.supplementary_questions_shrink = supplementary_questions_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers_shrink is not None:
            result['Answers'] = self.answers_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words_shrink is not None:
            result['KeyWords'] = self.key_words_shrink
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.supplementary_questions_shrink is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers_shrink = m.get('Answers')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words_shrink = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions_shrink = m.get('SupplementaryQuestions')
        return self


class AddCustomQAResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddCustomQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCustomQAResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddCustomQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCustomQAV2Headers(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddCustomQAV2Request(TeaModel):
    def __init__(
        self,
        answers: List[str] = None,
        hotel_id: str = None,
        key_words: List[str] = None,
        major_question: str = None,
        supplementary_questions: List[str] = None,
    ):
        # This parameter is required.
        self.answers = answers
        # This parameter is required.
        self.hotel_id = hotel_id
        self.key_words = key_words
        self.major_question = major_question
        self.supplementary_questions = supplementary_questions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers is not None:
            result['Answers'] = self.answers
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.supplementary_questions is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions = m.get('SupplementaryQuestions')
        return self


class AddCustomQAV2ShrinkRequest(TeaModel):
    def __init__(
        self,
        answers_shrink: str = None,
        hotel_id: str = None,
        key_words_shrink: str = None,
        major_question: str = None,
        supplementary_questions_shrink: str = None,
    ):
        # This parameter is required.
        self.answers_shrink = answers_shrink
        # This parameter is required.
        self.hotel_id = hotel_id
        self.key_words_shrink = key_words_shrink
        self.major_question = major_question
        self.supplementary_questions_shrink = supplementary_questions_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers_shrink is not None:
            result['Answers'] = self.answers_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words_shrink is not None:
            result['KeyWords'] = self.key_words_shrink
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.supplementary_questions_shrink is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers_shrink = m.get('Answers')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words_shrink = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions_shrink = m.get('SupplementaryQuestions')
        return self


class AddCustomQAV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        answers: str = None,
        create_time: str = None,
        hotel_id: str = None,
        key_words: str = None,
        last_operator: str = None,
        major_question: str = None,
        qa_id: str = None,
        status: int = None,
        supplementary_question: str = None,
        update_time: str = None,
    ):
        self.answers = answers
        self.create_time = create_time
        self.hotel_id = hotel_id
        self.key_words = key_words
        self.last_operator = last_operator
        self.major_question = major_question
        # qaID
        self.qa_id = qa_id
        self.status = status
        self.supplementary_question = supplementary_question
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers is not None:
            result['Answers'] = self.answers
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.last_operator is not None:
            result['LastOperator'] = self.last_operator
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.qa_id is not None:
            result['QaId'] = self.qa_id
        if self.status is not None:
            result['Status'] = self.status
        if self.supplementary_question is not None:
            result['SupplementaryQuestion'] = self.supplementary_question
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('LastOperator') is not None:
            self.last_operator = m.get('LastOperator')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('QaId') is not None:
            self.qa_id = m.get('QaId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementaryQuestion') is not None:
            self.supplementary_question = m.get('SupplementaryQuestion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class AddCustomQAV2ResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: AddCustomQAV2ResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddCustomQAV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddCustomQAV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCustomQAV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddCustomQAV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMessageTemplateHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddMessageTemplateRequest(TeaModel):
    def __init__(
        self,
        template_detail: str = None,
        template_name: str = None,
    ):
        # This parameter is required.
        self.template_detail = template_detail
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_detail is not None:
            result['TemplateDetail'] = self.template_detail
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateDetail') is not None:
            self.template_detail = m.get('TemplateDetail')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class AddMessageTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class AddMessageTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddMessageTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddMessageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrUpdateDisPlayModesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddOrUpdateDisPlayModesRequest(TeaModel):
    def __init__(
        self,
        hotel_device_mode_list: List[str] = None,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.hotel_device_mode_list = hotel_device_mode_list
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_device_mode_list is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list = m.get('HotelDeviceModeList')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class AddOrUpdateDisPlayModesShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_device_mode_list_shrink: str = None,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.hotel_device_mode_list_shrink = hotel_device_mode_list_shrink
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_device_mode_list_shrink is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list_shrink = m.get('HotelDeviceModeList')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class AddOrUpdateDisPlayModesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddOrUpdateDisPlayModesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddOrUpdateDisPlayModesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddOrUpdateDisPlayModesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrUpdateHotelSettingHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddOrUpdateHotelSettingRequestHotelScreenSaver(TeaModel):
    def __init__(
        self,
        screen_saver_pic_url: str = None,
        screen_saver_style: str = None,
    ):
        self.screen_saver_pic_url = screen_saver_pic_url
        self.screen_saver_style = screen_saver_style

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.screen_saver_pic_url is not None:
            result['ScreenSaverPicUrl'] = self.screen_saver_pic_url
        if self.screen_saver_style is not None:
            result['ScreenSaverStyle'] = self.screen_saver_style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScreenSaverPicUrl') is not None:
            self.screen_saver_pic_url = m.get('ScreenSaverPicUrl')
        if m.get('ScreenSaverStyle') is not None:
            self.screen_saver_style = m.get('ScreenSaverStyle')
        return self


class AddOrUpdateHotelSettingRequestNightMode(TeaModel):
    def __init__(
        self,
        default_bright: str = None,
        default_volume: str = None,
        enable: bool = None,
        end: str = None,
        standby_action: str = None,
        start: str = None,
    ):
        self.default_bright = default_bright
        self.default_volume = default_volume
        self.enable = enable
        self.end = end
        self.standby_action = standby_action
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_bright is not None:
            result['DefaultBright'] = self.default_bright
        if self.default_volume is not None:
            result['DefaultVolume'] = self.default_volume
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end is not None:
            result['End'] = self.end
        if self.standby_action is not None:
            result['StandbyAction'] = self.standby_action
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultBright') is not None:
            self.default_bright = m.get('DefaultBright')
        if m.get('DefaultVolume') is not None:
            self.default_volume = m.get('DefaultVolume')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('StandbyAction') is not None:
            self.standby_action = m.get('StandbyAction')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class AddOrUpdateHotelSettingRequest(TeaModel):
    def __init__(
        self,
        hotel_device_mode_list: List[str] = None,
        hotel_id: str = None,
        hotel_screen_saver: AddOrUpdateHotelSettingRequestHotelScreenSaver = None,
        night_mode: AddOrUpdateHotelSettingRequestNightMode = None,
        setting_type: str = None,
        value: str = None,
    ):
        self.hotel_device_mode_list = hotel_device_mode_list
        self.hotel_id = hotel_id
        self.hotel_screen_saver = hotel_screen_saver
        self.night_mode = night_mode
        self.setting_type = setting_type
        self.value = value

    def validate(self):
        if self.hotel_screen_saver:
            self.hotel_screen_saver.validate()
        if self.night_mode:
            self.night_mode.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_device_mode_list is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_screen_saver is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver.to_map()
        if self.night_mode is not None:
            result['NightMode'] = self.night_mode.to_map()
        if self.setting_type is not None:
            result['SettingType'] = self.setting_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list = m.get('HotelDeviceModeList')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelScreenSaver') is not None:
            temp_model = AddOrUpdateHotelSettingRequestHotelScreenSaver()
            self.hotel_screen_saver = temp_model.from_map(m['HotelScreenSaver'])
        if m.get('NightMode') is not None:
            temp_model = AddOrUpdateHotelSettingRequestNightMode()
            self.night_mode = temp_model.from_map(m['NightMode'])
        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddOrUpdateHotelSettingShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_device_mode_list_shrink: str = None,
        hotel_id: str = None,
        hotel_screen_saver_shrink: str = None,
        night_mode_shrink: str = None,
        setting_type: str = None,
        value: str = None,
    ):
        self.hotel_device_mode_list_shrink = hotel_device_mode_list_shrink
        self.hotel_id = hotel_id
        self.hotel_screen_saver_shrink = hotel_screen_saver_shrink
        self.night_mode_shrink = night_mode_shrink
        self.setting_type = setting_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_device_mode_list_shrink is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_screen_saver_shrink is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver_shrink
        if self.night_mode_shrink is not None:
            result['NightMode'] = self.night_mode_shrink
        if self.setting_type is not None:
            result['SettingType'] = self.setting_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list_shrink = m.get('HotelDeviceModeList')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelScreenSaver') is not None:
            self.hotel_screen_saver_shrink = m.get('HotelScreenSaver')
        if m.get('NightMode') is not None:
            self.night_mode_shrink = m.get('NightMode')
        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddOrUpdateHotelSettingResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddOrUpdateHotelSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddOrUpdateHotelSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddOrUpdateHotelSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrUpdateScreenSaverHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddOrUpdateScreenSaverRequestHotelScreenSaver(TeaModel):
    def __init__(
        self,
        screen_saver_pic_url: str = None,
        screen_saver_style: str = None,
    ):
        self.screen_saver_pic_url = screen_saver_pic_url
        self.screen_saver_style = screen_saver_style

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.screen_saver_pic_url is not None:
            result['ScreenSaverPicUrl'] = self.screen_saver_pic_url
        if self.screen_saver_style is not None:
            result['ScreenSaverStyle'] = self.screen_saver_style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScreenSaverPicUrl') is not None:
            self.screen_saver_pic_url = m.get('ScreenSaverPicUrl')
        if m.get('ScreenSaverStyle') is not None:
            self.screen_saver_style = m.get('ScreenSaverStyle')
        return self


class AddOrUpdateScreenSaverRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        hotel_screen_saver: AddOrUpdateScreenSaverRequestHotelScreenSaver = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.hotel_screen_saver = hotel_screen_saver

    def validate(self):
        if self.hotel_screen_saver:
            self.hotel_screen_saver.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_screen_saver is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelScreenSaver') is not None:
            temp_model = AddOrUpdateScreenSaverRequestHotelScreenSaver()
            self.hotel_screen_saver = temp_model.from_map(m['HotelScreenSaver'])
        return self


class AddOrUpdateScreenSaverShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        hotel_screen_saver_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.hotel_screen_saver_shrink = hotel_screen_saver_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_screen_saver_shrink is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelScreenSaver') is not None:
            self.hotel_screen_saver_shrink = m.get('HotelScreenSaver')
        return self


class AddOrUpdateScreenSaverResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddOrUpdateScreenSaverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddOrUpdateScreenSaverResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddOrUpdateScreenSaverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOrUpdateWelcomeTextHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AddOrUpdateWelcomeTextRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        music_url: str = None,
        welcome_text: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.music_url = music_url
        # This parameter is required.
        self.welcome_text = welcome_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        if self.welcome_text is not None:
            result['WelcomeText'] = self.welcome_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        if m.get('WelcomeText') is not None:
            self.welcome_text = m.get('WelcomeText')
        return self


class AddOrUpdateWelcomeTextResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class AddOrUpdateWelcomeTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddOrUpdateWelcomeTextResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddOrUpdateWelcomeTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuditHotelHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AuditHotelRequestAuditHotelReq(TeaModel):
    def __init__(
        self,
        audit_opinion: str = None,
        hotel_id: str = None,
        status: int = None,
    ):
        self.audit_opinion = audit_opinion
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_opinion is not None:
            result['AuditOpinion'] = self.audit_opinion
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditOpinion') is not None:
            self.audit_opinion = m.get('AuditOpinion')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class AuditHotelRequest(TeaModel):
    def __init__(
        self,
        audit_hotel_req: AuditHotelRequestAuditHotelReq = None,
    ):
        # This parameter is required.
        self.audit_hotel_req = audit_hotel_req

    def validate(self):
        if self.audit_hotel_req:
            self.audit_hotel_req.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_hotel_req is not None:
            result['AuditHotelReq'] = self.audit_hotel_req.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditHotelReq') is not None:
            temp_model = AuditHotelRequestAuditHotelReq()
            self.audit_hotel_req = temp_model.from_map(m['AuditHotelReq'])
        return self


class AuditHotelShrinkRequest(TeaModel):
    def __init__(
        self,
        audit_hotel_req_shrink: str = None,
    ):
        # This parameter is required.
        self.audit_hotel_req_shrink = audit_hotel_req_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_hotel_req_shrink is not None:
            result['AuditHotelReq'] = self.audit_hotel_req_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditHotelReq') is not None:
            self.audit_hotel_req_shrink = m.get('AuditHotelReq')
        return self


class AuditHotelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        # RequestId
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class AuditHotelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuditHotelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AuditHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddHotelRoomHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class BatchAddHotelRoomRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no_list: List[str] = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no_list = room_no_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no_list is not None:
            result['RoomNoList'] = self.room_no_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNoList') is not None:
            self.room_no_list = m.get('RoomNoList')
        return self


class BatchAddHotelRoomShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no_list_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no_list_shrink = room_no_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no_list_shrink is not None:
            result['RoomNoList'] = self.room_no_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNoList') is not None:
            self.room_no_list_shrink = m.get('RoomNoList')
        return self


class BatchAddHotelRoomResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class BatchAddHotelRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddHotelRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BatchAddHotelRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteHotelRoomHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class BatchDeleteHotelRoomRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no_list: List[str] = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no_list = room_no_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no_list is not None:
            result['RoomNoList'] = self.room_no_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNoList') is not None:
            self.room_no_list = m.get('RoomNoList')
        return self


class BatchDeleteHotelRoomShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no_list_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no_list_shrink = room_no_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no_list_shrink is not None:
            result['RoomNoList'] = self.room_no_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNoList') is not None:
            self.room_no_list_shrink = m.get('RoomNoList')
        return self


class BatchDeleteHotelRoomResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class BatchDeleteHotelRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteHotelRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BatchDeleteHotelRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckoutWithAKHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CheckoutWithAKRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class CheckoutWithAKResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class CheckoutWithAKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckoutWithAKResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckoutWithAKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChildAccountAuthHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ChildAccountAuthRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        app_key: str = None,
        hotel_id: str = None,
        tb_open_id: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.tb_open_id = tb_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class ChildAccountAuthResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ChildAccountAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChildAccountAuthResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ChildAccountAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ControlRoomDeviceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ControlRoomDeviceRequest(TeaModel):
    def __init__(
        self,
        cmd: str = None,
        device_index: int = None,
        device_number: str = None,
        hotel_id: str = None,
        properties: Dict[str, str] = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.cmd = cmd
        self.device_index = device_index
        # This parameter is required.
        self.device_number = device_number
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.properties = properties
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['Cmd'] = self.cmd
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ControlRoomDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        cmd: str = None,
        device_index: int = None,
        device_number: str = None,
        hotel_id: str = None,
        properties_shrink: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.cmd = cmd
        self.device_index = device_index
        # This parameter is required.
        self.device_number = device_number
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.properties_shrink = properties_shrink
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['Cmd'] = self.cmd
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.properties_shrink is not None:
            result['Properties'] = self.properties_shrink
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Properties') is not None:
            self.properties_shrink = m.get('Properties')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ControlRoomDeviceResponseBodyResult(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: int = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ControlRoomDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ControlRoomDeviceResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ControlRoomDeviceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ControlRoomDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ControlRoomDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ControlRoomDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHotelHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateHotelRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        est_open_time: str = None,
        hotel_address: str = None,
        hotel_email: str = None,
        hotel_name: str = None,
        phone_number: str = None,
        related_pk: str = None,
        related_pks: List[str] = None,
        remark: str = None,
        room_num: int = None,
        tb_open_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.est_open_time = est_open_time
        # This parameter is required.
        self.hotel_address = hotel_address
        # This parameter is required.
        self.hotel_email = hotel_email
        # This parameter is required.
        self.hotel_name = hotel_name
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.related_pk = related_pk
        # 酒店关联产品列表
        self.related_pks = related_pks
        self.remark = remark
        # This parameter is required.
        self.room_num = room_num
        # This parameter is required.
        self.tb_open_id = tb_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.est_open_time is not None:
            result['EstOpenTime'] = self.est_open_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_email is not None:
            result['HotelEmail'] = self.hotel_email
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.related_pk is not None:
            result['RelatedPk'] = self.related_pk
        if self.related_pks is not None:
            result['RelatedPks'] = self.related_pks
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.room_num is not None:
            result['RoomNum'] = self.room_num
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EstOpenTime') is not None:
            self.est_open_time = m.get('EstOpenTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelEmail') is not None:
            self.hotel_email = m.get('HotelEmail')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RelatedPk') is not None:
            self.related_pk = m.get('RelatedPk')
        if m.get('RelatedPks') is not None:
            self.related_pks = m.get('RelatedPks')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class CreateHotelShrinkRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        est_open_time: str = None,
        hotel_address: str = None,
        hotel_email: str = None,
        hotel_name: str = None,
        phone_number: str = None,
        related_pk: str = None,
        related_pks_shrink: str = None,
        remark: str = None,
        room_num: int = None,
        tb_open_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.est_open_time = est_open_time
        # This parameter is required.
        self.hotel_address = hotel_address
        # This parameter is required.
        self.hotel_email = hotel_email
        # This parameter is required.
        self.hotel_name = hotel_name
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.related_pk = related_pk
        # 酒店关联产品列表
        self.related_pks_shrink = related_pks_shrink
        self.remark = remark
        # This parameter is required.
        self.room_num = room_num
        # This parameter is required.
        self.tb_open_id = tb_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.est_open_time is not None:
            result['EstOpenTime'] = self.est_open_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_email is not None:
            result['HotelEmail'] = self.hotel_email
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.related_pk is not None:
            result['RelatedPk'] = self.related_pk
        if self.related_pks_shrink is not None:
            result['RelatedPks'] = self.related_pks_shrink
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.room_num is not None:
            result['RoomNum'] = self.room_num
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EstOpenTime') is not None:
            self.est_open_time = m.get('EstOpenTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelEmail') is not None:
            self.hotel_email = m.get('HotelEmail')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RelatedPk') is not None:
            self.related_pk = m.get('RelatedPk')
        if m.get('RelatedPks') is not None:
            self.related_pks_shrink = m.get('RelatedPks')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class CreateHotelResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class CreateHotelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHotelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHotelAlarmHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateHotelAlarmRequestScheduleInfoOnce(TeaModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class CreateHotelAlarmRequestScheduleInfoWeekly(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class CreateHotelAlarmRequestScheduleInfo(TeaModel):
    def __init__(
        self,
        once: CreateHotelAlarmRequestScheduleInfoOnce = None,
        type: str = None,
        weekly: CreateHotelAlarmRequestScheduleInfoWeekly = None,
    ):
        self.once = once
        # ONCE, WEEKLY
        # 
        # This parameter is required.
        self.type = type
        self.weekly = weekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = CreateHotelAlarmRequestScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = CreateHotelAlarmRequestScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class CreateHotelAlarmRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        music_type: str = None,
        rooms: List[str] = None,
        schedule_info: CreateHotelAlarmRequestScheduleInfo = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.music_type = music_type
        # This parameter is required.
        self.rooms = rooms
        # This parameter is required.
        self.schedule_info = schedule_info

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.rooms is not None:
            result['Rooms'] = self.rooms
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('Rooms') is not None:
            self.rooms = m.get('Rooms')
        if m.get('ScheduleInfo') is not None:
            temp_model = CreateHotelAlarmRequestScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        return self


class CreateHotelAlarmShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        music_type: str = None,
        rooms_shrink: str = None,
        schedule_info_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.music_type = music_type
        # This parameter is required.
        self.rooms_shrink = rooms_shrink
        # This parameter is required.
        self.schedule_info_shrink = schedule_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.rooms_shrink is not None:
            result['Rooms'] = self.rooms_shrink
        if self.schedule_info_shrink is not None:
            result['ScheduleInfo'] = self.schedule_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('Rooms') is not None:
            self.rooms_shrink = m.get('Rooms')
        if m.get('ScheduleInfo') is not None:
            self.schedule_info_shrink = m.get('ScheduleInfo')
        return self


class CreateHotelAlarmResponseBodyResult(TeaModel):
    def __init__(
        self,
        alarm_id: int = None,
        device_open_id: str = None,
        fail_msg: str = None,
        room_no: str = None,
        user_open_id: str = None,
    ):
        self.alarm_id = alarm_id
        self.device_open_id = device_open_id
        self.fail_msg = fail_msg
        self.room_no = room_no
        self.user_open_id = user_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        if self.fail_msg is not None:
            result['FailMsg'] = self.fail_msg
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        if m.get('FailMsg') is not None:
            self.fail_msg = m.get('FailMsg')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class CreateHotelAlarmResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: List[CreateHotelAlarmResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = CreateHotelAlarmResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class CreateHotelAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHotelAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateHotelAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRcuSceneHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateRcuSceneRequestSceneRelationExtDTO(TeaModel):
    def __init__(
        self,
        corpus_list: List[str] = None,
        description: str = None,
        icon: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.corpus_list = corpus_list
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.icon = icon
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corpus_list is not None:
            result['CorpusList'] = self.corpus_list
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpusList') is not None:
            self.corpus_list = m.get('CorpusList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateRcuSceneRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        scene_id: str = None,
        scene_relation_ext_dto: CreateRcuSceneRequestSceneRelationExtDTO = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.scene_id = scene_id
        # This parameter is required.
        self.scene_relation_ext_dto = scene_relation_ext_dto

    def validate(self):
        if self.scene_relation_ext_dto:
            self.scene_relation_ext_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_relation_ext_dto is not None:
            result['SceneRelationExtDTO'] = self.scene_relation_ext_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneRelationExtDTO') is not None:
            temp_model = CreateRcuSceneRequestSceneRelationExtDTO()
            self.scene_relation_ext_dto = temp_model.from_map(m['SceneRelationExtDTO'])
        return self


class CreateRcuSceneShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        scene_id: str = None,
        scene_relation_ext_dtoshrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.scene_id = scene_id
        # This parameter is required.
        self.scene_relation_ext_dtoshrink = scene_relation_ext_dtoshrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_relation_ext_dtoshrink is not None:
            result['SceneRelationExtDTO'] = self.scene_relation_ext_dtoshrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneRelationExtDTO') is not None:
            self.scene_relation_ext_dtoshrink = m.get('SceneRelationExtDTO')
        return self


class CreateRcuSceneResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class CreateRcuSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRcuSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateRcuSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCartoonHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteCartoonRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
    ):
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class DeleteCartoonResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteCartoonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCartoonResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteCartoonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomQAHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteCustomQARequest(TeaModel):
    def __init__(
        self,
        custom_qaids: List[str] = None,
        hotel_id: str = None,
    ):
        self.custom_qaids = custom_qaids
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_qaids is not None:
            result['CustomQAIds'] = self.custom_qaids
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomQAIds') is not None:
            self.custom_qaids = m.get('CustomQAIds')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class DeleteCustomQAShrinkRequest(TeaModel):
    def __init__(
        self,
        custom_qaids_shrink: str = None,
        hotel_id: str = None,
    ):
        self.custom_qaids_shrink = custom_qaids_shrink
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_qaids_shrink is not None:
            result['CustomQAIds'] = self.custom_qaids_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomQAIds') is not None:
            self.custom_qaids_shrink = m.get('CustomQAIds')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class DeleteCustomQAResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteCustomQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomQAResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteCustomQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHotelAlarmHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteHotelAlarmRequestAlarms(TeaModel):
    def __init__(
        self,
        alarm_id: int = None,
        device_open_id: str = None,
        room_no: str = None,
        user_open_id: str = None,
    ):
        # This parameter is required.
        self.alarm_id = alarm_id
        # This parameter is required.
        self.device_open_id = device_open_id
        self.room_no = room_no
        # This parameter is required.
        self.user_open_id = user_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class DeleteHotelAlarmRequest(TeaModel):
    def __init__(
        self,
        alarms: List[DeleteHotelAlarmRequestAlarms] = None,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.alarms = alarms
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        if self.alarms:
            for k in self.alarms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alarms'] = []
        if self.alarms is not None:
            for k in self.alarms:
                result['Alarms'].append(k.to_map() if k else None)
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarms = []
        if m.get('Alarms') is not None:
            for k in m.get('Alarms'):
                temp_model = DeleteHotelAlarmRequestAlarms()
                self.alarms.append(temp_model.from_map(k))
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class DeleteHotelAlarmShrinkRequest(TeaModel):
    def __init__(
        self,
        alarms_shrink: str = None,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.alarms_shrink = alarms_shrink
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarms_shrink is not None:
            result['Alarms'] = self.alarms_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alarms') is not None:
            self.alarms_shrink = m.get('Alarms')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class DeleteHotelAlarmResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteHotelAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHotelAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteHotelAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHotelSceneBookItemHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteHotelSceneBookItemRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        id: int = None,
        name: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteHotelSceneBookItemResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteHotelSceneBookItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHotelSceneBookItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteHotelSceneBookItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHotelSettingHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteHotelSettingRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        setting_type: str = None,
    ):
        self.hotel_id = hotel_id
        self.setting_type = setting_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.setting_type is not None:
            result['SettingType'] = self.setting_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')
        return self


class DeleteHotelSettingResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteHotelSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHotelSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteHotelSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMessageTemplateHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteMessageTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: int = None,
    ):
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteMessageTemplateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteMessageTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMessageTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteMessageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRcuSceneHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteRcuSceneRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        scene_id: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class DeleteRcuSceneResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DeleteRcuSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRcuSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteRcuSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeviceControlHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeviceControlRequestPayload(TeaModel):
    def __init__(
        self,
        category: str = None,
        cmd: str = None,
        device_number: str = None,
        extend_info: str = None,
        location: str = None,
        properties: Dict[str, str] = None,
    ):
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.cmd = cmd
        # This parameter is required.
        self.device_number = device_number
        self.extend_info = extend_info
        # This parameter is required.
        self.location = location
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.cmd is not None:
            result['Cmd'] = self.cmd
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.location is not None:
            result['Location'] = self.location
        if self.properties is not None:
            result['Properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        return self


class DeviceControlRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeviceControlRequest(TeaModel):
    def __init__(
        self,
        payload: DeviceControlRequestPayload = None,
        user_info: DeviceControlRequestUserInfo = None,
    ):
        self.payload = payload
        self.user_info = user_info

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = DeviceControlRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = DeviceControlRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class DeviceControlShrinkRequest(TeaModel):
    def __init__(
        self,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.payload_shrink = payload_shrink
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class DeviceControlResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeviceControlResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: DeviceControlResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeviceControlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeviceControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeviceControlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeviceControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteSceneHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ExecuteSceneRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
        scene_name: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no
        # This parameter is required.
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class ExecuteSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ExecuteSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ExecuteSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBasicInfoQAHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetBasicInfoQARequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class GetBasicInfoQAResponseBodyResult(TeaModel):
    def __init__(
        self,
        check_in_time: str = None,
        check_out_time: str = None,
        hotel_address: str = None,
        hotel_introduction: str = None,
        hotel_member: str = None,
        hotel_service: str = None,
        parking_expenses: str = None,
        parking_position: str = None,
        phone_number: str = None,
        wifi_name: str = None,
        wifi_password: str = None,
    ):
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.hotel_address = hotel_address
        self.hotel_introduction = hotel_introduction
        self.hotel_member = hotel_member
        self.hotel_service = hotel_service
        self.parking_expenses = parking_expenses
        self.parking_position = parking_position
        self.phone_number = phone_number
        self.wifi_name = wifi_name
        self.wifi_password = wifi_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_in_time is not None:
            result['CheckInTime'] = self.check_in_time
        if self.check_out_time is not None:
            result['CheckOutTime'] = self.check_out_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_introduction is not None:
            result['HotelIntroduction'] = self.hotel_introduction
        if self.hotel_member is not None:
            result['HotelMember'] = self.hotel_member
        if self.hotel_service is not None:
            result['HotelService'] = self.hotel_service
        if self.parking_expenses is not None:
            result['ParkingExpenses'] = self.parking_expenses
        if self.parking_position is not None:
            result['ParkingPosition'] = self.parking_position
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.wifi_name is not None:
            result['WifiName'] = self.wifi_name
        if self.wifi_password is not None:
            result['WifiPassword'] = self.wifi_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckInTime') is not None:
            self.check_in_time = m.get('CheckInTime')
        if m.get('CheckOutTime') is not None:
            self.check_out_time = m.get('CheckOutTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelIntroduction') is not None:
            self.hotel_introduction = m.get('HotelIntroduction')
        if m.get('HotelMember') is not None:
            self.hotel_member = m.get('HotelMember')
        if m.get('HotelService') is not None:
            self.hotel_service = m.get('HotelService')
        if m.get('ParkingExpenses') is not None:
            self.parking_expenses = m.get('ParkingExpenses')
        if m.get('ParkingPosition') is not None:
            self.parking_position = m.get('ParkingPosition')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('WifiName') is not None:
            self.wifi_name = m.get('WifiName')
        if m.get('WifiPassword') is not None:
            self.wifi_password = m.get('WifiPassword')
        return self


class GetBasicInfoQAResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: GetBasicInfoQAResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetBasicInfoQAResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetBasicInfoQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBasicInfoQAResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetBasicInfoQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCartoonHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetCartoonRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class GetCartoonResponseBodyResult(TeaModel):
    def __init__(
        self,
        start_video_md_5: str = None,
        start_video_url: str = None,
    ):
        self.start_video_md_5 = start_video_md_5
        self.start_video_url = start_video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_video_md_5 is not None:
            result['StartVideoMd5'] = self.start_video_md_5
        if self.start_video_url is not None:
            result['StartVideoUrl'] = self.start_video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartVideoMd5') is not None:
            self.start_video_md_5 = m.get('StartVideoMd5')
        if m.get('StartVideoUrl') is not None:
            self.start_video_url = m.get('StartVideoUrl')
        return self


class GetCartoonResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: GetCartoonResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetCartoonResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetCartoonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCartoonResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetCartoonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelContactByGenieDeviceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelContactByGenieDeviceRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelContactByGenieDeviceRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelContactByGenieDeviceRequest(TeaModel):
    def __init__(
        self,
        device_info: GetHotelContactByGenieDeviceRequestDeviceInfo = None,
        user_info: GetHotelContactByGenieDeviceRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetHotelContactByGenieDeviceRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = GetHotelContactByGenieDeviceRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelContactByGenieDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.device_info_shrink = device_info_shrink
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelContactByGenieDeviceResponseBodyResult(TeaModel):
    def __init__(
        self,
        expire_at: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hotel_id: str = None,
        icon: str = None,
        id: int = None,
        name: str = None,
        number: str = None,
        status: int = None,
        type: str = None,
        uuid: str = None,
    ):
        self.expire_at = expire_at
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hotel_id = hotel_id
        self.icon = icon
        self.id = id
        self.name = name
        self.number = number
        self.status = status
        self.type = type
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetHotelContactByGenieDeviceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: GetHotelContactByGenieDeviceResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelContactByGenieDeviceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelContactByGenieDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelContactByGenieDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelContactByGenieDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelContactByNumberHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelContactByNumberRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelContactByNumberRequest(TeaModel):
    def __init__(
        self,
        number: str = None,
        user_info: GetHotelContactByNumberRequestUserInfo = None,
    ):
        # This parameter is required.
        self.number = number
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('UserInfo') is not None:
            temp_model = GetHotelContactByNumberRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelContactByNumberShrinkRequest(TeaModel):
    def __init__(
        self,
        number: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.number = number
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelContactByNumberResponseBodyResult(TeaModel):
    def __init__(
        self,
        expire_at: str = None,
        hotel_id: str = None,
        icon: str = None,
        name: str = None,
        number: str = None,
        status: int = None,
        type: str = None,
        uuid: str = None,
    ):
        self.expire_at = expire_at
        self.hotel_id = hotel_id
        self.icon = icon
        self.name = name
        self.number = number
        self.status = status
        self.type = type
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetHotelContactByNumberResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: GetHotelContactByNumberResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelContactByNumberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelContactByNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelContactByNumberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelContactByNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelContactsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelContactsRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelContactsRequest(TeaModel):
    def __init__(
        self,
        user_info: GetHotelContactsRequestUserInfo = None,
    ):
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelContactsRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelContactsShrinkRequest(TeaModel):
    def __init__(
        self,
        user_info_shrink: str = None,
    ):
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelContactsResponseBodyResult(TeaModel):
    def __init__(
        self,
        expire_at: str = None,
        hotel_id: str = None,
        icon: str = None,
        name: str = None,
        number: str = None,
        status: int = None,
        type: str = None,
        uuid: str = None,
    ):
        self.expire_at = expire_at
        self.hotel_id = hotel_id
        self.icon = icon
        self.name = name
        self.number = number
        self.status = status
        self.type = type
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetHotelContactsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: List[GetHotelContactsResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetHotelContactsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelContactsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelHomeBackImageAndModesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelHomeBackImageAndModesRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelHomeBackImageAndModesRequest(TeaModel):
    def __init__(
        self,
        user_info: GetHotelHomeBackImageAndModesRequestUserInfo = None,
    ):
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelHomeBackImageAndModesRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelHomeBackImageAndModesShrinkRequest(TeaModel):
    def __init__(
        self,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelHomeBackImageAndModesResponseBodyResultModeList(TeaModel):
    def __init__(
        self,
        cn_name: str = None,
        code: str = None,
        icon: str = None,
    ):
        self.cn_name = cn_name
        self.code = code
        self.icon = icon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_name is not None:
            result['CnName'] = self.cn_name
        if self.code is not None:
            result['Code'] = self.code
        if self.icon is not None:
            result['Icon'] = self.icon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        return self


class GetHotelHomeBackImageAndModesResponseBodyResult(TeaModel):
    def __init__(
        self,
        background_image: str = None,
        hotel_name: str = None,
        mode_list: List[GetHotelHomeBackImageAndModesResponseBodyResultModeList] = None,
    ):
        self.background_image = background_image
        self.hotel_name = hotel_name
        self.mode_list = mode_list

    def validate(self):
        if self.mode_list:
            for k in self.mode_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_image is not None:
            result['BackgroundImage'] = self.background_image
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        result['ModeList'] = []
        if self.mode_list is not None:
            for k in self.mode_list:
                result['ModeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundImage') is not None:
            self.background_image = m.get('BackgroundImage')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        self.mode_list = []
        if m.get('ModeList') is not None:
            for k in m.get('ModeList'):
                temp_model = GetHotelHomeBackImageAndModesResponseBodyResultModeList()
                self.mode_list.append(temp_model.from_map(k))
        return self


class GetHotelHomeBackImageAndModesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetHotelHomeBackImageAndModesResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelHomeBackImageAndModesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetHotelHomeBackImageAndModesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelHomeBackImageAndModesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelHomeBackImageAndModesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelNoticeHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelNoticeRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelNoticeRequest(TeaModel):
    def __init__(
        self,
        user_info: GetHotelNoticeRequestUserInfo = None,
    ):
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelNoticeRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelNoticeShrinkRequest(TeaModel):
    def __init__(
        self,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelNoticeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
    ):
        self.code = code
        self.message = message
        # RequestId
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetHotelNoticeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelNoticeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelNoticeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelNoticeV2Headers(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelNoticeV2RequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelNoticeV2Request(TeaModel):
    def __init__(
        self,
        user_info: GetHotelNoticeV2RequestUserInfo = None,
    ):
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelNoticeV2RequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelNoticeV2ShrinkRequest(TeaModel):
    def __init__(
        self,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelNoticeV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        hotel_id: str = None,
        title: str = None,
    ):
        self.content = content
        self.hotel_id = hotel_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetHotelNoticeV2ResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: GetHotelNoticeV2ResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelNoticeV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelNoticeV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelNoticeV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelNoticeV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelOrderDetailHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelOrderDetailRequestPayload(TeaModel):
    def __init__(
        self,
        order_no: str = None,
    ):
        # This parameter is required.
        self.order_no = order_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        return self


class GetHotelOrderDetailRequest(TeaModel):
    def __init__(
        self,
        payload: GetHotelOrderDetailRequestPayload = None,
    ):
        # This parameter is required.
        self.payload = payload

    def validate(self):
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = GetHotelOrderDetailRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        return self


class GetHotelOrderDetailShrinkRequest(TeaModel):
    def __init__(
        self,
        payload_shrink: str = None,
    ):
        # This parameter is required.
        self.payload_shrink = payload_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        return self


class GetHotelOrderDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        apply_amt: int = None,
        gmt_create: int = None,
        item_url: str = None,
        name: str = None,
        quantity: int = None,
    ):
        self.apply_amt = apply_amt
        self.gmt_create = gmt_create
        self.item_url = item_url
        self.name = name
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_amt is not None:
            result['ApplyAmt'] = self.apply_amt
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.name is not None:
            result['Name'] = self.name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyAmt') is not None:
            self.apply_amt = m.get('ApplyAmt')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class GetHotelOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[GetHotelOrderDetailResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetHotelOrderDetailResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetHotelOrderDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelOrderDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelRoomDeviceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelRoomDeviceRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class GetHotelRoomDeviceResponseBodyResult(TeaModel):
    def __init__(
        self,
        firmware_version: str = None,
        hotel_id: str = None,
        mac: str = None,
        online_status: int = None,
        room_no: str = None,
        sn: str = None,
    ):
        self.firmware_version = firmware_version
        self.hotel_id = hotel_id
        self.mac = mac
        self.online_status = online_status
        self.room_no = room_no
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class GetHotelRoomDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[GetHotelRoomDeviceResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetHotelRoomDeviceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetHotelRoomDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelRoomDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelRoomDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelSampleUtterancesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelSampleUtterancesRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelSampleUtterancesRequest(TeaModel):
    def __init__(
        self,
        user_info: GetHotelSampleUtterancesRequestUserInfo = None,
    ):
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelSampleUtterancesRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelSampleUtterancesShrinkRequest(TeaModel):
    def __init__(
        self,
        user_info_shrink: str = None,
    ):
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelSampleUtterancesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetHotelSampleUtterancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelSampleUtterancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelSampleUtterancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelSceneItemDetailHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelSceneItemDetailRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        item_id: int = None,
        name: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        self.item_id = item_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetHotelSceneItemDetailResponseBodyResultDialogueList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        dialogue_id: str = None,
        no_answer: str = None,
        no_answer_template: str = None,
        process: int = None,
        question: str = None,
        service_id: str = None,
        update_time: int = None,
        yes_answer: str = None,
        yes_answer_template: str = None,
    ):
        self.create_time = create_time
        self.dialogue_id = dialogue_id
        self.no_answer = no_answer
        self.no_answer_template = no_answer_template
        self.process = process
        self.question = question
        self.service_id = service_id
        self.update_time = update_time
        self.yes_answer = yes_answer
        self.yes_answer_template = yes_answer_template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dialogue_id is not None:
            result['DialogueId'] = self.dialogue_id
        if self.no_answer is not None:
            result['NoAnswer'] = self.no_answer
        if self.no_answer_template is not None:
            result['NoAnswerTemplate'] = self.no_answer_template
        if self.process is not None:
            result['Process'] = self.process
        if self.question is not None:
            result['Question'] = self.question
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.yes_answer is not None:
            result['YesAnswer'] = self.yes_answer
        if self.yes_answer_template is not None:
            result['YesAnswerTemplate'] = self.yes_answer_template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DialogueId') is not None:
            self.dialogue_id = m.get('DialogueId')
        if m.get('NoAnswer') is not None:
            self.no_answer = m.get('NoAnswer')
        if m.get('NoAnswerTemplate') is not None:
            self.no_answer_template = m.get('NoAnswerTemplate')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('YesAnswer') is not None:
            self.yes_answer = m.get('YesAnswer')
        if m.get('YesAnswerTemplate') is not None:
            self.yes_answer_template = m.get('YesAnswerTemplate')
        return self


class GetHotelSceneItemDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        category: str = None,
        dialogue_list: List[GetHotelSceneItemDetailResponseBodyResultDialogueList] = None,
        icon: str = None,
        id: int = None,
        name: str = None,
        price: int = None,
        status: str = None,
        type: str = None,
        update_time: int = None,
    ):
        self.category = category
        self.dialogue_list = dialogue_list
        self.icon = icon
        self.id = id
        self.name = name
        self.price = price
        self.status = status
        self.type = type
        self.update_time = update_time

    def validate(self):
        if self.dialogue_list:
            for k in self.dialogue_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        result['DialogueList'] = []
        if self.dialogue_list is not None:
            for k in self.dialogue_list:
                result['DialogueList'].append(k.to_map() if k else None)
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.dialogue_list = []
        if m.get('DialogueList') is not None:
            for k in m.get('DialogueList'):
                temp_model = GetHotelSceneItemDetailResponseBodyResultDialogueList()
                self.dialogue_list.append(temp_model.from_map(k))
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetHotelSceneItemDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetHotelSceneItemDetailResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelSceneItemDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetHotelSceneItemDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelSceneItemDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelSceneItemDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelScreenSaverHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelScreenSaverRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetHotelScreenSaverRequest(TeaModel):
    def __init__(
        self,
        user_info: GetHotelScreenSaverRequestUserInfo = None,
    ):
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetHotelScreenSaverRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetHotelScreenSaverShrinkRequest(TeaModel):
    def __init__(
        self,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetHotelScreenSaverResponseBodyResult(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        style_code: str = None,
    ):
        self.pic_url = pic_url
        self.style_code = style_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.style_code is not None:
            result['StyleCode'] = self.style_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('StyleCode') is not None:
            self.style_code = m.get('StyleCode')
        return self


class GetHotelScreenSaverResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetHotelScreenSaverResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelScreenSaverResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetHotelScreenSaverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelScreenSaverResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelScreenSaverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelScreenSaverStyleHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelScreenSaverStyleRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
    ):
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class GetHotelScreenSaverStyleResponseBodyResult(TeaModel):
    def __init__(
        self,
        cn_name: str = None,
        code: str = None,
        en_name: str = None,
        pic_url: str = None,
    ):
        self.cn_name = cn_name
        self.code = code
        self.en_name = en_name
        self.pic_url = pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_name is not None:
            result['CnName'] = self.cn_name
        if self.code is not None:
            result['Code'] = self.code
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class GetHotelScreenSaverStyleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: List[GetHotelScreenSaverStyleResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetHotelScreenSaverStyleResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelScreenSaverStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelScreenSaverStyleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelScreenSaverStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotelSettingHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetHotelSettingRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        setting_type: str = None,
    ):
        self.hotel_id = hotel_id
        self.setting_type = setting_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.setting_type is not None:
            result['SettingType'] = self.setting_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')
        return self


class GetHotelSettingResponseBodyResultHotelScreenSaver(TeaModel):
    def __init__(
        self,
        screen_saver_pic_url: str = None,
        screen_saver_style: str = None,
    ):
        self.screen_saver_pic_url = screen_saver_pic_url
        self.screen_saver_style = screen_saver_style

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.screen_saver_pic_url is not None:
            result['ScreenSaverPicUrl'] = self.screen_saver_pic_url
        if self.screen_saver_style is not None:
            result['ScreenSaverStyle'] = self.screen_saver_style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScreenSaverPicUrl') is not None:
            self.screen_saver_pic_url = m.get('ScreenSaverPicUrl')
        if m.get('ScreenSaverStyle') is not None:
            self.screen_saver_style = m.get('ScreenSaverStyle')
        return self


class GetHotelSettingResponseBodyResultNightMode(TeaModel):
    def __init__(
        self,
        default_bright: str = None,
        default_volume: str = None,
        enable: bool = None,
        end: str = None,
        standby_action: str = None,
        start: str = None,
    ):
        # 夜间模式下的默认亮度
        self.default_bright = default_bright
        # 夜间模式下的默认音量
        self.default_volume = default_volume
        self.enable = enable
        self.end = end
        self.standby_action = standby_action
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_bright is not None:
            result['DefaultBright'] = self.default_bright
        if self.default_volume is not None:
            result['DefaultVolume'] = self.default_volume
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end is not None:
            result['End'] = self.end
        if self.standby_action is not None:
            result['StandbyAction'] = self.standby_action
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultBright') is not None:
            self.default_bright = m.get('DefaultBright')
        if m.get('DefaultVolume') is not None:
            self.default_volume = m.get('DefaultVolume')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('StandbyAction') is not None:
            self.standby_action = m.get('StandbyAction')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetHotelSettingResponseBodyResult(TeaModel):
    def __init__(
        self,
        delete_token: int = None,
        ext_info: str = None,
        hotel_device_mode_list: List[str] = None,
        hotel_id: str = None,
        hotel_screen_saver: GetHotelSettingResponseBodyResultHotelScreenSaver = None,
        night_mode: GetHotelSettingResponseBodyResultNightMode = None,
        setting_type: str = None,
        value: str = None,
    ):
        self.delete_token = delete_token
        self.ext_info = ext_info
        self.hotel_device_mode_list = hotel_device_mode_list
        self.hotel_id = hotel_id
        self.hotel_screen_saver = hotel_screen_saver
        self.night_mode = night_mode
        self.setting_type = setting_type
        self.value = value

    def validate(self):
        if self.hotel_screen_saver:
            self.hotel_screen_saver.validate()
        if self.night_mode:
            self.night_mode.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_token is not None:
            result['DeleteToken'] = self.delete_token
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.hotel_device_mode_list is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_screen_saver is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver.to_map()
        if self.night_mode is not None:
            result['NightMode'] = self.night_mode.to_map()
        if self.setting_type is not None:
            result['SettingType'] = self.setting_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteToken') is not None:
            self.delete_token = m.get('DeleteToken')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list = m.get('HotelDeviceModeList')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelScreenSaver') is not None:
            temp_model = GetHotelSettingResponseBodyResultHotelScreenSaver()
            self.hotel_screen_saver = temp_model.from_map(m['HotelScreenSaver'])
        if m.get('NightMode') is not None:
            temp_model = GetHotelSettingResponseBodyResultNightMode()
            self.night_mode = temp_model.from_map(m['NightMode'])
        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetHotelSettingResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: GetHotelSettingResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetHotelSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetHotelSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotelSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHotelSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRelationProductListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetRelationProductListResponseBodyResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        pk: str = None,
    ):
        self.name = name
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.pk is not None:
            result['Pk'] = self.pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        return self


class GetRelationProductListResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: List[GetRelationProductListResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetRelationProductListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetRelationProductListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRelationProductListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetRelationProductListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUnionIdHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetUnionIdRequest(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        return self


class GetUnionIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        union_id: str = None,
    ):
        self.organization_id = organization_id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.union_id is not None:
            result['UnionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')
        return self


class GetUnionIdResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: List[GetUnionIdResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetUnionIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetUnionIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUnionIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetUnionIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWelcomeTextAndMusicHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetWelcomeTextAndMusicRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class GetWelcomeTextAndMusicResponseBodyResult(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        music_url: str = None,
        text: str = None,
    ):
        self.hotel_id = hotel_id
        self.music_url = music_url
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetWelcomeTextAndMusicResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: GetWelcomeTextAndMusicResponseBodyResult = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetWelcomeTextAndMusicResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class GetWelcomeTextAndMusicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWelcomeTextAndMusicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetWelcomeTextAndMusicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HotelQrBindHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class HotelQrBindRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        code: str = None,
        ext_info: str = None,
        hotel_id: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        # This parameter is required.
        self.code = code
        self.ext_info = ext_info
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.code is not None:
            result['Code'] = self.code
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class HotelQrBindResponseBodyResultOpenDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class HotelQrBindResponseBodyResultOpenUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class HotelQrBindResponseBodyResult(TeaModel):
    def __init__(
        self,
        open_device_info: HotelQrBindResponseBodyResultOpenDeviceInfo = None,
        open_user_info: HotelQrBindResponseBodyResultOpenUserInfo = None,
    ):
        self.open_device_info = open_device_info
        self.open_user_info = open_user_info

    def validate(self):
        if self.open_device_info:
            self.open_device_info.validate()
        if self.open_user_info:
            self.open_user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_device_info is not None:
            result['OpenDeviceInfo'] = self.open_device_info.to_map()
        if self.open_user_info is not None:
            result['OpenUserInfo'] = self.open_user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenDeviceInfo') is not None:
            temp_model = HotelQrBindResponseBodyResultOpenDeviceInfo()
            self.open_device_info = temp_model.from_map(m['OpenDeviceInfo'])
        if m.get('OpenUserInfo') is not None:
            temp_model = HotelQrBindResponseBodyResultOpenUserInfo()
            self.open_user_info = temp_model.from_map(m['OpenUserInfo'])
        return self


class HotelQrBindResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: HotelQrBindResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = HotelQrBindResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class HotelQrBindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HotelQrBindResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = HotelQrBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportHotelConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ImportHotelConfigRequestImportHotelConfigRcuCustomScenes(TeaModel):
    def __init__(
        self,
        corpus_list: List[str] = None,
        description: str = None,
        icon: str = None,
        name: str = None,
        scene_id: str = None,
    ):
        # This parameter is required.
        self.corpus_list = corpus_list
        self.description = description
        self.icon = icon
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corpus_list is not None:
            result['CorpusList'] = self.corpus_list
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpusList') is not None:
            self.corpus_list = m.get('CorpusList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ImportHotelConfigRequestImportHotelConfig(TeaModel):
    def __init__(
        self,
        rcu_custom_scenes: List[ImportHotelConfigRequestImportHotelConfigRcuCustomScenes] = None,
    ):
        self.rcu_custom_scenes = rcu_custom_scenes

    def validate(self):
        if self.rcu_custom_scenes:
            for k in self.rcu_custom_scenes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RcuCustomScenes'] = []
        if self.rcu_custom_scenes is not None:
            for k in self.rcu_custom_scenes:
                result['RcuCustomScenes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rcu_custom_scenes = []
        if m.get('RcuCustomScenes') is not None:
            for k in m.get('RcuCustomScenes'):
                temp_model = ImportHotelConfigRequestImportHotelConfigRcuCustomScenes()
                self.rcu_custom_scenes.append(temp_model.from_map(k))
        return self


class ImportHotelConfigRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        import_hotel_config: ImportHotelConfigRequestImportHotelConfig = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.import_hotel_config = import_hotel_config

    def validate(self):
        if self.import_hotel_config:
            self.import_hotel_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.import_hotel_config is not None:
            result['ImportHotelConfig'] = self.import_hotel_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ImportHotelConfig') is not None:
            temp_model = ImportHotelConfigRequestImportHotelConfig()
            self.import_hotel_config = temp_model.from_map(m['ImportHotelConfig'])
        return self


class ImportHotelConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        import_hotel_config_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.import_hotel_config_shrink = import_hotel_config_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.import_hotel_config_shrink is not None:
            result['ImportHotelConfig'] = self.import_hotel_config_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ImportHotelConfig') is not None:
            self.import_hotel_config_shrink = m.get('ImportHotelConfig')
        return self


class ImportHotelConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ImportHotelConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportHotelConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ImportHotelConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportRoomControlDevicesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExtSwitchList(TeaModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        category: str = None,
        device_index: int = None,
        device_name: str = None,
        location: str = None,
    ):
        self.alias_list = alias_list
        self.category = category
        self.device_index = device_index
        self.device_name = device_name
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list
        if self.category is not None:
            result['Category'] = self.category
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExt(TeaModel):
    def __init__(
        self,
        switch_list: List[ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExtSwitchList] = None,
    ):
        self.switch_list = switch_list

    def validate(self):
        if self.switch_list:
            for k in self.switch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SwitchList'] = []
        if self.switch_list is not None:
            for k in self.switch_list:
                result['SwitchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.switch_list = []
        if m.get('SwitchList') is not None:
            for k in m.get('SwitchList'):
                temp_model = ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExtSwitchList()
                self.switch_list.append(temp_model.from_map(k))
        return self


class ImportRoomControlDevicesRequestLocationDevicesDevices(TeaModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        brand: str = None,
        city: str = None,
        connect_type: str = None,
        device_name: str = None,
        dn: str = None,
        infrared_id: str = None,
        infrared_index: str = None,
        infrared_version: str = None,
        multi_key_switch_ext: ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExt = None,
        name: str = None,
        number: str = None,
        pk: str = None,
        province: str = None,
        service_provider: str = None,
    ):
        self.alias_list = alias_list
        self.brand = brand
        self.city = city
        self.connect_type = connect_type
        # This parameter is required.
        self.device_name = device_name
        self.dn = dn
        self.infrared_id = infrared_id
        self.infrared_index = infrared_index
        self.infrared_version = infrared_version
        self.multi_key_switch_ext = multi_key_switch_ext
        # This parameter is required.
        self.name = name
        self.number = number
        self.pk = pk
        self.province = province
        self.service_provider = service_provider

    def validate(self):
        if self.multi_key_switch_ext:
            self.multi_key_switch_ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.city is not None:
            result['City'] = self.city
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.dn is not None:
            result['Dn'] = self.dn
        if self.infrared_id is not None:
            result['InfraredId'] = self.infrared_id
        if self.infrared_index is not None:
            result['InfraredIndex'] = self.infrared_index
        if self.infrared_version is not None:
            result['InfraredVersion'] = self.infrared_version
        if self.multi_key_switch_ext is not None:
            result['MultiKeySwitchExt'] = self.multi_key_switch_ext.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.province is not None:
            result['Province'] = self.province
        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Dn') is not None:
            self.dn = m.get('Dn')
        if m.get('InfraredId') is not None:
            self.infrared_id = m.get('InfraredId')
        if m.get('InfraredIndex') is not None:
            self.infrared_index = m.get('InfraredIndex')
        if m.get('InfraredVersion') is not None:
            self.infrared_version = m.get('InfraredVersion')
        if m.get('MultiKeySwitchExt') is not None:
            temp_model = ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExt()
            self.multi_key_switch_ext = temp_model.from_map(m['MultiKeySwitchExt'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')
        return self


class ImportRoomControlDevicesRequestLocationDevices(TeaModel):
    def __init__(
        self,
        devices: List[ImportRoomControlDevicesRequestLocationDevicesDevices] = None,
        location: str = None,
        location_name: str = None,
    ):
        self.devices = devices
        # This parameter is required.
        self.location = location
        self.location_name = location_name

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = ImportRoomControlDevicesRequestLocationDevicesDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        return self


class ImportRoomControlDevicesRequest(TeaModel):
    def __init__(
        self,
        enable_infrared_device_import: str = None,
        hotel_id: str = None,
        location_devices: List[ImportRoomControlDevicesRequestLocationDevices] = None,
        room_no: str = None,
    ):
        self.enable_infrared_device_import = enable_infrared_device_import
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.location_devices = location_devices
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        if self.location_devices:
            for k in self.location_devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_infrared_device_import is not None:
            result['EnableInfraredDeviceImport'] = self.enable_infrared_device_import
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        result['LocationDevices'] = []
        if self.location_devices is not None:
            for k in self.location_devices:
                result['LocationDevices'].append(k.to_map() if k else None)
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInfraredDeviceImport') is not None:
            self.enable_infrared_device_import = m.get('EnableInfraredDeviceImport')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        self.location_devices = []
        if m.get('LocationDevices') is not None:
            for k in m.get('LocationDevices'):
                temp_model = ImportRoomControlDevicesRequestLocationDevices()
                self.location_devices.append(temp_model.from_map(k))
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ImportRoomControlDevicesShrinkRequest(TeaModel):
    def __init__(
        self,
        enable_infrared_device_import: str = None,
        hotel_id: str = None,
        location_devices_shrink: str = None,
        room_no: str = None,
    ):
        self.enable_infrared_device_import = enable_infrared_device_import
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.location_devices_shrink = location_devices_shrink
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_infrared_device_import is not None:
            result['EnableInfraredDeviceImport'] = self.enable_infrared_device_import
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.location_devices_shrink is not None:
            result['LocationDevices'] = self.location_devices_shrink
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInfraredDeviceImport') is not None:
            self.enable_infrared_device_import = m.get('EnableInfraredDeviceImport')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('LocationDevices') is not None:
            self.location_devices_shrink = m.get('LocationDevices')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ImportRoomControlDevicesResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ImportRoomControlDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportRoomControlDevicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ImportRoomControlDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportRoomGenieScenesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ImportRoomGenieScenesRequestSceneListActionsAttributeValues(TeaModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
    ):
        # This parameter is required.
        self.attribute_name = attribute_name
        # This parameter is required.
        self.attribute_value = attribute_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        return self


class ImportRoomGenieScenesRequestSceneListActionsDevice(TeaModel):
    def __init__(
        self,
        category: str = None,
        device_index: int = None,
        device_number: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.category = category
        self.device_index = device_index
        # This parameter is required.
        self.device_number = device_number
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ImportRoomGenieScenesRequestSceneListActions(TeaModel):
    def __init__(
        self,
        attribute_values: List[ImportRoomGenieScenesRequestSceneListActionsAttributeValues] = None,
        device: ImportRoomGenieScenesRequestSceneListActionsDevice = None,
        reply: str = None,
        type: int = None,
    ):
        self.attribute_values = attribute_values
        self.device = device
        self.reply = reply
        self.type = type

    def validate(self):
        if self.attribute_values:
            for k in self.attribute_values:
                if k:
                    k.validate()
        if self.device:
            self.device.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AttributeValues'] = []
        if self.attribute_values is not None:
            for k in self.attribute_values:
                result['AttributeValues'].append(k.to_map() if k else None)
        if self.device is not None:
            result['Device'] = self.device.to_map()
        if self.reply is not None:
            result['Reply'] = self.reply
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_values = []
        if m.get('AttributeValues') is not None:
            for k in m.get('AttributeValues'):
                temp_model = ImportRoomGenieScenesRequestSceneListActionsAttributeValues()
                self.attribute_values.append(temp_model.from_map(k))
        if m.get('Device') is not None:
            temp_model = ImportRoomGenieScenesRequestSceneListActionsDevice()
            self.device = temp_model.from_map(m['Device'])
        if m.get('Reply') is not None:
            self.reply = m.get('Reply')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ImportRoomGenieScenesRequestSceneListTriggersAttributeValues(TeaModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
    ):
        # This parameter is required.
        self.attribute_name = attribute_name
        # This parameter is required.
        self.attribute_value = attribute_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        return self


class ImportRoomGenieScenesRequestSceneListTriggersDevice(TeaModel):
    def __init__(
        self,
        category: str = None,
        device_index: str = None,
        device_number: str = None,
    ):
        # This parameter is required.
        self.category = category
        self.device_index = device_index
        # This parameter is required.
        self.device_number = device_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        return self


class ImportRoomGenieScenesRequestSceneListTriggers(TeaModel):
    def __init__(
        self,
        attribute_values: List[ImportRoomGenieScenesRequestSceneListTriggersAttributeValues] = None,
        corpus_list: List[str] = None,
        device: ImportRoomGenieScenesRequestSceneListTriggersDevice = None,
        type: int = None,
    ):
        self.attribute_values = attribute_values
        self.corpus_list = corpus_list
        self.device = device
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.attribute_values:
            for k in self.attribute_values:
                if k:
                    k.validate()
        if self.device:
            self.device.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AttributeValues'] = []
        if self.attribute_values is not None:
            for k in self.attribute_values:
                result['AttributeValues'].append(k.to_map() if k else None)
        if self.corpus_list is not None:
            result['CorpusList'] = self.corpus_list
        if self.device is not None:
            result['Device'] = self.device.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_values = []
        if m.get('AttributeValues') is not None:
            for k in m.get('AttributeValues'):
                temp_model = ImportRoomGenieScenesRequestSceneListTriggersAttributeValues()
                self.attribute_values.append(temp_model.from_map(k))
        if m.get('CorpusList') is not None:
            self.corpus_list = m.get('CorpusList')
        if m.get('Device') is not None:
            temp_model = ImportRoomGenieScenesRequestSceneListTriggersDevice()
            self.device = temp_model.from_map(m['Device'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ImportRoomGenieScenesRequestSceneList(TeaModel):
    def __init__(
        self,
        actions: List[ImportRoomGenieScenesRequestSceneListActions] = None,
        description: str = None,
        display: bool = None,
        icon: str = None,
        scene_name: str = None,
        trigger_logical: int = None,
        triggers: List[ImportRoomGenieScenesRequestSceneListTriggers] = None,
    ):
        # This parameter is required.
        self.actions = actions
        self.description = description
        # This parameter is required.
        self.display = display
        self.icon = icon
        # This parameter is required.
        self.scene_name = scene_name
        # This parameter is required.
        self.trigger_logical = trigger_logical
        # This parameter is required.
        self.triggers = triggers

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.display is not None:
            result['Display'] = self.display
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.trigger_logical is not None:
            result['TriggerLogical'] = self.trigger_logical
        result['Triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['Triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = ImportRoomGenieScenesRequestSceneListActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('TriggerLogical') is not None:
            self.trigger_logical = m.get('TriggerLogical')
        self.triggers = []
        if m.get('Triggers') is not None:
            for k in m.get('Triggers'):
                temp_model = ImportRoomGenieScenesRequestSceneListTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class ImportRoomGenieScenesRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
        scene_list: List[ImportRoomGenieScenesRequestSceneList] = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no
        self.scene_list = scene_list

    def validate(self):
        if self.scene_list:
            for k in self.scene_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        result['SceneList'] = []
        if self.scene_list is not None:
            for k in self.scene_list:
                result['SceneList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        self.scene_list = []
        if m.get('SceneList') is not None:
            for k in m.get('SceneList'):
                temp_model = ImportRoomGenieScenesRequestSceneList()
                self.scene_list.append(temp_model.from_map(k))
        return self


class ImportRoomGenieScenesShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
        scene_list_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no
        self.scene_list_shrink = scene_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.scene_list_shrink is not None:
            result['SceneList'] = self.scene_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('SceneList') is not None:
            self.scene_list_shrink = m.get('SceneList')
        return self


class ImportRoomGenieScenesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ImportRoomGenieScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportRoomGenieScenesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ImportRoomGenieScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertHotelSceneBookItemHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class InsertHotelSceneBookItemRequestAddHotelSceneItemReq(TeaModel):
    def __init__(
        self,
        icon: str = None,
        name: str = None,
        price: int = None,
        type: str = None,
    ):
        # icon
        # 
        # This parameter is required.
        self.icon = icon
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.price = price
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InsertHotelSceneBookItemRequest(TeaModel):
    def __init__(
        self,
        add_hotel_scene_item_req: InsertHotelSceneBookItemRequestAddHotelSceneItemReq = None,
        hotel_id: str = None,
    ):
        # addHotelSceneItemReq
        # 
        # This parameter is required.
        self.add_hotel_scene_item_req = add_hotel_scene_item_req
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        if self.add_hotel_scene_item_req:
            self.add_hotel_scene_item_req.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_hotel_scene_item_req is not None:
            result['AddHotelSceneItemReq'] = self.add_hotel_scene_item_req.to_map()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddHotelSceneItemReq') is not None:
            temp_model = InsertHotelSceneBookItemRequestAddHotelSceneItemReq()
            self.add_hotel_scene_item_req = temp_model.from_map(m['AddHotelSceneItemReq'])
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class InsertHotelSceneBookItemShrinkRequest(TeaModel):
    def __init__(
        self,
        add_hotel_scene_item_req_shrink: str = None,
        hotel_id: str = None,
    ):
        # addHotelSceneItemReq
        # 
        # This parameter is required.
        self.add_hotel_scene_item_req_shrink = add_hotel_scene_item_req_shrink
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_hotel_scene_item_req_shrink is not None:
            result['AddHotelSceneItemReq'] = self.add_hotel_scene_item_req_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddHotelSceneItemReq') is not None:
            self.add_hotel_scene_item_req_shrink = m.get('AddHotelSceneItemReq')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class InsertHotelSceneBookItemResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        # RequestId
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InsertHotelSceneBookItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertHotelSceneBookItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = InsertHotelSceneBookItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeRobotPushHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class InvokeRobotPushRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        push_type: str = None,
        room_name: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.push_type = push_type
        self.room_name = room_name
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.room_name is not None:
            result['RoomName'] = self.room_name
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class InvokeRobotPushResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class InvokeRobotPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvokeRobotPushResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = InvokeRobotPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllProvincesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListAllProvincesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: List[str] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListAllProvincesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllProvincesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAllProvincesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCitiesByProvinceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListCitiesByProvinceRequest(TeaModel):
    def __init__(
        self,
        province: str = None,
    ):
        # This parameter is required.
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class ListCitiesByProvinceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: List[str] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListCitiesByProvinceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCitiesByProvinceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListCitiesByProvinceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomQAHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListCustomQARequestPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCustomQARequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        keyword: str = None,
        page: ListCustomQARequestPage = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.keyword = keyword
        # This parameter is required.
        self.page = page

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page is not None:
            result['Page'] = self.page.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            temp_model = ListCustomQARequestPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListCustomQAShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        keyword: str = None,
        page_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.keyword = keyword
        # This parameter is required.
        self.page_shrink = page_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        return self


class ListCustomQAResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListCustomQAResponseBodyResult(TeaModel):
    def __init__(
        self,
        answers: str = None,
        create_time: str = None,
        custom_qaid: str = None,
        hotel_id: str = None,
        key_words: str = None,
        major_question: str = None,
        status: int = None,
        supplementary_question: str = None,
        update_time: str = None,
    ):
        self.answers = answers
        self.create_time = create_time
        self.custom_qaid = custom_qaid
        self.hotel_id = hotel_id
        self.key_words = key_words
        self.major_question = major_question
        self.status = status
        self.supplementary_question = supplementary_question
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers is not None:
            result['Answers'] = self.answers
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_qaid is not None:
            result['CustomQAId'] = self.custom_qaid
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.status is not None:
            result['Status'] = self.status
        if self.supplementary_question is not None:
            result['SupplementaryQuestion'] = self.supplementary_question
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomQAId') is not None:
            self.custom_qaid = m.get('CustomQAId')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementaryQuestion') is not None:
            self.supplementary_question = m.get('SupplementaryQuestion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListCustomQAResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        page: ListCustomQAResponseBodyPage = None,
        request_id: str = None,
        result: List[ListCustomQAResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.message = message
        self.page = page
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = ListCustomQAResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCustomQAResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListCustomQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomQAResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListCustomQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDialogueTemplateHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListDialogueTemplateRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
    ):
        # hotelId
        # 
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class ListDialogueTemplateResponseBodyResultTemplateDetailFirstDialogueTemplate(TeaModel):
    def __init__(
        self,
        nonzero_price_yes_answer: str = None,
        zero_price_no_answer: str = None,
        zero_price_yes_answer: str = None,
    ):
        self.nonzero_price_yes_answer = nonzero_price_yes_answer
        self.zero_price_no_answer = zero_price_no_answer
        self.zero_price_yes_answer = zero_price_yes_answer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nonzero_price_yes_answer is not None:
            result['NonzeroPriceYesAnswer'] = self.nonzero_price_yes_answer
        if self.zero_price_no_answer is not None:
            result['ZeroPriceNoAnswer'] = self.zero_price_no_answer
        if self.zero_price_yes_answer is not None:
            result['ZeroPriceYesAnswer'] = self.zero_price_yes_answer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonzeroPriceYesAnswer') is not None:
            self.nonzero_price_yes_answer = m.get('NonzeroPriceYesAnswer')
        if m.get('ZeroPriceNoAnswer') is not None:
            self.zero_price_no_answer = m.get('ZeroPriceNoAnswer')
        if m.get('ZeroPriceYesAnswer') is not None:
            self.zero_price_yes_answer = m.get('ZeroPriceYesAnswer')
        return self


class ListDialogueTemplateResponseBodyResultTemplateDetailSecondDialogueTemplate(TeaModel):
    def __init__(
        self,
        nonzero_price_no_answer: str = None,
        nonzero_price_yes_answer: str = None,
    ):
        self.nonzero_price_no_answer = nonzero_price_no_answer
        self.nonzero_price_yes_answer = nonzero_price_yes_answer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nonzero_price_no_answer is not None:
            result['NonzeroPriceNoAnswer'] = self.nonzero_price_no_answer
        if self.nonzero_price_yes_answer is not None:
            result['NonzeroPriceYesAnswer'] = self.nonzero_price_yes_answer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonzeroPriceNoAnswer') is not None:
            self.nonzero_price_no_answer = m.get('NonzeroPriceNoAnswer')
        if m.get('NonzeroPriceYesAnswer') is not None:
            self.nonzero_price_yes_answer = m.get('NonzeroPriceYesAnswer')
        return self


class ListDialogueTemplateResponseBodyResultTemplateDetail(TeaModel):
    def __init__(
        self,
        first_dialogue_template: ListDialogueTemplateResponseBodyResultTemplateDetailFirstDialogueTemplate = None,
        second_dialogue_template: ListDialogueTemplateResponseBodyResultTemplateDetailSecondDialogueTemplate = None,
    ):
        self.first_dialogue_template = first_dialogue_template
        self.second_dialogue_template = second_dialogue_template

    def validate(self):
        if self.first_dialogue_template:
            self.first_dialogue_template.validate()
        if self.second_dialogue_template:
            self.second_dialogue_template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_dialogue_template is not None:
            result['FirstDialogueTemplate'] = self.first_dialogue_template.to_map()
        if self.second_dialogue_template is not None:
            result['SecondDialogueTemplate'] = self.second_dialogue_template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstDialogueTemplate') is not None:
            temp_model = ListDialogueTemplateResponseBodyResultTemplateDetailFirstDialogueTemplate()
            self.first_dialogue_template = temp_model.from_map(m['FirstDialogueTemplate'])
        if m.get('SecondDialogueTemplate') is not None:
            temp_model = ListDialogueTemplateResponseBodyResultTemplateDetailSecondDialogueTemplate()
            self.second_dialogue_template = temp_model.from_map(m['SecondDialogueTemplate'])
        return self


class ListDialogueTemplateResponseBodyResult(TeaModel):
    def __init__(
        self,
        template_detail: ListDialogueTemplateResponseBodyResultTemplateDetail = None,
        template_id: int = None,
        template_name: str = None,
        type: str = None,
    ):
        self.template_detail = template_detail
        self.template_id = template_id
        self.template_name = template_name
        self.type = type

    def validate(self):
        if self.template_detail:
            self.template_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_detail is not None:
            result['TemplateDetail'] = self.template_detail.to_map()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateDetail') is not None:
            temp_model = ListDialogueTemplateResponseBodyResultTemplateDetail()
            self.template_detail = temp_model.from_map(m['TemplateDetail'])
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDialogueTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListDialogueTemplateResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        # RequestId
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDialogueTemplateResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDialogueTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDialogueTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListDialogueTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelAlarmHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelAlarmRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        rooms: List[str] = None,
    ):
        self.hotel_id = hotel_id
        self.rooms = rooms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.rooms is not None:
            result['Rooms'] = self.rooms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Rooms') is not None:
            self.rooms = m.get('Rooms')
        return self


class ListHotelAlarmShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        rooms_shrink: str = None,
    ):
        self.hotel_id = hotel_id
        self.rooms_shrink = rooms_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.rooms_shrink is not None:
            result['Rooms'] = self.rooms_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Rooms') is not None:
            self.rooms_shrink = m.get('Rooms')
        return self


class ListHotelAlarmResponseBodyResultScheduleInfoOnce(TeaModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class ListHotelAlarmResponseBodyResultScheduleInfoWeekly(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class ListHotelAlarmResponseBodyResultScheduleInfo(TeaModel):
    def __init__(
        self,
        once: ListHotelAlarmResponseBodyResultScheduleInfoOnce = None,
        type: str = None,
        weekly: ListHotelAlarmResponseBodyResultScheduleInfoWeekly = None,
    ):
        self.once = once
        # ONCE, WEEKLY
        self.type = type
        self.weekly = weekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = ListHotelAlarmResponseBodyResultScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = ListHotelAlarmResponseBodyResultScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class ListHotelAlarmResponseBodyResult(TeaModel):
    def __init__(
        self,
        alarm_id: int = None,
        device_open_id: str = None,
        schedule_info: ListHotelAlarmResponseBodyResultScheduleInfo = None,
        user_open_id: str = None,
    ):
        self.alarm_id = alarm_id
        self.device_open_id = device_open_id
        self.schedule_info = schedule_info
        self.user_open_id = user_open_id

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        if m.get('ScheduleInfo') is not None:
            temp_model = ListHotelAlarmResponseBodyResultScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class ListHotelAlarmResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: List[ListHotelAlarmResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelAlarmResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListHotelAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelControlDeviceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelControlDeviceRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListHotelControlDeviceRequest(TeaModel):
    def __init__(
        self,
        user_info: ListHotelControlDeviceRequestUserInfo = None,
    ):
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = ListHotelControlDeviceRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListHotelControlDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        user_info_shrink: str = None,
    ):
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListHotelControlDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[Dict[str, str]] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ListHotelControlDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelControlDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelControlDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelInfoResponseBodyResultAuthAccount(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListHotelInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        auth_account: List[ListHotelInfoResponseBodyResultAuthAccount] = None,
        hotel_address: str = None,
        hotel_id: str = None,
        hotel_name: str = None,
    ):
        self.auth_account = auth_account
        self.hotel_address = hotel_address
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name

    def validate(self):
        if self.auth_account:
            for k in self.auth_account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthAccount'] = []
        if self.auth_account is not None:
            for k in self.auth_account:
                result['AuthAccount'].append(k.to_map() if k else None)
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_account = []
        if m.get('AuthAccount') is not None:
            for k in m.get('AuthAccount'):
                temp_model = ListHotelInfoResponseBodyResultAuthAccount()
                self.auth_account.append(temp_model.from_map(k))
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        return self


class ListHotelInfoResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: List[ListHotelInfoResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListHotelInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelMessageTemplateHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelMessageTemplateResponseBodyResult(TeaModel):
    def __init__(
        self,
        audit_mark: str = None,
        audit_status: str = None,
        template_detail: str = None,
        template_id: int = None,
        template_name: str = None,
    ):
        self.audit_mark = audit_mark
        self.audit_status = audit_status
        self.template_detail = template_detail
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_mark is not None:
            result['AuditMark'] = self.audit_mark
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.template_detail is not None:
            result['TemplateDetail'] = self.template_detail
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditMark') is not None:
            self.audit_mark = m.get('AuditMark')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('TemplateDetail') is not None:
            self.template_detail = m.get('TemplateDetail')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListHotelMessageTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListHotelMessageTemplateResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelMessageTemplateResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListHotelMessageTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelMessageTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelMessageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelOrderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelOrderRequestPayloadPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHotelOrderRequestPayload(TeaModel):
    def __init__(
        self,
        page: ListHotelOrderRequestPayloadPage = None,
    ):
        # This parameter is required.
        self.page = page

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = ListHotelOrderRequestPayloadPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListHotelOrderRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListHotelOrderRequest(TeaModel):
    def __init__(
        self,
        payload: ListHotelOrderRequestPayload = None,
        user_info: ListHotelOrderRequestUserInfo = None,
    ):
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = ListHotelOrderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListHotelOrderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListHotelOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListHotelOrderResponseBodyPage(TeaModel):
    def __init__(
        self,
        has_next: bool = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
        total_page: int = None,
    ):
        self.has_next = has_next
        self.page_number = page_number
        self.page_size = page_size
        self.total = total
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListHotelOrderResponseBodyResult(TeaModel):
    def __init__(
        self,
        amt: int = None,
        apply_amt: int = None,
        delivery_method: str = None,
        delivery_room_name: str = None,
        delivery_time: int = None,
        gmt_create: int = None,
        icon: str = None,
        item_id: int = None,
        item_type: str = None,
        name: str = None,
        order_no: str = None,
        order_status: str = None,
        payment_method: str = None,
        quantity: int = None,
        room_no: str = None,
        start_time: int = None,
        status: str = None,
        sum_amt: int = None,
        type: str = None,
        type_icon_url: str = None,
        type_name: str = None,
    ):
        self.amt = amt
        self.apply_amt = apply_amt
        self.delivery_method = delivery_method
        self.delivery_room_name = delivery_room_name
        self.delivery_time = delivery_time
        self.gmt_create = gmt_create
        self.icon = icon
        self.item_id = item_id
        self.item_type = item_type
        self.name = name
        self.order_no = order_no
        self.order_status = order_status
        self.payment_method = payment_method
        self.quantity = quantity
        self.room_no = room_no
        self.start_time = start_time
        self.status = status
        self.sum_amt = sum_amt
        self.type = type
        self.type_icon_url = type_icon_url
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amt is not None:
            result['Amt'] = self.amt
        if self.apply_amt is not None:
            result['ApplyAmt'] = self.apply_amt
        if self.delivery_method is not None:
            result['DeliveryMethod'] = self.delivery_method
        if self.delivery_room_name is not None:
            result['DeliveryRoomName'] = self.delivery_room_name
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.name is not None:
            result['Name'] = self.name
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.sum_amt is not None:
            result['SumAmt'] = self.sum_amt
        if self.type is not None:
            result['Type'] = self.type
        if self.type_icon_url is not None:
            result['TypeIconUrl'] = self.type_icon_url
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amt') is not None:
            self.amt = m.get('Amt')
        if m.get('ApplyAmt') is not None:
            self.apply_amt = m.get('ApplyAmt')
        if m.get('DeliveryMethod') is not None:
            self.delivery_method = m.get('DeliveryMethod')
        if m.get('DeliveryRoomName') is not None:
            self.delivery_room_name = m.get('DeliveryRoomName')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SumAmt') is not None:
            self.sum_amt = m.get('SumAmt')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeIconUrl') is not None:
            self.type_icon_url = m.get('TypeIconUrl')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListHotelOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page: ListHotelOrderResponseBodyPage = None,
        request_id: str = None,
        result: List[ListHotelOrderResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.page = page
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = ListHotelOrderResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelOrderResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListHotelOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelRoomsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelRoomsRequestHotelAdminRoom(TeaModel):
    def __init__(
        self,
        room_no: str = None,
    ):
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ListHotelRoomsRequest(TeaModel):
    def __init__(
        self,
        hotel_admin_room: ListHotelRoomsRequestHotelAdminRoom = None,
        hotel_id: str = None,
    ):
        self.hotel_admin_room = hotel_admin_room
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        if self.hotel_admin_room:
            self.hotel_admin_room.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_admin_room is not None:
            result['HotelAdminRoom'] = self.hotel_admin_room.to_map()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelAdminRoom') is not None:
            temp_model = ListHotelRoomsRequestHotelAdminRoom()
            self.hotel_admin_room = temp_model.from_map(m['HotelAdminRoom'])
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class ListHotelRoomsShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_admin_room_shrink: str = None,
        hotel_id: str = None,
    ):
        self.hotel_admin_room_shrink = hotel_admin_room_shrink
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_admin_room_shrink is not None:
            result['HotelAdminRoom'] = self.hotel_admin_room_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelAdminRoom') is not None:
            self.hotel_admin_room_shrink = m.get('HotelAdminRoom')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class ListHotelRoomsResponseBodyResult(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
    ):
        self.hotel_id = hotel_id
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class ListHotelRoomsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListHotelRoomsResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelRoomsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListHotelRoomsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelRoomsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelRoomsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelSceneBookItemsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelSceneBookItemsRequestPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHotelSceneBookItemsRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        page: ListHotelSceneBookItemsRequestPage = None,
        type: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Page') is not None:
            temp_model = ListHotelSceneBookItemsRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelSceneBookItemsShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        page_shrink: str = None,
        type: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.page_shrink = page_shrink
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelSceneBookItemsResponseBodyResultPage(TeaModel):
    def __init__(
        self,
        has_next: bool = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
        total_page: int = None,
    ):
        self.has_next = has_next
        self.page_number = page_number
        self.page_size = page_size
        self.total = total
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListHotelSceneBookItemsResponseBodyResultSceneItemList(TeaModel):
    def __init__(
        self,
        icon: str = None,
        id: int = None,
        name: str = None,
        price: int = None,
        status: str = None,
        type: str = None,
        update_time: int = None,
    ):
        self.icon = icon
        self.id = id
        self.name = name
        self.price = price
        self.status = status
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListHotelSceneBookItemsResponseBodyResult(TeaModel):
    def __init__(
        self,
        page: ListHotelSceneBookItemsResponseBodyResultPage = None,
        scene_item_list: List[ListHotelSceneBookItemsResponseBodyResultSceneItemList] = None,
    ):
        self.page = page
        self.scene_item_list = scene_item_list

    def validate(self):
        if self.page:
            self.page.validate()
        if self.scene_item_list:
            for k in self.scene_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        result['SceneItemList'] = []
        if self.scene_item_list is not None:
            for k in self.scene_item_list:
                result['SceneItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = ListHotelSceneBookItemsResponseBodyResultPage()
            self.page = temp_model.from_map(m['Page'])
        self.scene_item_list = []
        if m.get('SceneItemList') is not None:
            for k in m.get('SceneItemList'):
                temp_model = ListHotelSceneBookItemsResponseBodyResultSceneItemList()
                self.scene_item_list.append(temp_model.from_map(k))
        return self


class ListHotelSceneBookItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListHotelSceneBookItemsResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListHotelSceneBookItemsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListHotelSceneBookItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelSceneBookItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelSceneBookItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelSceneItemHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelSceneItemRequestPayload(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelSceneItemRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListHotelSceneItemRequest(TeaModel):
    def __init__(
        self,
        payload: ListHotelSceneItemRequestPayload = None,
        user_info: ListHotelSceneItemRequestUserInfo = None,
    ):
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = ListHotelSceneItemRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListHotelSceneItemRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListHotelSceneItemShrinkRequest(TeaModel):
    def __init__(
        self,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListHotelSceneItemResponseBodyPage(TeaModel):
    def __init__(
        self,
        has_next: bool = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
        total_page: int = None,
    ):
        self.has_next = has_next
        self.page_number = page_number
        self.page_size = page_size
        self.total = total
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListHotelSceneItemResponseBodyResultSecondCategoryListItemList(TeaModel):
    def __init__(
        self,
        category: str = None,
        icon: str = None,
        id: str = None,
        name: str = None,
        price: int = None,
        residue_limit: int = None,
        status: str = None,
        type: str = None,
    ):
        self.category = category
        self.icon = icon
        self.id = id
        self.name = name
        self.price = price
        self.residue_limit = residue_limit
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        if self.residue_limit is not None:
            result['ResidueLimit'] = self.residue_limit
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('ResidueLimit') is not None:
            self.residue_limit = m.get('ResidueLimit')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelSceneItemResponseBodyResultSecondCategoryList(TeaModel):
    def __init__(
        self,
        item_list: List[ListHotelSceneItemResponseBodyResultSecondCategoryListItemList] = None,
        second_category_name: str = None,
    ):
        self.item_list = item_list
        self.second_category_name = second_category_name

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = ListHotelSceneItemResponseBodyResultSecondCategoryListItemList()
                self.item_list.append(temp_model.from_map(k))
        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')
        return self


class ListHotelSceneItemResponseBodyResult(TeaModel):
    def __init__(
        self,
        second_category_list: List[ListHotelSceneItemResponseBodyResultSecondCategoryList] = None,
    ):
        self.second_category_list = second_category_list

    def validate(self):
        if self.second_category_list:
            for k in self.second_category_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecondCategoryList'] = []
        if self.second_category_list is not None:
            for k in self.second_category_list:
                result['SecondCategoryList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.second_category_list = []
        if m.get('SecondCategoryList') is not None:
            for k in m.get('SecondCategoryList'):
                temp_model = ListHotelSceneItemResponseBodyResultSecondCategoryList()
                self.second_category_list.append(temp_model.from_map(k))
        return self


class ListHotelSceneItemResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page: ListHotelSceneItemResponseBodyPage = None,
        request_id: str = None,
        result: ListHotelSceneItemResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.page = page
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = ListHotelSceneItemResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListHotelSceneItemResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListHotelSceneItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelSceneItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelSceneItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelSceneItemsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelSceneItemsRequestListHotelSceneReqPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHotelSceneItemsRequestListHotelSceneReq(TeaModel):
    def __init__(
        self,
        category: str = None,
        keywords: str = None,
        page: ListHotelSceneItemsRequestListHotelSceneReqPage = None,
        status: str = None,
        type: str = None,
    ):
        self.category = category
        self.keywords = keywords
        # This parameter is required.
        self.page = page
        self.status = status
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Page') is not None:
            temp_model = ListHotelSceneItemsRequestListHotelSceneReqPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelSceneItemsRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        list_hotel_scene_req: ListHotelSceneItemsRequestListHotelSceneReq = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # ListHotelSceneReq
        # 
        # This parameter is required.
        self.list_hotel_scene_req = list_hotel_scene_req

    def validate(self):
        if self.list_hotel_scene_req:
            self.list_hotel_scene_req.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.list_hotel_scene_req is not None:
            result['ListHotelSceneReq'] = self.list_hotel_scene_req.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ListHotelSceneReq') is not None:
            temp_model = ListHotelSceneItemsRequestListHotelSceneReq()
            self.list_hotel_scene_req = temp_model.from_map(m['ListHotelSceneReq'])
        return self


class ListHotelSceneItemsShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        list_hotel_scene_req_shrink: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # ListHotelSceneReq
        # 
        # This parameter is required.
        self.list_hotel_scene_req_shrink = list_hotel_scene_req_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.list_hotel_scene_req_shrink is not None:
            result['ListHotelSceneReq'] = self.list_hotel_scene_req_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ListHotelSceneReq') is not None:
            self.list_hotel_scene_req_shrink = m.get('ListHotelSceneReq')
        return self


class ListHotelSceneItemsResponseBodyResultPage(TeaModel):
    def __init__(
        self,
        has_next: bool = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
        total_page: int = None,
    ):
        self.has_next = has_next
        self.page_number = page_number
        self.page_size = page_size
        self.total = total
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListHotelSceneItemsResponseBodyResultSceneItemList(TeaModel):
    def __init__(
        self,
        beyond_limit_reply: str = None,
        category: str = None,
        delivery_method: str = None,
        icon: str = None,
        id: int = None,
        limit_number: int = None,
        limit_switch: int = None,
        name: str = None,
        payment_method: str = None,
        price: int = None,
        robot_name: str = None,
        status: str = None,
        type: str = None,
        update_time: int = None,
    ):
        self.beyond_limit_reply = beyond_limit_reply
        self.category = category
        self.delivery_method = delivery_method
        self.icon = icon
        # id
        self.id = id
        self.limit_number = limit_number
        self.limit_switch = limit_switch
        self.name = name
        self.payment_method = payment_method
        self.price = price
        self.robot_name = robot_name
        self.status = status
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beyond_limit_reply is not None:
            result['BeyondLimitReply'] = self.beyond_limit_reply
        if self.category is not None:
            result['Category'] = self.category
        if self.delivery_method is not None:
            result['DeliveryMethod'] = self.delivery_method
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.limit_number is not None:
            result['LimitNumber'] = self.limit_number
        if self.limit_switch is not None:
            result['LimitSwitch'] = self.limit_switch
        if self.name is not None:
            result['Name'] = self.name
        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method
        if self.price is not None:
            result['Price'] = self.price
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeyondLimitReply') is not None:
            self.beyond_limit_reply = m.get('BeyondLimitReply')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeliveryMethod') is not None:
            self.delivery_method = m.get('DeliveryMethod')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LimitNumber') is not None:
            self.limit_number = m.get('LimitNumber')
        if m.get('LimitSwitch') is not None:
            self.limit_switch = m.get('LimitSwitch')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListHotelSceneItemsResponseBodyResult(TeaModel):
    def __init__(
        self,
        page: ListHotelSceneItemsResponseBodyResultPage = None,
        scene_item_list: List[ListHotelSceneItemsResponseBodyResultSceneItemList] = None,
    ):
        self.page = page
        self.scene_item_list = scene_item_list

    def validate(self):
        if self.page:
            self.page.validate()
        if self.scene_item_list:
            for k in self.scene_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        result['SceneItemList'] = []
        if self.scene_item_list is not None:
            for k in self.scene_item_list:
                result['SceneItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = ListHotelSceneItemsResponseBodyResultPage()
            self.page = temp_model.from_map(m['Page'])
        self.scene_item_list = []
        if m.get('SceneItemList') is not None:
            for k in m.get('SceneItemList'):
                temp_model = ListHotelSceneItemsResponseBodyResultSceneItemList()
                self.scene_item_list.append(temp_model.from_map(k))
        return self


class ListHotelSceneItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListHotelSceneItemsResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListHotelSceneItemsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListHotelSceneItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelSceneItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelSceneItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelServiceCategoryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelServiceCategoryRequestPayload(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelServiceCategoryRequest(TeaModel):
    def __init__(
        self,
        payload: ListHotelServiceCategoryRequestPayload = None,
    ):
        # This parameter is required.
        self.payload = payload

    def validate(self):
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = ListHotelServiceCategoryRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        return self


class ListHotelServiceCategoryShrinkRequest(TeaModel):
    def __init__(
        self,
        payload_shrink: str = None,
    ):
        # This parameter is required.
        self.payload_shrink = payload_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        return self


class ListHotelServiceCategoryResponseBodyResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        desc: str = None,
        icon: str = None,
        name: str = None,
        type: str = None,
    ):
        self.code = code
        self.desc = desc
        self.icon = icon
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListHotelServiceCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListHotelServiceCategoryResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListHotelServiceCategoryResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListHotelServiceCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelServiceCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelServiceCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotelsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListHotelsRequestHotelRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
    ):
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class ListHotelsRequestPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHotelsRequest(TeaModel):
    def __init__(
        self,
        hotel_request: ListHotelsRequestHotelRequest = None,
        page: ListHotelsRequestPage = None,
        status: int = None,
    ):
        self.hotel_request = hotel_request
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.status = status

    def validate(self):
        if self.hotel_request:
            self.hotel_request.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_request is not None:
            result['HotelRequest'] = self.hotel_request.to_map()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelRequest') is not None:
            temp_model = ListHotelsRequestHotelRequest()
            self.hotel_request = temp_model.from_map(m['HotelRequest'])
        if m.get('Page') is not None:
            temp_model = ListHotelsRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListHotelsShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_request_shrink: str = None,
        page_shrink: str = None,
        status: int = None,
    ):
        self.hotel_request_shrink = hotel_request_shrink
        # This parameter is required.
        self.page_shrink = page_shrink
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_request_shrink is not None:
            result['HotelRequest'] = self.hotel_request_shrink
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelRequest') is not None:
            self.hotel_request_shrink = m.get('HotelRequest')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListHotelsResponseBodyResultHotelInfoList(TeaModel):
    def __init__(
        self,
        account_names: List[str] = None,
        create_time: int = None,
        hotel_address: str = None,
        hotel_id: str = None,
        hotel_name: str = None,
        industry_type: str = None,
        phone_number: str = None,
        related_product_name: str = None,
        room_num: int = None,
        status: int = None,
    ):
        self.account_names = account_names
        self.create_time = create_time
        self.hotel_address = hotel_address
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.industry_type = industry_type
        self.phone_number = phone_number
        self.related_product_name = related_product_name
        self.room_num = room_num
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_names is not None:
            result['AccountNames'] = self.account_names
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.industry_type is not None:
            result['IndustryType'] = self.industry_type
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.related_product_name is not None:
            result['RelatedProductName'] = self.related_product_name
        if self.room_num is not None:
            result['RoomNum'] = self.room_num
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNames') is not None:
            self.account_names = m.get('AccountNames')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('IndustryType') is not None:
            self.industry_type = m.get('IndustryType')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RelatedProductName') is not None:
            self.related_product_name = m.get('RelatedProductName')
        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListHotelsResponseBodyResultPage(TeaModel):
    def __init__(
        self,
        has_next: bool = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
        total_page: int = None,
    ):
        self.has_next = has_next
        self.page_number = page_number
        self.page_size = page_size
        self.total = total
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListHotelsResponseBodyResult(TeaModel):
    def __init__(
        self,
        hotel_info_list: List[ListHotelsResponseBodyResultHotelInfoList] = None,
        page: ListHotelsResponseBodyResultPage = None,
    ):
        self.hotel_info_list = hotel_info_list
        self.page = page

    def validate(self):
        if self.hotel_info_list:
            for k in self.hotel_info_list:
                if k:
                    k.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotelInfoList'] = []
        if self.hotel_info_list is not None:
            for k in self.hotel_info_list:
                result['HotelInfoList'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hotel_info_list = []
        if m.get('HotelInfoList') is not None:
            for k in m.get('HotelInfoList'):
                temp_model = ListHotelsResponseBodyResultHotelInfoList()
                self.hotel_info_list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            temp_model = ListHotelsResponseBodyResultPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListHotelsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListHotelsResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # RequestId
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListHotelsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListHotelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHotelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInfraredDeviceBrandsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListInfraredDeviceBrandsRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        service_provider: str = None,
    ):
        # This parameter is required.
        self.category = category
        self.service_provider = service_provider

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')
        return self


class ListInfraredDeviceBrandsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: Dict[str, List[str]] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListInfraredDeviceBrandsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInfraredDeviceBrandsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListInfraredDeviceBrandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInfraredRemoteControllersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListInfraredRemoteControllersRequest(TeaModel):
    def __init__(
        self,
        brand: str = None,
        category: str = None,
        city: str = None,
        hotel_id: str = None,
        province: str = None,
        service_provider: str = None,
    ):
        self.brand = brand
        # This parameter is required.
        self.category = category
        self.city = city
        # This parameter is required.
        self.hotel_id = hotel_id
        self.province = province
        self.service_provider = service_provider

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.category is not None:
            result['Category'] = self.category
        if self.city is not None:
            result['City'] = self.city
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.province is not None:
            result['Province'] = self.province
        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')
        return self


class ListInfraredRemoteControllersResponseBodyResult(TeaModel):
    def __init__(
        self,
        index: int = None,
        rid: int = None,
        version: str = None,
    ):
        self.index = index
        self.rid = rid
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListInfraredRemoteControllersResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: List[ListInfraredRemoteControllersResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListInfraredRemoteControllersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListInfraredRemoteControllersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInfraredRemoteControllersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListInfraredRemoteControllersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSTBServiceProvidersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListSTBServiceProvidersRequest(TeaModel):
    def __init__(
        self,
        city: str = None,
        province: str = None,
    ):
        # This parameter is required.
        self.city = city
        # This parameter is required.
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class ListSTBServiceProvidersResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: Dict[str, List[str]] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListSTBServiceProvidersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSTBServiceProvidersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListSTBServiceProvidersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSceneCategoryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListSceneCategoryRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        type: str = None,
    ):
        # hotelId
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListSceneCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.code = code
        self.message = message
        # RequestId
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ListSceneCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSceneCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListSceneCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceQAHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListServiceQARequestPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListServiceQARequest(TeaModel):
    def __init__(
        self,
        active: bool = None,
        hotel_id: str = None,
        keyword: str = None,
        page: ListServiceQARequestPage = None,
    ):
        self.active = active
        # This parameter is required.
        self.hotel_id = hotel_id
        self.keyword = keyword
        self.page = page

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page is not None:
            result['Page'] = self.page.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            temp_model = ListServiceQARequestPage()
            self.page = temp_model.from_map(m['Page'])
        return self


class ListServiceQAShrinkRequest(TeaModel):
    def __init__(
        self,
        active: bool = None,
        hotel_id: str = None,
        keyword: str = None,
        page_shrink: str = None,
    ):
        self.active = active
        # This parameter is required.
        self.hotel_id = hotel_id
        self.keyword = keyword
        self.page_shrink = page_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        return self


class ListServiceQAResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListServiceQAResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        answer: str = None,
        gmt_modified: str = None,
        question: str = None,
        service_qaid: int = None,
        templates: str = None,
    ):
        self.active = active
        self.answer = answer
        self.gmt_modified = gmt_modified
        self.question = question
        self.service_qaid = service_qaid
        self.templates = templates

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.question is not None:
            result['Question'] = self.question
        if self.service_qaid is not None:
            result['ServiceQAId'] = self.service_qaid
        if self.templates is not None:
            result['Templates'] = self.templates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('ServiceQAId') is not None:
            self.service_qaid = m.get('ServiceQAId')
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        return self


class ListServiceQAResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        page: ListServiceQAResponseBodyPage = None,
        request_id: str = None,
        result: List[ListServiceQAResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.message = message
        self.page = page
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = ListServiceQAResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListServiceQAResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListServiceQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceQAResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListServiceQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTicketsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListTicketsRequestPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTicketsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        hotel_id: str = None,
        is_desc: bool = None,
        is_need_callback: bool = None,
        is_need_charges: bool = None,
        page: ListTicketsRequestPage = None,
        room_no: str = None,
        sort_field: str = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.hotel_id = hotel_id
        self.is_desc = is_desc
        self.is_need_callback = is_need_callback
        self.is_need_charges = is_need_charges
        self.page = page
        self.room_no = room_no
        self.sort_field = sort_field
        self.start_time = start_time
        self.status = status
        self.type = type

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.is_desc is not None:
            result['IsDesc'] = self.is_desc
        if self.is_need_callback is not None:
            result['IsNeedCallback'] = self.is_need_callback
        if self.is_need_charges is not None:
            result['IsNeedCharges'] = self.is_need_charges
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('IsDesc') is not None:
            self.is_desc = m.get('IsDesc')
        if m.get('IsNeedCallback') is not None:
            self.is_need_callback = m.get('IsNeedCallback')
        if m.get('IsNeedCharges') is not None:
            self.is_need_charges = m.get('IsNeedCharges')
        if m.get('Page') is not None:
            temp_model = ListTicketsRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTicketsShrinkRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        hotel_id: str = None,
        is_desc: bool = None,
        is_need_callback: bool = None,
        is_need_charges: bool = None,
        page_shrink: str = None,
        room_no: str = None,
        sort_field: str = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.hotel_id = hotel_id
        self.is_desc = is_desc
        self.is_need_callback = is_need_callback
        self.is_need_charges = is_need_charges
        self.page_shrink = page_shrink
        self.room_no = room_no
        self.sort_field = sort_field
        self.start_time = start_time
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.is_desc is not None:
            result['IsDesc'] = self.is_desc
        if self.is_need_callback is not None:
            result['IsNeedCallback'] = self.is_need_callback
        if self.is_need_charges is not None:
            result['IsNeedCharges'] = self.is_need_charges
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('IsDesc') is not None:
            self.is_desc = m.get('IsDesc')
        if m.get('IsNeedCallback') is not None:
            self.is_need_callback = m.get('IsNeedCallback')
        if m.get('IsNeedCharges') is not None:
            self.is_need_charges = m.get('IsNeedCharges')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTicketsResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListTicketsResponseBodyResultDialogs(TeaModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
    ):
        self.answer = answer
        self.question = question

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.question is not None:
            result['Question'] = self.question
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        return self


class ListTicketsResponseBodyResult(TeaModel):
    def __init__(
        self,
        action: bool = None,
        assigned_handler: str = None,
        charges_remark: str = None,
        complete_remark: str = None,
        dialogs: List[ListTicketsResponseBodyResultDialogs] = None,
        gmt_called: str = None,
        gmt_create: str = None,
        gmt_delayed: str = None,
        gmt_modified: str = None,
        group_key: str = None,
        id: int = None,
        is_accepted_charges: bool = None,
        is_delayed: bool = None,
        is_need_callback: bool = None,
        is_need_charges: bool = None,
        operations: List[Dict[str, Any]] = None,
        remark: str = None,
        room_no: str = None,
        status: str = None,
        type: str = None,
    ):
        self.action = action
        self.assigned_handler = assigned_handler
        self.charges_remark = charges_remark
        self.complete_remark = complete_remark
        self.dialogs = dialogs
        self.gmt_called = gmt_called
        self.gmt_create = gmt_create
        self.gmt_delayed = gmt_delayed
        self.gmt_modified = gmt_modified
        self.group_key = group_key
        self.id = id
        self.is_accepted_charges = is_accepted_charges
        self.is_delayed = is_delayed
        self.is_need_callback = is_need_callback
        self.is_need_charges = is_need_charges
        self.operations = operations
        self.remark = remark
        self.room_no = room_no
        self.status = status
        self.type = type

    def validate(self):
        if self.dialogs:
            for k in self.dialogs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.assigned_handler is not None:
            result['AssignedHandler'] = self.assigned_handler
        if self.charges_remark is not None:
            result['ChargesRemark'] = self.charges_remark
        if self.complete_remark is not None:
            result['CompleteRemark'] = self.complete_remark
        result['Dialogs'] = []
        if self.dialogs is not None:
            for k in self.dialogs:
                result['Dialogs'].append(k.to_map() if k else None)
        if self.gmt_called is not None:
            result['GmtCalled'] = self.gmt_called
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_delayed is not None:
            result['GmtDelayed'] = self.gmt_delayed
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_key is not None:
            result['GroupKey'] = self.group_key
        if self.id is not None:
            result['Id'] = self.id
        if self.is_accepted_charges is not None:
            result['IsAcceptedCharges'] = self.is_accepted_charges
        if self.is_delayed is not None:
            result['IsDelayed'] = self.is_delayed
        if self.is_need_callback is not None:
            result['IsNeedCallback'] = self.is_need_callback
        if self.is_need_charges is not None:
            result['IsNeedCharges'] = self.is_need_charges
        if self.operations is not None:
            result['Operations'] = self.operations
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('AssignedHandler') is not None:
            self.assigned_handler = m.get('AssignedHandler')
        if m.get('ChargesRemark') is not None:
            self.charges_remark = m.get('ChargesRemark')
        if m.get('CompleteRemark') is not None:
            self.complete_remark = m.get('CompleteRemark')
        self.dialogs = []
        if m.get('Dialogs') is not None:
            for k in m.get('Dialogs'):
                temp_model = ListTicketsResponseBodyResultDialogs()
                self.dialogs.append(temp_model.from_map(k))
        if m.get('GmtCalled') is not None:
            self.gmt_called = m.get('GmtCalled')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtDelayed') is not None:
            self.gmt_delayed = m.get('GmtDelayed')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsAcceptedCharges') is not None:
            self.is_accepted_charges = m.get('IsAcceptedCharges')
        if m.get('IsDelayed') is not None:
            self.is_delayed = m.get('IsDelayed')
        if m.get('IsNeedCallback') is not None:
            self.is_need_callback = m.get('IsNeedCallback')
        if m.get('IsNeedCharges') is not None:
            self.is_need_charges = m.get('IsNeedCharges')
        if m.get('Operations') is not None:
            self.operations = m.get('Operations')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTicketsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        page: ListTicketsResponseBodyPage = None,
        request_id: str = None,
        result: List[ListTicketsResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.message = message
        self.page = page
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = ListTicketsResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListTicketsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListTicketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTicketsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageGetHotelRoomDevicesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PageGetHotelRoomDevicesRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class PageGetHotelRoomDevicesResponseBodyPage(TeaModel):
    def __init__(
        self,
        end: int = None,
        has_next: bool = None,
        page_number: int = None,
        page_size: int = None,
        start: int = None,
        total: int = None,
        total_page: int = None,
    ):
        self.end = end
        self.has_next = has_next
        self.page_number = page_number
        self.page_size = page_size
        self.start = start
        self.total = total
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start is not None:
            result['Start'] = self.start
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class PageGetHotelRoomDevicesResponseBodyResult(TeaModel):
    def __init__(
        self,
        firmware_version: str = None,
        hotel_id: str = None,
        mac: str = None,
        online_status: int = None,
        room_no: str = None,
        sn: str = None,
    ):
        self.firmware_version = firmware_version
        self.hotel_id = hotel_id
        self.mac = mac
        self.online_status = online_status
        self.room_no = room_no
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class PageGetHotelRoomDevicesResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        page: PageGetHotelRoomDevicesResponseBodyPage = None,
        request_id: str = None,
        result: List[PageGetHotelRoomDevicesResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.page = page
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = PageGetHotelRoomDevicesResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = PageGetHotelRoomDevicesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class PageGetHotelRoomDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageGetHotelRoomDevicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PageGetHotelRoomDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PmsEventReportHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PmsEventReportRequest(TeaModel):
    def __init__(
        self,
        payload: str = None,
    ):
        # This parameter is required.
        self.payload = payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        return self


class PmsEventReportResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class PmsEventReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PmsEventReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PmsEventReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushHotelMessageHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PushHotelMessageRequestPushHotelMessageReq(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        param_map: Dict[str, str] = None,
        room_no: str = None,
        template_id: int = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.param_map = param_map
        # This parameter is required.
        self.room_no = room_no
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.param_map is not None:
            result['ParamMap'] = self.param_map
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ParamMap') is not None:
            self.param_map = m.get('ParamMap')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class PushHotelMessageRequest(TeaModel):
    def __init__(
        self,
        push_hotel_message_req: PushHotelMessageRequestPushHotelMessageReq = None,
    ):
        # pushHotelMessageReq
        # 
        # This parameter is required.
        self.push_hotel_message_req = push_hotel_message_req

    def validate(self):
        if self.push_hotel_message_req:
            self.push_hotel_message_req.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_hotel_message_req is not None:
            result['PushHotelMessageReq'] = self.push_hotel_message_req.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushHotelMessageReq') is not None:
            temp_model = PushHotelMessageRequestPushHotelMessageReq()
            self.push_hotel_message_req = temp_model.from_map(m['PushHotelMessageReq'])
        return self


class PushHotelMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        push_hotel_message_req_shrink: str = None,
    ):
        # pushHotelMessageReq
        # 
        # This parameter is required.
        self.push_hotel_message_req_shrink = push_hotel_message_req_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_hotel_message_req_shrink is not None:
            result['PushHotelMessageReq'] = self.push_hotel_message_req_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushHotelMessageReq') is not None:
            self.push_hotel_message_req_shrink = m.get('PushHotelMessageReq')
        return self


class PushHotelMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class PushHotelMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushHotelMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PushHotelMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushVoiceBoxCommandsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PushVoiceBoxCommandsRequestCommands(TeaModel):
    def __init__(
        self,
        command_domain: str = None,
        command_name: str = None,
        payload: str = None,
    ):
        # This parameter is required.
        self.command_domain = command_domain
        # This parameter is required.
        self.command_name = command_name
        self.payload = payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_domain is not None:
            result['CommandDomain'] = self.command_domain
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        if self.payload is not None:
            result['Payload'] = self.payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandDomain') is not None:
            self.command_domain = m.get('CommandDomain')
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        return self


class PushVoiceBoxCommandsRequest(TeaModel):
    def __init__(
        self,
        commands: List[PushVoiceBoxCommandsRequestCommands] = None,
        hotel_id: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.commands = commands
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        if self.commands:
            for k in self.commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Commands'] = []
        if self.commands is not None:
            for k in self.commands:
                result['Commands'].append(k.to_map() if k else None)
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k in m.get('Commands'):
                temp_model = PushVoiceBoxCommandsRequestCommands()
                self.commands.append(temp_model.from_map(k))
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class PushVoiceBoxCommandsShrinkRequest(TeaModel):
    def __init__(
        self,
        commands_shrink: str = None,
        hotel_id: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.commands_shrink = commands_shrink
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commands_shrink is not None:
            result['Commands'] = self.commands_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands_shrink = m.get('Commands')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class PushVoiceBoxCommandsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class PushVoiceBoxCommandsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushVoiceBoxCommandsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PushVoiceBoxCommandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushWelcomeHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PushWelcomeRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_name: str = None,
        room_no: str = None,
        welcome_music_url: str = None,
        welcome_text: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.room_name = room_name
        self.room_no = room_no
        self.welcome_music_url = welcome_music_url
        # This parameter is required.
        self.welcome_text = welcome_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_name is not None:
            result['RoomName'] = self.room_name
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.welcome_music_url is not None:
            result['WelcomeMusicUrl'] = self.welcome_music_url
        if self.welcome_text is not None:
            result['WelcomeText'] = self.welcome_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('WelcomeMusicUrl') is not None:
            self.welcome_music_url = m.get('WelcomeMusicUrl')
        if m.get('WelcomeText') is not None:
            self.welcome_text = m.get('WelcomeText')
        return self


class PushWelcomeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class PushWelcomeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushWelcomeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PushWelcomeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushWelcomeTextAndMusicHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PushWelcomeTextAndMusicRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_name: str = None,
        room_no: str = None,
        template_variable: Dict[str, str] = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.room_name = room_name
        self.room_no = room_no
        self.template_variable = template_variable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_name is not None:
            result['RoomName'] = self.room_name
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.template_variable is not None:
            result['TemplateVariable'] = self.template_variable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('TemplateVariable') is not None:
            self.template_variable = m.get('TemplateVariable')
        return self


class PushWelcomeTextAndMusicShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_name: str = None,
        room_no: str = None,
        template_variable_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.room_name = room_name
        self.room_no = room_no
        self.template_variable_shrink = template_variable_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_name is not None:
            result['RoomName'] = self.room_name
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.template_variable_shrink is not None:
            result['TemplateVariable'] = self.template_variable_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('TemplateVariable') is not None:
            self.template_variable_shrink = m.get('TemplateVariable')
        return self


class PushWelcomeTextAndMusicResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class PushWelcomeTextAndMusicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushWelcomeTextAndMusicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PushWelcomeTextAndMusicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceStatusHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QueryDeviceStatusRequestPayloadLocationDevices(TeaModel):
    def __init__(
        self,
        device_number: str = None,
        device_type: str = None,
        location: str = None,
    ):
        self.device_number = device_number
        self.device_type = device_type
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class QueryDeviceStatusRequestPayload(TeaModel):
    def __init__(
        self,
        location_devices: List[QueryDeviceStatusRequestPayloadLocationDevices] = None,
        properties: Dict[str, str] = None,
    ):
        self.location_devices = location_devices
        self.properties = properties

    def validate(self):
        if self.location_devices:
            for k in self.location_devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LocationDevices'] = []
        if self.location_devices is not None:
            for k in self.location_devices:
                result['LocationDevices'].append(k.to_map() if k else None)
        if self.properties is not None:
            result['Properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.location_devices = []
        if m.get('LocationDevices') is not None:
            for k in m.get('LocationDevices'):
                temp_model = QueryDeviceStatusRequestPayloadLocationDevices()
                self.location_devices.append(temp_model.from_map(k))
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        return self


class QueryDeviceStatusRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class QueryDeviceStatusRequest(TeaModel):
    def __init__(
        self,
        payload: QueryDeviceStatusRequestPayload = None,
        user_info: QueryDeviceStatusRequestUserInfo = None,
    ):
        self.payload = payload
        self.user_info = user_info

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = QueryDeviceStatusRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = QueryDeviceStatusRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class QueryDeviceStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.payload_shrink = payload_shrink
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class QueryDeviceStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[Dict[str, str]] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class QueryDeviceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryDeviceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHotelRoomDetailHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QueryHotelRoomDetailRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        mac: str = None,
        room_no: str = None,
        sn: str = None,
        uuid: str = None,
    ):
        self.hotel_id = hotel_id
        self.mac = mac
        self.room_no = room_no
        # 设备sn信息
        # 注：若在mac uuid sn全都输入的情况下 按照输入正确的内容查询 若全输入都是正确的 则 按照 uuid > mac > sn 优先级查询
        # 传入mac uuid sn其中一个 则酒店id和房间号可不传
        self.sn = sn
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryHotelRoomDetailResponseBodyResultAuthAccounts(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        auth_time: str = None,
    ):
        self.account_name = account_name
        self.auth_time = auth_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.auth_time is not None:
            result['AuthTime'] = self.auth_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AuthTime') is not None:
            self.auth_time = m.get('AuthTime')
        return self


class QueryHotelRoomDetailResponseBodyResultDeviceInfos(TeaModel):
    def __init__(
        self,
        active_time: str = None,
        device_name: str = None,
        firmware_version: str = None,
        mac: str = None,
        online_status: int = None,
        sn: str = None,
        uuid: str = None,
    ):
        self.active_time = active_time
        self.device_name = device_name
        self.firmware_version = firmware_version
        self.mac = mac
        self.online_status = online_status
        self.sn = sn
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryHotelRoomDetailResponseBodyResultOtherService(TeaModel):
    def __init__(
        self,
        open_call: bool = None,
        unhandle_tickets: int = None,
    ):
        self.open_call = open_call
        self.unhandle_tickets = unhandle_tickets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_call is not None:
            result['OpenCall'] = self.open_call
        if self.unhandle_tickets is not None:
            result['UnhandleTickets'] = self.unhandle_tickets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenCall') is not None:
            self.open_call = m.get('OpenCall')
        if m.get('UnhandleTickets') is not None:
            self.unhandle_tickets = m.get('UnhandleTickets')
        return self


class QueryHotelRoomDetailResponseBodyResultRoomControlInfoDeviceInfos(TeaModel):
    def __init__(
        self,
        category_en_name: str = None,
        category_id: int = None,
        category_name: str = None,
        device_connect_type: str = None,
        device_count: int = None,
        device_id: str = None,
        device_name: str = None,
        location_en_name: str = None,
        location_id: int = None,
        location_name: str = None,
        product_key: str = None,
    ):
        self.category_en_name = category_en_name
        self.category_id = category_id
        self.category_name = category_name
        self.device_connect_type = device_connect_type
        self.device_count = device_count
        self.device_id = device_id
        self.device_name = device_name
        self.location_en_name = location_en_name
        self.location_id = location_id
        self.location_name = location_name
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_en_name is not None:
            result['CategoryEnName'] = self.category_en_name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.device_connect_type is not None:
            result['DeviceConnectType'] = self.device_connect_type
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.location_en_name is not None:
            result['LocationEnName'] = self.location_en_name
        if self.location_id is not None:
            result['LocationId'] = self.location_id
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryEnName') is not None:
            self.category_en_name = m.get('CategoryEnName')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('DeviceConnectType') is not None:
            self.device_connect_type = m.get('DeviceConnectType')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('LocationEnName') is not None:
            self.location_en_name = m.get('LocationEnName')
        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryHotelRoomDetailResponseBodyResultRoomControlInfo(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        device_infos: List[QueryHotelRoomDetailResponseBodyResultRoomControlInfoDeviceInfos] = None,
        rcu_url: str = None,
        template_id: int = None,
        template_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.device_infos = device_infos
        self.rcu_url = rcu_url
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        if self.device_infos:
            for k in self.device_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k in self.device_infos:
                result['DeviceInfos'].append(k.to_map() if k else None)
        if self.rcu_url is not None:
            result['RcuUrl'] = self.rcu_url
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k in m.get('DeviceInfos'):
                temp_model = QueryHotelRoomDetailResponseBodyResultRoomControlInfoDeviceInfos()
                self.device_infos.append(temp_model.from_map(k))
        if m.get('RcuUrl') is not None:
            self.rcu_url = m.get('RcuUrl')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class QueryHotelRoomDetailResponseBodyResultRoomServiceInfo(TeaModel):
    def __init__(
        self,
        book_service_cnt: int = None,
        goods_service_cnt: int = None,
        repair_service_cnt: int = None,
        room_service_cnt: int = None,
    ):
        self.book_service_cnt = book_service_cnt
        self.goods_service_cnt = goods_service_cnt
        self.repair_service_cnt = repair_service_cnt
        self.room_service_cnt = room_service_cnt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.book_service_cnt is not None:
            result['BookServiceCnt'] = self.book_service_cnt
        if self.goods_service_cnt is not None:
            result['GoodsServiceCnt'] = self.goods_service_cnt
        if self.repair_service_cnt is not None:
            result['RepairServiceCnt'] = self.repair_service_cnt
        if self.room_service_cnt is not None:
            result['RoomServiceCnt'] = self.room_service_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BookServiceCnt') is not None:
            self.book_service_cnt = m.get('BookServiceCnt')
        if m.get('GoodsServiceCnt') is not None:
            self.goods_service_cnt = m.get('GoodsServiceCnt')
        if m.get('RepairServiceCnt') is not None:
            self.repair_service_cnt = m.get('RepairServiceCnt')
        if m.get('RoomServiceCnt') is not None:
            self.room_service_cnt = m.get('RoomServiceCnt')
        return self


class QueryHotelRoomDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        auth_accounts: List[QueryHotelRoomDetailResponseBodyResultAuthAccounts] = None,
        connect_type: str = None,
        creator_account_name: str = None,
        device_infos: List[QueryHotelRoomDetailResponseBodyResultDeviceInfos] = None,
        hotel_id: str = None,
        hotel_name: str = None,
        other_service: QueryHotelRoomDetailResponseBodyResultOtherService = None,
        room_control_info: QueryHotelRoomDetailResponseBodyResultRoomControlInfo = None,
        room_no: str = None,
        room_service_info: QueryHotelRoomDetailResponseBodyResultRoomServiceInfo = None,
    ):
        self.auth_accounts = auth_accounts
        self.connect_type = connect_type
        self.creator_account_name = creator_account_name
        self.device_infos = device_infos
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.other_service = other_service
        self.room_control_info = room_control_info
        self.room_no = room_no
        self.room_service_info = room_service_info

    def validate(self):
        if self.auth_accounts:
            for k in self.auth_accounts:
                if k:
                    k.validate()
        if self.device_infos:
            for k in self.device_infos:
                if k:
                    k.validate()
        if self.other_service:
            self.other_service.validate()
        if self.room_control_info:
            self.room_control_info.validate()
        if self.room_service_info:
            self.room_service_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthAccounts'] = []
        if self.auth_accounts is not None:
            for k in self.auth_accounts:
                result['AuthAccounts'].append(k.to_map() if k else None)
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.creator_account_name is not None:
            result['CreatorAccountName'] = self.creator_account_name
        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k in self.device_infos:
                result['DeviceInfos'].append(k.to_map() if k else None)
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.other_service is not None:
            result['OtherService'] = self.other_service.to_map()
        if self.room_control_info is not None:
            result['RoomControlInfo'] = self.room_control_info.to_map()
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.room_service_info is not None:
            result['RoomServiceInfo'] = self.room_service_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_accounts = []
        if m.get('AuthAccounts') is not None:
            for k in m.get('AuthAccounts'):
                temp_model = QueryHotelRoomDetailResponseBodyResultAuthAccounts()
                self.auth_accounts.append(temp_model.from_map(k))
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('CreatorAccountName') is not None:
            self.creator_account_name = m.get('CreatorAccountName')
        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k in m.get('DeviceInfos'):
                temp_model = QueryHotelRoomDetailResponseBodyResultDeviceInfos()
                self.device_infos.append(temp_model.from_map(k))
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('OtherService') is not None:
            temp_model = QueryHotelRoomDetailResponseBodyResultOtherService()
            self.other_service = temp_model.from_map(m['OtherService'])
        if m.get('RoomControlInfo') is not None:
            temp_model = QueryHotelRoomDetailResponseBodyResultRoomControlInfo()
            self.room_control_info = temp_model.from_map(m['RoomControlInfo'])
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('RoomServiceInfo') is not None:
            temp_model = QueryHotelRoomDetailResponseBodyResultRoomServiceInfo()
            self.room_service_info = temp_model.from_map(m['RoomServiceInfo'])
        return self


class QueryHotelRoomDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: QueryHotelRoomDetailResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryHotelRoomDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryHotelRoomDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryHotelRoomDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryHotelRoomDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRoomControlDevicesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QueryRoomControlDevicesRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExtSwitchList(TeaModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        category: str = None,
        device_index: int = None,
        device_name: str = None,
        device_status: str = None,
        element_code: str = None,
        location: str = None,
    ):
        self.alias_list = alias_list
        self.category = category
        self.device_index = device_index
        self.device_name = device_name
        self.device_status = device_status
        self.element_code = element_code
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list
        if self.category is not None:
            result['Category'] = self.category
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.element_code is not None:
            result['ElementCode'] = self.element_code
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('ElementCode') is not None:
            self.element_code = m.get('ElementCode')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExt(TeaModel):
    def __init__(
        self,
        switch_list: List[QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExtSwitchList] = None,
    ):
        self.switch_list = switch_list

    def validate(self):
        if self.switch_list:
            for k in self.switch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SwitchList'] = []
        if self.switch_list is not None:
            for k in self.switch_list:
                result['SwitchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.switch_list = []
        if m.get('SwitchList') is not None:
            for k in m.get('SwitchList'):
                temp_model = QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExtSwitchList()
                self.switch_list.append(temp_model.from_map(k))
        return self


class QueryRoomControlDevicesResponseBodyResultDevices(TeaModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        connect_type: str = None,
        dn: str = None,
        device_name: str = None,
        device_status: str = None,
        multi_key_switch_ext: QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExt = None,
        name: str = None,
        number: str = None,
        pk: str = None,
    ):
        self.alias_list = alias_list
        self.connect_type = connect_type
        self.dn = dn
        self.device_name = device_name
        self.device_status = device_status
        self.multi_key_switch_ext = multi_key_switch_ext
        self.name = name
        self.number = number
        self.pk = pk

    def validate(self):
        if self.multi_key_switch_ext:
            self.multi_key_switch_ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.dn is not None:
            result['DN'] = self.dn
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.multi_key_switch_ext is not None:
            result['MultiKeySwitchExt'] = self.multi_key_switch_ext.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.pk is not None:
            result['PK'] = self.pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('DN') is not None:
            self.dn = m.get('DN')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('MultiKeySwitchExt') is not None:
            temp_model = QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExt()
            self.multi_key_switch_ext = temp_model.from_map(m['MultiKeySwitchExt'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('PK') is not None:
            self.pk = m.get('PK')
        return self


class QueryRoomControlDevicesResponseBodyResult(TeaModel):
    def __init__(
        self,
        devices: List[QueryRoomControlDevicesResponseBodyResultDevices] = None,
        location: str = None,
        location_name: str = None,
    ):
        self.devices = devices
        self.location = location
        self.location_name = location_name

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = QueryRoomControlDevicesResponseBodyResultDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        return self


class QueryRoomControlDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[QueryRoomControlDevicesResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryRoomControlDevicesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryRoomControlDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRoomControlDevicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryRoomControlDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRoomControlDevicesAndStatusHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QueryRoomControlDevicesAndStatusRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
    ):
        self.hotel_id = hotel_id
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExtSwitchList(TeaModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        category: str = None,
        device_index: int = None,
        device_name: str = None,
        device_status: str = None,
        element_code: str = None,
        location: str = None,
        status: Dict[str, str] = None,
        tags: List[str] = None,
    ):
        self.alias_list = alias_list
        self.category = category
        self.device_index = device_index
        self.device_name = device_name
        self.device_status = device_status
        self.element_code = element_code
        self.location = location
        self.status = status
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list
        if self.category is not None:
            result['Category'] = self.category
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.element_code is not None:
            result['ElementCode'] = self.element_code
        if self.location is not None:
            result['Location'] = self.location
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('ElementCode') is not None:
            self.element_code = m.get('ElementCode')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExt(TeaModel):
    def __init__(
        self,
        switch_list: List[QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExtSwitchList] = None,
    ):
        self.switch_list = switch_list

    def validate(self):
        if self.switch_list:
            for k in self.switch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SwitchList'] = []
        if self.switch_list is not None:
            for k in self.switch_list:
                result['SwitchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.switch_list = []
        if m.get('SwitchList') is not None:
            for k in m.get('SwitchList'):
                temp_model = QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExtSwitchList()
                self.switch_list.append(temp_model.from_map(k))
        return self


class QueryRoomControlDevicesAndStatusResponseBodyResultDevices(TeaModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        brand: str = None,
        city: str = None,
        connect_type: str = None,
        device_name: str = None,
        device_status: str = None,
        dn: str = None,
        infrared_id: str = None,
        infrared_index: str = None,
        infrared_version: str = None,
        multi_key_switch_ext: QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExt = None,
        name: str = None,
        number: str = None,
        pk: str = None,
        province: str = None,
        service_provider: str = None,
        status: Dict[str, str] = None,
    ):
        self.alias_list = alias_list
        self.brand = brand
        self.city = city
        self.connect_type = connect_type
        self.device_name = device_name
        self.device_status = device_status
        self.dn = dn
        self.infrared_id = infrared_id
        self.infrared_index = infrared_index
        self.infrared_version = infrared_version
        self.multi_key_switch_ext = multi_key_switch_ext
        self.name = name
        self.number = number
        self.pk = pk
        self.province = province
        self.service_provider = service_provider
        self.status = status

    def validate(self):
        if self.multi_key_switch_ext:
            self.multi_key_switch_ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.city is not None:
            result['City'] = self.city
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.dn is not None:
            result['Dn'] = self.dn
        if self.infrared_id is not None:
            result['InfraredId'] = self.infrared_id
        if self.infrared_index is not None:
            result['InfraredIndex'] = self.infrared_index
        if self.infrared_version is not None:
            result['InfraredVersion'] = self.infrared_version
        if self.multi_key_switch_ext is not None:
            result['MultiKeySwitchExt'] = self.multi_key_switch_ext.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.province is not None:
            result['Province'] = self.province
        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('Dn') is not None:
            self.dn = m.get('Dn')
        if m.get('InfraredId') is not None:
            self.infrared_id = m.get('InfraredId')
        if m.get('InfraredIndex') is not None:
            self.infrared_index = m.get('InfraredIndex')
        if m.get('InfraredVersion') is not None:
            self.infrared_version = m.get('InfraredVersion')
        if m.get('MultiKeySwitchExt') is not None:
            temp_model = QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExt()
            self.multi_key_switch_ext = temp_model.from_map(m['MultiKeySwitchExt'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryRoomControlDevicesAndStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        devices: List[QueryRoomControlDevicesAndStatusResponseBodyResultDevices] = None,
        location: str = None,
        location_name: str = None,
        room_no: str = None,
    ):
        self.devices = devices
        self.location = location
        self.location_name = location_name
        self.room_no = room_no

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = QueryRoomControlDevicesAndStatusResponseBodyResultDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class QueryRoomControlDevicesAndStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[QueryRoomControlDevicesAndStatusResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryRoomControlDevicesAndStatusResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryRoomControlDevicesAndStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRoomControlDevicesAndStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryRoomControlDevicesAndStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRoomStatusHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QueryRoomStatusRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
    ):
        self.hotel_id = hotel_id
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        return self


class QueryRoomStatusResponseBodyResultSceneList(TeaModel):
    def __init__(
        self,
        scene_name: str = None,
    ):
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class QueryRoomStatusResponseBodyResultStatusList(TeaModel):
    def __init__(
        self,
        status_name: str = None,
        status_value: str = None,
        update_time: str = None,
    ):
        self.status_name = status_name
        self.status_value = status_value
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.status_value is not None:
            result['StatusValue'] = self.status_value
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('StatusValue') is not None:
            self.status_value = m.get('StatusValue')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryRoomStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
        scene_list: List[QueryRoomStatusResponseBodyResultSceneList] = None,
        status_list: List[QueryRoomStatusResponseBodyResultStatusList] = None,
    ):
        self.hotel_id = hotel_id
        self.room_no = room_no
        self.scene_list = scene_list
        self.status_list = status_list

    def validate(self):
        if self.scene_list:
            for k in self.scene_list:
                if k:
                    k.validate()
        if self.status_list:
            for k in self.status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        result['SceneList'] = []
        if self.scene_list is not None:
            for k in self.scene_list:
                result['SceneList'].append(k.to_map() if k else None)
        result['StatusList'] = []
        if self.status_list is not None:
            for k in self.status_list:
                result['StatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        self.scene_list = []
        if m.get('SceneList') is not None:
            for k in m.get('SceneList'):
                temp_model = QueryRoomStatusResponseBodyResultSceneList()
                self.scene_list.append(temp_model.from_map(k))
        self.status_list = []
        if m.get('StatusList') is not None:
            for k in m.get('StatusList'):
                temp_model = QueryRoomStatusResponseBodyResultStatusList()
                self.status_list.append(temp_model.from_map(k))
        return self


class QueryRoomStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: QueryRoomStatusResponseBodyResult = None,
        status_code: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryRoomStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryRoomStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRoomStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryRoomStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySceneListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class QuerySceneListRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        scene_states: List[int] = None,
        scene_types: List[str] = None,
        template_info_ids: List[str] = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.scene_states = scene_states
        self.scene_types = scene_types
        self.template_info_ids = template_info_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_states is not None:
            result['SceneStates'] = self.scene_states
        if self.scene_types is not None:
            result['SceneTypes'] = self.scene_types
        if self.template_info_ids is not None:
            result['TemplateInfoIds'] = self.template_info_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneStates') is not None:
            self.scene_states = m.get('SceneStates')
        if m.get('SceneTypes') is not None:
            self.scene_types = m.get('SceneTypes')
        if m.get('TemplateInfoIds') is not None:
            self.template_info_ids = m.get('TemplateInfoIds')
        return self


class QuerySceneListShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        scene_states_shrink: str = None,
        scene_types_shrink: str = None,
        template_info_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.scene_states_shrink = scene_states_shrink
        self.scene_types_shrink = scene_types_shrink
        self.template_info_ids_shrink = template_info_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_states_shrink is not None:
            result['SceneStates'] = self.scene_states_shrink
        if self.scene_types_shrink is not None:
            result['SceneTypes'] = self.scene_types_shrink
        if self.template_info_ids_shrink is not None:
            result['TemplateInfoIds'] = self.template_info_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneStates') is not None:
            self.scene_states_shrink = m.get('SceneStates')
        if m.get('SceneTypes') is not None:
            self.scene_types_shrink = m.get('SceneTypes')
        if m.get('TemplateInfoIds') is not None:
            self.template_info_ids_shrink = m.get('TemplateInfoIds')
        return self


class QuerySceneListResponseBodyResultsTemplateInfoDTOList(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QuerySceneListResponseBodyResults(TeaModel):
    def __init__(
        self,
        icon: str = None,
        scene_id: str = None,
        scene_name: str = None,
        scene_source: str = None,
        scene_state: int = None,
        scene_type: str = None,
        template_info_dtolist: List[QuerySceneListResponseBodyResultsTemplateInfoDTOList] = None,
        unavailable_reason: str = None,
    ):
        self.icon = icon
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.scene_source = scene_source
        self.scene_state = scene_state
        self.scene_type = scene_type
        self.template_info_dtolist = template_info_dtolist
        self.unavailable_reason = unavailable_reason

    def validate(self):
        if self.template_info_dtolist:
            for k in self.template_info_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.scene_source is not None:
            result['SceneSource'] = self.scene_source
        if self.scene_state is not None:
            result['SceneState'] = self.scene_state
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        result['TemplateInfoDTOList'] = []
        if self.template_info_dtolist is not None:
            for k in self.template_info_dtolist:
                result['TemplateInfoDTOList'].append(k.to_map() if k else None)
        if self.unavailable_reason is not None:
            result['UnavailableReason'] = self.unavailable_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SceneSource') is not None:
            self.scene_source = m.get('SceneSource')
        if m.get('SceneState') is not None:
            self.scene_state = m.get('SceneState')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        self.template_info_dtolist = []
        if m.get('TemplateInfoDTOList') is not None:
            for k in m.get('TemplateInfoDTOList'):
                temp_model = QuerySceneListResponseBodyResultsTemplateInfoDTOList()
                self.template_info_dtolist.append(temp_model.from_map(k))
        if m.get('UnavailableReason') is not None:
            self.unavailable_reason = m.get('UnavailableReason')
        return self


class QuerySceneListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        results: List[QuerySceneListResponseBodyResults] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.results = results
        self.status_code = status_code

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = QuerySceneListResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QuerySceneListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySceneListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QuerySceneListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveChildAccountAuthHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class RemoveChildAccountAuthRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        child_account_name: str = None,
        hotel_id: str = None,
        tb_open_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.child_account_name = child_account_name
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.tb_open_id = tb_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.child_account_name is not None:
            result['ChildAccountName'] = self.child_account_name
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ChildAccountName') is not None:
            self.child_account_name = m.get('ChildAccountName')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class RemoveChildAccountAuthResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class RemoveChildAccountAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveChildAccountAuthResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveChildAccountAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveHotelHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class RemoveHotelRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        hotel_id: str = None,
        tb_open_id: str = None,
    ):
        # appkey
        # 
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.tb_open_id = tb_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class RemoveHotelResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class RemoveHotelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveHotelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetWelcomeTextAndMusicHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ResetWelcomeTextAndMusicRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        return self


class ResetWelcomeTextAndMusicResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ResetWelcomeTextAndMusicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetWelcomeTextAndMusicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ResetWelcomeTextAndMusicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RoomCheckOutHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class RoomCheckOutRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class RoomCheckOutRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class RoomCheckOutRequest(TeaModel):
    def __init__(
        self,
        device_info: RoomCheckOutRequestDeviceInfo = None,
        user_info: RoomCheckOutRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = RoomCheckOutRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = RoomCheckOutRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class RoomCheckOutShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.device_info_shrink = device_info_shrink
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class RoomCheckOutResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RoomCheckOutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RoomCheckOutResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RoomCheckOutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitHotelOrderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class SubmitHotelOrderRequestPayloadItemList(TeaModel):
    def __init__(
        self,
        item_id: int = None,
        quantity: int = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.item_id = item_id
        # This parameter is required.
        self.quantity = quantity
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class SubmitHotelOrderRequestPayload(TeaModel):
    def __init__(
        self,
        item_list: List[SubmitHotelOrderRequestPayloadItemList] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.item_list = item_list
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = SubmitHotelOrderRequestPayloadItemList()
                self.item_list.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SubmitHotelOrderRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SubmitHotelOrderRequest(TeaModel):
    def __init__(
        self,
        payload: SubmitHotelOrderRequestPayload = None,
        user_info: SubmitHotelOrderRequestUserInfo = None,
    ):
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = SubmitHotelOrderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = SubmitHotelOrderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class SubmitHotelOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class SubmitHotelOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
        status_code: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitHotelOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitHotelOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SubmitHotelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncDeviceStatusWithAkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class SyncDeviceStatusWithAkRequest(TeaModel):
    def __init__(
        self,
        category_cn_name: str = None,
        category_en_name: str = None,
        device_name: str = None,
        hotel_id: str = None,
        location: str = None,
        location_cn_name: str = None,
        number: str = None,
        room_no: str = None,
        switch: int = None,
        fan_speed: str = None,
        mode: str = None,
        room_temperature: str = None,
        temperature: str = None,
        value: int = None,
    ):
        self.category_cn_name = category_cn_name
        # This parameter is required.
        self.category_en_name = category_en_name
        self.device_name = device_name
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.location = location
        self.location_cn_name = location_cn_name
        # This parameter is required.
        self.number = number
        # This parameter is required.
        self.room_no = room_no
        # This parameter is required.
        self.switch = switch
        self.fan_speed = fan_speed
        self.mode = mode
        self.room_temperature = room_temperature
        self.temperature = temperature
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_cn_name is not None:
            result['CategoryCnName'] = self.category_cn_name
        if self.category_en_name is not None:
            result['CategoryEnName'] = self.category_en_name
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.location is not None:
            result['Location'] = self.location
        if self.location_cn_name is not None:
            result['LocationCnName'] = self.location_cn_name
        if self.number is not None:
            result['Number'] = self.number
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.switch is not None:
            result['Switch'] = self.switch
        if self.fan_speed is not None:
            result['fanSpeed'] = self.fan_speed
        if self.mode is not None:
            result['mode'] = self.mode
        if self.room_temperature is not None:
            result['roomTemperature'] = self.room_temperature
        if self.temperature is not None:
            result['temperature'] = self.temperature
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCnName') is not None:
            self.category_cn_name = m.get('CategoryCnName')
        if m.get('CategoryEnName') is not None:
            self.category_en_name = m.get('CategoryEnName')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('LocationCnName') is not None:
            self.location_cn_name = m.get('LocationCnName')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        if m.get('fanSpeed') is not None:
            self.fan_speed = m.get('fanSpeed')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('roomTemperature') is not None:
            self.room_temperature = m.get('roomTemperature')
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SyncDeviceStatusWithAkResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        result: bool = None,
        status_code: int = None,
        request_id: str = None,
    ):
        self.message = message
        self.result = result
        self.status_code = status_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SyncDeviceStatusWithAkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncDeviceStatusWithAkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SyncDeviceStatusWithAkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBasicInfoQAHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateBasicInfoQARequest(TeaModel):
    def __init__(
        self,
        check_in_time: str = None,
        check_out_time: str = None,
        hotel_address: str = None,
        hotel_id: str = None,
        hotel_introduction: str = None,
        hotel_member: str = None,
        hotel_service: str = None,
        parking_expenses: str = None,
        parking_position: str = None,
        phone_number: str = None,
        wifi_name: str = None,
        wifi_password: str = None,
    ):
        # This parameter is required.
        self.check_in_time = check_in_time
        # This parameter is required.
        self.check_out_time = check_out_time
        # This parameter is required.
        self.hotel_address = hotel_address
        # This parameter is required.
        self.hotel_id = hotel_id
        self.hotel_introduction = hotel_introduction
        self.hotel_member = hotel_member
        self.hotel_service = hotel_service
        # This parameter is required.
        self.parking_expenses = parking_expenses
        # This parameter is required.
        self.parking_position = parking_position
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.wifi_name = wifi_name
        # This parameter is required.
        self.wifi_password = wifi_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_in_time is not None:
            result['CheckInTime'] = self.check_in_time
        if self.check_out_time is not None:
            result['CheckOutTime'] = self.check_out_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_introduction is not None:
            result['HotelIntroduction'] = self.hotel_introduction
        if self.hotel_member is not None:
            result['HotelMember'] = self.hotel_member
        if self.hotel_service is not None:
            result['HotelService'] = self.hotel_service
        if self.parking_expenses is not None:
            result['ParkingExpenses'] = self.parking_expenses
        if self.parking_position is not None:
            result['ParkingPosition'] = self.parking_position
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.wifi_name is not None:
            result['WifiName'] = self.wifi_name
        if self.wifi_password is not None:
            result['WifiPassword'] = self.wifi_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckInTime') is not None:
            self.check_in_time = m.get('CheckInTime')
        if m.get('CheckOutTime') is not None:
            self.check_out_time = m.get('CheckOutTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelIntroduction') is not None:
            self.hotel_introduction = m.get('HotelIntroduction')
        if m.get('HotelMember') is not None:
            self.hotel_member = m.get('HotelMember')
        if m.get('HotelService') is not None:
            self.hotel_service = m.get('HotelService')
        if m.get('ParkingExpenses') is not None:
            self.parking_expenses = m.get('ParkingExpenses')
        if m.get('ParkingPosition') is not None:
            self.parking_position = m.get('ParkingPosition')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('WifiName') is not None:
            self.wifi_name = m.get('WifiName')
        if m.get('WifiPassword') is not None:
            self.wifi_password = m.get('WifiPassword')
        return self


class UpdateBasicInfoQAResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateBasicInfoQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBasicInfoQAResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateBasicInfoQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomQAHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateCustomQARequest(TeaModel):
    def __init__(
        self,
        answers: List[str] = None,
        custom_qaid: str = None,
        hotel_id: str = None,
        key_words: List[str] = None,
        major_question: str = None,
        supplementary_questions: List[str] = None,
    ):
        self.answers = answers
        # This parameter is required.
        self.custom_qaid = custom_qaid
        # This parameter is required.
        self.hotel_id = hotel_id
        self.key_words = key_words
        self.major_question = major_question
        self.supplementary_questions = supplementary_questions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers is not None:
            result['Answers'] = self.answers
        if self.custom_qaid is not None:
            result['CustomQAId'] = self.custom_qaid
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.supplementary_questions is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        if m.get('CustomQAId') is not None:
            self.custom_qaid = m.get('CustomQAId')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions = m.get('SupplementaryQuestions')
        return self


class UpdateCustomQAShrinkRequest(TeaModel):
    def __init__(
        self,
        answers_shrink: str = None,
        custom_qaid: str = None,
        hotel_id: str = None,
        key_words_shrink: str = None,
        major_question: str = None,
        supplementary_questions_shrink: str = None,
    ):
        self.answers_shrink = answers_shrink
        # This parameter is required.
        self.custom_qaid = custom_qaid
        # This parameter is required.
        self.hotel_id = hotel_id
        self.key_words_shrink = key_words_shrink
        self.major_question = major_question
        self.supplementary_questions_shrink = supplementary_questions_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answers_shrink is not None:
            result['Answers'] = self.answers_shrink
        if self.custom_qaid is not None:
            result['CustomQAId'] = self.custom_qaid
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.key_words_shrink is not None:
            result['KeyWords'] = self.key_words_shrink
        if self.major_question is not None:
            result['MajorQuestion'] = self.major_question
        if self.supplementary_questions_shrink is not None:
            result['SupplementaryQuestions'] = self.supplementary_questions_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answers') is not None:
            self.answers_shrink = m.get('Answers')
        if m.get('CustomQAId') is not None:
            self.custom_qaid = m.get('CustomQAId')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('KeyWords') is not None:
            self.key_words_shrink = m.get('KeyWords')
        if m.get('MajorQuestion') is not None:
            self.major_question = m.get('MajorQuestion')
        if m.get('SupplementaryQuestions') is not None:
            self.supplementary_questions_shrink = m.get('SupplementaryQuestions')
        return self


class UpdateCustomQAResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateCustomQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomQAResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateCustomQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHotelHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateHotelRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        est_open_time: str = None,
        hotel_address: str = None,
        hotel_email: str = None,
        hotel_id: str = None,
        hotel_name: str = None,
        phone_number: str = None,
        related_pks: List[str] = None,
        remark: str = None,
        room_num: int = None,
        tb_open_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        self.est_open_time = est_open_time
        self.hotel_address = hotel_address
        self.hotel_email = hotel_email
        # This parameter is required.
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.phone_number = phone_number
        self.related_pks = related_pks
        self.remark = remark
        self.room_num = room_num
        # This parameter is required.
        self.tb_open_id = tb_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.est_open_time is not None:
            result['EstOpenTime'] = self.est_open_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_email is not None:
            result['HotelEmail'] = self.hotel_email
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.related_pks is not None:
            result['RelatedPks'] = self.related_pks
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.room_num is not None:
            result['RoomNum'] = self.room_num
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EstOpenTime') is not None:
            self.est_open_time = m.get('EstOpenTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelEmail') is not None:
            self.hotel_email = m.get('HotelEmail')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RelatedPks') is not None:
            self.related_pks = m.get('RelatedPks')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class UpdateHotelShrinkRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        est_open_time: str = None,
        hotel_address: str = None,
        hotel_email: str = None,
        hotel_id: str = None,
        hotel_name: str = None,
        phone_number: str = None,
        related_pks_shrink: str = None,
        remark: str = None,
        room_num: int = None,
        tb_open_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        self.est_open_time = est_open_time
        self.hotel_address = hotel_address
        self.hotel_email = hotel_email
        # This parameter is required.
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.phone_number = phone_number
        self.related_pks_shrink = related_pks_shrink
        self.remark = remark
        self.room_num = room_num
        # This parameter is required.
        self.tb_open_id = tb_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.est_open_time is not None:
            result['EstOpenTime'] = self.est_open_time
        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address
        if self.hotel_email is not None:
            result['HotelEmail'] = self.hotel_email
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.related_pks_shrink is not None:
            result['RelatedPks'] = self.related_pks_shrink
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.room_num is not None:
            result['RoomNum'] = self.room_num
        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EstOpenTime') is not None:
            self.est_open_time = m.get('EstOpenTime')
        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')
        if m.get('HotelEmail') is not None:
            self.hotel_email = m.get('HotelEmail')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RelatedPks') is not None:
            self.related_pks_shrink = m.get('RelatedPks')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')
        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')
        return self


class UpdateHotelResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateHotelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHotelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHotelAlarmHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateHotelAlarmRequestAlarms(TeaModel):
    def __init__(
        self,
        alarm_id: int = None,
        device_open_id: str = None,
        room_no: str = None,
        user_open_id: str = None,
    ):
        # This parameter is required.
        self.alarm_id = alarm_id
        # This parameter is required.
        self.device_open_id = device_open_id
        self.room_no = room_no
        # This parameter is required.
        self.user_open_id = user_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        if self.room_no is not None:
            result['RoomNo'] = self.room_no
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class UpdateHotelAlarmRequestScheduleInfoOnce(TeaModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class UpdateHotelAlarmRequestScheduleInfoWeekly(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class UpdateHotelAlarmRequestScheduleInfo(TeaModel):
    def __init__(
        self,
        once: UpdateHotelAlarmRequestScheduleInfoOnce = None,
        type: str = None,
        weekly: UpdateHotelAlarmRequestScheduleInfoWeekly = None,
    ):
        self.once = once
        # ONCE, WEEKLY
        self.type = type
        self.weekly = weekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = UpdateHotelAlarmRequestScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = UpdateHotelAlarmRequestScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class UpdateHotelAlarmRequest(TeaModel):
    def __init__(
        self,
        alarms: List[UpdateHotelAlarmRequestAlarms] = None,
        hotel_id: str = None,
        schedule_info: UpdateHotelAlarmRequestScheduleInfo = None,
    ):
        # This parameter is required.
        self.alarms = alarms
        # This parameter is required.
        self.hotel_id = hotel_id
        self.schedule_info = schedule_info

    def validate(self):
        if self.alarms:
            for k in self.alarms:
                if k:
                    k.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alarms'] = []
        if self.alarms is not None:
            for k in self.alarms:
                result['Alarms'].append(k.to_map() if k else None)
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarms = []
        if m.get('Alarms') is not None:
            for k in m.get('Alarms'):
                temp_model = UpdateHotelAlarmRequestAlarms()
                self.alarms.append(temp_model.from_map(k))
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ScheduleInfo') is not None:
            temp_model = UpdateHotelAlarmRequestScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        return self


class UpdateHotelAlarmShrinkRequest(TeaModel):
    def __init__(
        self,
        alarms_shrink: str = None,
        hotel_id: str = None,
        schedule_info_shrink: str = None,
    ):
        # This parameter is required.
        self.alarms_shrink = alarms_shrink
        # This parameter is required.
        self.hotel_id = hotel_id
        self.schedule_info_shrink = schedule_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarms_shrink is not None:
            result['Alarms'] = self.alarms_shrink
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.schedule_info_shrink is not None:
            result['ScheduleInfo'] = self.schedule_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alarms') is not None:
            self.alarms_shrink = m.get('Alarms')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ScheduleInfo') is not None:
            self.schedule_info_shrink = m.get('ScheduleInfo')
        return self


class UpdateHotelAlarmResponseBody(TeaModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateHotelAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHotelAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateHotelAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHotelSceneBookItemHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateHotelSceneBookItemRequestUpdateHotelSceneBookReq(TeaModel):
    def __init__(
        self,
        icon: str = None,
        id: int = None,
        name: str = None,
        price: int = None,
    ):
        # icon
        # 
        # This parameter is required.
        self.icon = icon
        self.id = id
        self.name = name
        # This parameter is required.
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        return self


class UpdateHotelSceneBookItemRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        update_hotel_scene_book_req: UpdateHotelSceneBookItemRequestUpdateHotelSceneBookReq = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # updateHotelSceneBookReq
        # 
        # This parameter is required.
        self.update_hotel_scene_book_req = update_hotel_scene_book_req

    def validate(self):
        if self.update_hotel_scene_book_req:
            self.update_hotel_scene_book_req.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.update_hotel_scene_book_req is not None:
            result['UpdateHotelSceneBookReq'] = self.update_hotel_scene_book_req.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('UpdateHotelSceneBookReq') is not None:
            temp_model = UpdateHotelSceneBookItemRequestUpdateHotelSceneBookReq()
            self.update_hotel_scene_book_req = temp_model.from_map(m['UpdateHotelSceneBookReq'])
        return self


class UpdateHotelSceneBookItemShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        update_hotel_scene_book_req_shrink: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # updateHotelSceneBookReq
        # 
        # This parameter is required.
        self.update_hotel_scene_book_req_shrink = update_hotel_scene_book_req_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.update_hotel_scene_book_req_shrink is not None:
            result['UpdateHotelSceneBookReq'] = self.update_hotel_scene_book_req_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('UpdateHotelSceneBookReq') is not None:
            self.update_hotel_scene_book_req_shrink = m.get('UpdateHotelSceneBookReq')
        return self


class UpdateHotelSceneBookItemResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateHotelSceneBookItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHotelSceneBookItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateHotelSceneBookItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHotelSceneItemHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateHotelSceneItemRequestUpdateHotelSceneOperateReq(TeaModel):
    def __init__(
        self,
        is_use_template_answer: bool = None,
        operate_type: str = None,
    ):
        # This parameter is required.
        self.is_use_template_answer = is_use_template_answer
        # This parameter is required.
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_use_template_answer is not None:
            result['IsUseTemplateAnswer'] = self.is_use_template_answer
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsUseTemplateAnswer') is not None:
            self.is_use_template_answer = m.get('IsUseTemplateAnswer')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class UpdateHotelSceneItemRequestUpdateHotelSceneReqDialogueList(TeaModel):
    def __init__(
        self,
        dialogue_id: str = None,
        no_answer: str = None,
        no_answer_template: str = None,
        process: int = None,
        question: str = None,
        service_id: str = None,
        yes_answer: str = None,
        yes_answer_template: str = None,
    ):
        self.dialogue_id = dialogue_id
        self.no_answer = no_answer
        self.no_answer_template = no_answer_template
        self.process = process
        self.question = question
        # itemId
        self.service_id = service_id
        self.yes_answer = yes_answer
        self.yes_answer_template = yes_answer_template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialogue_id is not None:
            result['DialogueId'] = self.dialogue_id
        if self.no_answer is not None:
            result['NoAnswer'] = self.no_answer
        if self.no_answer_template is not None:
            result['NoAnswerTemplate'] = self.no_answer_template
        if self.process is not None:
            result['Process'] = self.process
        if self.question is not None:
            result['Question'] = self.question
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.yes_answer is not None:
            result['YesAnswer'] = self.yes_answer
        if self.yes_answer_template is not None:
            result['YesAnswerTemplate'] = self.yes_answer_template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogueId') is not None:
            self.dialogue_id = m.get('DialogueId')
        if m.get('NoAnswer') is not None:
            self.no_answer = m.get('NoAnswer')
        if m.get('NoAnswerTemplate') is not None:
            self.no_answer_template = m.get('NoAnswerTemplate')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('YesAnswer') is not None:
            self.yes_answer = m.get('YesAnswer')
        if m.get('YesAnswerTemplate') is not None:
            self.yes_answer_template = m.get('YesAnswerTemplate')
        return self


class UpdateHotelSceneItemRequestUpdateHotelSceneReq(TeaModel):
    def __init__(
        self,
        beyond_limit_reply: str = None,
        delivery_method: str = None,
        dialogue_list: List[UpdateHotelSceneItemRequestUpdateHotelSceneReqDialogueList] = None,
        icon: str = None,
        id: int = None,
        limit_number: int = None,
        limit_switch: int = None,
        name: str = None,
        payment_method: str = None,
        price: int = None,
        robot_name: str = None,
        status: str = None,
    ):
        self.beyond_limit_reply = beyond_limit_reply
        self.delivery_method = delivery_method
        # This parameter is required.
        self.dialogue_list = dialogue_list
        # icon
        # 
        # This parameter is required.
        self.icon = icon
        # itemID
        self.id = id
        self.limit_number = limit_number
        self.limit_switch = limit_switch
        self.name = name
        self.payment_method = payment_method
        # This parameter is required.
        self.price = price
        self.robot_name = robot_name
        # This parameter is required.
        self.status = status

    def validate(self):
        if self.dialogue_list:
            for k in self.dialogue_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beyond_limit_reply is not None:
            result['BeyondLimitReply'] = self.beyond_limit_reply
        if self.delivery_method is not None:
            result['DeliveryMethod'] = self.delivery_method
        result['DialogueList'] = []
        if self.dialogue_list is not None:
            for k in self.dialogue_list:
                result['DialogueList'].append(k.to_map() if k else None)
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.limit_number is not None:
            result['LimitNumber'] = self.limit_number
        if self.limit_switch is not None:
            result['LimitSwitch'] = self.limit_switch
        if self.name is not None:
            result['Name'] = self.name
        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method
        if self.price is not None:
            result['Price'] = self.price
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeyondLimitReply') is not None:
            self.beyond_limit_reply = m.get('BeyondLimitReply')
        if m.get('DeliveryMethod') is not None:
            self.delivery_method = m.get('DeliveryMethod')
        self.dialogue_list = []
        if m.get('DialogueList') is not None:
            for k in m.get('DialogueList'):
                temp_model = UpdateHotelSceneItemRequestUpdateHotelSceneReqDialogueList()
                self.dialogue_list.append(temp_model.from_map(k))
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LimitNumber') is not None:
            self.limit_number = m.get('LimitNumber')
        if m.get('LimitSwitch') is not None:
            self.limit_switch = m.get('LimitSwitch')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateHotelSceneItemRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        update_hotel_scene_operate_req: UpdateHotelSceneItemRequestUpdateHotelSceneOperateReq = None,
        update_hotel_scene_req: UpdateHotelSceneItemRequestUpdateHotelSceneReq = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # updateHotelSceneReq
        # 
        # This parameter is required.
        self.update_hotel_scene_operate_req = update_hotel_scene_operate_req
        # UpdateHotelSceneReq
        # 
        # This parameter is required.
        self.update_hotel_scene_req = update_hotel_scene_req

    def validate(self):
        if self.update_hotel_scene_operate_req:
            self.update_hotel_scene_operate_req.validate()
        if self.update_hotel_scene_req:
            self.update_hotel_scene_req.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.update_hotel_scene_operate_req is not None:
            result['UpdateHotelSceneOperateReq'] = self.update_hotel_scene_operate_req.to_map()
        if self.update_hotel_scene_req is not None:
            result['UpdateHotelSceneReq'] = self.update_hotel_scene_req.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('UpdateHotelSceneOperateReq') is not None:
            temp_model = UpdateHotelSceneItemRequestUpdateHotelSceneOperateReq()
            self.update_hotel_scene_operate_req = temp_model.from_map(m['UpdateHotelSceneOperateReq'])
        if m.get('UpdateHotelSceneReq') is not None:
            temp_model = UpdateHotelSceneItemRequestUpdateHotelSceneReq()
            self.update_hotel_scene_req = temp_model.from_map(m['UpdateHotelSceneReq'])
        return self


class UpdateHotelSceneItemShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        update_hotel_scene_operate_req_shrink: str = None,
        update_hotel_scene_req_shrink: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # updateHotelSceneReq
        # 
        # This parameter is required.
        self.update_hotel_scene_operate_req_shrink = update_hotel_scene_operate_req_shrink
        # UpdateHotelSceneReq
        # 
        # This parameter is required.
        self.update_hotel_scene_req_shrink = update_hotel_scene_req_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.update_hotel_scene_operate_req_shrink is not None:
            result['UpdateHotelSceneOperateReq'] = self.update_hotel_scene_operate_req_shrink
        if self.update_hotel_scene_req_shrink is not None:
            result['UpdateHotelSceneReq'] = self.update_hotel_scene_req_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('UpdateHotelSceneOperateReq') is not None:
            self.update_hotel_scene_operate_req_shrink = m.get('UpdateHotelSceneOperateReq')
        if m.get('UpdateHotelSceneReq') is not None:
            self.update_hotel_scene_req_shrink = m.get('UpdateHotelSceneReq')
        return self


class UpdateHotelSceneItemResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateHotelSceneItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHotelSceneItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateHotelSceneItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMessageTemplateHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateMessageTemplateRequest(TeaModel):
    def __init__(
        self,
        template_detail: str = None,
        template_id: int = None,
        template_name: str = None,
    ):
        self.template_detail = template_detail
        # This parameter is required.
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_detail is not None:
            result['TemplateDetail'] = self.template_detail
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateDetail') is not None:
            self.template_detail = m.get('TemplateDetail')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class UpdateMessageTemplateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateMessageTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMessageTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateMessageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRcuSceneHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateRcuSceneRequestSceneRelationExtDTO(TeaModel):
    def __init__(
        self,
        corpus_list: List[str] = None,
        description: str = None,
        icon: str = None,
        name: str = None,
    ):
        self.corpus_list = corpus_list
        self.description = description
        self.icon = icon
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corpus_list is not None:
            result['CorpusList'] = self.corpus_list
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpusList') is not None:
            self.corpus_list = m.get('CorpusList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateRcuSceneRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        scene_id: str = None,
        scene_relation_ext_dto: UpdateRcuSceneRequestSceneRelationExtDTO = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.scene_id = scene_id
        # This parameter is required.
        self.scene_relation_ext_dto = scene_relation_ext_dto

    def validate(self):
        if self.scene_relation_ext_dto:
            self.scene_relation_ext_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_relation_ext_dto is not None:
            result['SceneRelationExtDTO'] = self.scene_relation_ext_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneRelationExtDTO') is not None:
            temp_model = UpdateRcuSceneRequestSceneRelationExtDTO()
            self.scene_relation_ext_dto = temp_model.from_map(m['SceneRelationExtDTO'])
        return self


class UpdateRcuSceneShrinkRequest(TeaModel):
    def __init__(
        self,
        hotel_id: str = None,
        scene_id: str = None,
        scene_relation_ext_dtoshrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.scene_id = scene_id
        # This parameter is required.
        self.scene_relation_ext_dtoshrink = scene_relation_ext_dtoshrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_relation_ext_dtoshrink is not None:
            result['SceneRelationExtDTO'] = self.scene_relation_ext_dtoshrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneRelationExtDTO') is not None:
            self.scene_relation_ext_dtoshrink = m.get('SceneRelationExtDTO')
        return self


class UpdateRcuSceneResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateRcuSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRcuSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateRcuSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceQAHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateServiceQARequest(TeaModel):
    def __init__(
        self,
        answer: str = None,
        hotel_id: str = None,
        service_qaid: int = None,
        is_active: bool = None,
    ):
        self.answer = answer
        # This parameter is required.
        self.hotel_id = hotel_id
        self.service_qaid = service_qaid
        self.is_active = is_active

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.service_qaid is not None:
            result['ServiceQAId'] = self.service_qaid
        if self.is_active is not None:
            result['isActive'] = self.is_active
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('ServiceQAId') is not None:
            self.service_qaid = m.get('ServiceQAId')
        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')
        return self


class UpdateServiceQAResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateServiceQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceQAResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateServiceQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTicketHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateTicketRequest(TeaModel):
    def __init__(
        self,
        group_key: str = None,
        hotel_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.group_key = group_key
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_key is not None:
            result['GroupKey'] = self.group_key
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateTicketResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class UpdateTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


