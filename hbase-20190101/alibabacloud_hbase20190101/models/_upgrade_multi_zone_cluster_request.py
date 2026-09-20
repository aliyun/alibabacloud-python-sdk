# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeMultiZoneClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        components: str = None,
        restart_components: str = None,
        run_mode: str = None,
        upgrade_ins_name: str = None,
        versions: str = None,
    ):
        # The ID of the multi-zone instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The component names. You can specify multiple component names separated by commas (,).
        # 
        # This parameter is required.
        self.components = components
        # The names of the components that need to be restarted after the upgrade. You can specify multiple component names separated by commas (,).
        self.restart_components = restart_components
        # The execution mode. If UpgradeInsName is not empty, the mode is forcibly set to single. If UpgradeInsName is empty and RunMode is not specified, the default value is serial. Valid values:
        # 
        # - serial: all sub-instances are upgraded.
        # - single: only the specified sub-instance is upgraded.
        self.run_mode = run_mode
        # The name of the sub-instance to upgrade. You can obtain this value from the MultiZoneInstanceModels field in the response of the [DescribeMultiZoneCluster](~~DescribeMultiZoneCluster~~) operation. This parameter is optional. If you do not specify this parameter, all sub-instances are upgraded.
        self.upgrade_ins_name = upgrade_ins_name
        # The RPM version to upgrade to. If you do not specify this parameter, the components are upgraded to the latest version. If you specify multiple values for Components, you must also specify the same number of values for Versions, separated by commas (,).
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.components is not None:
            result['Components'] = self.components

        if self.restart_components is not None:
            result['RestartComponents'] = self.restart_components

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.upgrade_ins_name is not None:
            result['UpgradeInsName'] = self.upgrade_ins_name

        if self.versions is not None:
            result['Versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Components') is not None:
            self.components = m.get('Components')

        if m.get('RestartComponents') is not None:
            self.restart_components = m.get('RestartComponents')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('UpgradeInsName') is not None:
            self.upgrade_ins_name = m.get('UpgradeInsName')

        if m.get('Versions') is not None:
            self.versions = m.get('Versions')

        return self

