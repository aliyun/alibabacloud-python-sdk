# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20180612 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of instances.
        self.instances = instances
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        applicable_operations: List[str] = None,
        concurrency: int = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        modify_time: int = None,
        modify_user_name: str = None,
        name: str = None,
        nlu_service_params_json: str = None,
        numbers: List[str] = None,
        status: str = None,
        union_instance_id: str = None,
        union_source: str = None,
    ):
        # A list of applicable operations.
        self.applicable_operations = applicable_operations
        # The maximum number of concurrent calls.
        self.concurrency = concurrency
        # The time when the instance was created. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The description of the instance.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The time when the instance was last modified. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.modify_time = modify_time
        # The user who last modified the instance.
        self.modify_user_name = modify_user_name
        # The name of the instance.
        self.name = name
        # The parameters of the NLU service in the JSON format.
        self.nlu_service_params_json = nlu_service_params_json
        # The list of inbound numbers.
        self.numbers = numbers
        # The status of the instance.
        self.status = status
        # The instance ID from the source system.
        # 
        # > If UnionSource is CCC, this parameter indicates the instance ID of the Cloud Communication Center instance.
        self.union_instance_id = union_instance_id
        # The source of the instance.
        # 
        # - `CCC`: Cloud Communication Center
        self.union_source = union_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicable_operations is not None:
            result['ApplicableOperations'] = self.applicable_operations

        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.numbers is not None:
            result['Numbers'] = self.numbers

        if self.status is not None:
            result['Status'] = self.status

        if self.union_instance_id is not None:
            result['UnionInstanceId'] = self.union_instance_id

        if self.union_source is not None:
            result['UnionSource'] = self.union_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableOperations') is not None:
            self.applicable_operations = m.get('ApplicableOperations')

        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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

        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnionInstanceId') is not None:
            self.union_instance_id = m.get('UnionInstanceId')

        if m.get('UnionSource') is not None:
            self.union_source = m.get('UnionSource')

        return self

