# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class UnifiedQueryContext(DaraModel):
    def __init__(
        self,
        engine_type: str = None,
        original_query: main_models.UnifiedOriginalQuery = None,
        rewrite: main_models.UnifiedRewrite = None,
    ):
        self.engine_type = engine_type
        self.original_query = original_query
        self.rewrite = rewrite

    def validate(self):
        if self.original_query:
            self.original_query.validate()
        if self.rewrite:
            self.rewrite.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_type is not None:
            result['engineType'] = self.engine_type

        if self.original_query is not None:
            result['originalQuery'] = self.original_query.to_map()

        if self.rewrite is not None:
            result['rewrite'] = self.rewrite.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')

        if m.get('originalQuery') is not None:
            temp_model = main_models.UnifiedOriginalQuery()
            self.original_query = temp_model.from_map(m.get('originalQuery'))

        if m.get('rewrite') is not None:
            temp_model = main_models.UnifiedRewrite()
            self.rewrite = temp_model.from_map(m.get('rewrite'))

        return self

