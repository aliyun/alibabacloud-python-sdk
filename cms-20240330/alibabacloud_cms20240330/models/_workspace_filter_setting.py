# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class WorkspaceFilterSetting(DaraModel):
    def __init__(
        self,
        tag_selector: main_models.FilterSetting = None,
        workspace_uuids: List[str] = None,
    ):
        self.tag_selector = tag_selector
        self.workspace_uuids = workspace_uuids

    def validate(self):
        if self.tag_selector:
            self.tag_selector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_selector is not None:
            result['tagSelector'] = self.tag_selector.to_map()

        if self.workspace_uuids is not None:
            result['workspaceUuids'] = self.workspace_uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagSelector') is not None:
            temp_model = main_models.FilterSetting()
            self.tag_selector = temp_model.from_map(m.get('tagSelector'))

        if m.get('workspaceUuids') is not None:
            self.workspace_uuids = m.get('workspaceUuids')

        return self

