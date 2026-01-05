# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetNetworkResponseBody(DaraModel):
    def __init__(
        self,
        network: main_models.GetNetworkResponseBodyNetwork = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the network resource.
        self.network = network
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.network:
            self.network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Network') is not None:
            temp_model = main_models.GetNetworkResponseBodyNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetNetworkResponseBodyNetwork(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        id: int = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        status: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # The time when the network resource was created. The value is a 64-bit timestamp.
        self.create_time = create_time
        # The ID of the user who creates the network resource.
        self.create_user = create_user
        # The network ID.
        self.id = id
        # The ID of the serverless resource group.
        self.resource_group_id = resource_group_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The status of the network resource. Valid values:
        # 
        # *   Pending: The network resource is waiting to be created.
        # *   Creating: The network resource is being created.
        # *   Running: The network resource is running as expected.
        # *   Deleting: The network resource is being deleted.
        # *   Deleted: The network resource is deleted.
        self.status = status
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The VSwitch ID.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.id is not None:
            result['Id'] = self.id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

