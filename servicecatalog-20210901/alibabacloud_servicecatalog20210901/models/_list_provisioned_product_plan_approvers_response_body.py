# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListProvisionedProductPlanApproversResponseBody(DaraModel):
    def __init__(
        self,
        approvers: List[main_models.ListProvisionedProductPlanApproversResponseBodyApprovers] = None,
        request_id: str = None,
    ):
        # An array that consists of reviewers.
        self.approvers = approvers
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.approvers:
            for v1 in self.approvers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Approvers'] = []
        if self.approvers is not None:
            for k1 in self.approvers:
                result['Approvers'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approvers = []
        if m.get('Approvers') is not None:
            for k1 in m.get('Approvers'):
                temp_model = main_models.ListProvisionedProductPlanApproversResponseBodyApprovers()
                self.approvers.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProvisionedProductPlanApproversResponseBodyApprovers(DaraModel):
    def __init__(
        self,
        principal_name: str = None,
        principal_type: str = None,
    ):
        # The name of the reviewer.
        self.principal_name = principal_name
        # The type of the Resource Access Management (RAM) entity of the reviewer. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

