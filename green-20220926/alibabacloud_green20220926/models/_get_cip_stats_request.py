# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCipStatsRequest(DaraModel):
    def __init__(
        self,
        by_month: bool = None,
        end_date: str = None,
        label: str = None,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        start_date: str = None,
        sub_uid: str = None,
        type: str = None,
    ):
        self.by_month = by_month
        self.end_date = end_date
        self.label = label
        self.region_id = region_id
        self.resource_type = resource_type
        self.service_code = service_code
        self.start_date = start_date
        self.sub_uid = sub_uid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.by_month is not None:
            result['ByMonth'] = self.by_month

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.label is not None:
            result['Label'] = self.label

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByMonth') is not None:
            self.by_month = m.get('ByMonth')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

