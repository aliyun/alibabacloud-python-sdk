# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class UpdateTaskFlowConstantsRequest(DaraModel):
    def __init__(
        self,
        dag_constants: List[main_models.UpdateTaskFlowConstantsRequestDagConstants] = None,
        dag_id: int = None,
        tid: int = None,
    ):
        # The constants for the task flow.
        self.dag_constants = dag_constants
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        if self.dag_constants:
            for v1 in self.dag_constants:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DagConstants'] = []
        if self.dag_constants is not None:
            for k1 in self.dag_constants:
                result['DagConstants'].append(k1.to_map() if k1 else None)

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dag_constants = []
        if m.get('DagConstants') is not None:
            for k1 in m.get('DagConstants'):
                temp_model = main_models.UpdateTaskFlowConstantsRequestDagConstants()
                self.dag_constants.append(temp_model.from_map(k1))

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class UpdateTaskFlowConstantsRequestDagConstants(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key name of a constant for the task flow.
        self.key = key
        # The key value of a constant for the task flow.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

