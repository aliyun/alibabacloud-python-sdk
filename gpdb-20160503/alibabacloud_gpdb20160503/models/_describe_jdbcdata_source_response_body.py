# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeJDBCDataSourceResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_source_description: str = None,
        data_source_id: str = None,
        data_source_name: str = None,
        data_source_status: str = None,
        data_source_type: str = None,
        external_data_service_id: str = None,
        jdbcconnection_string: str = None,
        jdbcpassword: str = None,
        jdbcuser_name: str = None,
        modify_time: str = None,
        request_id: str = None,
        status_message: str = None,
    ):
        # The time when the service was created.
        self.create_time = create_time
        # The description of the service. The description can be up to 256 characters in length.
        self.data_source_description = data_source_description
        # The data source ID.
        self.data_source_id = data_source_id
        # The name of data soruce
        self.data_source_name = data_source_name
        # The status of the service. Valid values:
        # 
        # *   Init
        # *   Running
        # *   Exception
        self.data_source_status = data_source_status
        # The type of the data source.
        self.data_source_type = data_source_type
        # The id of the external data service
        self.external_data_service_id = external_data_service_id
        # The JDBC connection string.
        self.jdbcconnection_string = jdbcconnection_string
        # The password of the database account.
        self.jdbcpassword = jdbcpassword
        # The name of the database account.
        self.jdbcuser_name = jdbcuser_name
        # The time when the data source was last modified.
        self.modify_time = modify_time
        # The request ID.
        self.request_id = request_id
        # The message of the status
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

        if self.jdbcconnection_string is not None:
            result['JDBCConnectionString'] = self.jdbcconnection_string

        if self.jdbcpassword is not None:
            result['JDBCPassword'] = self.jdbcpassword

        if self.jdbcuser_name is not None:
            result['JDBCUserName'] = self.jdbcuser_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSourceDescription') is not None:
            self.data_source_description = m.get('DataSourceDescription')

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

        if m.get('JDBCConnectionString') is not None:
            self.jdbcconnection_string = m.get('JDBCConnectionString')

        if m.get('JDBCPassword') is not None:
            self.jdbcpassword = m.get('JDBCPassword')

        if m.get('JDBCUserName') is not None:
            self.jdbcuser_name = m.get('JDBCUserName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        return self

