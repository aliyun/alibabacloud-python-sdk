# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchCloudGtmMonitorTemplatesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        ip_version: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        protocol: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # The IP address type of health check nodes. An exact search is performed based on the IP address type. Valid values:
        # 
        # *   IPv4: applicable when the destination address of health checks is an IPv4 address
        # *   IPv6: applicable when the destination address of health checks is an IPv6 address
        self.ip_version = ip_version
        self.name = name
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

