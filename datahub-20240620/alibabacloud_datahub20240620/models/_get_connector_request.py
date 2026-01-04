# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConnectorRequest(DaraModel):
    def __init__(
        self,
        connector_id: str = None,
        project_name: str = None,
        topic_name: str = None,
    ):
        # This parameter is required.
        self.connector_id = connector_id
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

