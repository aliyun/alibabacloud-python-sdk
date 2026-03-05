# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelservice20220614 import models as main_models
from darabonba.model import DaraModel

class ListRechargeBillsResponseBody(DaraModel):
    def __init__(
        self,
        instanse_infos: List[main_models.ListRechargeBillsResponseBodyInstanseInfos] = None,
        request_id: str = None,
        residue_amount: int = None,
        total_count: int = None,
    ):
        self.instanse_infos = instanse_infos
        self.request_id = request_id
        self.residue_amount = residue_amount
        self.total_count = total_count

    def validate(self):
        if self.instanse_infos:
            for v1 in self.instanse_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanseInfos'] = []
        if self.instanse_infos is not None:
            for k1 in self.instanse_infos:
                result['InstanseInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.residue_amount is not None:
            result['ResidueAmount'] = self.residue_amount

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instanse_infos = []
        if m.get('InstanseInfos') is not None:
            for k1 in m.get('InstanseInfos'):
                temp_model = main_models.ListRechargeBillsResponseBodyInstanseInfos()
                self.instanse_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResidueAmount') is not None:
            self.residue_amount = m.get('ResidueAmount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRechargeBillsResponseBodyInstanseInfos(DaraModel):
    def __init__(
        self,
        curr_times: int = None,
        gmt_end_time: str = None,
        init_times: int = None,
        instance_id: str = None,
        source: str = None,
    ):
        self.curr_times = curr_times
        self.gmt_end_time = gmt_end_time
        self.init_times = init_times
        self.instance_id = instance_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.curr_times is not None:
            result['CurrTimes'] = self.curr_times

        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time

        if self.init_times is not None:
            result['InitTimes'] = self.init_times

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrTimes') is not None:
            self.curr_times = m.get('CurrTimes')

        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')

        if m.get('InitTimes') is not None:
            self.init_times = m.get('InitTimes')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

