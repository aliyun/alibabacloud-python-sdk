# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MicroServiceDigest(DaraModel):
    def __init__(
        self,
        service_id: int = None,
        service_name: str = None,
        lane_mq_group_infos: main_models.LaneMqGroupInfo = None,
    ):
        self.service_id = service_id
        self.service_name = service_name
        self.lane_mq_group_infos = lane_mq_group_infos

    def validate(self):
        if self.lane_mq_group_infos:
            self.lane_mq_group_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.lane_mq_group_infos is not None:
            result['laneMqGroupInfos'] = self.lane_mq_group_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('laneMqGroupInfos') is not None:
            temp_model = main_models.LaneMqGroupInfo()
            self.lane_mq_group_infos = temp_model.from_map(m.get('laneMqGroupInfos'))

        return self

