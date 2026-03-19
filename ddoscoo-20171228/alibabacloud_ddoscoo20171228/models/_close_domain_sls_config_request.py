# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloseDomainSlsConfigRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

