# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDisposeStrategyShrinkRequest(DaraModel):
    def __init__(
        self,
        alert_uuid: str = None,
        current_page: int = None,
        effective_status: int = None,
        end_time: int = None,
        entity_identity: str = None,
        entity_type: str = None,
        entity_uuid_list_shrink: str = None,
        group_by: str = None,
        group_key: str = None,
        incident_uuid: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_field: str = None,
        page_size: int = None,
        playbook_name: str = None,
        playbook_types: str = None,
        playbook_uuid: str = None,
        query_mode: str = None,
        region_id: str = None,
        response_rule_id: str = None,
        role_for: int = None,
        role_type: int = None,
        sophon_task_id: str = None,
        start_time: int = None,
        status: int = None,
        strategy_id: str = None,
    ):
        self.alert_uuid = alert_uuid
        # The current page number, which must be greater than or equal to 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The policy status. Valid values:
        self.effective_status = effective_status
        # The query end time, in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The entity characteristic value, which can be used for fuzzy match on response entities.
        self.entity_identity = entity_identity
        # The entity type. Valid values:
        self.entity_type = entity_type
        self.entity_uuid_list_shrink = entity_uuid_list_shrink
        self.group_by = group_by
        self.group_key = group_key
        # The event ID.
        self.incident_uuid = incident_uuid
        self.max_results = max_results
        self.next_token = next_token
        # The sort direction. Valid values:
        self.order = order
        # The field used to sort results. Valid values:
        # - GmtModified: sorts results by update time.
        # - GmtCreate: sorts results by creation time.
        # - FinishTime: sorts results by policy end time.
        self.order_field = order_field
        # The number of entries per page, with a maximum of 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The unique identifier name of the playbook.
        self.playbook_name = playbook_name
        # The playbook type. Valid values:
        # - system: manual handling
        # - custom: event-triggered playbook
        # - custom_alert: alert-triggered playbook
        # - soar-manual: manually run playbook
        # - soar-mdr: MDR-run playbook
        self.playbook_types = playbook_types
        # The playbook UUID.
        self.playbook_uuid = playbook_uuid
        self.query_mode = query_mode
        # The region where the data management center of Cloud Threat Detection and Response (CTDR) is located. Specify the management center based on the region of your assets. Valid values:
        self.region_id = region_id
        self.response_rule_id = response_rule_id
        # The Alibaba Cloud account ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # The view type.
        self.role_type = role_type
        # The SOAR response policy ID.
        self.sophon_task_id = sophon_task_id
        # The query start time, in milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The response policy status.
        self.status = status
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

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

        if self.entity_uuid_list_shrink is not None:
            result['EntityUuidList'] = self.entity_uuid_list_shrink

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

        if self.group_key is not None:
            result['GroupKey'] = self.group_key

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.response_rule_id is not None:
            result['ResponseRuleId'] = self.response_rule_id

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

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

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

        if m.get('EntityUuidList') is not None:
            self.entity_uuid_list_shrink = m.get('EntityUuidList')

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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

        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResponseRuleId') is not None:
            self.response_rule_id = m.get('ResponseRuleId')

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

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        return self

