# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCaseDetailRequest(DaraModel):
    def __init__(
        self,
        case_id: str = None,
        instance_id: str = None,
        product_code: str = None,
    ):
        # The case ID.
        # 
        # This parameter is required.
        self.case_id = case_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The product code.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_id is not None:
            result['CaseId'] = self.case_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

