# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeKernelVersionRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        kernel_version: str = None,
        lang: str = None,
        product_code: str = None,
        product_id: int = None,
        switch_time: int = None,
        upgrade_time: str = None,
    ):
        # The database instance identity. You can obtain this value from Items[].InstanceId returned by ListDataMaskingInstances.
        self.instance_id = instance_id
        # The target kernel version. You can obtain this value from KernelVersions[].KernelVersion returned by ListMiniEngineVersions.
        self.kernel_version = kernel_version
        # The language of the response description. Valid values:
        # 
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # The cloud product code. Column encryption supports RDS, POLARDB, and PolarDBX2. If you also specify ProductId, the two values must correspond to each other.
        self.product_code = product_code
        # The cloud product type identifier. Valid values:
        # 
        # - 5: RDS.
        # - 8: POLARDB.
        # - 27: PolarDBX2.
        # 
        # If you specify both ProductId and ProductCode, the values must correspond to each other.
        self.product_id = product_id
        # The specified upgrade time. This value is a UNIX timestamp in milliseconds since 1970-01-01 00:00:00 UTC. Specify this parameter only when UpgradeTime is set to SpecifyTime. The value must be later than the current time.
        self.switch_time = switch_time
        # The time at which the kernel upgrade is performed. Valid values:
        # 
        # - Immediate: The upgrade is performed immediately.
        # - MaintainTime: The upgrade is performed during the maintenance window.
        # - SpecifyTime: The upgrade is performed at a specified time.
        # 
        # PolarDB-X 2.0 does not support SpecifyTime.
        self.upgrade_time = upgrade_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.upgrade_time is not None:
            result['UpgradeTime'] = self.upgrade_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('UpgradeTime') is not None:
            self.upgrade_time = m.get('UpgradeTime')

        return self

