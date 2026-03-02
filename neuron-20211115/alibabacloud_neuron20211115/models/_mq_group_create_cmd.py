# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MqGroupCreateCmd(DaraModel):
    def __init__(
        self,
        env: str = None,
        lane_id: int = None,
        lane_name: str = None,
        message_type: int = None,
        protocol_type: str = None,
        remark: str = None,
        service_id: str = None,
    ):
        self.env = env
        self.lane_id = lane_id
        self.lane_name = lane_name
        self.message_type = message_type
        self.protocol_type = protocol_type
        self.remark = remark
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['env'] = self.env

        if self.lane_id is not None:
            result['laneId'] = self.lane_id

        if self.lane_name is not None:
            result['laneName'] = self.lane_name

        if self.message_type is not None:
            result['messageType'] = self.message_type

        if self.protocol_type is not None:
            result['protocolType'] = self.protocol_type

        if self.remark is not None:
            result['remark'] = self.remark

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('laneId') is not None:
            self.lane_id = m.get('laneId')

        if m.get('laneName') is not None:
            self.lane_name = m.get('laneName')

        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')

        if m.get('protocolType') is not None:
            self.protocol_type = m.get('protocolType')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

