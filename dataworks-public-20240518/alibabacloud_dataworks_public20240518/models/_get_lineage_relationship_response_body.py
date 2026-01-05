# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetLineageRelationshipResponseBody(DaraModel):
    def __init__(
        self,
        lineage_relationship: main_models.LineageRelationship = None,
        request_id: str = None,
    ):
        # The lineage structure.
        self.lineage_relationship = lineage_relationship
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.lineage_relationship:
            self.lineage_relationship.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lineage_relationship is not None:
            result['LineageRelationship'] = self.lineage_relationship.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineageRelationship') is not None:
            temp_model = main_models.LineageRelationship()
            self.lineage_relationship = temp_model.from_map(m.get('LineageRelationship'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

