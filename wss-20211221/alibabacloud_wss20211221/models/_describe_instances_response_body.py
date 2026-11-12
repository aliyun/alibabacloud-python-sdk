# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeInstancesResponseBodyInstances] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of sold instances that meet the query conditions.
        self.instances = instances
        # The maximum number of records to return per query.
        self.max_results = max_results
        # The pagination token. Leave it empty for the first query. For subsequent queries, pass the NextToken value returned in the previous response as is. Do not construct or decode it yourself.
        self.next_token = next_token
        # The unique identifier of the request, which can be used to troubleshoot call issues.
        self.request_id = request_id

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        expired_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        property_list: List[main_models.DescribeInstancesResponseBodyInstancesPropertyList] = None,
        resource_id: str = None,
        resource_type: str = None,
        start_time: str = None,
        state: str = None,
        total_time: int = None,
        used_time: int = None,
    ):
        # The Alibaba Cloud account ID to which the resource belongs.
        self.ali_uid = ali_uid
        # The expiration time in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.expired_time = expired_time
        # The sold instance ID, which is used to identify the purchased instance.
        self.instance_id = instance_id
        # The instance type identifier.
        self.instance_type = instance_type
        # The list of instance properties. Each item contains the property name Key and the property value Value.
        self.property_list = property_list
        # The associated business resource ID, which is used to distinguish from the sold instance ID.
        self.resource_id = resource_id
        # The resource type. For example, CorePackage indicates a core-hour package. It must be consistent with the resource type of the target instance.
        self.resource_type = resource_type
        # The effective time in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.start_time = start_time
        # The instance status. Valid values:
        # - NORMAL: Normal.
        # - DELETED: Deleted.
        # - PENDING: Pending activation.
        # - EXPIRED: Expired.
        # - ARCHIVED: Historical archived status.
        self.state = state
        # The total metering quota included in the instance, using the same unit as UsedTime. A CorePackage core-hour package is metered in core-seconds. For example, 360000 indicates 100 core-hours.
        self.total_time = total_time
        # The consumed metering quota of the instance. For a CorePackage core-hour package, the unit is core-seconds. Divide by 3600 to convert to core-hours. For other resource types, read according to the corresponding metering criteria.
        self.used_time = used_time

    def validate(self):
        if self.property_list:
            for v1 in self.property_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        result['PropertyList'] = []
        if self.property_list is not None:
            for k1 in self.property_list:
                result['PropertyList'].append(k1.to_map() if k1 else None)

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.total_time is not None:
            result['TotalTime'] = self.total_time

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        self.property_list = []
        if m.get('PropertyList') is not None:
            for k1 in m.get('PropertyList'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesPropertyList()
                self.property_list.append(temp_model.from_map(k1))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

class DescribeInstancesResponseBodyInstancesPropertyList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The instance property name.
        self.key = key
        # The instance property value, which corresponds to the Key in the same entry.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

