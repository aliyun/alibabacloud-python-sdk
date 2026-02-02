# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class UpdateTunnelInfo(DaraModel):
    def __init__(
        self,
        tags: str = None,
        tunnel_qos: main_models.TunnelQos = None,
    ):
        self.tags = tags
        self.tunnel_qos = tunnel_qos

    def validate(self):
        if self.tunnel_qos:
            self.tunnel_qos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tags is not None:
            result['Tags'] = self.tags

        if self.tunnel_qos is not None:
            result['TunnelQos'] = self.tunnel_qos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TunnelQos') is not None:
            temp_model = main_models.TunnelQos()
            self.tunnel_qos = temp_model.from_map(m.get('TunnelQos'))

        return self

