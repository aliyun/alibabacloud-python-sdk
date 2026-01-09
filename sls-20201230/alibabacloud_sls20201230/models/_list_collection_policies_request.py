# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCollectionPoliciesRequest(DaraModel):
    def __init__(
        self,
        central_project: str = None,
        data_code: str = None,
        instance_id: str = None,
        offset: int = None,
        policy_name: str = None,
        product_code: str = None,
        size: int = None,
    ):
        self.central_project = central_project
        self.data_code = data_code
        self.instance_id = instance_id
        self.offset = offset
        self.policy_name = policy_name
        # The code of the service.
        self.product_code = product_code
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.central_project is not None:
            result['centralProject'] = self.central_project

        if self.data_code is not None:
            result['dataCode'] = self.data_code

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.offset is not None:
            result['offset'] = self.offset

        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        if self.product_code is not None:
            result['productCode'] = self.product_code

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('centralProject') is not None:
            self.central_project = m.get('centralProject')

        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

