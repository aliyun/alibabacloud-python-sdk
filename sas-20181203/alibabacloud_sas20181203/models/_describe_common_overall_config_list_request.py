# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCommonOverallConfigListRequest(DaraModel):
    def __init__(
        self,
        source_ip: str = None,
        type_list: List[str] = None,
    ):
        # The source IP address of the request.
        self.source_ip = source_ip
        # The types of the configuration items.
        # 
        # >  You can query up to 50 types at a time.
        # 
        # This parameter is required.
        self.type_list = type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type_list is not None:
            result['TypeList'] = self.type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TypeList') is not None:
            self.type_list = m.get('TypeList')

        return self

