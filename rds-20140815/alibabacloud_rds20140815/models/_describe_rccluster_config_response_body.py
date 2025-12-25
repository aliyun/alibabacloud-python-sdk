# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCClusterConfigResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        expiration: str = None,
        request_id: str = None,
    ):
        # The kubeconfig file of the cluster.
        self.config = config
        # The expiration time of the kubeconfig file. Format: the UTC time in the RFC3339 format.
        self.expiration = expiration
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

