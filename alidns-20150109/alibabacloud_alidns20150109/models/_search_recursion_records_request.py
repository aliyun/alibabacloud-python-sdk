# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchRecursionRecordsRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        enable_status: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        remark: str = None,
        request_source: str = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        value: str = None,
        weight: int = None,
        zone_id: str = None,
    ):
        self.direction = direction
        self.enable_status = enable_status
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.remark = remark
        self.request_source = request_source
        self.rr = rr
        self.ttl = ttl
        self.type = type
        self.value = value
        self.weight = weight
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_source is not None:
            result['RequestSource'] = self.request_source

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.weight is not None:
            result['Weight'] = self.weight

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

