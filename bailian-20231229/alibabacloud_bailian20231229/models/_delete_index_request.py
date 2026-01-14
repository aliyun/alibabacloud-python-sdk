# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteIndexRequest(DaraModel):
    def __init__(
        self,
        index_id: str = None,
    ):
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_id is not None:
            result['IndexId'] = self.index_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        return self

