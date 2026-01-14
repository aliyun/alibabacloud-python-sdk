# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListSpareIpsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        spare_ips: List[main_models.ListSpareIpsResponseBodySpareIps] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The secondary IP addresses that are associated with the CNAME.
        self.spare_ips = spare_ips

    def validate(self):
        if self.spare_ips:
            for v1 in self.spare_ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SpareIps'] = []
        if self.spare_ips is not None:
            for k1 in self.spare_ips:
                result['SpareIps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.spare_ips = []
        if m.get('SpareIps') is not None:
            for k1 in m.get('SpareIps'):
                temp_model = main_models.ListSpareIpsResponseBodySpareIps()
                self.spare_ips.append(temp_model.from_map(k1))

        return self

class ListSpareIpsResponseBodySpareIps(DaraModel):
    def __init__(
        self,
        spare_ip: str = None,
        state: str = None,
    ):
        # The secondary IP address that is associated with the CNAME. If the acceleration area becomes unavailable, GA redirects traffic to the secondary IP address.
        self.spare_ip = spare_ip
        # The status of the secondary IP address. Valid values:
        # 
        # *   **active:** The secondary IP address is available.
        # *   **inuse:** The secondary IP address is in use.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.spare_ip is not None:
            result['SpareIp'] = self.spare_ip

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpareIp') is not None:
            self.spare_ip = m.get('SpareIp')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

