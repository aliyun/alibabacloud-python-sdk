# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ValidateStatementResult(DaraModel):
    def __init__(
        self,
        error_details: main_models.ValidationErrorDetails = None,
        validation_result: str = None,
    ):
        # The details of verification errors of the SQL syntax.
        self.error_details = error_details
        # The verification result.
        self.validation_result = validation_result

    def validate(self):
        if self.error_details:
            self.error_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_details is not None:
            result['errorDetails'] = self.error_details.to_map()

        if self.validation_result is not None:
            result['validationResult'] = self.validation_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorDetails') is not None:
            temp_model = main_models.ValidationErrorDetails()
            self.error_details = temp_model.from_map(m.get('errorDetails'))

        if m.get('validationResult') is not None:
            self.validation_result = m.get('validationResult')

        return self

