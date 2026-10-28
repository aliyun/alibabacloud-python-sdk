# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSearchConditionRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        type: str = None,
    ):
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The source IP address.
        self.source_ip = source_ip
        # The Asset Type to query. Valid values:
        # 
        # - **ecs**: queries the filter conditions for all ECS servers.
        # - **cloud_product**: queries the filter conditions for all other cloud services.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

