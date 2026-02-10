# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudVendorTrialConfigRequest(DaraModel):
    def __init__(
        self,
        auth_id: int = None,
        vendor: str = None,
    ):
        # Unique ID of the AK.
        # 
        # > You can call [DescribeCloudVendorAccountAKList](~~DescribeCloudVendorAccountAKList~~) to get the AuthId.
        # > -
        # 
        # This parameter is required.
        self.auth_id = auth_id
        # Cloud asset vendor. Values:
        # - **Tencent**: Tencent Cloud
        # - **AWS**: Amazon Web Services
        # 
        # This parameter is required.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

