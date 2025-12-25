# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOnlineDDLProgressRequest(DaraModel):
    def __init__(
        self,
        job_detail_id: int = None,
        tid: int = None,
    ):
        # The ID of the OnlineDDL SQL task details. You can call the [ListDBTaskSQLJobDetail](https://help.aliyun.com/document_detail/207073.html) operation to obtain the task detail ID.
        # 
        # This parameter is required.
        self.job_detail_id = job_detail_id
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html) topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_detail_id is not None:
            result['JobDetailId'] = self.job_detail_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobDetailId') is not None:
            self.job_detail_id = m.get('JobDetailId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

