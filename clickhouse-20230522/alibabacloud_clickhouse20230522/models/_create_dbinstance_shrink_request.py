# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class CreateDBInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        category: str = None,
        client_token: str = None,
        dbinstance_description: str = None,
        dbtime_zone: str = None,
        deploy_schema: str = None,
        engine: str = None,
        engine_version: str = None,
        multi_zone_shrink: str = None,
        node_count: int = None,
        node_scale_max: int = None,
        node_scale_min: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        scale_max: str = None,
        scale_min: str = None,
        source_dbinstance_id: str = None,
        storage_quota: int = None,
        storage_type: str = None,
        tags: List[main_models.CreateDBInstanceShrinkRequestTags] = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # The backup set ID.
        self.backup_set_id = backup_set_id
        # The edition of the instance. Valid value:
        # 
        # - `enterprise`: Enterprise Edition
        self.category = category
        # A client-provided token to ensure request idempotence. It must be unique across requests, contain only ASCII characters, and not exceed 64 characters in length.
        self.client_token = client_token
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The time zone of the database, which must be an IANA time zone identifier.
        self.dbtime_zone = dbtime_zone
        # The deployment mode of the instance.
        self.deploy_schema = deploy_schema
        # The engine type.
        self.engine = engine
        # The engine version.
        self.engine_version = engine_version
        # The multi-zone configuration.
        self.multi_zone_shrink = multi_zone_shrink
        # The number of nodes. Valid values: 2 to 16. This parameter is required when you configure an elastic scaling range by using the `NodeScaleMin` and `NodeScaleMax` parameters.
        self.node_count = node_count
        # The maximum number of nodes for serverless elastic scaling. Valid values: 4 to 32. The value must be greater than the `NodeScaleMin` parameter.
        self.node_scale_max = node_scale_max
        # The minimum number of nodes for serverless elastic scaling. Valid values: 4 to 32.
        self.node_scale_min = node_scale_min
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # This parameter is deprecated. Use the `NodeCount`, `NodeScaleMin`, and `NodeScaleMax` parameters to configure elastic scaling.
        self.scale_max = scale_max
        # This parameter is deprecated. Use the `NodeCount`, `NodeScaleMin`, and `NodeScaleMax` parameters to configure elastic scaling.
        self.scale_min = scale_min
        # The ID of the source instance. This parameter is required when restoring from a backup.
        self.source_dbinstance_id = source_dbinstance_id
        self.storage_quota = storage_quota
        self.storage_type = storage_type
        # The tags to add to the instance.
        self.tags = tags
        # The VPC ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The zone ID.
        self.zone_id = zone_id

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
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.category is not None:
            result['Category'] = self.category

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbtime_zone is not None:
            result['DBTimeZone'] = self.dbtime_zone

        if self.deploy_schema is not None:
            result['DeploySchema'] = self.deploy_schema

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.multi_zone_shrink is not None:
            result['MultiZone'] = self.multi_zone_shrink

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_scale_max is not None:
            result['NodeScaleMax'] = self.node_scale_max

        if self.node_scale_min is not None:
            result['NodeScaleMin'] = self.node_scale_min

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.source_dbinstance_id is not None:
            result['SourceDBInstanceId'] = self.source_dbinstance_id

        if self.storage_quota is not None:
            result['StorageQuota'] = self.storage_quota

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBTimeZone') is not None:
            self.dbtime_zone = m.get('DBTimeZone')

        if m.get('DeploySchema') is not None:
            self.deploy_schema = m.get('DeploySchema')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('MultiZone') is not None:
            self.multi_zone_shrink = m.get('MultiZone')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeScaleMax') is not None:
            self.node_scale_max = m.get('NodeScaleMax')

        if m.get('NodeScaleMin') is not None:
            self.node_scale_min = m.get('NodeScaleMin')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('SourceDBInstanceId') is not None:
            self.source_dbinstance_id = m.get('SourceDBInstanceId')

        if m.get('StorageQuota') is not None:
            self.storage_quota = m.get('StorageQuota')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateDBInstanceShrinkRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateDBInstanceShrinkRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

