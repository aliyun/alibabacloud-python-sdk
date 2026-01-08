# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAclBackupListResponseBody(DaraModel):
    def __init__(
        self,
        backups: List[main_models.DescribeAclBackupListResponseBodyBackups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.backups = backups
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.backups:
            for v1 in self.backups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Backups'] = []
        if self.backups is not None:
            for k1 in self.backups:
                result['Backups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backups = []
        if m.get('Backups') is not None:
            for k1 in m.get('Backups'):
                temp_model = main_models.DescribeAclBackupListResponseBodyBackups()
                self.backups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAclBackupListResponseBodyBackups(DaraModel):
    def __init__(
        self,
        acl_count: int = None,
        back_up_time: int = None,
        description: str = None,
    ):
        self.acl_count = acl_count
        self.back_up_time = back_up_time
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_count is not None:
            result['AclCount'] = self.acl_count

        if self.back_up_time is not None:
            result['BackUpTime'] = self.back_up_time

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclCount') is not None:
            self.acl_count = m.get('AclCount')

        if m.get('BackUpTime') is not None:
            self.back_up_time = m.get('BackUpTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

