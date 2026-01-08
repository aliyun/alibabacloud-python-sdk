# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInternetSlbRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        instance_id: str = None,
        instance_name: str = None,
        ip_protocol: str = None,
        lang: str = None,
        page_size: str = None,
        port: str = None,
        public_ip: str = None,
        region_no: str = None,
        source_ip: str = None,
        tag: str = None,
    ):
        self.current_page = current_page
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.ip_protocol = ip_protocol
        self.lang = lang
        self.page_size = page_size
        self.port = port
        self.public_ip = public_ip
        self.region_no = region_no
        self.source_ip = source_ip
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

