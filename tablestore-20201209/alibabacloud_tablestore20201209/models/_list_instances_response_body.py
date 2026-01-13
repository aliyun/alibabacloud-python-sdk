# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details about the instances.
        self.instances = instances
        # The token that determines the start position of the next query. If this parameter is empty, all instances that you want to query are returned.
        self.next_token = next_token
        # The request ID, which can be used to troubleshoot issues.
        self.request_id = request_id
        # The total number of instances returned.
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

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        create_time: str = None,
        instance_description: str = None,
        instance_name: str = None,
        instance_specification: str = None,
        instance_status: str = None,
        is_multi_az: bool = None,
        payment_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        spinstance_id: str = None,
        storage_type: str = None,
        user_id: str = None,
        vcuquota: int = None,
    ):
        # The instance alias.
        self.alias_name = alias_name
        # The time when the instance was created.
        self.create_time = create_time
        # The instance description.
        self.instance_description = instance_description
        # The name of the instance, which is used to uniquely identify the instance.
        self.instance_name = instance_name
        # The type of the instance.
        # 
        # *   SSD: high-performance instance
        # *   HYBRID: capacity instance
        self.instance_specification = instance_specification
        # The status of the instance.
        # 
        # *   normal: The instance runs as expected.
        # *   forbidden: The instance is disabled.
        # *   Deleting: The instance is being released.
        self.instance_status = instance_status
        # Indicates whether zone-redundant storage (ZRS) is enabled for the instance.
        # 
        # *   true: ZRS is enabled for the instance.
        # *   false: Locally redundant storage (LRS) is enabled for the instance.
        self.is_multi_az = is_multi_az
        # The billing method.
        # 
        # *   Subscription: subscription
        # *   PayAsYouGo: pay as you go
        self.payment_type = payment_type
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The instance ID.
        self.spinstance_id = spinstance_id
        # The storage type.
        # 
        # *   SSD: high-performance
        # *   HYBRID: capacity
        self.storage_type = storage_type
        # The user ID.
        self.user_id = user_id
        # The VCU quota.
        self.vcuquota = vcuquota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_specification is not None:
            result['InstanceSpecification'] = self.instance_specification

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.is_multi_az is not None:
            result['IsMultiAZ'] = self.is_multi_az

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spinstance_id is not None:
            result['SPInstanceId'] = self.spinstance_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vcuquota is not None:
            result['VCUQuota'] = self.vcuquota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceSpecification') is not None:
            self.instance_specification = m.get('InstanceSpecification')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('IsMultiAZ') is not None:
            self.is_multi_az = m.get('IsMultiAZ')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SPInstanceId') is not None:
            self.spinstance_id = m.get('SPInstanceId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VCUQuota') is not None:
            self.vcuquota = m.get('VCUQuota')

        return self

