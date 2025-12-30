# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateCustomLineRequest(DaraModel):
    def __init__(
        self,
        dns_category: str = None,
        ipv_4s: List[str] = None,
        lang: str = None,
        line_id: str = None,
        name: str = None,
    ):
        self.dns_category = dns_category
        # The IPv4 CIDR blocks.
        # 
        # This parameter is required.
        self.ipv_4s = ipv_4s
        # The language.
        self.lang = lang
        # The unique ID of the custom line.
        # 
        # This parameter is required.
        self.line_id = line_id
        # The name of the custom line.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_category is not None:
            result['DnsCategory'] = self.dns_category

        if self.ipv_4s is not None:
            result['Ipv4s'] = self.ipv_4s

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.line_id is not None:
            result['LineId'] = self.line_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsCategory') is not None:
            self.dns_category = m.get('DnsCategory')

        if m.get('Ipv4s') is not None:
            self.ipv_4s = m.get('Ipv4s')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

