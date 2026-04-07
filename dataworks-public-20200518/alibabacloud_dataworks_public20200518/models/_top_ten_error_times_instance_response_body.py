# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class TopTenErrorTimesInstanceResponseBody(DaraModel):
    def __init__(
        self,
        instance_error_rank: main_models.TopTenErrorTimesInstanceResponseBodyInstanceErrorRank = None,
        request_id: str = None,
    ):
        # The ranking data of nodes on which errors occurred.
        self.instance_error_rank = instance_error_rank
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_error_rank:
            self.instance_error_rank.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_error_rank is not None:
            result['InstanceErrorRank'] = self.instance_error_rank.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceErrorRank') is not None:
            temp_model = main_models.TopTenErrorTimesInstanceResponseBodyInstanceErrorRank()
            self.instance_error_rank = temp_model.from_map(m.get('InstanceErrorRank'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TopTenErrorTimesInstanceResponseBodyInstanceErrorRank(DaraModel):
    def __init__(
        self,
        error_rank: List[main_models.TopTenErrorTimesInstanceResponseBodyInstanceErrorRankErrorRank] = None,
        update_time: int = None,
    ):
        # The ranking data of nodes on which errors occurred within the last month.
        self.error_rank = error_rank
        # The timestamp at which the rankings were updated.
        self.update_time = update_time

    def validate(self):
        if self.error_rank:
            for v1 in self.error_rank:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorRank'] = []
        if self.error_rank is not None:
            for k1 in self.error_rank:
                result['ErrorRank'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_rank = []
        if m.get('ErrorRank') is not None:
            for k1 in m.get('ErrorRank'):
                temp_model = main_models.TopTenErrorTimesInstanceResponseBodyInstanceErrorRankErrorRank()
                self.error_rank.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class TopTenErrorTimesInstanceResponseBodyInstanceErrorRankErrorRank(DaraModel):
    def __init__(
        self,
        count: int = None,
        node_id: int = None,
        node_name: str = None,
        owner: str = None,
        program_type: int = None,
        project_id: int = None,
    ):
        # The number of errors that occurred on the node.
        self.count = count
        # The node ID.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The ID of the Alibaba Cloud account used by the node owner.
        self.owner = owner
        # The type of the node. Valid values: 6 (Shell), 10 (ODPS SQL), 11 (ODPS MR), 23 (Data Integration), 24 (ODPS Script), 99 (zero load), 221 (PyODPS 2), 225 (ODPS Spark), 227 (EMR Hive), 228 (EMR Spark), 229 (EMR Spark SQL), 230 (EMR MR), 239 (OSS object inspection), 257 (EMR Shell), 258 (EMR Spark Shell), 259 (EMR Presto), 260 (EMR Impala), 900 (real-time synchronization), 1089 (cross-tenant collaboration), 1091 (Hologres development), 1093 (Hologres SQL), 1100 (assignment), and 1221 (PyODPS 3)
        self.program_type = program_type
        # The DataWorks workspace ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.program_type is not None:
            result['ProgramType'] = self.program_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProgramType') is not None:
            self.program_type = m.get('ProgramType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

