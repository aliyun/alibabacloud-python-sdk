# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProjectRequest(DaraModel):
    def __init__(
        self,
        verbose: bool = None,
        with_quota_product_type: bool = None,
        with_storage_tier_info: bool = None,
    ):
        # Specifies whether to use additional information.
        self.verbose = verbose
        self.with_quota_product_type = with_quota_product_type
        self.with_storage_tier_info = with_storage_tier_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.verbose is not None:
            result['verbose'] = self.verbose

        if self.with_quota_product_type is not None:
            result['withQuotaProductType'] = self.with_quota_product_type

        if self.with_storage_tier_info is not None:
            result['withStorageTierInfo'] = self.with_storage_tier_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('verbose') is not None:
            self.verbose = m.get('verbose')

        if m.get('withQuotaProductType') is not None:
            self.with_quota_product_type = m.get('withQuotaProductType')

        if m.get('withStorageTierInfo') is not None:
            self.with_storage_tier_info = m.get('withStorageTierInfo')

        return self

