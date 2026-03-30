# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetGovernanceReportStatusResponseBody(DaraModel):
    def __init__(
        self,
        governance_items_status: main_models.GetGovernanceReportStatusResponseBodyGovernanceItemsStatus = None,
        request_id: str = None,
        whole_report_status: str = None,
    ):
        self.governance_items_status = governance_items_status
        self.request_id = request_id
        self.whole_report_status = whole_report_status

    def validate(self):
        if self.governance_items_status:
            self.governance_items_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.governance_items_status is not None:
            result['GovernanceItemsStatus'] = self.governance_items_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.whole_report_status is not None:
            result['WholeReportStatus'] = self.whole_report_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GovernanceItemsStatus') is not None:
            temp_model = main_models.GetGovernanceReportStatusResponseBodyGovernanceItemsStatus()
            self.governance_items_status = temp_model.from_map(m.get('GovernanceItemsStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WholeReportStatus') is not None:
            self.whole_report_status = m.get('WholeReportStatus')

        return self

class GetGovernanceReportStatusResponseBodyGovernanceItemsStatus(DaraModel):
    def __init__(
        self,
        governance_item_status: List[main_models.GetGovernanceReportStatusResponseBodyGovernanceItemsStatusGovernanceItemStatus] = None,
    ):
        self.governance_item_status = governance_item_status

    def validate(self):
        if self.governance_item_status:
            for v1 in self.governance_item_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GovernanceItemStatus'] = []
        if self.governance_item_status is not None:
            for k1 in self.governance_item_status:
                result['GovernanceItemStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.governance_item_status = []
        if m.get('GovernanceItemStatus') is not None:
            for k1 in m.get('GovernanceItemStatus'):
                temp_model = main_models.GetGovernanceReportStatusResponseBodyGovernanceItemsStatusGovernanceItemStatus()
                self.governance_item_status.append(temp_model.from_map(k1))

        return self

class GetGovernanceReportStatusResponseBodyGovernanceItemsStatusGovernanceItemStatus(DaraModel):
    def __init__(
        self,
        governance_item: str = None,
        status: str = None,
    ):
        self.governance_item = governance_item
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.governance_item is not None:
            result['GovernanceItem'] = self.governance_item

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GovernanceItem') is not None:
            self.governance_item = m.get('GovernanceItem')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

