# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class ListTunnelResponseBody(DaraModel):
    def __init__(
        self,
        import_tunnel_list: main_models.ListTunnelResp = None,
    ):
        # The details of the tunnels.
        self.import_tunnel_list = import_tunnel_list

    def validate(self):
        if self.import_tunnel_list:
            self.import_tunnel_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_tunnel_list is not None:
            result['ImportTunnelList'] = self.import_tunnel_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportTunnelList') is not None:
            temp_model = main_models.ListTunnelResp()
            self.import_tunnel_list = temp_model.from_map(m.get('ImportTunnelList'))

        return self

