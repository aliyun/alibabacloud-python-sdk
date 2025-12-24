# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeActivationsResponseBody(DaraModel):
    def __init__(
        self,
        activation_list: List[main_models.DescribeActivationsResponseBodyActivationList] = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The activation codes and their usage information.
        self.activation_list = activation_list
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.activation_list:
            for v1 in self.activation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActivationList'] = []
        if self.activation_list is not None:
            for k1 in self.activation_list:
                result['ActivationList'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        self.activation_list = []
        if m.get('ActivationList') is not None:
            for k1 in m.get('ActivationList'):
                temp_model = main_models.DescribeActivationsResponseBodyActivationList()
                self.activation_list.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeActivationsResponseBodyActivationList(DaraModel):
    def __init__(
        self,
        activation_id: str = None,
        creation_time: str = None,
        deregistered_count: int = None,
        description: str = None,
        disabled: bool = None,
        instance_count: int = None,
        instance_name: str = None,
        ip_address_range: str = None,
        registered_count: int = None,
        resource_group_id: str = None,
        tags: List[main_models.DescribeActivationsResponseBodyActivationListTags] = None,
        time_to_live_in_hours: int = None,
    ):
        # The ID of the activation code.
        self.activation_id = activation_id
        # The time when the activation code was created.
        self.creation_time = creation_time
        # The number of instances that were deregistered.
        self.deregistered_count = deregistered_count
        # The description of the activation code.
        self.description = description
        # Indicates whether the activation code is disabled.
        self.disabled = disabled
        # The maximum number of times that the activation code can be used to register managed instances.
        self.instance_count = instance_count
        # The default instance name prefix.
        self.instance_name = instance_name
        # The IP addresses of hosts that are allowed to use the activation code.
        self.ip_address_range = ip_address_range
        # The number of instances that were registered.
        self.registered_count = registered_count
        # The ID of the resource group to which the activation code belongs.
        self.resource_group_id = resource_group_id
        # The tags of the activation code.
        self.tags = tags
        # The validity period of the activation code. Unit: hours.
        self.time_to_live_in_hours = time_to_live_in_hours

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation_id is not None:
            result['ActivationId'] = self.activation_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.deregistered_count is not None:
            result['DeregisteredCount'] = self.deregistered_count

        if self.description is not None:
            result['Description'] = self.description

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.ip_address_range is not None:
            result['IpAddressRange'] = self.ip_address_range

        if self.registered_count is not None:
            result['RegisteredCount'] = self.registered_count

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.time_to_live_in_hours is not None:
            result['TimeToLiveInHours'] = self.time_to_live_in_hours

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationId') is not None:
            self.activation_id = m.get('ActivationId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeregisteredCount') is not None:
            self.deregistered_count = m.get('DeregisteredCount')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IpAddressRange') is not None:
            self.ip_address_range = m.get('IpAddressRange')

        if m.get('RegisteredCount') is not None:
            self.registered_count = m.get('RegisteredCount')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeActivationsResponseBodyActivationListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TimeToLiveInHours') is not None:
            self.time_to_live_in_hours = m.get('TimeToLiveInHours')

        return self

class DescribeActivationsResponseBodyActivationListTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the activation code.
        self.tag_key = tag_key
        # The tag value of the activation code.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

