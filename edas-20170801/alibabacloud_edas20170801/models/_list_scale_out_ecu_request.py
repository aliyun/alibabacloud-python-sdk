# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScaleOutEcuRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cluster_id: str = None,
        cpu: int = None,
        group_id: str = None,
        instance_num: int = None,
        logical_region_id: str = None,
        mem: int = None,
    ):
        # The ID of the application. Specify this parameter if you want to query the available ECUs in the cluster where the application is deployed.
        # 
        # > Specify at least one of the ClusterId and AppId parameters as the query parameter.
        self.app_id = app_id
        # The ID of the cluster. Specify this parameter if you want to query the available ECUs in the cluster.
        # 
        # > Specify at least one of the ClusterId and AppId parameters as the query parameter.
        self.cluster_id = cluster_id
        # The number of CPU cores based on which you want to query the available ECUs in the cluster.
        self.cpu = cpu
        # The ID of the instance group. Specify this parameter if you want to query the available ECUs in the cluster where the instance group resides.
        self.group_id = group_id
        # The number of ECUs that you want to query. If this parameter is not specified, all the ECUs that meet the query conditions are returned.
        self.instance_num = instance_num
        # The ID of the namespace.
        # 
        # - The ID of a custom namespace is in the `region ID:namespace identifier` format. Example: cn-beijing:test.
        # 
        # - The ID of the default namespace is in the `region ID` format. Example: cn-beijing.
        self.logical_region_id = logical_region_id
        # The size of available memory based on which you want to query the available ECUs in the cluster. Unit: MB.
        self.mem = mem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num

        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        if self.mem is not None:
            result['Mem'] = self.mem

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')

        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        return self

