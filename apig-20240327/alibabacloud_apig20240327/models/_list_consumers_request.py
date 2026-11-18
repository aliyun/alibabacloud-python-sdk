# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConsumersRequest(DaraModel):
    def __init__(
        self,
        expire_status: str = None,
        gateway_type: str = None,
        include_expiration_summary: bool = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # The validity status filter. Valid values: Permanent, InEffect, AboutToExpire, and Expired. You can specify multiple values separated by commas to form a union. If this parameter is not specified, all statuses are included and intersected with the name and display status filters.
        self.expire_status = expire_status
        # The gateway type used for filtering. Currently, **AI** and **API** gateway types are supported.
        self.gateway_type = gateway_type
        # Specifies whether to return the full expiration reminder count. Default value: false. The statistical scope is limited only by the current account and gatewayType.
        self.include_expiration_summary = include_expiration_summary
        # The keyword used for fuzzy search by API name.
        self.name_like = name_like
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The display status filter. Valid values: Enabled (enabled and not expired), Disabled (disabled regardless of expiration), and Expired (enabled and expired). If this parameter is not specified, all statuses are included and intersected with other filter conditions.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_status is not None:
            result['expireStatus'] = self.expire_status

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.include_expiration_summary is not None:
            result['includeExpirationSummary'] = self.include_expiration_summary

        if self.name_like is not None:
            result['nameLike'] = self.name_like

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireStatus') is not None:
            self.expire_status = m.get('expireStatus')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('includeExpirationSummary') is not None:
            self.include_expiration_summary = m.get('includeExpirationSummary')

        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

