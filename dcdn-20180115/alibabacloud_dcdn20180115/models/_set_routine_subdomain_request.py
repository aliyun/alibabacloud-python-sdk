# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class SetRoutineSubdomainRequest(DaraModel):
    def __init__(
        self,
        subdomains: Dict[str, Any] = None,
    ):
        # The parameters of the subdomain.
        # 
        # The parameters are in the following format:
        # 
        #     Subdomains: [
        #         "subdomain-test"
        #     ]
        # 
        # This parameter is required.
        self.subdomains = subdomains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.subdomains is not None:
            result['Subdomains'] = self.subdomains

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Subdomains') is not None:
            self.subdomains = m.get('Subdomains')

        return self

