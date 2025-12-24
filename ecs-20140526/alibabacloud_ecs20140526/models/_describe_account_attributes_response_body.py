# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountAttributesResponseBody(DaraModel):
    def __init__(
        self,
        account_attribute_items: main_models.DescribeAccountAttributesResponseBodyAccountAttributeItems = None,
        request_id: str = None,
    ):
        # Details about account privileges in the specified region.
        self.account_attribute_items = account_attribute_items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account_attribute_items:
            self.account_attribute_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_attribute_items is not None:
            result['AccountAttributeItems'] = self.account_attribute_items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountAttributeItems') is not None:
            temp_model = main_models.DescribeAccountAttributesResponseBodyAccountAttributeItems()
            self.account_attribute_items = temp_model.from_map(m.get('AccountAttributeItems'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccountAttributesResponseBodyAccountAttributeItems(DaraModel):
    def __init__(
        self,
        account_attribute_item: List[main_models.DescribeAccountAttributesResponseBodyAccountAttributeItemsAccountAttributeItem] = None,
    ):
        self.account_attribute_item = account_attribute_item

    def validate(self):
        if self.account_attribute_item:
            for v1 in self.account_attribute_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountAttributeItem'] = []
        if self.account_attribute_item is not None:
            for k1 in self.account_attribute_item:
                result['AccountAttributeItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_attribute_item = []
        if m.get('AccountAttributeItem') is not None:
            for k1 in m.get('AccountAttributeItem'):
                temp_model = main_models.DescribeAccountAttributesResponseBodyAccountAttributeItemsAccountAttributeItem()
                self.account_attribute_item.append(temp_model.from_map(k1))

        return self

class DescribeAccountAttributesResponseBodyAccountAttributeItemsAccountAttributeItem(DaraModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_values: main_models.DescribeAccountAttributesResponseBodyAccountAttributeItemsAccountAttributeItemAttributeValues = None,
    ):
        # The type of the resource quota in the specified region. Valid values:
        # 
        # *   instance-network-type: the available network types.
        # *   max-security-groups: the maximum number of security groups.
        # *   max-elastic-network-interfaces: the maximum number of ENIs.
        # *   max-postpaid-instance-vcpu-count: the maximum number of vCPUs for pay-as-you-go instances.
        # *   max-spot-instance-vcpu-count: the maximum number of vCPUs for spot instances.
        # *   used-postpaid-instance-vcpu-count: the number of vCPUs that were allocated to pay-as-you-go instances.
        # *   used-spot-instance-vcpu-count: the number of vCPUs that were allocated to spot instances.
        # *   max-postpaid-yundisk-capacity: the maximum capacity of pay-as-you-go data disks. (The value is deprecated.)
        # *   used-postpaid-yundisk-capacity: the capacity of pay-as-you-go data disks that were created. (The value is deprecated.)
        # *   max-dedicated-hosts: the maximum number of dedicated hosts.
        # *   supported-postpaid-instance-types: the instance types of pay-as-you-go I/O optimized instances.
        # *   max-axt-command-count: the maximum number of Cloud Assistant commands.
        # *   max-axt-invocation-daily: the maximum number of Cloud Assistant command executions per day.
        # *   real-name-authentication: whether the account completed the real-name verification.
        # *   max-cloud-assistant-activation-count: the maximum number of activation codes that can be created to use to register managed instances.
        self.attribute_name = attribute_name
        # The values of resource quotas.
        self.attribute_values = attribute_values

    def validate(self):
        if self.attribute_values:
            self.attribute_values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name

        if self.attribute_values is not None:
            result['AttributeValues'] = self.attribute_values.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')

        if m.get('AttributeValues') is not None:
            temp_model = main_models.DescribeAccountAttributesResponseBodyAccountAttributeItemsAccountAttributeItemAttributeValues()
            self.attribute_values = temp_model.from_map(m.get('AttributeValues'))

        return self

class DescribeAccountAttributesResponseBodyAccountAttributeItemsAccountAttributeItemAttributeValues(DaraModel):
    def __init__(
        self,
        value_item: List[main_models.DescribeAccountAttributesResponseBodyAccountAttributeItemsAccountAttributeItemAttributeValuesValueItem] = None,
    ):
        self.value_item = value_item

    def validate(self):
        if self.value_item:
            for v1 in self.value_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ValueItem'] = []
        if self.value_item is not None:
            for k1 in self.value_item:
                result['ValueItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.value_item = []
        if m.get('ValueItem') is not None:
            for k1 in m.get('ValueItem'):
                temp_model = main_models.DescribeAccountAttributesResponseBodyAccountAttributeItemsAccountAttributeItemAttributeValuesValueItem()
                self.value_item.append(temp_model.from_map(k1))

        return self

class DescribeAccountAttributesResponseBodyAccountAttributeItemsAccountAttributeItemAttributeValuesValueItem(DaraModel):
    def __init__(
        self,
        count: int = None,
        disk_category: str = None,
        expired_time: str = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        value: str = None,
        zone_id: str = None,
    ):
        # The number of privilege attributes in the account.
        self.count = count
        # The data disk category. Valid values:
        # 
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   cloud_essd: enhanced SSD (ESSD)
        self.disk_category = disk_category
        # The expiration time of a privilege. This parameter is returned only when the account privilege has an expiration time. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.expired_time = expired_time
        # The billing method of the instance.
        self.instance_charge_type = instance_charge_type
        # The type of the instance.
        self.instance_type = instance_type
        # The value of the resource quota in the specified region. Valid values:
        # 
        # The values returned for the resource quotas to which the following AttributeName values correspond are 0 or positive integers:
        # 
        # *   max-security-groups
        # *   max-elastic-network-interfaces
        # *   max-postpaid-instance-vcpu-count
        # *   max-spot-instance-vcpu-count
        # *   used-postpaid-instance-vcpu-count
        # *   used-spot-instance-vcpu-count
        # *   max-postpaid-yundisk-capacity (the value is deprecated)
        # *   used-postpaid-yundisk-capacity (the value is deprecated)
        # *   max-dedicated-hosts
        # *   max-axt-command-count
        # *   max-axt-invocation-daily
        # *   max-cloud-assistant-activation-count
        # 
        # When AttributeName is set to supported-postpay-instance-types, instance types are returned. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        # 
        # When AttributeName is set to real-name-authentications, one of the following values is returned:
        # 
        # *   yes
        # *   none
        # *   unnecessary
        # 
        # When AttributeName is set to instance-network-type, one of the following values is returned:
        # 
        # *   vpc
        # *   classic
        self.value = value
        # The ID of the zone in which the resource resides.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.value is not None:
            result['Value'] = self.value

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

