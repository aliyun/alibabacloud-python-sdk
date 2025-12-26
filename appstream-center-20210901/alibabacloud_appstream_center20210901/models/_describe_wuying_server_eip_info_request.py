# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWuyingServerEipInfoRequest(DaraModel):
    def __init__(
        self,
        isp: str = None,
        wuying_server_id: str = None,
    ):
        # The Internet service provider (ISP). Valid values:
        # 
        # *   ChinaMobile: China Mobile
        # *   ChinaTelecom: China Telecom
        # *   ChinaUnicom: China Unicom
        self.isp = isp
        # The ID of the workstation.
        # 
        # This parameter is required.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isp is not None:
            result['Isp'] = self.isp

        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')

        return self

