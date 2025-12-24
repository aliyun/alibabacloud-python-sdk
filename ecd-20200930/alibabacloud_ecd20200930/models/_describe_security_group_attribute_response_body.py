# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityGroupAttributeResponseBody(DaraModel):
    def __init__(
        self,
        egress_permissions: List[main_models.Permission] = None,
        ingress_permissions: List[main_models.Permission] = None,
        request_id: str = None,
    ):
        self.egress_permissions = egress_permissions
        self.ingress_permissions = ingress_permissions
        self.request_id = request_id

    def validate(self):
        if self.egress_permissions:
            for v1 in self.egress_permissions:
                 if v1:
                    v1.validate()
        if self.ingress_permissions:
            for v1 in self.ingress_permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EgressPermissions'] = []
        if self.egress_permissions is not None:
            for k1 in self.egress_permissions:
                result['EgressPermissions'].append(k1.to_map() if k1 else None)

        result['IngressPermissions'] = []
        if self.ingress_permissions is not None:
            for k1 in self.ingress_permissions:
                result['IngressPermissions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.egress_permissions = []
        if m.get('EgressPermissions') is not None:
            for k1 in m.get('EgressPermissions'):
                temp_model = main_models.Permission()
                self.egress_permissions.append(temp_model.from_map(k1))

        self.ingress_permissions = []
        if m.get('IngressPermissions') is not None:
            for k1 in m.get('IngressPermissions'):
                temp_model = main_models.Permission()
                self.ingress_permissions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

