# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDBInstancePlanResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        plan_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The error message returned.
        # 
        # This parameter is returned only when the operation fails.
        self.error_message = error_message
        # The ID of the plan.
        self.plan_id = plan_id
        # The ID of the request.
        self.request_id = request_id
        # The state of the operation.
        # 
        # If the operation is successful, **success** is returned. If the operation fails, this parameter is not returned.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

