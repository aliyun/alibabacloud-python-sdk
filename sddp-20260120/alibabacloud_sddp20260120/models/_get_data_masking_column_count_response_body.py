# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class GetDataMaskingColumnCountResponseBody(DaraModel):
    def __init__(
        self,
        column_count: main_models.GetDataMaskingColumnCountResponseBodyColumnCount = None,
        request_id: str = None,
    ):
        self.column_count = column_count
        self.request_id = request_id

    def validate(self):
        if self.column_count:
            self.column_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_count is not None:
            result['ColumnCount'] = self.column_count.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnCount') is not None:
            temp_model = main_models.GetDataMaskingColumnCountResponseBodyColumnCount()
            self.column_count = temp_model.from_map(m.get('ColumnCount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataMaskingColumnCountResponseBodyColumnCount(DaraModel):
    def __init__(
        self,
        masked_count: int = None,
        masking_failed_count: int = None,
        sensitive_count: int = None,
        total_count: int = None,
    ):
        self.masked_count = masked_count
        self.masking_failed_count = masking_failed_count
        self.sensitive_count = sensitive_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.masked_count is not None:
            result['MaskedCount'] = self.masked_count

        if self.masking_failed_count is not None:
            result['MaskingFailedCount'] = self.masking_failed_count

        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaskedCount') is not None:
            self.masked_count = m.get('MaskedCount')

        if m.get('MaskingFailedCount') is not None:
            self.masking_failed_count = m.get('MaskingFailedCount')

        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

