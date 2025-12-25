# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UndeployHttpApiRequest(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
        gateway_id: str = None,
        operation_id: str = None,
        route_id: str = None,
    ):
        # The environment ID.
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.operation_id = operation_id
        # The route ID. You must specify this parameter when you unpublish the route of an HTTP API.
        self.route_id = route_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        if self.route_id is not None:
            result['routeId'] = self.route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')

        return self

