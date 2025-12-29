# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListCustomQAResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        page: main_models.ListCustomQAResponseBodyPage = None,
        request_id: str = None,
        result: List[main_models.ListCustomQAResponseBodyResult] = None,
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
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Page') is not None:
            temp_model = main_models.ListCustomQAResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListCustomQAResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class ListCustomQAResponseBodyResult(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ListCustomQAResponseBodyPage(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

