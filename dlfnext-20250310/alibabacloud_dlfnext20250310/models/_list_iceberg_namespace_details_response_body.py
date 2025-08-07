# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from alibabacloud_dlfnext20250310 import models as main_models 
from typing import List


class ListIcebergNamespaceDetailsResponseBody(DaraModel):
    def __init__(
        self,
        namespace_details: List[main_models.Namespace] = None,
        next_page_token: str = None,
    ):
        self.namespace_details = namespace_details
        self.next_page_token = next_page_token

    def validate(self):
        if self.namespace_details:
            for v1 in self.namespace_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['namespaceDetails'] = []
        if self.namespace_details is not None:
            for k1 in self.namespace_details:
                result['namespaceDetails'].append(k1.to_map() if k1 else None)

        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespace_details = []
        if m.get('namespaceDetails') is not None:
            for k1 in m.get('namespaceDetails'):
                temp_model = main_models.Namespace()
                self.namespace_details.append(temp_model.from_map(k1))

        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')

        return self

