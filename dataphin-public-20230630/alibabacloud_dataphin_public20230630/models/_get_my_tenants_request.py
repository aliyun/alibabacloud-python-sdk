# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetMyTenantsRequest(DaraModel):
    def __init__(
        self,
        feature_code_list: List[str] = None,
        op_tenant_id: int = None,
    ):
        self.feature_code_list = feature_code_list
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_code_list is not None:
            result['FeatureCodeList'] = self.feature_code_list

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureCodeList') is not None:
            self.feature_code_list = m.get('FeatureCodeList')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

