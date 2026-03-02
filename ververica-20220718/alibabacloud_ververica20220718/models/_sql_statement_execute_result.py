# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class SqlStatementExecuteResult(DaraModel):
    def __init__(
        self,
        error_details: main_models.ErrorDetails = None,
        execute_success: bool = None,
        statement: str = None,
    ):
        # The error details returned.
        self.error_details = error_details
        # Indicates whether the request was successful.
        self.execute_success = execute_success
        # The statement that was executed.
        self.statement = statement

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

        if self.execute_success is not None:
            result['executeSuccess'] = self.execute_success

        if self.statement is not None:
            result['statement'] = self.statement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorDetails') is not None:
            temp_model = main_models.ErrorDetails()
            self.error_details = temp_model.from_map(m.get('errorDetails'))

        if m.get('executeSuccess') is not None:
            self.execute_success = m.get('executeSuccess')

        if m.get('statement') is not None:
            self.statement = m.get('statement')

        return self

