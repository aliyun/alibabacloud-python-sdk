# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListWebApplicationRevisionsOutput(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        revisions: List[main_models.Revision] = None,
    ):
        self.next_token = next_token
        self.revisions = revisions

    def validate(self):
        if self.revisions:
            for v1 in self.revisions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Revisions'] = []
        if self.revisions is not None:
            for k1 in self.revisions:
                result['Revisions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.revisions = []
        if m.get('Revisions') is not None:
            for k1 in m.get('Revisions'):
                temp_model = main_models.Revision()
                self.revisions.append(temp_model.from_map(k1))

        return self

