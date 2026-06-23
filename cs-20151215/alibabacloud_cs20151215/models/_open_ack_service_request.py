# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenAckServiceRequest(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The type of service to activate. Valid values:
        # 
        # - `propayasgo`: Container Service for Kubernetes (including ACK managed clusters and ACK dedicated clusters), Container Service Serverless, and registered clusters.
        # - `edgepayasgo`: Container Service Edge.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

