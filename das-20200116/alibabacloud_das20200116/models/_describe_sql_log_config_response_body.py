# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSqlLogConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response code.
        self.code = code
        # The data that is returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.DescribeSqlLogConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSqlLogConfigResponseBodyData(DaraModel):
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
        support_migration: bool = None,
        support_version: str = None,
        version: str = None,
    ):
        # Indicates whether the cold data storage is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.cold_enable = cold_enable
        # The number of days for which the SQL Explorer and Audit data is stored in cold storage.
        self.cold_retention = cold_retention
        # The time when the cold data storage was enabled. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.cold_start_time = cold_start_time
        # The collector version. Valid values:
        # 
        # *   **MYSQL_V0**
        # *   **MYSQL_V1**
        # *   **MYSQL_V2**
        # *   **MYSQL_V3**
        # *   **PG_V1**
        # *   **rdspg_v1**
        # *   **polarpg_v1**
        self.collector_version = collector_version
        # Indicates whether the hot data storage is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.hot_enable = hot_enable
        # The number of days for which the SQL Explorer and Audit data is stored in hot storage.
        self.hot_retention = hot_retention
        # The time when the hot data storage was enabled. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.hot_start_time = hot_start_time
        # A reserved parameter.
        self.log_filter = log_filter
        # Indicates whether the SQL Explorer feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.request_enable = request_enable
        # The time when the SQL Explorer feature was enabled. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.request_start_time = request_start_time
        # The time when DAS Enterprise Edition V1 expired. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.request_stop_time = request_stop_time
        # The total storage duration of the SQL Explorer and Audit data. The value of this parameter is the sum of the values of **HotRetention** and **ColdRetention**. Unit: day.
        self.retention = retention
        # Indicates whether DAS Enterprise Edition is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.sql_log_enable = sql_log_enable
        # A reserved parameter.
        self.sql_log_source = sql_log_source
        # The state of data migration. Valid values:
        # 
        # *   **FINISH**: The historical data is migrated.
        # *   **RUNNING**: The historical data is being migrated.
        # *   **FAILURE**: The historical data fails to be migrated.
        self.sql_log_state = sql_log_state
        # The time when DAS Enterprise Edition was enabled. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.sql_log_visible_time = sql_log_visible_time
        # A reserved parameter.
        self.support_migration = support_migration
        # The latest version of DAS Enterprise Edition that supports the database instance. Valid values:
        # 
        # *   **SQL_LOG_V0**: DAS Enterprise Edition V0.
        # *   **SQL_LOG_V1**: DAS Enterprise version V1.
        # *   **SQL_LOG_V2**: DAS Enterprise Edition V2.
        # *   **SQL_LOG_V3**: DAS Enterprise Edition V3.
        # *   **SQL_LOG_NOT_ENABLE**: DAS Enterprise Edition is not enabled.
        # *   **SQL_LOG_NOT_SUPPORT**: DAS Enterprise Edition is not supported.
        self.support_version = support_version
        # The version of DAS Enterprise Edition that is enabled for the database instance. Valid values:
        # 
        # *   **SQL_LOG_V0**: DAS Enterprise Edition V0.
        # *   **SQL_LOG_V1**: DAS Enterprise version V1.
        # *   **SQL_LOG_V2**: DAS Enterprise Edition V2.
        # *   **SQL_LOG_V3**: DAS Enterprise Edition V3.
        # *   **SQL_LOG_NOT_ENABLE**: DAS Enterprise Edition is not enabled.
        # *   **SQL_LOG_NOT_SUPPORT**: DAS Enterprise Edition is not supported.
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

        if self.support_migration is not None:
            result['SupportMigration'] = self.support_migration

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

        if m.get('SupportMigration') is not None:
            self.support_migration = m.get('SupportMigration')

        if m.get('SupportVersion') is not None:
            self.support_version = m.get('SupportVersion')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

