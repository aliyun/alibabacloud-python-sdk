# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetFileTypeStatisticResponseBody(DaraModel):
    def __init__(
        self,
        program_type_and_counts: List[main_models.GetFileTypeStatisticResponseBodyProgramTypeAndCounts] = None,
        request_id: str = None,
    ):
        # An array of node types and quantity.
        self.program_type_and_counts = program_type_and_counts
        # The ID of the request. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.program_type_and_counts:
            for v1 in self.program_type_and_counts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProgramTypeAndCounts'] = []
        if self.program_type_and_counts is not None:
            for k1 in self.program_type_and_counts:
                result['ProgramTypeAndCounts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.program_type_and_counts = []
        if m.get('ProgramTypeAndCounts') is not None:
            for k1 in m.get('ProgramTypeAndCounts'):
                temp_model = main_models.GetFileTypeStatisticResponseBodyProgramTypeAndCounts()
                self.program_type_and_counts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFileTypeStatisticResponseBodyProgramTypeAndCounts(DaraModel):
    def __init__(
        self,
        count: int = None,
        program_type: str = None,
    ):
        # The number of nodes.
        self.count = count
        # The type of the node.
        # 
        # Valid values:
        # 
        # 6 (Shell node), 10 (ODPS SQL node), 11 (ODPS MR node), 23 (Data Integration node), 24 (ODPS Script node), 99 (zero load node), 221 (PyODPS 2 node), 225 (ODPS Spark node), 227 (EMR Hive node), 228 (EMR Spark node), 229 (EMR Spark SQL node), 230 (EMR MR node), 239 (OSS object inspection node), 257 (EMR Shell node), 258 (EMR Spark Shell node), 259 (EMR Presto node), 260 (EMR Impala node), 900 (real-time data synchronization node), 1089 (cross-tenant collaboration node), 1091 (Hologres development node), 1093 (Hologres SQL node), 1100 (assignment node), and 1221 (PyODPS 3 node).
        self.program_type = program_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.program_type is not None:
            result['ProgramType'] = self.program_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('ProgramType') is not None:
            self.program_type = m.get('ProgramType')

        return self

