# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFaceUserGroupAndDeviceGroupRelationRequest(DaraModel):
    def __init__(
        self,
        control_id: str = None,
        isolation_id: str = None,
        relation: str = None,
    ):
        # The control ID of the synchronization relationship between the user group and the device group. Pass the **ControlId** value that you obtained and saved locally when you called the [AddFaceUserGroupAndDeviceGroupRelation](https://help.aliyun.com/document_detail/288342.html) operation to add the face synchronization relationship between the user group and the device group.
        # 
        # This parameter is required.
        self.control_id = control_id
        # The business isolation ID, which is used to isolate data between different business applications under the same Alibaba Cloud account. The value must be the same as the **IsolationId** value that you specified when you called the [AddFaceUserGroupAndDeviceGroupRelation](https://help.aliyun.com/document_detail/288342.html) operation to add the face synchronization relationship between the user group and the device group.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The face synchronization relationship. Currently, only **SYNC_INFO_PICTURE** is supported, which indicates that user photos and user information are synchronized.
        # 
        # This parameter is required.
        self.relation = relation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_id is not None:
            result['ControlId'] = self.control_id

        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        if self.relation is not None:
            result['Relation'] = self.relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')

        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        return self

