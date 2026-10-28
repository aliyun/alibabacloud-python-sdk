# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertHistoriesShrinkRequest(DaraModel):
    def __init__(
        self,
        alert_history_id: str = None,
        alert_rule_id: str = None,
        biz_source: str = None,
        cms_namespace: str = None,
        cms_product_category: str = None,
        display_name_key_word: str = None,
        instance_key: str = None,
        label_filter_shrink: str = None,
        latest_level: str = None,
        max_level: str = None,
        max_results: int = None,
        migration_status: int = None,
        next_token: str = None,
        notification_filter_shrink: str = None,
        observe_relation_type: str = None,
        observe_resource_domain: str = None,
        observe_resource_global_scope: bool = None,
        observe_resource_instance_id: str = None,
        observe_resource_type: str = None,
        page_number: int = None,
        page_size: int = None,
        partition_key: str = None,
        start_time_from: int = None,
        start_time_to: int = None,
        status: str = None,
        workspace: str = None,
    ):
        # The unique identifier (transId) of an alert history record.
        self.alert_history_id = alert_history_id
        # Filters the history records by a specific alert rule. Specify the unique identifier (ruleUuid) of the alert rule.
        self.alert_rule_id = alert_rule_id
        # The business source of the alert history. For example, `managed_service_for_prometheus` indicates the managed type of the Prometheus integration center. The default value is empty. Leave this parameter empty if you are unsure about the value.
        self.biz_source = biz_source
        # The namespace of CloudMonitor. Examples: acs_rds_dashboard and acs_ecs_dashboard.
        self.cms_namespace = cms_namespace
        # The product category of CloudMonitor.
        self.cms_product_category = cms_product_category
        # The keyword used for fuzzy matching and filtering based on the display name of the alert rule.
        self.display_name_key_word = display_name_key_word
        # The unique key (instanceKey) used to identify the alert object instance.
        self.instance_key = instance_key
        # The filter condition for rule labels. The value is a JSON-formatted string that supports filtering by label key-value pairs.
        self.label_filter_shrink = label_filter_shrink
        # The level of the most recent alert during the alert duration. Valid values: CRITICAL, WARN, and INFO.
        self.latest_level = latest_level
        # The highest alert level reached during the alert duration. Valid values: CRITICAL, WARN, and INFO.
        self.max_level = max_level
        # The maximum number of results to return on each page. This parameter is not supported. Use pageSize and pageNumber for pagination.
        self.max_results = max_results
        # The migration status of the alert history.
        self.migration_status = migration_status
        # The pagination token used for the next query. This parameter is not supported. Use pageSize and pageNumber for pagination.
        self.next_token = next_token
        # Filters alert rules that contain specific notification recipients. Only rules that contain at least one of the notification recipients specified in notifyTargets are returned in the result list.
        self.notification_filter_shrink = notification_filter_shrink
        # The relation type of the observed object. Examples: GROUP, INSTANCE, and TAG.
        self.observe_relation_type = observe_relation_type
        # The dimension column (domain) of the observed object.
        self.observe_resource_domain = observe_resource_domain
        # Specifies whether the observed object is in the global scope.
        self.observe_resource_global_scope = observe_resource_global_scope
        # Filters the alert history by resource instance ID.
        self.observe_resource_instance_id = observe_resource_instance_id
        # The type of the observed object. Examples: PROMETHEUS, APM, RUM, and cms_basic.
        self.observe_resource_type = observe_resource_type
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of alert history records to return on each page. Default value: 10.
        self.page_size = page_size
        # The key used for data partitioning. Typically, you do not need to specify this parameter.
        self.partition_key = partition_key
        # The start timestamp of the time range for the alert start time. The value is a UNIX timestamp in milliseconds. If not specified, the default value is the time 30 days ago.
        self.start_time_from = start_time_from
        # The end timestamp of the time range for the alert start time. The value is a UNIX timestamp in milliseconds. If not specified, the default value is the current time.
        self.start_time_to = start_time_to
        # The current status of the alert history. Valid values: OK and ALARM.
        self.status = status
        # The identifier of the workspace to which the alert history belongs. If not specified, the default workspace is used.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_history_id is not None:
            result['alertHistoryId'] = self.alert_history_id

        if self.alert_rule_id is not None:
            result['alertRuleId'] = self.alert_rule_id

        if self.biz_source is not None:
            result['bizSource'] = self.biz_source

        if self.cms_namespace is not None:
            result['cmsNamespace'] = self.cms_namespace

        if self.cms_product_category is not None:
            result['cmsProductCategory'] = self.cms_product_category

        if self.display_name_key_word is not None:
            result['displayNameKeyWord'] = self.display_name_key_word

        if self.instance_key is not None:
            result['instanceKey'] = self.instance_key

        if self.label_filter_shrink is not None:
            result['labelFilter'] = self.label_filter_shrink

        if self.latest_level is not None:
            result['latestLevel'] = self.latest_level

        if self.max_level is not None:
            result['maxLevel'] = self.max_level

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.migration_status is not None:
            result['migrationStatus'] = self.migration_status

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.notification_filter_shrink is not None:
            result['notificationFilter'] = self.notification_filter_shrink

        if self.observe_relation_type is not None:
            result['observeRelationType'] = self.observe_relation_type

        if self.observe_resource_domain is not None:
            result['observeResourceDomain'] = self.observe_resource_domain

        if self.observe_resource_global_scope is not None:
            result['observeResourceGlobalScope'] = self.observe_resource_global_scope

        if self.observe_resource_instance_id is not None:
            result['observeResourceInstanceId'] = self.observe_resource_instance_id

        if self.observe_resource_type is not None:
            result['observeResourceType'] = self.observe_resource_type

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.partition_key is not None:
            result['partitionKey'] = self.partition_key

        if self.start_time_from is not None:
            result['startTimeFrom'] = self.start_time_from

        if self.start_time_to is not None:
            result['startTimeTo'] = self.start_time_to

        if self.status is not None:
            result['status'] = self.status

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertHistoryId') is not None:
            self.alert_history_id = m.get('alertHistoryId')

        if m.get('alertRuleId') is not None:
            self.alert_rule_id = m.get('alertRuleId')

        if m.get('bizSource') is not None:
            self.biz_source = m.get('bizSource')

        if m.get('cmsNamespace') is not None:
            self.cms_namespace = m.get('cmsNamespace')

        if m.get('cmsProductCategory') is not None:
            self.cms_product_category = m.get('cmsProductCategory')

        if m.get('displayNameKeyWord') is not None:
            self.display_name_key_word = m.get('displayNameKeyWord')

        if m.get('instanceKey') is not None:
            self.instance_key = m.get('instanceKey')

        if m.get('labelFilter') is not None:
            self.label_filter_shrink = m.get('labelFilter')

        if m.get('latestLevel') is not None:
            self.latest_level = m.get('latestLevel')

        if m.get('maxLevel') is not None:
            self.max_level = m.get('maxLevel')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('migrationStatus') is not None:
            self.migration_status = m.get('migrationStatus')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('notificationFilter') is not None:
            self.notification_filter_shrink = m.get('notificationFilter')

        if m.get('observeRelationType') is not None:
            self.observe_relation_type = m.get('observeRelationType')

        if m.get('observeResourceDomain') is not None:
            self.observe_resource_domain = m.get('observeResourceDomain')

        if m.get('observeResourceGlobalScope') is not None:
            self.observe_resource_global_scope = m.get('observeResourceGlobalScope')

        if m.get('observeResourceInstanceId') is not None:
            self.observe_resource_instance_id = m.get('observeResourceInstanceId')

        if m.get('observeResourceType') is not None:
            self.observe_resource_type = m.get('observeResourceType')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('partitionKey') is not None:
            self.partition_key = m.get('partitionKey')

        if m.get('startTimeFrom') is not None:
            self.start_time_from = m.get('startTimeFrom')

        if m.get('startTimeTo') is not None:
            self.start_time_to = m.get('startTimeTo')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

