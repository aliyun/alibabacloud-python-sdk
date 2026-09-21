# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class ModifySqlLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ModifySqlLogConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The response message.
        # 
        # > If the request is successful, **Successful** is returned. Otherwise, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ModifySqlLogConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ModifySqlLogConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        cold_enable: bool = None,
        cold_retention: int = None,
        cold_start_time: int = None,
        collector_version: str = None,
        hot_enable: bool = None,
        hot_retention: int = None,
        hot_start_time: int = None,
        log_filter: str = None,
        request_enable: bool = None,
        request_start_time: int = None,
        request_stop_time: int = None,
        retention: int = None,
        sql_log_enable: bool = None,
        sql_log_source: str = None,
        sql_log_state: str = None,
        sql_log_visible_time: int = None,
        support_version: str = None,
        version: str = None,
    ):
        # Indicates whether the cold data storage is enabled.
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.cold_enable = cold_enable
        # The retention period of the cold data. Unit: day. This value is calculated by using the following formula: `Retention - HotRetention`.
        self.cold_retention = cold_retention
        # The time when the cold data storage was enabled. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.cold_start_time = cold_start_time
        # The version of the database collector. Valid values:
        # 
        # - **MYSQL_V0**: MySQL V0
        # 
        # - **MYSQL_V1**: MySQL V1
        # 
        # - **MYSQL_V2**: MySQL V2
        # 
        # - **MYSQL_V3**: MySQL V3
        # 
        # - **PG_V1**: PostgreSQL V1
        # 
        # - **rdspg_v1**: ApsaraDB RDS for PostgreSQL V1
        # 
        # - **polarpg_v1**: PolarDB for PostgreSQL V1
        self.collector_version = collector_version
        # Indicates whether the hot data storage is enabled.
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.hot_enable = hot_enable
        # The retention period of the hot data. Unit: day.
        self.hot_retention = hot_retention
        # The time when the hot data storage was enabled. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.hot_start_time = hot_start_time
        # A reserved parameter.
        self.log_filter = log_filter
        # Indicates whether SQL Explorer is enabled.
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.request_enable = request_enable
        # The time when SQL Explorer was enabled. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.request_start_time = request_start_time
        # The expiration time of DAS Enterprise Edition. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.request_stop_time = request_stop_time
        # The total retention period of data. Unit: day.
        self.retention = retention
        # Indicates whether DAS Enterprise Edition is enabled.
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.sql_log_enable = sql_log_enable
        # The source of the audit log.
        self.sql_log_source = sql_log_source
        # The data migration state. Valid values:
        # 
        # - **FINISH**: The historical data is migrated.
        # 
        # - **RUNNING**: The historical data is being migrated.
        # 
        # - **FAILURE**: The historical data fails to be migrated.
        self.sql_log_state = sql_log_state
        # The time when DAS Enterprise Edition was enabled. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.sql_log_visible_time = sql_log_visible_time
        # The latest supported version of DAS Enterprise Edition. Valid values:
        # 
        # - **SQL_LOG_V0**: DAS Enterprise Edition V0
        # 
        # - **SQL_LOG_V1**: DAS Enterprise Edition V1
        # 
        # - **SQL_LOG_V2**: DAS Enterprise Edition V2
        # 
        # - **SQL_LOG_V3**: DAS Enterprise Edition V3
        # 
        # - **SQL_LOG_NOT_ENABLE**: DAS Enterprise Edition is not enabled.
        # 
        # - **SQL_LOG_NOT_SUPPORT**: DAS Enterprise Edition is not supported.
        self.support_version = support_version
        # The current version of DAS Enterprise Edition. Valid values:
        # 
        # - **SQL_LOG_V0**: DAS Enterprise Edition V0
        # 
        # - **SQL_LOG_V1**: DAS Enterprise Edition V1
        # 
        # - **SQL_LOG_V2**: DAS Enterprise Edition V2
        # 
        # - **SQL_LOG_V3**: DAS Enterprise Edition V3
        # 
        # - **SQL_LOG_NOT_ENABLE**: DAS Enterprise Edition is not enabled.
        # 
        # - **SQL_LOG_NOT_SUPPORT**: DAS Enterprise Edition is not supported.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_enable is not None:
            result['ColdEnable'] = self.cold_enable

        if self.cold_retention is not None:
            result['ColdRetention'] = self.cold_retention

        if self.cold_start_time is not None:
            result['ColdStartTime'] = self.cold_start_time

        if self.collector_version is not None:
            result['CollectorVersion'] = self.collector_version

        if self.hot_enable is not None:
            result['HotEnable'] = self.hot_enable

        if self.hot_retention is not None:
            result['HotRetention'] = self.hot_retention

        if self.hot_start_time is not None:
            result['HotStartTime'] = self.hot_start_time

        if self.log_filter is not None:
            result['LogFilter'] = self.log_filter

        if self.request_enable is not None:
            result['RequestEnable'] = self.request_enable

        if self.request_start_time is not None:
            result['RequestStartTime'] = self.request_start_time

        if self.request_stop_time is not None:
            result['RequestStopTime'] = self.request_stop_time

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.sql_log_enable is not None:
            result['SqlLogEnable'] = self.sql_log_enable

        if self.sql_log_source is not None:
            result['SqlLogSource'] = self.sql_log_source

        if self.sql_log_state is not None:
            result['SqlLogState'] = self.sql_log_state

        if self.sql_log_visible_time is not None:
            result['SqlLogVisibleTime'] = self.sql_log_visible_time

        if self.support_version is not None:
            result['SupportVersion'] = self.support_version

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdEnable') is not None:
            self.cold_enable = m.get('ColdEnable')

        if m.get('ColdRetention') is not None:
            self.cold_retention = m.get('ColdRetention')

        if m.get('ColdStartTime') is not None:
            self.cold_start_time = m.get('ColdStartTime')

        if m.get('CollectorVersion') is not None:
            self.collector_version = m.get('CollectorVersion')

        if m.get('HotEnable') is not None:
            self.hot_enable = m.get('HotEnable')

        if m.get('HotRetention') is not None:
            self.hot_retention = m.get('HotRetention')

        if m.get('HotStartTime') is not None:
            self.hot_start_time = m.get('HotStartTime')

        if m.get('LogFilter') is not None:
            self.log_filter = m.get('LogFilter')

        if m.get('RequestEnable') is not None:
            self.request_enable = m.get('RequestEnable')

        if m.get('RequestStartTime') is not None:
            self.request_start_time = m.get('RequestStartTime')

        if m.get('RequestStopTime') is not None:
            self.request_stop_time = m.get('RequestStopTime')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('SqlLogEnable') is not None:
            self.sql_log_enable = m.get('SqlLogEnable')

        if m.get('SqlLogSource') is not None:
            self.sql_log_source = m.get('SqlLogSource')

        if m.get('SqlLogState') is not None:
            self.sql_log_state = m.get('SqlLogState')

        if m.get('SqlLogVisibleTime') is not None:
            self.sql_log_visible_time = m.get('SqlLogVisibleTime')

        if m.get('SupportVersion') is not None:
            self.support_version = m.get('SupportVersion')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

