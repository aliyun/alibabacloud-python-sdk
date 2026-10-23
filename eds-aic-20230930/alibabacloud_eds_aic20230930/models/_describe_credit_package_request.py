# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCreditPackageRequest(DaraModel):
    def __init__(
        self,
        credit_package_id: str = None,
        credit_package_status: str = None,
    ):
        # The ID of the credit package.
        self.credit_package_id = credit_package_id
        # The status of the credit package.
        self.credit_package_status = credit_package_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_package_id is not None:
            result['CreditPackageId'] = self.credit_package_id

        if self.credit_package_status is not None:
            result['CreditPackageStatus'] = self.credit_package_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditPackageId') is not None:
            self.credit_package_id = m.get('CreditPackageId')

        if m.get('CreditPackageStatus') is not None:
            self.credit_package_status = m.get('CreditPackageStatus')

        return self

