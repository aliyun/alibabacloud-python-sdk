# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDBClusterPriceShrinkRequest(DaraModel):
    def __init__(
        self,
        creation_category: str = None,
        dbcluster_id: str = None,
        dbnode_class: str = None,
        dbnode_ids: List[str] = None,
        dbnode_num: int = None,
        dbnodes_shrink: str = None,
        dbtype: str = None,
        dbversion: str = None,
        hot_standby_cluster: str = None,
        modify_type: str = None,
        order_type: str = None,
        pay_type: str = None,
        period: str = None,
        provisioned_iops: str = None,
        region_id: str = None,
        serverless_type: str = None,
        storage_charge_type: str = None,
        storage_space: str = None,
        storage_type: str = None,
        used_time: str = None,
        zone_id: str = None,
    ):
        # The cluster edition. Valid values:
        # - Normal: Cluster Edition.
        # - Basic: Single Node Edition.
        # - ArchiveNormal: Archive Database.
        # - SENormal: Standard Edition.
        # - NormalMultimaster: Multi-master Cluster.
        self.creation_category = creation_category
        # The cluster ID. Required for non-BUY scenarios.
        self.dbcluster_id = dbcluster_id
        # The node specifications. Required for the BUY scenario. Example format: polar.mysql.x4.large.
        self.dbnode_class = dbnode_class
        # The list of node IDs to delete. Used when ModifyType is set to DELETE.
        self.dbnode_ids = dbnode_ids
        # The number of nodes. Valid for the BUY scenario. This value includes the read/write node. Minimum value: 1. Default value: 1.
        self.dbnode_num = dbnode_num
        # The list of heterogeneous specification change nodes. Used for specification change scenarios to specify the target specifications for each node.
        self.dbnodes_shrink = dbnodes_shrink
        # The database engine type. Required for the BUY scenario. Valid values: MySQL, PostgreSQL, and Oracle.
        self.dbtype = dbtype
        # The database engine version. Required for the BUY scenario. Valid values for MySQL: 5.6, 5.7, and 8.0. Valid values for PostgreSQL: 11 and 14. Valid values for Oracle: 11 and 14.
        self.dbversion = dbversion
        # Specifies whether to enable the hot standby cluster. Valid values:
        # - ON: Enable.
        # - OFF: Disable.
        # 
        # Valid for the BUY and specification change scenarios.
        self.hot_standby_cluster = hot_standby_cluster
        # The specification change direction. Valid values:
        # - ADD: add nodes.
        # - DELETE: remove nodes.
        # - UPGRADE: upgrade specifications.
        # - DOWNGRADE: downgrade specifications.
        # - HOT_STANDBY: hot standby change.
        # - STORAGE: storage space change.
        # - STORAGE_TYPE: storage type change.
        self.modify_type = modify_type
        # The order type. Valid values:
        # - BUY: new purchase.
        # - CONVERT: billing method conversion.
        # - RENEW: renewal.
        # - UPGRADE: upgrade specifications or add nodes.
        # - DOWNGRADE: downgrade specifications or remove nodes.
        # 
        # This parameter is required.
        self.order_type = order_type
        # The billing method. Required for the BUY and CONVERT scenarios. Valid values:
        # - Prepaid: subscription.
        # - Postpaid: pay-as-you-go.
        self.pay_type = pay_type
        # The subscription cycle. Valid values:
        # - Month: monthly.
        # - Year: yearly.
        self.period = period
        # The provisioned IOPS. Used for the Standard Edition (SENormal) scenario.
        self.provisioned_iops = provisioned_iops
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The serverless type. Valid values: AgileServerless.
        self.serverless_type = serverless_type
        # The storage billing type. Valid values:
        # - Prepaid: subscription.
        # - Postpaid: pay-as-you-go.
        self.storage_charge_type = storage_charge_type
        # The storage space, in GB. Used for prepaid storage or storage specification change scenarios.
        self.storage_space = storage_space
        # The storage type. Valid values:
        # - PSL5: high performance.
        # - PSL4: standard.
        # - ESSDPL0
        # - ESSDPL1
        # - ESSDPL2
        # - ESSDPL3
        # - ESSDAUTOPL
        self.storage_type = storage_type
        # The subscription duration. Used together with Period. Valid for the BUY, CONVERT, and RENEW scenarios when the billing method is Prepaid.
        self.used_time = used_time
        # The zone ID. We recommend that you specify this parameter for the BUY scenario.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_category is not None:
            result['CreationCategory'] = self.creation_category

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids

        if self.dbnode_num is not None:
            result['DBNodeNum'] = self.dbnode_num

        if self.dbnodes_shrink is not None:
            result['DBNodes'] = self.dbnodes_shrink

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.hot_standby_cluster is not None:
            result['HotStandbyCluster'] = self.hot_standby_cluster

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.storage_charge_type is not None:
            result['StorageChargeType'] = self.storage_charge_type

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationCategory') is not None:
            self.creation_category = m.get('CreationCategory')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeIds') is not None:
            self.dbnode_ids = m.get('DBNodeIds')

        if m.get('DBNodeNum') is not None:
            self.dbnode_num = m.get('DBNodeNum')

        if m.get('DBNodes') is not None:
            self.dbnodes_shrink = m.get('DBNodes')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('HotStandbyCluster') is not None:
            self.hot_standby_cluster = m.get('HotStandbyCluster')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('StorageChargeType') is not None:
            self.storage_charge_type = m.get('StorageChargeType')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

