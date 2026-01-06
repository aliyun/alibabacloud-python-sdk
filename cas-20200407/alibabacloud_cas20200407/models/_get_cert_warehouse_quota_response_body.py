# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCertWarehouseQuotaResponseBody(DaraModel):
    def __init__(
        self,
        app_total_quota: int = None,
        app_use_count: int = None,
        request_id: str = None,
        total_quota: int = None,
        use_count: int = None,
    ):
        self.app_total_quota = app_total_quota
        self.app_use_count = app_use_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total quota for certificate repositories, including the free quota and purchased quota.
        self.total_quota = total_quota
        # The used quota.
        self.use_count = use_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_total_quota is not None:
            result['AppTotalQuota'] = self.app_total_quota

        if self.app_use_count is not None:
            result['AppUseCount'] = self.app_use_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.use_count is not None:
            result['UseCount'] = self.use_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTotalQuota') is not None:
            self.app_total_quota = m.get('AppTotalQuota')

        if m.get('AppUseCount') is not None:
            self.app_use_count = m.get('AppUseCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')

        return self

