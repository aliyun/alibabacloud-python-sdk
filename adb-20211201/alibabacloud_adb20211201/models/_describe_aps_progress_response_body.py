# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeApsProgressResponseBody(DaraModel):
    def __init__(
        self,
        aps_hive_progress: List[main_models.DescribeApsProgressResponseBodyApsHiveProgress] = None,
        request_id: str = None,
        success_percentage: int = None,
        success_table_count: int = None,
        total_table_count: int = None,
    ):
        # The migration progress.
        self.aps_hive_progress = aps_hive_progress
        # The request ID.
        self.request_id = request_id
        # The success rate.
        self.success_percentage = success_percentage
        # The total number of migrated tables returned.
        self.success_table_count = success_table_count
        # The total number of tables to be migrated.
        self.total_table_count = total_table_count

    def validate(self):
        if self.aps_hive_progress:
            for v1 in self.aps_hive_progress:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApsHiveProgress'] = []
        if self.aps_hive_progress is not None:
            for k1 in self.aps_hive_progress:
                result['ApsHiveProgress'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_percentage is not None:
            result['SuccessPercentage'] = self.success_percentage

        if self.success_table_count is not None:
            result['SuccessTableCount'] = self.success_table_count

        if self.total_table_count is not None:
            result['TotalTableCount'] = self.total_table_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aps_hive_progress = []
        if m.get('ApsHiveProgress') is not None:
            for k1 in m.get('ApsHiveProgress'):
                temp_model = main_models.DescribeApsProgressResponseBodyApsHiveProgress()
                self.aps_hive_progress.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessPercentage') is not None:
            self.success_percentage = m.get('SuccessPercentage')

        if m.get('SuccessTableCount') is not None:
            self.success_table_count = m.get('SuccessTableCount')

        if m.get('TotalTableCount') is not None:
            self.total_table_count = m.get('TotalTableCount')

        return self

class DescribeApsProgressResponseBodyApsHiveProgress(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        progress: str = None,
        speed: str = None,
        tb_name: str = None,
    ):
        # The name of the database.
        self.db_name = db_name
        # The migration progress.
        self.progress = progress
        # The migration speed.
        self.speed = speed
        # The name of the table.
        self.tb_name = tb_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.tb_name is not None:
            result['TbName'] = self.tb_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('TbName') is not None:
            self.tb_name = m.get('TbName')

        return self

