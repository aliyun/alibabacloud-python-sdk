# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListStreamingDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        data_source_items: List[main_models.ListStreamingDataSourcesResponseBodyDataSourceItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The queried data sources.
        self.data_source_items = data_source_items
        # The page number.
        self.page_number = page_number
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.data_source_items:
            for v1 in self.data_source_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSourceItems'] = []
        if self.data_source_items is not None:
            for k1 in self.data_source_items:
                result['DataSourceItems'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source_items = []
        if m.get('DataSourceItems') is not None:
            for k1 in m.get('DataSourceItems'):
                temp_model = main_models.ListStreamingDataSourcesResponseBodyDataSourceItems()
                self.data_source_items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListStreamingDataSourcesResponseBodyDataSourceItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_source_config: str = None,
        data_source_description: str = None,
        data_source_id: int = None,
        data_source_name: str = None,
        data_source_type: str = None,
        error_message: str = None,
        modify_time: str = None,
        service_id: int = None,
        status: str = None,
    ):
        # The time when the data source was created.
        self.create_time = create_time
        # The configurations of the data source.
        self.data_source_config = data_source_config
        # The description of the data source.
        self.data_source_description = data_source_description
        # The data source ID.
        self.data_source_id = data_source_id
        # The name of the data source.
        self.data_source_name = data_source_name
        # The type of the data source. Valid values:
        # 
        # *   kafka
        self.data_source_type = data_source_type
        # The information about the service status. For example, if the service is in the exception state, the cause of the exception is displayed. If the service is in the running state, this parameter is left empty.
        self.error_message = error_message
        # The time when the data source was last modified.
        self.modify_time = modify_time
        # The service ID.
        self.service_id = service_id
        # The status of the service. Valid values:
        # 
        # *   init
        # *   running
        # *   exception
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source_config is not None:
            result['DataSourceConfig'] = self.data_source_config

        if self.data_source_description is not None:
            result['DataSourceDescription'] = self.data_source_description

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSourceConfig') is not None:
            self.data_source_config = m.get('DataSourceConfig')

        if m.get('DataSourceDescription') is not None:
            self.data_source_description = m.get('DataSourceDescription')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

