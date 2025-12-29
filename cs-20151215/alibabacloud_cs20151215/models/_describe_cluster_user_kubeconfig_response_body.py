# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterUserKubeconfigResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        expiration: str = None,
    ):
        # The kubeconfig file of the cluster.
        self.config = config
        # The expiration time of the kubeconfig file. Format: the UTC time in the RFC3339 format.
        self.expiration = expiration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.expiration is not None:
            result['expiration'] = self.expiration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')

        return self

