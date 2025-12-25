# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishAndDeployTaskFlowRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        tid: int = None,
        version_comments: str = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid
        # The description of the version.
        self.version_comments = version_comments

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.version_comments is not None:
            result['VersionComments'] = self.version_comments

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('VersionComments') is not None:
            self.version_comments = m.get('VersionComments')

        return self

