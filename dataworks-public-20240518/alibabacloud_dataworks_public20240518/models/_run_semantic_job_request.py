# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunSemanticJobRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the job to run. Use the Data.Name value from the CreateSemanticJob response or the Name value from a ListSemanticJobs list item. The Source, ResourceGroupId, and reference files of the job are determined by the definition saved at creation time.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

