# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetErServiceResponseBody(DaraModel):
    def __init__(
        self,
        plan_name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The billing mode. Valid values:
        # 
        # *   er_paymode: billed for customers on the China site.
        # *   er_freemode: free for customers on the China site.
        # *   er_paymodeintl: billed for customers on the International site.
        # *   err_freemodeintl: free for customers on the International site
        self.plan_name = plan_name
        # The request ID.
        self.request_id = request_id
        # The service status. Valid values:
        # 
        # *   Creating
        # *   Running
        # *   NotOpened
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

