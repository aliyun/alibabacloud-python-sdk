# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreRangeInfoResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: main_models.DescribeRestoreRangeInfoResponseBodyItems = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        self.items = items
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request succeeded. Valid values:
        # 
        # - **true**: The request succeeded.
        # 
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeRestoreRangeInfoResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeRestoreRangeInfoResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbsrecover_range: List[main_models.DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRange] = None,
    ):
        self.dbsrecover_range = dbsrecover_range

    def validate(self):
        if self.dbsrecover_range:
            for v1 in self.dbsrecover_range:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBSRecoverRange'] = []
        if self.dbsrecover_range is not None:
            for k1 in self.dbsrecover_range:
                result['DBSRecoverRange'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbsrecover_range = []
        if m.get('DBSRecoverRange') is not None:
            for k1 in m.get('DBSRecoverRange'):
                temp_model = main_models.DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRange()
                self.dbsrecover_range.append(temp_model.from_map(k1))

        return self

class DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRange(DaraModel):
    def __init__(
        self,
        backup_source_host: str = None,
        backup_source_instance_id: str = None,
        backup_source_instance_type: str = None,
        backup_source_port: str = None,
        begin_timestamp_for_restore: int = None,
        end_timestamp_for_restore: int = None,
        full_backup_list: main_models.DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupList = None,
        range_type: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
    ):
        self.backup_source_host = backup_source_host
        self.backup_source_instance_id = backup_source_instance_id
        self.backup_source_instance_type = backup_source_instance_type
        self.backup_source_port = backup_source_port
        self.begin_timestamp_for_restore = begin_timestamp_for_restore
        self.end_timestamp_for_restore = end_timestamp_for_restore
        self.full_backup_list = full_backup_list
        self.range_type = range_type
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_instance_type = source_endpoint_instance_type

    def validate(self):
        if self.full_backup_list:
            self.full_backup_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_source_host is not None:
            result['BackupSourceHost'] = self.backup_source_host

        if self.backup_source_instance_id is not None:
            result['BackupSourceInstanceId'] = self.backup_source_instance_id

        if self.backup_source_instance_type is not None:
            result['BackupSourceInstanceType'] = self.backup_source_instance_type

        if self.backup_source_port is not None:
            result['BackupSourcePort'] = self.backup_source_port

        if self.begin_timestamp_for_restore is not None:
            result['BeginTimestampForRestore'] = self.begin_timestamp_for_restore

        if self.end_timestamp_for_restore is not None:
            result['EndTimestampForRestore'] = self.end_timestamp_for_restore

        if self.full_backup_list is not None:
            result['FullBackupList'] = self.full_backup_list.to_map()

        if self.range_type is not None:
            result['RangeType'] = self.range_type

        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id

        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSourceHost') is not None:
            self.backup_source_host = m.get('BackupSourceHost')

        if m.get('BackupSourceInstanceId') is not None:
            self.backup_source_instance_id = m.get('BackupSourceInstanceId')

        if m.get('BackupSourceInstanceType') is not None:
            self.backup_source_instance_type = m.get('BackupSourceInstanceType')

        if m.get('BackupSourcePort') is not None:
            self.backup_source_port = m.get('BackupSourcePort')

        if m.get('BeginTimestampForRestore') is not None:
            self.begin_timestamp_for_restore = m.get('BeginTimestampForRestore')

        if m.get('EndTimestampForRestore') is not None:
            self.end_timestamp_for_restore = m.get('EndTimestampForRestore')

        if m.get('FullBackupList') is not None:
            temp_model = main_models.DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupList()
            self.full_backup_list = temp_model.from_map(m.get('FullBackupList'))

        if m.get('RangeType') is not None:
            self.range_type = m.get('RangeType')

        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')

        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')

        return self

class DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupList(DaraModel):
    def __init__(
        self,
        full_backup_detail: List[main_models.DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupListFullBackupDetail] = None,
    ):
        self.full_backup_detail = full_backup_detail

    def validate(self):
        if self.full_backup_detail:
            for v1 in self.full_backup_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FullBackupDetail'] = []
        if self.full_backup_detail is not None:
            for k1 in self.full_backup_detail:
                result['FullBackupDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.full_backup_detail = []
        if m.get('FullBackupDetail') is not None:
            for k1 in m.get('FullBackupDetail'):
                temp_model = main_models.DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupListFullBackupDetail()
                self.full_backup_detail.append(temp_model.from_map(k1))

        return self

class DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupListFullBackupDetail(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        end_time: int = None,
        start_time: int = None,
    ):
        self.backup_set_id = backup_set_id
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

