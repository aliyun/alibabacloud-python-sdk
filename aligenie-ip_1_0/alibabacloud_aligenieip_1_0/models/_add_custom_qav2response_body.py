# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class AddCustomQAV2ResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: main_models.AddCustomQAV2ResponseBodyResult = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.AddCustomQAV2ResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self



class AddCustomQAV2ResponseBodyResult(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

