# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAuthorizationByUserIdRequest(DaraModel):
    def __init__(
        self,
        qbi_user_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The Quick BI user ID.
        # 
        # This parameter is required.
        self.qbi_user_id = qbi_user_id
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # - dashboard: dashboard
        # - report: workbook
        # - dashboardOfflineQuery: self-service data retrieval
        # - cube: dataset
        # - datasource: data source
        # - screen: data dashboard
        # - ANALYSIS: ad hoc analysis
        # - dataForm: data entry form
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qbi_user_id is not None:
            result['QbiUserId'] = self.qbi_user_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QbiUserId') is not None:
            self.qbi_user_id = m.get('QbiUserId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

