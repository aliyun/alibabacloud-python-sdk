# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class Revision(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        revision_config: main_models.RevisionConfig = None,
        revision_id: str = None,
        weight: float = None,
    ):
        self.created_time = created_time
        self.description = description
        self.revision_config = revision_config
        self.revision_id = revision_id
        self.weight = weight

    def validate(self):
        if self.revision_config:
            self.revision_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.revision_config is not None:
            result['RevisionConfig'] = self.revision_config.to_map()

        if self.revision_id is not None:
            result['RevisionId'] = self.revision_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RevisionConfig') is not None:
            temp_model = main_models.RevisionConfig()
            self.revision_config = temp_model.from_map(m.get('RevisionConfig'))

        if m.get('RevisionId') is not None:
            self.revision_id = m.get('RevisionId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

