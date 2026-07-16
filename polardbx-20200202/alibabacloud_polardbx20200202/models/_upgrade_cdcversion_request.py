# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeCDCVersionRequest(DaraModel):
    def __init__(
        self,
        cdc_db_version: str = None,
        cdc_minor_version: str = None,
        dbinstance_name: str = None,
        instance_name: str = None,
        region_id: str = None,
        switch_mode: str = None,
    ):
        # The target database engine version to which you want to upgrade. > You can call the [DescribeDBClusterVersion](https://help.aliyun.com/document_detail/196830.html) operation to query the upgrade instructions for all database engine versions in a specific region.
        self.cdc_db_version = cdc_db_version
        # The target version number to which you want to upgrade.
        self.cdc_minor_version = cdc_minor_version
        # The instance ID. > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) operation to query the details of all instances in a specific region, including instance IDs.
        self.dbinstance_name = dbinstance_name
        # The instance name.
        self.instance_name = instance_name
        # The region in which the instance resides. > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196841.html) operation to query the regions supported by PolarDB-X, including region IDs.
        self.region_id = region_id
        # The switch mode. Valid values:
        # 
        # - 0: immediately switches.
        # - 1: switches within the O&M window.
        self.switch_mode = switch_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdc_db_version is not None:
            result['CdcDbVersion'] = self.cdc_db_version

        if self.cdc_minor_version is not None:
            result['CdcMinorVersion'] = self.cdc_minor_version

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdcDbVersion') is not None:
            self.cdc_db_version = m.get('CdcDbVersion')

        if m.get('CdcMinorVersion') is not None:
            self.cdc_minor_version = m.get('CdcMinorVersion')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self

