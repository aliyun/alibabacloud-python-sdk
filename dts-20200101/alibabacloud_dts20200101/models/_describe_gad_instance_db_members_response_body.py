# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeGadInstanceDbMembersResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        db_engine_type: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        instance_id: str = None,
        instance_name: str = None,
        master_db_instance_id: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        slave_db_instances: main_models.DescribeGadInstanceDbMembersResponseBodySlaveDbInstances = None,
        status: str = None,
        success: str = None,
    ):
        # The timestamp when the instance was created.
        self.create_time = create_time
        # The database engine.
        self.db_engine_type = db_engine_type
        # The dynamic error code associated with the request.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace the **%s** placeholder in the **ErrMessage** error message.
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **Type**, it indicates that the **Type** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error code returned if the call fails.
        self.err_code = err_code
        # The error message returned if the call fails.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The name of the instance group.
        self.instance_name = instance_name
        # The instance ID of the primary role.
        self.master_db_instance_id = master_db_instance_id
        # The region where the DTS instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.slave_db_instances = slave_db_instances
        # The status of the active geo-redundancy instance group.
        self.status = status
        # Indicates whether the request was successful. Valid values:
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.slave_db_instances:
            self.slave_db_instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.db_engine_type is not None:
            result['DbEngineType'] = self.db_engine_type

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.master_db_instance_id is not None:
            result['MasterDbInstanceId'] = self.master_db_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slave_db_instances is not None:
            result['SlaveDbInstances'] = self.slave_db_instances.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DbEngineType') is not None:
            self.db_engine_type = m.get('DbEngineType')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MasterDbInstanceId') is not None:
            self.master_db_instance_id = m.get('MasterDbInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlaveDbInstances') is not None:
            temp_model = main_models.DescribeGadInstanceDbMembersResponseBodySlaveDbInstances()
            self.slave_db_instances = temp_model.from_map(m.get('SlaveDbInstances'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeGadInstanceDbMembersResponseBodySlaveDbInstances(DaraModel):
    def __init__(
        self,
        slave_db_instances: List[main_models.DescribeGadInstanceDbMembersResponseBodySlaveDbInstancesSlaveDbInstances] = None,
    ):
        self.slave_db_instances = slave_db_instances

    def validate(self):
        if self.slave_db_instances:
            for v1 in self.slave_db_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlaveDbInstances'] = []
        if self.slave_db_instances is not None:
            for k1 in self.slave_db_instances:
                result['SlaveDbInstances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slave_db_instances = []
        if m.get('SlaveDbInstances') is not None:
            for k1 in m.get('SlaveDbInstances'):
                temp_model = main_models.DescribeGadInstanceDbMembersResponseBodySlaveDbInstancesSlaveDbInstances()
                self.slave_db_instances.append(temp_model.from_map(k1))

        return self

class DescribeGadInstanceDbMembersResponseBodySlaveDbInstancesSlaveDbInstances(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        db_instance_id: str = None,
        dts_instance_id: str = None,
        sync_architecture: str = None,
    ):
        self.create_time = create_time
        self.db_instance_id = db_instance_id
        self.dts_instance_id = dts_instance_id
        self.sync_architecture = sync_architecture

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.sync_architecture is not None:
            result['SyncArchitecture'] = self.sync_architecture

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('SyncArchitecture') is not None:
            self.sync_architecture = m.get('SyncArchitecture')

        return self

