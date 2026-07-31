# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserResourcePackageRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        sort_field: str = None,
        sort_rule: str = None,
        status: str = None,
    ):
        # The resource plan instance ID.
        self.instance_id = instance_id
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        self.security_token = security_token
        # The sorting field. Valid values:
        # - startTime: the effective period of the instance.
        # - endTime: the expiration time of the instance.
        self.sort_field = sort_field
        # The sorting collation. Default value: desc. Valid values:
        # - asc
        # - desc
        self.sort_rule = sort_rule
        # The status of the resource plan. Default value: valid. Valid values:
        # - valid: Valid.
        # - invalid: Invalid.
        # - exhaust: Exhausted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        if self.sort_rule is not None:
            result['SortRule'] = self.sort_rule

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        if m.get('SortRule') is not None:
            self.sort_rule = m.get('SortRule')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

