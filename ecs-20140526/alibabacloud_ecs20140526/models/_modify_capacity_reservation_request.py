# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyCapacityReservationRequest(DaraModel):
    def __init__(
        self,
        private_pool_options: main_models.ModifyCapacityReservationRequestPrivatePoolOptions = None,
        description: str = None,
        end_time: str = None,
        end_time_type: str = None,
        instance_amount: int = None,
        owner_account: str = None,
        owner_id: int = None,
        platform: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.private_pool_options = private_pool_options
        # The description of the capacity reservation. The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://`.
        self.description = description
        # The expiration time of the capacity reservation. This parameter takes effect only when `EndTimeType` is set to Limited. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.end_time = end_time
        # The release mode of the capacity reservation. Valid values:
        # 
        # *   Limited: The capacity reservation is automatically released at the specified point in time. If you configure this parameter, you must also configure `EndTime`.
        # *   Unlimited: The capacity reservation must be manually released. You can release it anytime.
        self.end_time_type = end_time_type
        # The total number of instances for which capacity is reserved. Valid values: the number of used instances to 1000.
        # 
        # > When you increase the number of instances, the increase may fail due to insufficient resources.
        self.instance_amount = instance_amount
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The operating system of the image used by the instance. Valid values:
        # 
        # *   Windows
        # *   Linux
        # 
        # > This parameter is unavailable.
        self.platform = platform
        # The region ID of the capacity reservation. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The mode in which the capacity reservation takes effect. Only immediate capacity reservations are supported. You do not need to specify a value for this parameter.
        # 
        # > If you do not specify a value for this parameter, the capacity reservation immediately takes effect.
        self.start_time = start_time

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_time_type is not None:
            result['EndTimeType'] = self.end_time_type

        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.ModifyCapacityReservationRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimeType') is not None:
            self.end_time_type = m.get('EndTimeType')

        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ModifyCapacityReservationRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The capacity reservation ID.
        # 
        # This parameter is required.
        self.id = id
        # The name of the capacity reservation. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

