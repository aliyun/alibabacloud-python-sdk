# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeUniBackupStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        protected_database_count: int = None,
        region_count_list: List[main_models.DescribeUniBackupStatisticsResponseBodyRegionCountList] = None,
        request_id: str = None,
        restoring_task_count: int = None,
        total_recoverable_count: int = None,
        total_restore_task_count: int = None,
        unprotected_database_count: int = None,
    ):
        # The number of protected database instances.
        self.protected_database_count = protected_database_count
        # The regions of the database instances.
        self.region_count_list = region_count_list
        # The request ID.
        self.request_id = request_id
        # The number of the restoration tasks that are running.
        self.restoring_task_count = restoring_task_count
        # The total number of database instances that can be restored.
        self.total_recoverable_count = total_recoverable_count
        # The total number of the restoration tasks.
        self.total_restore_task_count = total_restore_task_count
        # The number of unprotected database instances.
        self.unprotected_database_count = unprotected_database_count

    def validate(self):
        if self.region_count_list:
            for v1 in self.region_count_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protected_database_count is not None:
            result['ProtectedDatabaseCount'] = self.protected_database_count

        result['RegionCountList'] = []
        if self.region_count_list is not None:
            for k1 in self.region_count_list:
                result['RegionCountList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restoring_task_count is not None:
            result['RestoringTaskCount'] = self.restoring_task_count

        if self.total_recoverable_count is not None:
            result['TotalRecoverableCount'] = self.total_recoverable_count

        if self.total_restore_task_count is not None:
            result['TotalRestoreTaskCount'] = self.total_restore_task_count

        if self.unprotected_database_count is not None:
            result['UnprotectedDatabaseCount'] = self.unprotected_database_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectedDatabaseCount') is not None:
            self.protected_database_count = m.get('ProtectedDatabaseCount')

        self.region_count_list = []
        if m.get('RegionCountList') is not None:
            for k1 in m.get('RegionCountList'):
                temp_model = main_models.DescribeUniBackupStatisticsResponseBodyRegionCountList()
                self.region_count_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RestoringTaskCount') is not None:
            self.restoring_task_count = m.get('RestoringTaskCount')

        if m.get('TotalRecoverableCount') is not None:
            self.total_recoverable_count = m.get('TotalRecoverableCount')

        if m.get('TotalRestoreTaskCount') is not None:
            self.total_restore_task_count = m.get('TotalRestoreTaskCount')

        if m.get('UnprotectedDatabaseCount') is not None:
            self.unprotected_database_count = m.get('UnprotectedDatabaseCount')

        return self

class DescribeUniBackupStatisticsResponseBodyRegionCountList(DaraModel):
    def __init__(
        self,
        automatic_count: str = None,
        region_id: str = None,
    ):
        # The number of database instances that are automatically scanned.
        self.automatic_count = automatic_count
        # The ID of the region in which the database instance resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.automatic_count is not None:
            result['AutomaticCount'] = self.automatic_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutomaticCount') is not None:
            self.automatic_count = m.get('AutomaticCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

