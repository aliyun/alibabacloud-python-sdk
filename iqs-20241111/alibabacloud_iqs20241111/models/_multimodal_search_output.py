# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class MultimodalSearchOutput(DaraModel):
    def __init__(
        self,
        image_items: List[main_models.UnifiedImageItem] = None,
        query_context: main_models.MultimodalQueryContext = None,
        request_id: str = None,
        search_information: main_models.SearchInformation = None,
    ):
        self.image_items = image_items
        self.query_context = query_context
        self.request_id = request_id
        self.search_information = search_information

    def validate(self):
        if self.image_items:
            for v1 in self.image_items:
                 if v1:
                    v1.validate()
        if self.query_context:
            self.query_context.validate()
        if self.search_information:
            self.search_information.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['imageItems'] = []
        if self.image_items is not None:
            for k1 in self.image_items:
                result['imageItems'].append(k1.to_map() if k1 else None)

        if self.query_context is not None:
            result['queryContext'] = self.query_context.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.search_information is not None:
            result['searchInformation'] = self.search_information.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_items = []
        if m.get('imageItems') is not None:
            for k1 in m.get('imageItems'):
                temp_model = main_models.UnifiedImageItem()
                self.image_items.append(temp_model.from_map(k1))

        if m.get('queryContext') is not None:
            temp_model = main_models.MultimodalQueryContext()
            self.query_context = temp_model.from_map(m.get('queryContext'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('searchInformation') is not None:
            temp_model = main_models.SearchInformation()
            self.search_information = temp_model.from_map(m.get('searchInformation'))

        return self

