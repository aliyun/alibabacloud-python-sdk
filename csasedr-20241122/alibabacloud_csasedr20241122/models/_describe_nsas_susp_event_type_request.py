# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNsasSuspEventTypeRequest(DaraModel):
    def __init__(
        self,
        container_field_name: str = None,
        container_field_value: str = None,
        lang: str = None,
        name: str = None,
        remark: str = None,
        source_ip: str = None,
        uuids: str = None,
    ):
        # The container field. This parameter is not supported by SASE-EDR.
        self.container_field_name = container_field_name
        # The value of the container field. This parameter is not supported by SASE-EDR.
        self.container_field_value = container_field_value
        # The language of the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The name of the security alert type.
        self.name = name
        # The name or IP address of the server.
        self.remark = remark
        # The source IP address.
        self.source_ip = source_ip
        # The UUIDs of the servers. Separate multiple UUIDs with commas (,).
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name

        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')

        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

