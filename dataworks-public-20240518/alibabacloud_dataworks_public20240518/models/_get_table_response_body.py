# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetTableResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        table: main_models.Table = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request succeeded.
        self.success = success
        # Detailed information about the table.
        self.table = table

    def validate(self):
        if self.table:
            self.table.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.table is not None:
            result['Table'] = self.table.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Table') is not None:
            temp_model = main_models.Table()
            self.table = temp_model.from_map(m.get('Table'))

        return self

