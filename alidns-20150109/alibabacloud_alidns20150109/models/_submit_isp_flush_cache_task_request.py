# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SubmitIspFlushCacheTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        domain_name: str = None,
        isp: List[str] = None,
        lang: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.isp = isp
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

