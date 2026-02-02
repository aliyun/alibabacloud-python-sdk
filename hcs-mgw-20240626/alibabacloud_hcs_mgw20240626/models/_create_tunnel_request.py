# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class CreateTunnelRequest(DaraModel):
    def __init__(
        self,
        import_tunnel: main_models.CreateTunnelInfo = None,
    ):
        # The details for creating the tunnel.
        self.import_tunnel = import_tunnel

    def validate(self):
        if self.import_tunnel:
            self.import_tunnel.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_tunnel is not None:
            result['ImportTunnel'] = self.import_tunnel.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportTunnel') is not None:
            temp_model = main_models.CreateTunnelInfo()
            self.import_tunnel = temp_model.from_map(m.get('ImportTunnel'))

        return self

