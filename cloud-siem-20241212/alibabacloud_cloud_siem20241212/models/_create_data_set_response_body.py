# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class CreateDataSetResponseBody(DaraModel):
    def __init__(
        self,
        data_set_record_statistic: main_models.CreateDataSetResponseBodyDataSetRecordStatistic = None,
        request_id: str = None,
    ):
        self.data_set_record_statistic = data_set_record_statistic
        self.request_id = request_id

    def validate(self):
        if self.data_set_record_statistic:
            self.data_set_record_statistic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_record_statistic is not None:
            result['DataSetRecordStatistic'] = self.data_set_record_statistic.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetRecordStatistic') is not None:
            temp_model = main_models.CreateDataSetResponseBodyDataSetRecordStatistic()
            self.data_set_record_statistic = temp_model.from_map(m.get('DataSetRecordStatistic'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateDataSetResponseBodyDataSetRecordStatistic(DaraModel):
    def __init__(
        self,
        data_set_id: str = None,
        new_data_set_record_count: int = None,
    ):
        self.data_set_id = data_set_id
        self.new_data_set_record_count = new_data_set_record_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id

        if self.new_data_set_record_count is not None:
            result['NewDataSetRecordCount'] = self.new_data_set_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')

        if m.get('NewDataSetRecordCount') is not None:
            self.new_data_set_record_count = m.get('NewDataSetRecordCount')

        return self

