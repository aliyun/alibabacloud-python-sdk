# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDIJobRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        id: int = None,
        project_id: int = None,
    ):
        # This parameter is deprecated. Use the Id parameter instead.
        self.dijob_id = dijob_id
        # The ID of the synchronization task.
        self.id = id
        # The DataWorks workspace ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.id is not None:
            result['Id'] = self.id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

