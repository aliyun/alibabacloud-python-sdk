# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetInstanceConsumeTimeRankResponseBody(DaraModel):
    def __init__(
        self,
        instance_consume_time_rank: main_models.GetInstanceConsumeTimeRankResponseBodyInstanceConsumeTimeRank = None,
        request_id: str = None,
    ):
        # The ranking record of the running durations of instances.
        self.instance_consume_time_rank = instance_consume_time_rank
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_consume_time_rank:
            self.instance_consume_time_rank.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_consume_time_rank is not None:
            result['InstanceConsumeTimeRank'] = self.instance_consume_time_rank.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceConsumeTimeRank') is not None:
            temp_model = main_models.GetInstanceConsumeTimeRankResponseBodyInstanceConsumeTimeRank()
            self.instance_consume_time_rank = temp_model.from_map(m.get('InstanceConsumeTimeRank'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceConsumeTimeRankResponseBodyInstanceConsumeTimeRank(DaraModel):
    def __init__(
        self,
        consume_time_rank: List[main_models.GetInstanceConsumeTimeRankResponseBodyInstanceConsumeTimeRankConsumeTimeRank] = None,
        update_time: int = None,
    ):
        # The ranking data of the running durations of instances.
        self.consume_time_rank = consume_time_rank
        # The timestamp when the ranking was updated.
        self.update_time = update_time

    def validate(self):
        if self.consume_time_rank:
            for v1 in self.consume_time_rank:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConsumeTimeRank'] = []
        if self.consume_time_rank is not None:
            for k1 in self.consume_time_rank:
                result['ConsumeTimeRank'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consume_time_rank = []
        if m.get('ConsumeTimeRank') is not None:
            for k1 in m.get('ConsumeTimeRank'):
                temp_model = main_models.GetInstanceConsumeTimeRankResponseBodyInstanceConsumeTimeRankConsumeTimeRank()
                self.consume_time_rank.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetInstanceConsumeTimeRankResponseBodyInstanceConsumeTimeRankConsumeTimeRank(DaraModel):
    def __init__(
        self,
        bizdate: int = None,
        consumed: int = None,
        instance_id: int = None,
        node_id: int = None,
        node_name: str = None,
        owner: str = None,
        prg_type: int = None,
    ):
        # The data timestamp of the instance.
        self.bizdate = bizdate
        # The running duration of the instance. Unit: seconds.
        self.consumed = consumed
        # The instance ID.
        self.instance_id = instance_id
        # The node ID.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The ID of the Alibaba Cloud account used by the node owner.
        self.owner = owner
        # The type of the node.
        self.prg_type = prg_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.consumed is not None:
            result['Consumed'] = self.consumed

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.prg_type is not None:
            result['PrgType'] = self.prg_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PrgType') is not None:
            self.prg_type = m.get('PrgType')

        return self

