# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class UpdateDataSetRecordResponseBody(DaraModel):
    def __init__(
        self,
        data_set_record_statistic: main_models.UpdateDataSetRecordResponseBodyDataSetRecordStatistic = None,
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
            temp_model = main_models.UpdateDataSetRecordResponseBodyDataSetRecordStatistic()
            self.data_set_record_statistic = temp_model.from_map(m.get('DataSetRecordStatistic'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateDataSetRecordResponseBodyDataSetRecordStatistic(DaraModel):
    def __init__(
        self,
        new_data_set_record_count: int = None,
        update_data_set_record_count: int = None,
    ):
        self.new_data_set_record_count = new_data_set_record_count
        self.update_data_set_record_count = update_data_set_record_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_data_set_record_count is not None:
            result['NewDataSetRecordCount'] = self.new_data_set_record_count

        if self.update_data_set_record_count is not None:
            result['UpdateDataSetRecordCount'] = self.update_data_set_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDataSetRecordCount') is not None:
            self.new_data_set_record_count = m.get('NewDataSetRecordCount')

        if m.get('UpdateDataSetRecordCount') is not None:
            self.update_data_set_record_count = m.get('UpdateDataSetRecordCount')

        return self

