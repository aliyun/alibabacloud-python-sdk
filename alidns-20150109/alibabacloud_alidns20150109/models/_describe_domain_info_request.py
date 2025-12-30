# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainInfoRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        need_detail_attributes: bool = None,
    ):
        # The domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The language type.
        self.lang = lang
        # Specifies whether detailed attributes are required. Default value: **false**, which indicates that detailed attributes are not returned.
        # 
        # If you set this parameter to **true**, the values of the following parameters are returned: LineType, MinTtl, RecordLineTreeJson, RecordLines, LineCode, LineDisplayName, LineName, RegionLines, and SlaveDns.
        self.need_detail_attributes = need_detail_attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.need_detail_attributes is not None:
            result['NeedDetailAttributes'] = self.need_detail_attributes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NeedDetailAttributes') is not None:
            self.need_detail_attributes = m.get('NeedDetailAttributes')

        return self

