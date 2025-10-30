# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeStreamingDataSourceResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_source_config: str = None,
        data_source_description: str = None,
        data_source_id: str = None,
        data_source_name: str = None,
        data_source_type: str = None,
        error_message: str = None,
        request_id: str = None,
        service_id: int = None,
        status: str = None,
    ):
        # Creation time.
        self.create_time = create_time
        # Data source configuration information.
        self.data_source_config = data_source_config
        # Data source description.
        self.data_source_description = data_source_description
        # Data source ID.
        self.data_source_id = data_source_id
        # Data source name.
        self.data_source_name = data_source_name
        # Data source type, values include:
        #  -  kafka
        self.data_source_type = data_source_type
        # Service status message, for example, in case of an exception, it will show the reason for the exception. In normal Running state, this value is empty.
        self.error_message = error_message
        # Request ID.
        self.request_id = request_id
        # External data service ID.
        self.service_id = service_id
        # Service status:
        # 
        # - Initializing init
        # 
        # - Running running
        # 
        # - Exception exception
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

