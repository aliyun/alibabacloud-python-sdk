# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs_workbench20220220 import models as main_models
from darabonba.model import DaraModel

class GetInstanceRecordConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        root: main_models.GetInstanceRecordConfigResponseBodyRoot = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root is not None:
            result['Root'] = self.root.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Root') is not None:
            temp_model = main_models.GetInstanceRecordConfigResponseBodyRoot()
            self.root = temp_model.from_map(m.get('Root'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class GetInstanceRecordConfigResponseBodyRoot(DaraModel):
    def __init__(
        self,
        expiration_days: int = None,
        instance_id: str = None,
        parent_id: str = None,
        record_storage_target: str = None,
    ):
        self.expiration_days = expiration_days
        self.instance_id = instance_id
        self.parent_id = parent_id
        self.record_storage_target = record_storage_target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration_days is not None:
            result['ExpirationDays'] = self.expiration_days

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.record_storage_target is not None:
            result['RecordStorageTarget'] = self.record_storage_target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpirationDays') is not None:
            self.expiration_days = m.get('ExpirationDays')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('RecordStorageTarget') is not None:
            self.record_storage_target = m.get('RecordStorageTarget')

        return self

