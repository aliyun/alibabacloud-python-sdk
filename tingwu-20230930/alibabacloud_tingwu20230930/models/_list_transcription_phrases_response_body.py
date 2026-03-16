# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tingwu20230930 import models as main_models
from darabonba.model import DaraModel

class ListTranscriptionPhrasesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListTranscriptionPhrasesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = main_models.ListTranscriptionPhrasesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTranscriptionPhrasesResponseBodyData(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        phrases: List[main_models.ListTranscriptionPhrasesResponseBodyDataPhrases] = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.phrases = phrases
        self.status = status

    def validate(self):
        if self.phrases:
            for v1 in self.phrases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['Phrases'] = []
        if self.phrases is not None:
            for k1 in self.phrases:
                result['Phrases'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.phrases = []
        if m.get('Phrases') is not None:
            for k1 in m.get('Phrases'):
                temp_model = main_models.ListTranscriptionPhrasesResponseBodyDataPhrases()
                self.phrases.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListTranscriptionPhrasesResponseBodyDataPhrases(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        phrase_id: str = None,
    ):
        self.description = description
        self.name = name
        self.phrase_id = phrase_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.phrase_id is not None:
            result['PhraseId'] = self.phrase_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PhraseId') is not None:
            self.phrase_id = m.get('PhraseId')

        return self

