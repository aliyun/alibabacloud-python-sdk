# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IpWhiteListConfigRequest(DaraModel):
    def __init__(
        self,
        ip_white_list: str = None,
        operation: str = None,
    ):
        # Required for increase and delete operations. The IP whitelist. Separate multiple IP addresses with commas.
        self.ip_white_list = ip_white_list
        # The operation type. Valid values:
        # 
        # - ADD: incrementally adds entries.
        # - DELETE: deletes entries.
        # - QUERY: queries entries.
        # 
        # This parameter is required.
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_white_list is not None:
            result['IpWhiteList'] = self.ip_white_list

        if self.operation is not None:
            result['Operation'] = self.operation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpWhiteList') is not None:
            self.ip_white_list = m.get('IpWhiteList')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        return self

