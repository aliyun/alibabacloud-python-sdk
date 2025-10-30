# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeLogBackupsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeLogBackupsResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_log_size: int = None,
    ):
        # Details of the backup sets.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of backup sets on the current page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The total size of logs in the time range. Unit: bytes.
        self.total_log_size = total_log_size

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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_log_size is not None:
            result['TotalLogSize'] = self.total_log_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeLogBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalLogSize') is not None:
            self.total_log_size = m.get('TotalLogSize')

        return self

class DescribeLogBackupsResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        dbinstance_id: str = None,
        log_file_name: str = None,
        log_file_size: int = None,
        log_time: str = None,
        segment_name: str = None,
    ):
        # The ID of the backup set.
        self.backup_id = backup_id
        # The ID of the coordinator node.
        self.dbinstance_id = dbinstance_id
        # The name of the log backup set that is stored in Object Storage Service (OSS).
        self.log_file_name = log_file_name
        # The size of the log backup set. Unit: bytes.
        self.log_file_size = log_file_size
        # The timestamp of the log.
        self.log_time = log_time
        # The name of the compute node.
        self.segment_name = segment_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.log_file_name is not None:
            result['LogFileName'] = self.log_file_name

        if self.log_file_size is not None:
            result['LogFileSize'] = self.log_file_size

        if self.log_time is not None:
            result['LogTime'] = self.log_time

        if self.segment_name is not None:
            result['SegmentName'] = self.segment_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('LogFileName') is not None:
            self.log_file_name = m.get('LogFileName')

        if m.get('LogFileSize') is not None:
            self.log_file_size = m.get('LogFileSize')

        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')

        if m.get('SegmentName') is not None:
            self.segment_name = m.get('SegmentName')

        return self

