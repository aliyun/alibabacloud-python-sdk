# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class MultimodalQueryContext(DaraModel):
    def __init__(
        self,
        original_query: main_models.MultimodalOriginalQuery = None,
    ):
        self.original_query = original_query

    def validate(self):
        if self.original_query:
            self.original_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.original_query is not None:
            result['originalQuery'] = self.original_query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalQuery') is not None:
            temp_model = main_models.MultimodalOriginalQuery()
            self.original_query = temp_model.from_map(m.get('originalQuery'))

        return self

