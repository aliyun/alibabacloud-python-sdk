# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataSetBloodRequest(DaraModel):
    def __init__(
        self,
        data_set_ids: str = None,
        user_id: str = None,
        works_type: str = None,
    ):
        # List of dataset IDs, separated by English commas.
        # 
        # This parameter is required.
        self.data_set_ids = data_set_ids
        # Specify the owner of the report, which is the userId.
        self.user_id = user_id
        # Specify the type of report:
        # - REPORT: Workbooks
        # - dashboardOfflineQuery: Downloads
        # - DASHBOARD: Dashboard
        # - ANALYSIS: Ad Hoc Analysis
        # - SCREEN: Visualization Screen
        # - PAGE: Old dashboard
        self.works_type = works_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_ids is not None:
            result['DataSetIds'] = self.data_set_ids

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.works_type is not None:
            result['WorksType'] = self.works_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetIds') is not None:
            self.data_set_ids = m.get('DataSetIds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')

        return self

