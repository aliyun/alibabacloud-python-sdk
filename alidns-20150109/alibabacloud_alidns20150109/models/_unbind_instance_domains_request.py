# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindInstanceDomainsRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        instance_id: str = None,
        lang: str = None,
    ):
        # The domain names.
        # 
        # Separate multiple domain names with commas (,). Up to 100 domain names can be entered.
        # 
        # This parameter is required.
        self.domain_names = domain_names
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

