# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelReportShareRequest(DaraModel):
    def __init__(
        self,
        report_id: str = None,
        share_to_ids: str = None,
        share_to_type: int = None,
    ):
        # The ID of the data work. Data works include data portals, dashboards, workbooks, and ad hoc queries.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The ID of the sharee. It can be a Quick BI user ID or a user group ID.
        # 
        # - If ShareToType is set to 0 (user), the value is the user ID.
        # - If ShareToType is set to 1 (user group), the value is the user group ID.
        # - If ShareToType is set to 2 (organization), the value is the organization ID.
        # 
        # This parameter is required.
        self.share_to_ids = share_to_ids
        # The deletion method. Valid values:
        # 
        # - 0: Delete by user.
        # - 1: Delete by user group.
        # - 2: Delete by organization.
        # 
        # This parameter is required.
        self.share_to_type = share_to_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.share_to_ids is not None:
            result['ShareToIds'] = self.share_to_ids

        if self.share_to_type is not None:
            result['ShareToType'] = self.share_to_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ShareToIds') is not None:
            self.share_to_ids = m.get('ShareToIds')

        if m.get('ShareToType') is not None:
            self.share_to_type = m.get('ShareToType')

        return self

