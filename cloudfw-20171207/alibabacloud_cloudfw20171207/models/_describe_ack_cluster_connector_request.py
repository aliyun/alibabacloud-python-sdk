# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAckClusterConnectorRequest(DaraModel):
    def __init__(
        self,
        connector_id: str = None,
        lang: str = None,
    ):
        # The ID of the ACK cluster connector. You can obtain the ID by calling the [DescribeAckClusterConnectors](~~DescribeAckClusterConnectors~~) operation to query a list of ACK cluster connectors.
        # 
        # - [DescribeAckClusterConnectors](~~DescribeAckClusterConnectors~~): Queries a list of ACK cluster connectors.
        # 
        # This parameter is required.
        self.connector_id = connector_id
        # The language of the error messages that are returned for the health check status of the ACK cluster connector.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

