# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAckClusterNamespacesRequest(DaraModel):
    def __init__(
        self,
        connector_id: str = None,
    ):
        # The ID of the ACK cluster connector. To obtain this ID, call the [DescribeAckClusterConnectors](~~DescribeAckClusterConnectors~~) operation.
        # 
        # - [DescribeAckClusterConnectors](~~DescribeAckClusterConnectors~~): Queries a list of ACK cluster connectors.
        # 
        # This parameter is required.
        self.connector_id = connector_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        return self

