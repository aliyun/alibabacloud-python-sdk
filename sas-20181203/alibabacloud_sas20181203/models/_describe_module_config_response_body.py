# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeModuleConfigResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        http_status_code: int = None,
        module_config_list: List[main_models.DescribeModuleConfigResponseBodyModuleConfigList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The number of configurations for the module.
        self.count = count
        # The HTTP status code.
        self.http_status_code = http_status_code
        # An array that consists of the configurations of the module.
        self.module_config_list = module_config_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.module_config_list:
            for v1 in self.module_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['ModuleConfigList'] = []
        if self.module_config_list is not None:
            for k1 in self.module_config_list:
                result['ModuleConfigList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.module_config_list = []
        if m.get('ModuleConfigList') is not None:
            for k1 in m.get('ModuleConfigList'):
                temp_model = main_models.DescribeModuleConfigResponseBodyModuleConfigList()
                self.module_config_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeModuleConfigResponseBodyModuleConfigList(DaraModel):
    def __init__(
        self,
        config_name: str = None,
        items: List[main_models.DescribeModuleConfigResponseBodyModuleConfigListItems] = None,
        module_name: str = None,
    ):
        # The name of the configuration.
        self.config_name = config_name
        # An array that consists of the configuration items.
        self.items = items
        # The name of the module.
        self.module_name = module_name

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeModuleConfigResponseBodyModuleConfigListItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

class DescribeModuleConfigResponseBodyModuleConfigListItems(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        instance_id: str = None,
        instance_name: str = None,
        ip: str = None,
        region: str = None,
        uuid: str = None,
    ):
        # The ID of the server group.
        self.group_id = group_id
        # The ID of the server.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The IP address of the server.
        self.ip = ip
        # The region in which the server resides.
        self.region = region
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.region is not None:
            result['Region'] = self.region

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

