# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class GenerateSqlBySemanticSqlResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GenerateSqlBySemanticSqlResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GenerateSqlBySemanticSqlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GenerateSqlBySemanticSqlResponseBodyData(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        generated_sql: str = None,
        success: bool = None,
    ):
        # The error message returned when the task fails to be created.
        self.error_message = error_message
        # The generated executable SQL statement.
        self.generated_sql = generated_sql
        # Indicates whether the generation request was successful. Valid values:
        # - **true**: Successful.
        # - **false**: Failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.generated_sql is not None:
            result['GeneratedSql'] = self.generated_sql

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GeneratedSql') is not None:
            self.generated_sql = m.get('GeneratedSql')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

