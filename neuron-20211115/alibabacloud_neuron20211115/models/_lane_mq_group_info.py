# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class LaneMqGroupInfo(DaraModel):
    def __init__(
        self,
        allow_clean: bool = None,
        lane_id: int = None,
        lane_name: str = None,
        mq_groups: main_models.MqGroup = None,
    ):
        self.allow_clean = allow_clean
        self.lane_id = lane_id
        self.lane_name = lane_name
        self.mq_groups = mq_groups

    def validate(self):
        if self.mq_groups:
            self.mq_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_clean is not None:
            result['allowClean'] = self.allow_clean

        if self.lane_id is not None:
            result['laneId'] = self.lane_id

        if self.lane_name is not None:
            result['laneName'] = self.lane_name

        if self.mq_groups is not None:
            result['mqGroups'] = self.mq_groups.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowClean') is not None:
            self.allow_clean = m.get('allowClean')

        if m.get('laneId') is not None:
            self.lane_id = m.get('laneId')

        if m.get('laneName') is not None:
            self.lane_name = m.get('laneName')

        if m.get('mqGroups') is not None:
            temp_model = main_models.MqGroup()
            self.mq_groups = temp_model.from_map(m.get('mqGroups'))

        return self

