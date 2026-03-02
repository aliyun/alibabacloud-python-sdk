# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class SqlStatementValidationResult(DaraModel):
    def __init__(
        self,
        error_details: main_models.ErrorDetails = None,
        message: str = None,
        success: bool = None,
        validation_result: str = None,
    ):
        # The error message of the verification result.
        self.error_details = error_details
        # The verification information.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success
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

        if self.message is not None:
            result['message'] = self.message

        if self.success is not None:
            result['success'] = self.success

        if self.validation_result is not None:
            result['validationResult'] = self.validation_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorDetails') is not None:
            temp_model = main_models.ErrorDetails()
            self.error_details = temp_model.from_map(m.get('errorDetails'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('validationResult') is not None:
            self.validation_result = m.get('validationResult')

        return self

