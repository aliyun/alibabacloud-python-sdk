# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudGtmMonitorTemplatesRequest(DaraModel):
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
        # The IP address type of health check nodes. Valid values:
        # 
        # *   IPv4: applicable when health checks are performed on IPv4 addresses.
        # *   IPv6: applicable when health checks are performed on IPv6 addresses.
        self.ip_version = ip_version
        # The name of the health check probe template, which is recommended to be distinguishable for configuration personnel to differentiate and remember, ideally indicating the health check protocol.
        self.name = name
        # Current page number, starting from **1**, default is **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of rows per page when paginating queries, with a maximum value of 100 and a default of 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Protocol types for initiating probes to the target IP address:
        # - ping
        # - tcp
        # - http
        # - https
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

