# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_tingwu20230930 import models as main_models
from darabonba.model import DaraModel

class DeleteTranscriptionPhrasesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DeleteTranscriptionPhrasesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        status: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.status = status

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DeleteTranscriptionPhrasesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DeleteTranscriptionPhrasesResponseBodyData(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

