# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class ListInstanceServiceConfigHistoriesResponseBody(DaraModel):
    def __init__(
        self,
        configure_history_list: main_models.ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryList = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.configure_history_list = configure_history_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.configure_history_list:
            self.configure_history_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configure_history_list is not None:
            result['ConfigureHistoryList'] = self.configure_history_list.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigureHistoryList') is not None:
            temp_model = main_models.ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryList()
            self.configure_history_list = temp_model.from_map(m.get('ConfigureHistoryList'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryList(DaraModel):
    def __init__(
        self,
        config: List[main_models.ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryListConfig] = None,
    ):
        self.config = config

    def validate(self):
        if self.config:
            for v1 in self.config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Config'] = []
        if self.config is not None:
            for k1 in self.config:
                result['Config'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config = []
        if m.get('Config') is not None:
            for k1 in m.get('Config'):
                temp_model = main_models.ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryListConfig()
                self.config.append(temp_model.from_map(k1))

        return self

class ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryListConfig(DaraModel):
    def __init__(
        self,
        configure_name: str = None,
        create_time: str = None,
        effective: str = None,
        new_value: str = None,
        old_value: str = None,
    ):
        self.configure_name = configure_name
        self.create_time = create_time
        self.effective = effective
        self.new_value = new_value
        self.old_value = old_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configure_name is not None:
            result['ConfigureName'] = self.configure_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.effective is not None:
            result['Effective'] = self.effective

        if self.new_value is not None:
            result['NewValue'] = self.new_value

        if self.old_value is not None:
            result['OldValue'] = self.old_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigureName') is not None:
            self.configure_name = m.get('ConfigureName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Effective') is not None:
            self.effective = m.get('Effective')

        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')

        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')

        return self

