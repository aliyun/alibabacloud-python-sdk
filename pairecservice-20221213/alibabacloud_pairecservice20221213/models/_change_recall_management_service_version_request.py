# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeRecallManagementServiceVersionRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        recall_management_service_version_id: str = None,
    ):
        self.instance_id = instance_id
        self.recall_management_service_version_id = recall_management_service_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.recall_management_service_version_id is not None:
            result['RecallManagementServiceVersionId'] = self.recall_management_service_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RecallManagementServiceVersionId') is not None:
            self.recall_management_service_version_id = m.get('RecallManagementServiceVersionId')

        return self

