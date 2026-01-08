# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetChatappTemplateMetricResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.GetChatappTemplateMetricResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The value OK indicates that the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetChatappTemplateMetricResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetChatappTemplateMetricResponseBodyData(DaraModel):
    def __init__(
        self,
        cliented: List[main_models.GetChatappTemplateMetricResponseBodyDataCliented] = None,
        delivered_count: int = None,
        end: int = None,
        language: str = None,
        read_count: int = None,
        sent_count: int = None,
        start: int = None,
        template_code: str = None,
    ):
        # The statistics on button clicks.
        self.cliented = cliented
        # The number of delivered messages.
        self.delivered_count = delivered_count
        # The end of the time range you queried.
        self.end = end
        # The template language.
        self.language = language
        # The number of read messages.
        self.read_count = read_count
        # The number of sent messages.
        self.sent_count = sent_count
        # The beginning of the time range you queried.
        self.start = start
        # The template code.
        self.template_code = template_code

    def validate(self):
        if self.cliented:
            for v1 in self.cliented:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cliented'] = []
        if self.cliented is not None:
            for k1 in self.cliented:
                result['Cliented'].append(k1.to_map() if k1 else None)

        if self.delivered_count is not None:
            result['DeliveredCount'] = self.delivered_count

        if self.end is not None:
            result['End'] = self.end

        if self.language is not None:
            result['Language'] = self.language

        if self.read_count is not None:
            result['ReadCount'] = self.read_count

        if self.sent_count is not None:
            result['SentCount'] = self.sent_count

        if self.start is not None:
            result['Start'] = self.start

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cliented = []
        if m.get('Cliented') is not None:
            for k1 in m.get('Cliented'):
                temp_model = main_models.GetChatappTemplateMetricResponseBodyDataCliented()
                self.cliented.append(temp_model.from_map(k1))

        if m.get('DeliveredCount') is not None:
            self.delivered_count = m.get('DeliveredCount')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')

        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

class GetChatappTemplateMetricResponseBodyDataCliented(DaraModel):
    def __init__(
        self,
        button_content: str = None,
        count: int = None,
        type: str = None,
    ):
        # The text on the button.
        self.button_content = button_content
        # The number of clicks.
        self.count = count
        # The button type.
        # 
        # Valid values:
        # 
        # *   phone_number_button
        # *   url_button
        # *   quick_relpy_button
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.button_content is not None:
            result['ButtonContent'] = self.button_content

        if self.count is not None:
            result['Count'] = self.count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ButtonContent') is not None:
            self.button_content = m.get('ButtonContent')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

