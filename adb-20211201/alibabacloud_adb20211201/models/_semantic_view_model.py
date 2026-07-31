# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SemanticViewModel(DaraModel):
    def __init__(
        self,
        comment: str = None,
        definition: str = None,
        score: float = None,
        view_name: str = None,
        view_schema: str = None,
    ):
        # The annotation for the semantic view
        self.comment = comment
        # The YAML definition of the semantic view
        self.definition = definition
        # The vector retrieval match score (defaults to 1; during retrieval queries, it is a decimal between 0 and 1 representing vector similarity)
        self.score = score
        # The name of the semantic view
        self.view_name = view_name
        # The schema where the semantic view resides
        self.view_schema = view_schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.score is not None:
            result['Score'] = self.score

        if self.view_name is not None:
            result['ViewName'] = self.view_name

        if self.view_schema is not None:
            result['ViewSchema'] = self.view_schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ViewName') is not None:
            self.view_name = m.get('ViewName')

        if m.get('ViewSchema') is not None:
            self.view_schema = m.get('ViewSchema')

        return self

