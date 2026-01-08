# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConfiguredDomainNamesRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        direction: str = None,
        domain_name: str = None,
        group_name: str = None,
        lang: str = None,
        page_size: str = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.current_page = current_page
        # This parameter is required.
        self.direction = direction
        self.domain_name = domain_name
        # This parameter is required.
        self.group_name = group_name
        self.lang = lang
        self.page_size = page_size
        # This parameter is required.
        self.source_code = source_code
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

