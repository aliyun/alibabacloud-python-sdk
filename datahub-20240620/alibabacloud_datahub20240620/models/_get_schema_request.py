# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSchemaRequest(DaraModel):
    def __init__(
        self,
        project_name: str = None,
        topic_name: str = None,
        version_id: str = None,
    ):
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.topic_name = topic_name
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

