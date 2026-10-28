# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDependentQuotasRequest(DaraModel):
    def __init__(
        self,
        product_code: str = None,
        quota_action_code: str = None,
    ):
        # The abbreviated name of the cloud service.
        # 
        # > For more information about how to obtain the abbreviated name of a cloud service, see `ProductCode` in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        # 
        # This parameter is required.
        self.product_code = product_code
        # The quota ID.
        # 
        # > For more information about how to obtain the quota ID of a target cloud service, see `QuotaActionCode` in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # 
        # This parameter is required.
        self.quota_action_code = quota_action_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        return self

