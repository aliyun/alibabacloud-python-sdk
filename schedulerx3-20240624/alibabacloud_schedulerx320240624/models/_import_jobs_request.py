# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportJobsRequest(DaraModel):
    def __init__(
        self,
        auto_create_app: bool = None,
        cluster_id: str = None,
        content: str = None,
        overwrite: bool = None,
    ):
        self.auto_create_app = auto_create_app
        # This parameter is required.
        self.cluster_id = cluster_id
        self.content = content
        self.overwrite = overwrite

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create_app is not None:
            result['AutoCreateApp'] = self.auto_create_app

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.content is not None:
            result['Content'] = self.content

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateApp') is not None:
            self.auto_create_app = m.get('AutoCreateApp')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        return self

