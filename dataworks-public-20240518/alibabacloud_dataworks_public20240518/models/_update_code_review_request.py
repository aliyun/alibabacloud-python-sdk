# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCodeReviewRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        project_id: int = None,
        status: str = None,
    ):
        # The unique identifier of the review.
        # 
        # This parameter is required.
        self.id = id
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The final decision. Valid values: Accepted, Rejected.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

