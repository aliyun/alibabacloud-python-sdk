# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class AlterShareResourcesRequest(DaraModel):
    def __init__(
        self,
        catalog_id: str = None,
        share_resource_list: List[main_models.ShareResource] = None,
    ):
        self.catalog_id = catalog_id
        self.share_resource_list = share_resource_list

    def validate(self):
        if self.share_resource_list:
            for v1 in self.share_resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_id is not None:
            result['catalogId'] = self.catalog_id

        result['shareResourceList'] = []
        if self.share_resource_list is not None:
            for k1 in self.share_resource_list:
                result['shareResourceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogId') is not None:
            self.catalog_id = m.get('catalogId')

        self.share_resource_list = []
        if m.get('shareResourceList') is not None:
            for k1 in m.get('shareResourceList'):
                temp_model = main_models.ShareResource()
                self.share_resource_list.append(temp_model.from_map(k1))

        return self

