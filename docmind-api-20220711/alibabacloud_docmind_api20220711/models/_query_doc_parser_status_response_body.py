# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_docmind_api20220711 import models as main_models
from darabonba.model import DaraModel

class QueryDocParserStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryDocParserStatusResponseBodyData = None,
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
            temp_model = main_models.QueryDocParserStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDocParserStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        image_count: int = None,
        number_of_successful_parsing: int = None,
        page_count_estimate: int = None,
        paragraph_count: int = None,
        processing: float = None,
        status: str = None,
        table_count: int = None,
        tokens: int = None,
    ):
        self.image_count = image_count
        self.number_of_successful_parsing = number_of_successful_parsing
        self.page_count_estimate = page_count_estimate
        self.paragraph_count = paragraph_count
        self.processing = processing
        self.status = status
        self.table_count = table_count
        self.tokens = tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_count is not None:
            result['ImageCount'] = self.image_count

        if self.number_of_successful_parsing is not None:
            result['NumberOfSuccessfulParsing'] = self.number_of_successful_parsing

        if self.page_count_estimate is not None:
            result['PageCountEstimate'] = self.page_count_estimate

        if self.paragraph_count is not None:
            result['ParagraphCount'] = self.paragraph_count

        if self.processing is not None:
            result['Processing'] = self.processing

        if self.status is not None:
            result['Status'] = self.status

        if self.table_count is not None:
            result['TableCount'] = self.table_count

        if self.tokens is not None:
            result['Tokens'] = self.tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')

        if m.get('NumberOfSuccessfulParsing') is not None:
            self.number_of_successful_parsing = m.get('NumberOfSuccessfulParsing')

        if m.get('PageCountEstimate') is not None:
            self.page_count_estimate = m.get('PageCountEstimate')

        if m.get('ParagraphCount') is not None:
            self.paragraph_count = m.get('ParagraphCount')

        if m.get('Processing') is not None:
            self.processing = m.get('Processing')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')

        if m.get('Tokens') is not None:
            self.tokens = m.get('Tokens')

        return self

