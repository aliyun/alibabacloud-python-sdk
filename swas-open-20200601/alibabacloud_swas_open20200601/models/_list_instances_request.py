# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListInstancesRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        instance_ids: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        plan_type: str = None,
        public_ip_addresses: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tag: List[main_models.ListInstancesRequestTag] = None,
    ):
        # The billing method of the instance. Valid values:
        # - PrePaid: subscription. Currently, only the subscription billing method is supported.
        # 
        # Default value: PrePaid.
        self.charge_type = charge_type
        # The instance IDs of the simple application servers. The value can be a JSON array that consists of up to 100 instance IDs. Separate multiple IDs with commas (,).
        # 
        # > If you specify both the InstanceIds and PublicIpAddresses parameters, ensure that the specified instance IDs and public IP addresses belong to the same simple application server. Otherwise, an empty response is returned.
        self.instance_ids = instance_ids
        # The name of the simple application server. You can use the asterisk (*) wildcard for fuzzy search.
        self.instance_name = instance_name
        # The page number of the simple application server list.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page in a paged query. Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The plan type. Valid values:
        # 
        # - NORMAL: general-purpose.
        # - CAPACITY: storage-optimized.
        # - PREVIOUS: previous generation.
        # - MULTI_IP: multi-public-IP.
        # - INTERNATIONAL: international.
        # 
        # > For more information, see [Instance families](https://help.aliyun.com/document_detail/2861773.html).
        self.plan_type = plan_type
        # The public IP addresses of the simple application servers. The value can be a JSON array that consists of up to 100 public IP addresses. Separate multiple IP addresses with commas (,).
        # 
        # > If you specify both the InstanceIds and PublicIpAddresses parameters, ensure that the specified instance IDs and public IP addresses belong to the same simple application server. Otherwise, an empty response is returned.
        self.public_ip_addresses = public_ip_addresses
        # The region ID of the simple application server.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the simple application server belongs.
        self.resource_group_id = resource_group_id
        # The instance status. Valid values:
        # 
        # - Pending: The instance is being prepared.
        # - Starting: The instance is starting.
        # - Running: The instance is running.
        # - Stopping: The instance is stopping.
        # - Stopped: The instance is stopped.
        # - Resetting: The instance is being reset.
        # - Upgrading: The instance is being upgraded.
        # - Disabled: The instance is unavailable.
        self.status = status
        # The tags of the instance.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('PublicIpAddresses') is not None:
            self.public_ip_addresses = m.get('PublicIpAddresses')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance. The tag key must be 1 to 64 characters in length. Valid values of N: 1 to 20.
        self.key = key
        # The tag value of the instance. The tag value must be 1 to 64 characters in length. Valid values of N: 1 to 20.
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

