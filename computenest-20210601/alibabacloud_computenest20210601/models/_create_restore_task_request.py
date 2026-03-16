# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRestoreTaskRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        service_instance_id: str = None,
    ):
        # The backup ID.
        # 
        # This parameter is required.
        self.backup_id = backup_id
        # The ID of the service instance.
        # 
        # You can call [ListServiceInstances](https://help.aliyun.com/document_detail/396200.html) to obtain the ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

