# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetSchemaResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        schema: main_models.Schema = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The schema information.
        self.schema = schema
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema is not None:
            result['Schema'] = self.schema.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Schema') is not None:
            temp_model = main_models.Schema()
            self.schema = temp_model.from_map(m.get('Schema'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

