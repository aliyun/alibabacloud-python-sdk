# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListExternalDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListExternalDataSourcesResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The Hadoop external table services.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListExternalDataSourcesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListExternalDataSourcesResponseBodyItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_source_description: str = None,
        data_source_dir: str = None,
        data_source_id: int = None,
        data_source_name: str = None,
        data_source_status: str = None,
        data_source_type: str = None,
        external_data_service_id: int = None,
        modify_time: str = None,
        status_message: str = None,
    ):
        # The time when the service was created.
        self.create_time = create_time
        # The description of the data source.
        self.data_source_description = data_source_description
        # The service directory in which Hadoop-related configuration files are stored.
        self.data_source_dir = data_source_dir
        # The service ID.
        self.data_source_id = data_source_id
        # The name of the service.
        self.data_source_name = data_source_name
        # The status of the service. Valid values:
        # 
        # *   init
        # *   running
        # *   exception
        self.data_source_status = data_source_status
        # The type of the data source.
        self.data_source_type = data_source_type
        # The Id of external data service
        self.external_data_service_id = external_data_service_id
        # The time when the service was last modified.
        self.modify_time = modify_time
        # The information about the service status. For example, if the service is in the exception state, the cause of the exception is displayed. If the service is in the running state, this parameter is left empty.
        self.status_message = status_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source_description is not None:
            result['DataSourceDescription'] = self.data_source_description

        if self.data_source_dir is not None:
            result['DataSourceDir'] = self.data_source_dir

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_status is not None:
            result['DataSourceStatus'] = self.data_source_status

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.external_data_service_id is not None:
            result['ExternalDataServiceId'] = self.external_data_service_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSourceDescription') is not None:
            self.data_source_description = m.get('DataSourceDescription')

        if m.get('DataSourceDir') is not None:
            self.data_source_dir = m.get('DataSourceDir')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceStatus') is not None:
            self.data_source_status = m.get('DataSourceStatus')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('ExternalDataServiceId') is not None:
            self.external_data_service_id = m.get('ExternalDataServiceId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        return self

