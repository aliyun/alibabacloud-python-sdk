# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        auto_backup: bool = None,
        auto_pay: bool = None,
        components: List[main_models.UpdateInstanceRequestComponents] = None,
        configuration: str = None,
        ha: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        client_token: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # Specifies whether to enable automatic backup.
        self.auto_backup = auto_backup
        self.auto_pay = auto_pay
        # The component information.
        self.components = components
        # The configuration information.
        self.configuration = configuration
        # Specifies whether to enable high availability (HA).
        self.ha = ha
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token

    def validate(self):
        if self.components:
            for v1 in self.components:
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

        if self.auto_pay is not None:
            result['autoPay'] = self.auto_pay

        result['components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['components'].append(k1.to_map() if k1 else None)

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.ha is not None:
            result['ha'] = self.ha

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('autoBackup') is not None:
            self.auto_backup = m.get('autoBackup')

        if m.get('autoPay') is not None:
            self.auto_pay = m.get('autoPay')

        self.components = []
        if m.get('components') is not None:
            for k1 in m.get('components'):
                temp_model = main_models.UpdateInstanceRequestComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('ha') is not None:
            self.ha = m.get('ha')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateInstanceRequestComponents(DaraModel):
    def __init__(
        self,
        cu_num: int = None,
        cu_type: str = None,
        data_disk: main_models.UpdateInstanceRequestComponentsDataDisk = None,
        pay_type: str = None,
        replica: int = None,
        type: str = None,
    ):
        # The number of compute units (CUs).
        # 
        # This parameter is required.
        self.cu_num = cu_num
        # The CU type. general indicates a 1:4 ratio, and ram indicates a 1:8 ratio.
        self.cu_type = cu_type
        # The QueryNode data cloud disk configuration. This parameter is supported only when type is set to query.
        self.data_disk = data_disk
        self.pay_type = pay_type
        # The number of replicas.
        # 
        # This parameter is required.
        self.replica = replica
        # The component type.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.data_disk:
            self.data_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_num is not None:
            result['cuNum'] = self.cu_num

        if self.cu_type is not None:
            result['cuType'] = self.cu_type

        if self.data_disk is not None:
            result['dataDisk'] = self.data_disk.to_map()

        if self.pay_type is not None:
            result['payType'] = self.pay_type

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

        if m.get('dataDisk') is not None:
            temp_model = main_models.UpdateInstanceRequestComponentsDataDisk()
            self.data_disk = temp_model.from_map(m.get('dataDisk'))

        if m.get('payType') is not None:
            self.pay_type = m.get('payType')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateInstanceRequestComponentsDataDisk(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        performance_level: str = None,
        size: int = None,
        storage_class: str = None,
    ):
        # Specifies whether to enable the QueryNode data cloud disk.
        self.enabled = enabled
        # The ESSD performance level (PL). Valid values: PL0, PL1, PL2, and PL3. If StorageClass is not specified, this field is used for parsing.
        self.performance_level = performance_level
        # The data cloud disk capacity. Unit: GiB.
        self.size = size
        # The StorageClass of the data cloud disk. Valid values: alicloud-disk-essd-pl0, alicloud-disk-essd-pl1, alicloud-disk-essd-pl2, and alicloud-disk-essd-pl3.
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level

        if self.size is not None:
            result['size'] = self.size

        if self.storage_class is not None:
            result['storageClass'] = self.storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('storageClass') is not None:
            self.storage_class = m.get('storageClass')

        return self

