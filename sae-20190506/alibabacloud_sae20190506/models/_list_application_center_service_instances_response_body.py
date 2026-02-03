# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListApplicationCenterServiceInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListApplicationCenterServiceInstancesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListApplicationCenterServiceInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class ListApplicationCenterServiceInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        service_instances: List[main_models.ListApplicationCenterServiceInstancesResponseBodyDataServiceInstances] = None,
    ):
        self.service_instances = service_instances

    def validate(self):
        if self.service_instances:
            for v1 in self.service_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServiceInstances'] = []
        if self.service_instances is not None:
            for k1 in self.service_instances:
                result['ServiceInstances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_instances = []
        if m.get('ServiceInstances') is not None:
            for k1 in m.get('ServiceInstances'):
                temp_model = main_models.ListApplicationCenterServiceInstancesResponseBodyDataServiceInstances()
                self.service_instances.append(temp_model.from_map(k1))

        return self

class ListApplicationCenterServiceInstancesResponseBodyDataServiceInstances(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        service_instance_id: str = None,
        service_name: str = None,
        template_name: str = None,
    ):
        self.create_time = create_time
        self.name = name
        self.service_instance_id = service_instance_id
        self.service_name = service_name
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.name is not None:
            result['Name'] = self.name

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

