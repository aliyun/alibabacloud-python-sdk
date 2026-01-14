# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAvatarProjectShrinkRequest(DaraModel):
    def __init__(
        self,
        project_id_list_shrink: str = None,
    ):
        self.project_id_list_shrink = project_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id_list_shrink is not None:
            result['projectIdList'] = self.project_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectIdList') is not None:
            self.project_id_list_shrink = m.get('projectIdList')

        return self

