# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPostpaidRatePlanInstancesRequest(DaraModel):
    def __init__(
        self,
        check_remaining_site_quota: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        status: str = None,
        unrelated_type: str = None,
    ):
        self.check_remaining_site_quota = check_remaining_site_quota
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.status = status
        self.unrelated_type = unrelated_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_remaining_site_quota is not None:
            result['CheckRemainingSiteQuota'] = self.check_remaining_site_quota

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.status is not None:
            result['Status'] = self.status

        if self.unrelated_type is not None:
            result['UnrelatedType'] = self.unrelated_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRemainingSiteQuota') is not None:
            self.check_remaining_site_quota = m.get('CheckRemainingSiteQuota')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnrelatedType') is not None:
            self.unrelated_type = m.get('UnrelatedType')

        return self

