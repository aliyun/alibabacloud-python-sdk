# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateDBNodesRequest(DaraModel):
    def __init__(
        self,
        auto_use_coupon: bool = None,
        client_token: str = None,
        cloud_provider: str = None,
        dbcluster_id: str = None,
        dbnode: List[main_models.CreateDBNodesRequestDBNode] = None,
        dbnode_type: str = None,
        endpoint_bind_list: str = None,
        imci_switch: str = None,
        owner_account: str = None,
        owner_id: int = None,
        planned_end_time: str = None,
        planned_start_time: str = None,
        promotion_code: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auto_use_coupon = auto_use_coupon
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. The token is case-sensitive.
        self.client_token = client_token
        self.cloud_provider = cloud_provider
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The details of the read-only node.
        # 
        # This parameter is required.
        self.dbnode = dbnode
        # The node type. Valid values:
        # 
        # *   RO
        # *   STANDBY
        # *   DLNode
        # 
        # Enumerated values:
        # 
        # *   DLNode: AI node
        # *   STANDBY: standby node
        # *   RO: read-only node
        self.dbnode_type = dbnode_type
        # The ID of the cluster endpoint to which the read-only node is added. If you want to add the read-only node to multiple endpoints at the same time, separate the endpoint IDs with commas (,).
        # > - You can call the [DescribeDBClusterEndpoints](https://help.aliyun.com/document_detail/98205.html) operation to query the details of cluster endpoints, including endpoint IDs.
        # >- You can enter the ID of the default cluster endpoint or a custom cluster endpoint.
        # >- If you leave this parameter empty, the read-only node is added to all cluster endpoints for which the **Automatically Associate New Nodes** feature is enabled. If you set `AutoAddNewNodes` to `Enable`, the Automatically Associate New Nodes feature is enabled.
        self.endpoint_bind_list = endpoint_bind_list
        # Specifies whether to enable the In-Memory Column Index (IMCI) feature. Default value: OFF. Valid values:
        # 
        # *   **ON**
        # *   **OFF**
        # 
        # > This parameter is invalid for a PolarDB for Oracle or PolarDB for PostgreSQL cluster.
        self.imci_switch = imci_switch
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest start time for upgrading the specifications within the scheduled time period. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # >- The value of this parameter must be at least 30 minutes later than the value of PlannedStartTime.
        # >- If you specify `PlannedStartTime` but do not specify PlannedEndTime, the latest start time of the task is set to a value that is calculated by using the following formula: `PlannedEndTime value + 30 minutes`. For example, if you set `PlannedStartTime` to `2021-01-14T09:00:00Z` and you do not specify PlannedEndTime, the latest start time of the task is set to `2021-01-14T09:30:00Z`.
        self.planned_end_time = planned_end_time
        # The earliest start time of the scheduled task for adding the read-only node. The scheduled task specifies that the task is run in the required period. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        # 
        # >- The earliest start time of the scheduled task can be a point in time within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, you can specify a point in time between `2021-01-14T09:00:00Z` and `2021-01-15T09:00:00Z`.
        # >- If you leave this parameter empty, the task for adding the read-only node is immediately run by default.
        self.planned_start_time = planned_start_time
        self.promotion_code = promotion_code
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.dbnode:
            for v1 in self.dbnode:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cloud_provider is not None:
            result['CloudProvider'] = self.cloud_provider

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['DBNode'] = []
        if self.dbnode is not None:
            for k1 in self.dbnode:
                result['DBNode'].append(k1.to_map() if k1 else None)

        if self.dbnode_type is not None:
            result['DBNodeType'] = self.dbnode_type

        if self.endpoint_bind_list is not None:
            result['EndpointBindList'] = self.endpoint_bind_list

        if self.imci_switch is not None:
            result['ImciSwitch'] = self.imci_switch

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CloudProvider') is not None:
            self.cloud_provider = m.get('CloudProvider')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.dbnode = []
        if m.get('DBNode') is not None:
            for k1 in m.get('DBNode'):
                temp_model = main_models.CreateDBNodesRequestDBNode()
                self.dbnode.append(temp_model.from_map(k1))

        if m.get('DBNodeType') is not None:
            self.dbnode_type = m.get('DBNodeType')

        if m.get('EndpointBindList') is not None:
            self.endpoint_bind_list = m.get('EndpointBindList')

        if m.get('ImciSwitch') is not None:
            self.imci_switch = m.get('ImciSwitch')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class CreateDBNodesRequestDBNode(DaraModel):
    def __init__(
        self,
        target_class: str = None,
        zone_id: str = None,
    ):
        # The specifications of the read-only node that you want to add, which must be the same as the specifications of the existing nodes. For more information, see the following topics:
        # 
        # *   PolarDB for MySQL: [Specifications of compute nodes](https://help.aliyun.com/document_detail/102542.html)
        # *   PolarDB for PostgreSQL (Compatible with Oracle): [Specifications of compute nodes](https://help.aliyun.com/document_detail/207921.html)
        # *   PolarDB for PostgreSQL: [Specifications of compute nodes](https://help.aliyun.com/document_detail/209380.html)
        # 
        # >- You need to specify either DBNode.N.ZoneId or DBNode.N.TargetClass. N is an integer that starts from 1. The maximum value of N is equal to 16 minus the number of existing nodes.
        # >- You can add multiple read-only nodes at the same time only to PolarDB for MySQL clusters, which can contain up to of 15 read-only nodes.
        # >- This parameter is required for PolarDB for PostgreSQL (Compatible with Oracle) clusters or PolarDB for PostgreSQL clusters. This parameter is optional for PolarDB for MySQL clusters.
        self.target_class = target_class
        # The zone ID of the node that you want to add, which must be the same as the zone ID of existing nodes. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the IDs of zones.
        # 
        # >- You need to specify either DBNode.N.ZoneId or DBNode.N.TargetClass. N is an integer that starts from 1. The maximum value of N is equal to 16 minus the number of existing nodes.
        # >- You can add multiple read-only nodes at the same time only to PolarDB for MySQL clusters, which can contain up to of 15 read-only nodes.
        # >- This parameter is required for PolarDB for PostgreSQL (Compatible with Oracle) clusters or PolarDB for PostgreSQL clusters. This parameter is optional for PolarDB for MySQL clusters.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_class is not None:
            result['TargetClass'] = self.target_class

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetClass') is not None:
            self.target_class = m.get('TargetClass')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

