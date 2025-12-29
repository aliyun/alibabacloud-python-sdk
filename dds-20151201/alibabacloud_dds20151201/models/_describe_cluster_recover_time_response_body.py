# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterRecoverTimeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        restore_ranges: List[main_models.DescribeClusterRecoverTimeResponseBodyRestoreRanges] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The cluster backup sets of the instance. A cluster backup file contains the backup sets of each node.
        self.restore_ranges = restore_ranges

    def validate(self):
        if self.restore_ranges:
            for v1 in self.restore_ranges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RestoreRanges'] = []
        if self.restore_ranges is not None:
            for k1 in self.restore_ranges:
                result['RestoreRanges'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.restore_ranges = []
        if m.get('RestoreRanges') is not None:
            for k1 in m.get('RestoreRanges'):
                temp_model = main_models.DescribeClusterRecoverTimeResponseBodyRestoreRanges()
                self.restore_ranges.append(temp_model.from_map(k1))

        return self

class DescribeClusterRecoverTimeResponseBodyRestoreRanges(DaraModel):
    def __init__(
        self,
        restore_begin_time: str = None,
        restore_end_time: str = None,
        restore_type: str = None,
    ):
        # The beginning of the time range to which data can be restored.
        self.restore_begin_time = restore_begin_time
        # The end of the time range to which data can be restored.
        self.restore_end_time = restore_end_time
        # The method used to restore data. Valid values:
        # 
        # *   **PointInTime** (default): Data is restored based on point in time
        self.restore_type = restore_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.restore_begin_time is not None:
            result['RestoreBeginTime'] = self.restore_begin_time

        if self.restore_end_time is not None:
            result['RestoreEndTime'] = self.restore_end_time

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreBeginTime') is not None:
            self.restore_begin_time = m.get('RestoreBeginTime')

        if m.get('RestoreEndTime') is not None:
            self.restore_end_time = m.get('RestoreEndTime')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        return self

