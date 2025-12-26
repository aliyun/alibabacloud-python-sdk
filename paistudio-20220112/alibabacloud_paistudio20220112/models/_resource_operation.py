# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceOperation(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        gmt_created_time: str = None,
        gmt_end_time: str = None,
        gmt_modified_time: str = None,
        gmt_start_time: str = None,
        object_id: str = None,
        object_type: str = None,
        operation_description: str = None,
        operation_id: str = None,
        operation_spec_json: str = None,
        operation_type: str = None,
        reason_code: str = None,
        reason_message: str = None,
        status: str = None,
    ):
        self.creator_id = creator_id
        self.gmt_created_time = gmt_created_time
        self.gmt_end_time = gmt_end_time
        self.gmt_modified_time = gmt_modified_time
        self.gmt_start_time = gmt_start_time
        self.object_id = object_id
        self.object_type = object_type
        self.operation_description = operation_description
        self.operation_id = operation_id
        self.operation_spec_json = operation_spec_json
        self.operation_type = operation_type
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time

        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.operation_spec_json is not None:
            result['OperationSpecJson'] = self.operation_spec_json

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')

        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('OperationSpecJson') is not None:
            self.operation_spec_json = m.get('OperationSpecJson')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

