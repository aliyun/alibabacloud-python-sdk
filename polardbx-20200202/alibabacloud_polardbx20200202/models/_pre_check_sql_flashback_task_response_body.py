# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class PreCheckSqlFlashbackTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.PreCheckSqlFlashbackTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result set.
        self.data = data
        # The response message. This parameter is empty when the request succeeds. If the request fails, an exception message is returned, such as an error code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The request result.
        self.success = success

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.PreCheckSqlFlashbackTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PreCheckSqlFlashbackTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        check_result: main_models.PreCheckSqlFlashbackTaskResponseBodyDataCheckResult = None,
    ):
        # The check result.
        self.check_result = check_result

    def validate(self):
        if self.check_result:
            self.check_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_result is not None:
            result['CheckResult'] = self.check_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            temp_model = main_models.PreCheckSqlFlashbackTaskResponseBodyDataCheckResult()
            self.check_result = temp_model.from_map(m.get('CheckResult'))

        return self

class PreCheckSqlFlashbackTaskResponseBodyDataCheckResult(DaraModel):
    def __init__(
        self,
        binlog_exists: bool = None,
        binlog_row_query_event_enabled: bool = None,
        can_upgrade_support_binlog_row_query_events: bool = None,
        has_table: bool = None,
        support_binlog_row_query_events: bool = None,
    ):
        # Indicates whether valid binary log files exist. This value is used to determine whether operations such as flashback and synchronization can be performed.
        self.binlog_exists = binlog_exists
        # Indicates whether the recording of original SQL query events is enabled. Valid values:
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.binlog_row_query_event_enabled = binlog_row_query_event_enabled
        # Indicates whether the upgrade can succeed.
        self.can_upgrade_support_binlog_row_query_events = can_upgrade_support_binlog_row_query_events
        # Indicates whether the table exists. Valid values: true and false.
        self.has_table = has_table
        # Indicates whether log recording is supported. Valid values:
        # - **true**: Supported.
        # - **false**: Not supported.
        self.support_binlog_row_query_events = support_binlog_row_query_events

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binlog_exists is not None:
            result['BinlogExists'] = self.binlog_exists

        if self.binlog_row_query_event_enabled is not None:
            result['BinlogRowQueryEventEnabled'] = self.binlog_row_query_event_enabled

        if self.can_upgrade_support_binlog_row_query_events is not None:
            result['CanUpgradeSupportBinlogRowQueryEvents'] = self.can_upgrade_support_binlog_row_query_events

        if self.has_table is not None:
            result['HasTable'] = self.has_table

        if self.support_binlog_row_query_events is not None:
            result['SupportBinlogRowQueryEvents'] = self.support_binlog_row_query_events

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BinlogExists') is not None:
            self.binlog_exists = m.get('BinlogExists')

        if m.get('BinlogRowQueryEventEnabled') is not None:
            self.binlog_row_query_event_enabled = m.get('BinlogRowQueryEventEnabled')

        if m.get('CanUpgradeSupportBinlogRowQueryEvents') is not None:
            self.can_upgrade_support_binlog_row_query_events = m.get('CanUpgradeSupportBinlogRowQueryEvents')

        if m.get('HasTable') is not None:
            self.has_table = m.get('HasTable')

        if m.get('SupportBinlogRowQueryEvents') is not None:
            self.support_binlog_row_query_events = m.get('SupportBinlogRowQueryEvents')

        return self

