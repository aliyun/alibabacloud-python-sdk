# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class GetTunnelResp(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        owner: str = None,
        tags: str = None,
        tunnel_id: str = None,
        tunnel_qos: main_models.TunnelQos = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.owner = owner
        self.tags = tags
        self.tunnel_id = tunnel_id
        self.tunnel_qos = tunnel_qos

    def validate(self):
        if self.tunnel_qos:
            self.tunnel_qos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        if self.tunnel_qos is not None:
            result['TunnelQos'] = self.tunnel_qos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('TunnelQos') is not None:
            temp_model = main_models.TunnelQos()
            self.tunnel_qos = temp_model.from_map(m.get('TunnelQos'))

        return self

