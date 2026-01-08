# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAclChecksResponseBody(DaraModel):
    def __init__(
        self,
        check_records: main_models.DescribeAclChecksResponseBodyCheckRecords = None,
        request_id: str = None,
    ):
        self.check_records = check_records
        self.request_id = request_id

    def validate(self):
        if self.check_records:
            self.check_records.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_records is not None:
            result['CheckRecords'] = self.check_records.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRecords') is not None:
            temp_model = main_models.DescribeAclChecksResponseBodyCheckRecords()
            self.check_records = temp_model.from_map(m.get('CheckRecords'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAclChecksResponseBodyCheckRecords(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        records: List[main_models.DescribeAclChecksResponseBodyCheckRecordsRecords] = None,
    ):
        self.acl_type = acl_type
        self.records = records

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.DescribeAclChecksResponseBodyCheckRecordsRecords()
                self.records.append(temp_model.from_map(k1))

        return self

class DescribeAclChecksResponseBodyCheckRecordsRecords(DaraModel):
    def __init__(
        self,
        acl_pending_count: int = None,
        acl_total_count: int = None,
        check_name: str = None,
        check_status: str = None,
        check_type: str = None,
        last_check_time: str = None,
        level: str = None,
        task_id: str = None,
    ):
        self.acl_pending_count = acl_pending_count
        self.acl_total_count = acl_total_count
        self.check_name = check_name
        self.check_status = check_status
        self.check_type = check_type
        self.last_check_time = last_check_time
        self.level = level
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_pending_count is not None:
            result['AclPendingCount'] = self.acl_pending_count

        if self.acl_total_count is not None:
            result['AclTotalCount'] = self.acl_total_count

        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        if self.level is not None:
            result['Level'] = self.level

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclPendingCount') is not None:
            self.acl_pending_count = m.get('AclPendingCount')

        if m.get('AclTotalCount') is not None:
            self.acl_total_count = m.get('AclTotalCount')

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

