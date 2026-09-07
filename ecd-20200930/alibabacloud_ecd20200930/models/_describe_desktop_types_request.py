# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDesktopTypesRequest(DaraModel):
    def __init__(
        self,
        applied_scope: str = None,
        business_channel: str = None,
        cpu_count: int = None,
        desktop_group_id_for_modify: str = None,
        desktop_id_for_modify: str = None,
        desktop_scenario: str = None,
        desktop_type_id: str = None,
        desktop_type_id_list: List[str] = None,
        gpu_count: float = None,
        gpu_driver_type: str = None,
        gpu_memory: int = None,
        instance_type_family: str = None,
        memory_size: int = None,
        office_site_id: str = None,
        order_by: str = None,
        order_type: str = None,
        region_id: str = None,
        scope: str = None,
        scope_set: List[str] = None,
        sort_type: str = None,
        support_min_session_count: int = None,
        zone_id: str = None,
    ):
        # The applicable scope of the specification. Default value: `Public`.
        self.applied_scope = applied_scope
        # The business channel. Valid values:
        # Enterprise: Enterprise Edition.
        # Business: Business Edition.
        self.business_channel = business_channel
        # The number of vCPUs.
        self.cpu_count = cpu_count
        # The ID of the shared cloud computer for which you want to change the specification. If this parameter is specified, the response includes compatibility information between the specification and the shared cloud computer.
        self.desktop_group_id_for_modify = desktop_group_id_for_modify
        # The ID of the cloud computer for which you want to change the specification. If this parameter is specified, the response includes compatibility information between the specification and the cloud computer.
        self.desktop_id_for_modify = desktop_id_for_modify
        # The scenarios of the cloud computer.
        self.desktop_scenario = desktop_scenario
        # The specification ID.
        # 
        # > If both `InstanceTypeFamily` and `DesktopTypeId` are left empty, information about all cloud computer specifications is returned.
        self.desktop_type_id = desktop_type_id
        # The list of specification IDs.
        self.desktop_type_id_list = desktop_type_id_list
        # The number of GPU cores.
        self.gpu_count = gpu_count
        # The GPU driver type.
        self.gpu_driver_type = gpu_driver_type
        # The GPU memory size. This parameter is meaningful only for GPU-accelerated cloud computers. Unit: MB.
        self.gpu_memory = gpu_memory
        # The instance family name.
        # 
        # > If both `InstanceTypeFamily` and `DesktopTypeId` are left empty, information about all cloud computer specifications is returned.
        self.instance_type_family = instance_type_family
        # The memory size. Unit: MiB.
        self.memory_size = memory_size
        # The ID of the office network to which the shared cloud computer belongs.
        self.office_site_id = office_site_id
        # The field by which to sort the results. If this parameter is not specified, results are sorted by creation time in descending order.
        self.order_by = order_by
        # The order type.
        self.order_type = order_type
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The billing method of the specification.
        self.scope = scope
        # The list of applicable scopes.
        self.scope_set = scope_set
        # The sort order.
        self.sort_type = sort_type
        # The minimum number of multi-sessions supported by the specification.
        self.support_min_session_count = support_min_session_count
        # > This parameter is not publicly available.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_scope is not None:
            result['AppliedScope'] = self.applied_scope

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count

        if self.desktop_group_id_for_modify is not None:
            result['DesktopGroupIdForModify'] = self.desktop_group_id_for_modify

        if self.desktop_id_for_modify is not None:
            result['DesktopIdForModify'] = self.desktop_id_for_modify

        if self.desktop_scenario is not None:
            result['DesktopScenario'] = self.desktop_scenario

        if self.desktop_type_id is not None:
            result['DesktopTypeId'] = self.desktop_type_id

        if self.desktop_type_id_list is not None:
            result['DesktopTypeIdList'] = self.desktop_type_id_list

        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_driver_type is not None:
            result['GpuDriverType'] = self.gpu_driver_type

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.scope_set is not None:
            result['ScopeSet'] = self.scope_set

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.support_min_session_count is not None:
            result['SupportMinSessionCount'] = self.support_min_session_count

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedScope') is not None:
            self.applied_scope = m.get('AppliedScope')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')

        if m.get('DesktopGroupIdForModify') is not None:
            self.desktop_group_id_for_modify = m.get('DesktopGroupIdForModify')

        if m.get('DesktopIdForModify') is not None:
            self.desktop_id_for_modify = m.get('DesktopIdForModify')

        if m.get('DesktopScenario') is not None:
            self.desktop_scenario = m.get('DesktopScenario')

        if m.get('DesktopTypeId') is not None:
            self.desktop_type_id = m.get('DesktopTypeId')

        if m.get('DesktopTypeIdList') is not None:
            self.desktop_type_id_list = m.get('DesktopTypeIdList')

        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuDriverType') is not None:
            self.gpu_driver_type = m.get('GpuDriverType')

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('ScopeSet') is not None:
            self.scope_set = m.get('ScopeSet')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('SupportMinSessionCount') is not None:
            self.support_min_session_count = m.get('SupportMinSessionCount')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

