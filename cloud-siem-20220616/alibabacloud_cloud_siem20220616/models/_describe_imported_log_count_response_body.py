# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeImportedLogCountResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeImportedLogCountResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
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
            temp_model = main_models.DescribeImportedLogCountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImportedLogCountResponseBodyData(DaraModel):
    def __init__(
        self,
        imported_log_count: int = None,
        total_log_count: int = None,
        un_imported_log_count: int = None,
    ):
        # The number of logs that are added.
        self.imported_log_count = imported_log_count
        # The total number of logs.
        self.total_log_count = total_log_count
        # The number of logs that are not added.
        self.un_imported_log_count = un_imported_log_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.imported_log_count is not None:
            result['ImportedLogCount'] = self.imported_log_count

        if self.total_log_count is not None:
            result['TotalLogCount'] = self.total_log_count

        if self.un_imported_log_count is not None:
            result['UnImportedLogCount'] = self.un_imported_log_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportedLogCount') is not None:
            self.imported_log_count = m.get('ImportedLogCount')

        if m.get('TotalLogCount') is not None:
            self.total_log_count = m.get('TotalLogCount')

        if m.get('UnImportedLogCount') is not None:
            self.un_imported_log_count = m.get('UnImportedLogCount')

        return self

