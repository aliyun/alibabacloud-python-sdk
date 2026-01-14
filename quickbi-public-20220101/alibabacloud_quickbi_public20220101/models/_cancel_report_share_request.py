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
        # The ID of the work. The works here include BI portal, dashboards, spreadsheets, and self-service access.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The ID of the person to be shared, which may be the user ID of the Quick BI or the user group ID.
        # 
        # *   If ShareToType is 0 (user), ShareTo is the user ID.
        # *   When ShareToType is set to 1 (user group), ShareTo is the user group ID.
        # *   When ShareToType=2 (organization), ShareTo is the ID of the organization.
        # 
        # This parameter is required.
        self.share_to_ids = share_to_ids
        # The deletion method. Valid values:
        # 
        # *   0: Delete by user
        # *   1: Delete by user group
        # *   2: Delete by organization
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

