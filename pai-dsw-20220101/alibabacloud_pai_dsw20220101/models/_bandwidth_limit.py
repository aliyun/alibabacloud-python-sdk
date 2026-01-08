# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BandwidthLimit(DaraModel):
    def __init__(
        self,
        egress_rate: str = None,
        egress_whitelists: List[str] = None,
        ingress_rate: str = None,
        ingress_whitelists: List[str] = None,
    ):
        self.egress_rate = egress_rate
        self.egress_whitelists = egress_whitelists
        self.ingress_rate = ingress_rate
        self.ingress_whitelists = ingress_whitelists

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_rate is not None:
            result['EgressRate'] = self.egress_rate

        if self.egress_whitelists is not None:
            result['EgressWhitelists'] = self.egress_whitelists

        if self.ingress_rate is not None:
            result['IngressRate'] = self.ingress_rate

        if self.ingress_whitelists is not None:
            result['IngressWhitelists'] = self.ingress_whitelists

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressRate') is not None:
            self.egress_rate = m.get('EgressRate')

        if m.get('EgressWhitelists') is not None:
            self.egress_whitelists = m.get('EgressWhitelists')

        if m.get('IngressRate') is not None:
            self.ingress_rate = m.get('IngressRate')

        if m.get('IngressWhitelists') is not None:
            self.ingress_whitelists = m.get('IngressWhitelists')

        return self

