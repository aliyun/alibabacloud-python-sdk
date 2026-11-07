# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ValidateLlmTemplateConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ValidateLlmTemplateConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ValidateLlmTemplateConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ValidateLlmTemplateConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        valid: bool = None,
        validation_errors: List[main_models.ValidateLlmTemplateConfigResponseBodyDataValidationErrors] = None,
    ):
        self.valid = valid
        self.validation_errors = validation_errors

    def validate(self):
        if self.validation_errors:
            for v1 in self.validation_errors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.valid is not None:
            result['Valid'] = self.valid

        result['ValidationErrors'] = []
        if self.validation_errors is not None:
            for k1 in self.validation_errors:
                result['ValidationErrors'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        self.validation_errors = []
        if m.get('ValidationErrors') is not None:
            for k1 in m.get('ValidationErrors'):
                temp_model = main_models.ValidateLlmTemplateConfigResponseBodyDataValidationErrors()
                self.validation_errors.append(temp_model.from_map(k1))

        return self

class ValidateLlmTemplateConfigResponseBodyDataValidationErrors(DaraModel):
    def __init__(
        self,
        code: str = None,
        field: str = None,
        message: str = None,
    ):
        self.code = code
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.field is not None:
            result['Field'] = self.field

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

