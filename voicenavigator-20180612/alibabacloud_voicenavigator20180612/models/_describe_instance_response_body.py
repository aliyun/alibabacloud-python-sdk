# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInstanceResponseBody(DaraModel):
    def __init__(
        self,
        ability_type: str = None,
        applicable_operations: List[str] = None,
        concurrency: int = None,
        description: str = None,
        instance_id: str = None,
        modify_time: int = None,
        modify_user_name: str = None,
        name: str = None,
        nlu_service_params_json: str = None,
        request_id: str = None,
        status: str = None,
        union_instance_id: str = None,
        union_source: str = None,
    ):
        # The capability type of the instance.<br>
        # DEFAULT: Full capabilities.<br>
        # VOICE_ONLY: Voice-only capabilities, which do not include conversation intervention.<br><br>
        self.ability_type = ability_type
        # Applicable operations.
        self.applicable_operations = applicable_operations
        # The concurrency of the instance.
        self.concurrency = concurrency
        # The description of the instance.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The last modification time of the instance.
        self.modify_time = modify_time
        # The user who last modified the instance.
        self.modify_user_name = modify_user_name
        # The instance name.
        self.name = name
        self.nlu_service_params_json = nlu_service_params_json
        # The request ID.
        self.request_id = request_id
        # The status of the instance.
        self.status = status
        self.union_instance_id = union_instance_id
        self.union_source = union_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ability_type is not None:
            result['AbilityType'] = self.ability_type

        if self.applicable_operations is not None:
            result['ApplicableOperations'] = self.applicable_operations

        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

        if self.name is not None:
            result['Name'] = self.name

        if self.nlu_service_params_json is not None:
            result['NluServiceParamsJson'] = self.nlu_service_params_json

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.union_instance_id is not None:
            result['UnionInstanceId'] = self.union_instance_id

        if self.union_source is not None:
            result['UnionSource'] = self.union_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbilityType') is not None:
            self.ability_type = m.get('AbilityType')

        if m.get('ApplicableOperations') is not None:
            self.applicable_operations = m.get('ApplicableOperations')

        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NluServiceParamsJson') is not None:
            self.nlu_service_params_json = m.get('NluServiceParamsJson')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnionInstanceId') is not None:
            self.union_instance_id = m.get('UnionInstanceId')

        if m.get('UnionSource') is not None:
            self.union_source = m.get('UnionSource')

        return self

