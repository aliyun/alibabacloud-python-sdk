# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class ListShareResourcesResponseBody(DaraModel):
    def __init__(
        self,
        catalog_id: str = None,
        next_page_token: str = None,
        share_resources: List[main_models.ShareResource] = None,
    ):
        self.catalog_id = catalog_id
        self.next_page_token = next_page_token
        self.share_resources = share_resources

    def validate(self):
        if self.share_resources:
            for v1 in self.share_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_id is not None:
            result['catalogId'] = self.catalog_id

        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token

        result['shareResources'] = []
        if self.share_resources is not None:
            for k1 in self.share_resources:
                result['shareResources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogId') is not None:
            self.catalog_id = m.get('catalogId')

        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')

        self.share_resources = []
        if m.get('shareResources') is not None:
            for k1 in m.get('shareResources'):
                temp_model = main_models.ShareResource()
                self.share_resources.append(temp_model.from_map(k1))

        return self

