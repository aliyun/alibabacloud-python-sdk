# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeShowStorageInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeShowStorageInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeShowStorageInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeShowStorageInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        storage_infos: List[main_models.DescribeShowStorageInfoResponseBodyDataStorageInfos] = None,
    ):
        self.storage_infos = storage_infos

    def validate(self):
        if self.storage_infos:
            for v1 in self.storage_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StorageInfos'] = []
        if self.storage_infos is not None:
            for k1 in self.storage_infos:
                result['StorageInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.storage_infos = []
        if m.get('StorageInfos') is not None:
            for k1 in m.get('StorageInfos'):
                temp_model = main_models.DescribeShowStorageInfoResponseBodyDataStorageInfos()
                self.storage_infos.append(temp_model.from_map(k1))

        return self

class DescribeShowStorageInfoResponseBodyDataStorageInfos(DaraModel):
    def __init__(
        self,
        class_: str = None,
        db_count: int = None,
        deletable: bool = None,
        group_count: int = None,
        inst_kind: str = None,
        is_healthy: bool = None,
        leader_node: str = None,
        status: int = None,
        storage_inst_name: str = None,
    ):
        self.class_ = class_
        self.db_count = db_count
        self.deletable = deletable
        self.group_count = group_count
        self.inst_kind = inst_kind
        self.is_healthy = is_healthy
        self.leader_node = leader_node
        self.status = status
        self.storage_inst_name = storage_inst_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_ is not None:
            result['Class'] = self.class_

        if self.db_count is not None:
            result['DbCount'] = self.db_count

        if self.deletable is not None:
            result['Deletable'] = self.deletable

        if self.group_count is not None:
            result['GroupCount'] = self.group_count

        if self.inst_kind is not None:
            result['InstKind'] = self.inst_kind

        if self.is_healthy is not None:
            result['IsHealthy'] = self.is_healthy

        if self.leader_node is not None:
            result['LeaderNode'] = self.leader_node

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_inst_name is not None:
            result['StorageInstName'] = self.storage_inst_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')

        if m.get('DbCount') is not None:
            self.db_count = m.get('DbCount')

        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')

        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')

        if m.get('InstKind') is not None:
            self.inst_kind = m.get('InstKind')

        if m.get('IsHealthy') is not None:
            self.is_healthy = m.get('IsHealthy')

        if m.get('LeaderNode') is not None:
            self.leader_node = m.get('LeaderNode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageInstName') is not None:
            self.storage_inst_name = m.get('StorageInstName')

        return self

