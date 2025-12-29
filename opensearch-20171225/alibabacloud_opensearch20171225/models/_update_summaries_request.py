# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class UpdateSummariesRequest(DaraModel):
    def __init__(
        self,
        body: List[main_models.UpdateSummariesRequestBody] = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether the request is a dry run.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.UpdateSummariesRequestBody()
                self.body.append(temp_model.from_map(k1))

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

class UpdateSummariesRequestBody(DaraModel):
    def __init__(
        self,
        element: str = None,
        ellipsis: str = None,
        field: str = None,
        len: int = None,
        snippet: int = None,
    ):
        # The HTML tag that is used to highlight terms in red.
        self.element = element
        # The connector that is used to connect segments.
        self.ellipsis = ellipsis
        # The field.
        self.field = field
        # The length of a segment.
        self.len = len
        # The number of segments.
        self.snippet = snippet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.element is not None:
            result['element'] = self.element

        if self.ellipsis is not None:
            result['ellipsis'] = self.ellipsis

        if self.field is not None:
            result['field'] = self.field

        if self.len is not None:
            result['len'] = self.len

        if self.snippet is not None:
            result['snippet'] = self.snippet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')

        if m.get('ellipsis') is not None:
            self.ellipsis = m.get('ellipsis')

        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('len') is not None:
            self.len = m.get('len')

        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')

        return self

