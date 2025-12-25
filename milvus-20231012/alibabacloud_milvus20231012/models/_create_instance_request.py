# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        auto_backup: bool = None,
        auto_renew: bool = None,
        components: List[main_models.CreateInstanceRequestComponents] = None,
        configuration: str = None,
        db_admin_password: str = None,
        db_version: str = None,
        encrypted: bool = None,
        ha: bool = None,
        instance_name: str = None,
        is_multi_az_storage: bool = None,
        kms_key_id: str = None,
        load_replicas: int = None,
        multi_zone_mode: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        promotion_no: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateInstanceRequestTags] = None,
        v_switch_ids: List[main_models.CreateInstanceRequestVSwitchIds] = None,
        vpc_id: str = None,
        zone_id: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.auto_backup = auto_backup
        self.auto_renew = auto_renew
        self.components = components
        self.configuration = configuration
        self.db_admin_password = db_admin_password
        # This parameter is required.
        self.db_version = db_version
        self.encrypted = encrypted
        self.ha = ha
        self.instance_name = instance_name
        self.is_multi_az_storage = is_multi_az_storage
        self.kms_key_id = kms_key_id
        self.load_replicas = load_replicas
        self.multi_zone_mode = multi_zone_mode
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        # This parameter is required.
        self.payment_type = payment_type
        self.promotion_no = promotion_no
        self.resource_group_id = resource_group_id
        self.tags = tags
        self.v_switch_ids = v_switch_ids
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.zone_id = zone_id
        self.client_token = client_token

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.v_switch_ids:
            for v1 in self.v_switch_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.auto_backup is not None:
            result['autoBackup'] = self.auto_backup

        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        result['components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['components'].append(k1.to_map() if k1 else None)

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.db_admin_password is not None:
            result['dbAdminPassword'] = self.db_admin_password

        if self.db_version is not None:
            result['dbVersion'] = self.db_version

        if self.encrypted is not None:
            result['encrypted'] = self.encrypted

        if self.ha is not None:
            result['ha'] = self.ha

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.is_multi_az_storage is not None:
            result['isMultiAzStorage'] = self.is_multi_az_storage

        if self.kms_key_id is not None:
            result['kmsKeyId'] = self.kms_key_id

        if self.load_replicas is not None:
            result['loadReplicas'] = self.load_replicas

        if self.multi_zone_mode is not None:
            result['multiZoneMode'] = self.multi_zone_mode

        if self.payment_duration is not None:
            result['paymentDuration'] = self.payment_duration

        if self.payment_duration_unit is not None:
            result['paymentDurationUnit'] = self.payment_duration_unit

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.promotion_no is not None:
            result['promotionNo'] = self.promotion_no

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        result['vSwitchIds'] = []
        if self.v_switch_ids is not None:
            for k1 in self.v_switch_ids:
                result['vSwitchIds'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('autoBackup') is not None:
            self.auto_backup = m.get('autoBackup')

        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        self.components = []
        if m.get('components') is not None:
            for k1 in m.get('components'):
                temp_model = main_models.CreateInstanceRequestComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('dbAdminPassword') is not None:
            self.db_admin_password = m.get('dbAdminPassword')

        if m.get('dbVersion') is not None:
            self.db_version = m.get('dbVersion')

        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')

        if m.get('ha') is not None:
            self.ha = m.get('ha')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('isMultiAzStorage') is not None:
            self.is_multi_az_storage = m.get('isMultiAzStorage')

        if m.get('kmsKeyId') is not None:
            self.kms_key_id = m.get('kmsKeyId')

        if m.get('loadReplicas') is not None:
            self.load_replicas = m.get('loadReplicas')

        if m.get('multiZoneMode') is not None:
            self.multi_zone_mode = m.get('multiZoneMode')

        if m.get('paymentDuration') is not None:
            self.payment_duration = m.get('paymentDuration')

        if m.get('paymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('paymentDurationUnit')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('promotionNo') is not None:
            self.promotion_no = m.get('promotionNo')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        self.v_switch_ids = []
        if m.get('vSwitchIds') is not None:
            for k1 in m.get('vSwitchIds'):
                temp_model = main_models.CreateInstanceRequestVSwitchIds()
                self.v_switch_ids.append(temp_model.from_map(k1))

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateInstanceRequestVSwitchIds(DaraModel):
    def __init__(
        self,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        self.vsw_id = vsw_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vsw_id is not None:
            result['vswId'] = self.vsw_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vswId') is not None:
            self.vsw_id = m.get('vswId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class CreateInstanceRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class CreateInstanceRequestComponents(DaraModel):
    def __init__(
        self,
        cu_num: int = None,
        cu_type: str = None,
        disk_size_type: str = None,
        replica: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.cu_num = cu_num
        self.cu_type = cu_type
        self.disk_size_type = disk_size_type
        # This parameter is required.
        self.replica = replica
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_num is not None:
            result['cuNum'] = self.cu_num

        if self.cu_type is not None:
            result['cuType'] = self.cu_type

        if self.disk_size_type is not None:
            result['diskSizeType'] = self.disk_size_type

        if self.replica is not None:
            result['replica'] = self.replica

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuNum') is not None:
            self.cu_num = m.get('cuNum')

        if m.get('cuType') is not None:
            self.cu_type = m.get('cuType')

        if m.get('diskSizeType') is not None:
            self.disk_size_type = m.get('diskSizeType')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

