# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDisposeStrategyRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        effective_status: int = None,
        end_time: int = None,
        entity_identity: str = None,
        entity_type: str = None,
        incident_uuid: str = None,
        order: str = None,
        order_field: str = None,
        page_size: int = None,
        playbook_name: str = None,
        playbook_types: str = None,
        playbook_uuid: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        sophon_task_id: str = None,
        start_time: int = None,
        status: int = None,
    ):
        # The page number. Pages start from page 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The status of the policy. Valid values:
        # 
        # *   0: invalid
        # *   1: valid
        self.effective_status = effective_status
        # The end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The feature value of the entity. Fuzzy match is supported.
        self.entity_identity = entity_identity
        # The entity type of the playbook. Valid values:
        # 
        # *   ip
        # *   process
        # *   file
        self.entity_type = entity_type
        self.incident_uuid = incident_uuid
        # The sort order. Valid values:
        # 
        # *   desc: descending order.
        # *   asc: ascending order.
        self.order = order
        # The sort field. Valid values:
        # 
        # *   GmtModified: sorts the policies by update time.
        # *   GmtCreate: sorts the policies by creation time.
        # *   FinishTime: sorts the policies by end time.
        self.order_field = order_field
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The name of the playbook, which is the unique identifier of the playbook.
        self.playbook_name = playbook_name
        # The type of the playbook. Valid values:
        # 
        # *   system: user-triggered playbook
        # *   custom: event-triggered playbook
        # *   custom_alert: alert-triggered playbook
        # *   soar-manual: user-run playbook
        # *   soar-mdr: MDR-run playbook
        self.playbook_types = playbook_types
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id
        # The ID of the account that you switch from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # - 0: the current Alibaba Cloud account
        # - 1: the global account
        self.role_type = role_type
        # The ID of the SOAR handling policy.
        self.sophon_task_id = sophon_task_id
        # The beginning of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.effective_status is not None:
            result['EffectiveStatus'] = self.effective_status

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.entity_identity is not None:
            result['EntityIdentity'] = self.entity_identity

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.order is not None:
            result['Order'] = self.order

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name

        if self.playbook_types is not None:
            result['PlaybookTypes'] = self.playbook_types

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EffectiveStatus') is not None:
            self.effective_status = m.get('EffectiveStatus')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EntityIdentity') is not None:
            self.entity_identity = m.get('EntityIdentity')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')

        if m.get('PlaybookTypes') is not None:
            self.playbook_types = m.get('PlaybookTypes')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

