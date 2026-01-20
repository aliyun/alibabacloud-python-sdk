# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        self.request_id = request_id
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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        feature_dbinfo: main_models.ListInstancesResponseBodyInstancesFeatureDBInfo = None,
        feature_dbinstance_info: main_models.ListInstancesResponseBodyInstancesFeatureDBInstanceInfo = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.feature_dbinfo = feature_dbinfo
        self.feature_dbinstance_info = feature_dbinstance_info
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.instance_id = instance_id
        self.region_id = region_id
        self.status = status
        self.type = type

    def validate(self):
        if self.feature_dbinfo:
            self.feature_dbinfo.validate()
        if self.feature_dbinstance_info:
            self.feature_dbinstance_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_dbinfo is not None:
            result['FeatureDBInfo'] = self.feature_dbinfo.to_map()

        if self.feature_dbinstance_info is not None:
            result['FeatureDBInstanceInfo'] = self.feature_dbinstance_info.to_map()

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureDBInfo') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesFeatureDBInfo()
            self.feature_dbinfo = temp_model.from_map(m.get('FeatureDBInfo'))

        if m.get('FeatureDBInstanceInfo') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesFeatureDBInstanceInfo()
            self.feature_dbinstance_info = temp_model.from_map(m.get('FeatureDBInstanceInfo'))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListInstancesResponseBodyInstancesFeatureDBInstanceInfo(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstancesResponseBodyInstancesFeatureDBInfo(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

