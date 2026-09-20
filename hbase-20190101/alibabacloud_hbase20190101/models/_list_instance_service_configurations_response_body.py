# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class ListInstanceServiceConfigurationsResponseBody(DaraModel):
    def __init__(
        self,
        configure_list: main_models.ListInstanceServiceConfigurationsResponseBodyConfigureList = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.configure_list = configure_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.configure_list:
            self.configure_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configure_list is not None:
            result['ConfigureList'] = self.configure_list.to_map()

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
        if m.get('ConfigureList') is not None:
            temp_model = main_models.ListInstanceServiceConfigurationsResponseBodyConfigureList()
            self.configure_list = temp_model.from_map(m.get('ConfigureList'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListInstanceServiceConfigurationsResponseBodyConfigureList(DaraModel):
    def __init__(
        self,
        config: List[main_models.ListInstanceServiceConfigurationsResponseBodyConfigureListConfig] = None,
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
                temp_model = main_models.ListInstanceServiceConfigurationsResponseBodyConfigureListConfig()
                self.config.append(temp_model.from_map(k1))

        return self

class ListInstanceServiceConfigurationsResponseBodyConfigureListConfig(DaraModel):
    def __init__(
        self,
        configure_name: str = None,
        configure_unit: str = None,
        default_value: str = None,
        description: str = None,
        need_restart: str = None,
        running_value: str = None,
        value_range: str = None,
    ):
        self.configure_name = configure_name
        self.configure_unit = configure_unit
        self.default_value = default_value
        self.description = description
        self.need_restart = need_restart
        self.running_value = running_value
        self.value_range = value_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configure_name is not None:
            result['ConfigureName'] = self.configure_name

        if self.configure_unit is not None:
            result['ConfigureUnit'] = self.configure_unit

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.need_restart is not None:
            result['NeedRestart'] = self.need_restart

        if self.running_value is not None:
            result['RunningValue'] = self.running_value

        if self.value_range is not None:
            result['ValueRange'] = self.value_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigureName') is not None:
            self.configure_name = m.get('ConfigureName')

        if m.get('ConfigureUnit') is not None:
            self.configure_unit = m.get('ConfigureUnit')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NeedRestart') is not None:
            self.need_restart = m.get('NeedRestart')

        if m.get('RunningValue') is not None:
            self.running_value = m.get('RunningValue')

        if m.get('ValueRange') is not None:
            self.value_range = m.get('ValueRange')

        return self

