# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeRecoverableOtsInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        ots_instances: List[main_models.DescribeRecoverableOtsInstancesResponseBodyOtsInstances] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The list of Tablestore instances that can be restored and the tables in the instances.
        self.ots_instances = ots_instances
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.ots_instances:
            for v1 in self.ots_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['OtsInstances'] = []
        if self.ots_instances is not None:
            for k1 in self.ots_instances:
                result['OtsInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.ots_instances = []
        if m.get('OtsInstances') is not None:
            for k1 in m.get('OtsInstances'):
                temp_model = main_models.DescribeRecoverableOtsInstancesResponseBodyOtsInstances()
                self.ots_instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeRecoverableOtsInstancesResponseBodyOtsInstances(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        table_names: List[str] = None,
    ):
        # The name of the Tablestore instance that can be restored.
        self.instance_name = instance_name
        # The names of the tables in the Tablestore instance.
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.table_names is not None:
            result['TableNames'] = self.table_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        return self

