# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ModifyDataSourceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ModifyDataSourceResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request.
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
            temp_model = main_models.ModifyDataSourceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyDataSourceResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
        data_source_instance_id: str = None,
    ):
        # The number of modified data sources. A value of 1 indicates success. A value of 0 or less indicates failure.
        self.count = count
        # The ID of the data source. The ID is an MD5 hash that is calculated based on the values of other parameters.
        self.data_source_instance_id = data_source_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')

        return self

