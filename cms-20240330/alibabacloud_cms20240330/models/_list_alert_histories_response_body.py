# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListAlertHistoriesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAlertHistoriesResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of alert histories that match the query conditions.
        self.data = data
        # The maximum number of entries to return.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The unique identifier of the request.
        self.request_id = request_id
        # The total number of alert history records that match the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListAlertHistoriesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListAlertHistoriesResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_history_id: str = None,
        alert_rule_id: str = None,
        annotations: Dict[str, str] = None,
        biz_source: str = None,
        count: int = None,
        end_time: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        instance_detail: Dict[str, str] = None,
        instance_key: str = None,
        labels: Dict[str, str] = None,
        latest_level: str = None,
        max_level: str = None,
        message: str = None,
        observe_resource_global_scope: bool = None,
        observe_resource_list: str = None,
        observe_resource_type: str = None,
        region_id: str = None,
        rule_display_name: str = None,
        send: main_models.AlertRuleSend = None,
        start_time: int = None,
        status: str = None,
        workspace: str = None,
    ):
        # The unique identifier of the alert history.
        self.alert_history_id = alert_history_id
        # The unique identifier of the alert rule that generated the alert history.
        self.alert_rule_id = alert_rule_id
        # The snapshot of the annotations of the alert rule. The annotations are stored as key-value pairs and copied from the rule when the alert is triggered.
        self.annotations = annotations
        # The business source.
        self.biz_source = biz_source
        # The cumulative number of alerts (alert events) during the alert duration.
        self.count = count
        # The end time (recovery time) of the alert. This field has a value only when the alert history enters the OK state. The value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The creation time of the alert history record. The value is a UNIX timestamp in milliseconds.
        self.gmt_create = gmt_create
        # The last modification time of the alert history record. The value is a UNIX timestamp in milliseconds.
        self.gmt_modified = gmt_modified
        # The detailed information of the alert object. The information is stored as key-value pairs.
        self.instance_detail = instance_detail
        # The unique key (instanceKey) used to identify the alert object instance.
        self.instance_key = instance_key
        # The snapshot of the labels of the alert rule. The labels are stored as key-value pairs and copied from the rule when the alert is triggered.
        self.labels = labels
        # The level of the most recent alert during the alert duration, such as CRITICAL, WARN, or INFO.
        self.latest_level = latest_level
        # The highest alert level reached during the alert duration.
        self.max_level = max_level
        # The content of the latest alert message.
        self.message = message
        # Indicates whether the observed object is in the global scope. The value is copied from the rule when the alert history is created.
        self.observe_resource_global_scope = observe_resource_global_scope
        # The serialized string of the observed object list. The value is copied from the rule when the alert history is created.
        self.observe_resource_list = observe_resource_list
        # The type of the observed object, such as PROMETHEUS, APM, RUM, or cms_basic. The value is copied from the rule when the alert history is created.
        self.observe_resource_type = observe_resource_type
        # The ID of the region to which the alert history belongs.
        self.region_id = region_id
        # The display name of the corresponding rule.
        self.rule_display_name = rule_display_name
        # The notification sending configuration information corresponding to the alert history.
        self.send = send
        # The start time of the alert history. The value is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # The current alert status of the rule. Valid values: OK (recovered) and ALARM (alerting).
        self.status = status
        # The identifier of the workspace to which the alert history belongs.
        self.workspace = workspace

    def validate(self):
        if self.send:
            self.send.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_history_id is not None:
            result['alertHistoryId'] = self.alert_history_id

        if self.alert_rule_id is not None:
            result['alertRuleId'] = self.alert_rule_id

        if self.annotations is not None:
            result['annotations'] = self.annotations

        if self.biz_source is not None:
            result['bizSource'] = self.biz_source

        if self.count is not None:
            result['count'] = self.count

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.instance_detail is not None:
            result['instanceDetail'] = self.instance_detail

        if self.instance_key is not None:
            result['instanceKey'] = self.instance_key

        if self.labels is not None:
            result['labels'] = self.labels

        if self.latest_level is not None:
            result['latestLevel'] = self.latest_level

        if self.max_level is not None:
            result['maxLevel'] = self.max_level

        if self.message is not None:
            result['message'] = self.message

        if self.observe_resource_global_scope is not None:
            result['observeResourceGlobalScope'] = self.observe_resource_global_scope

        if self.observe_resource_list is not None:
            result['observeResourceList'] = self.observe_resource_list

        if self.observe_resource_type is not None:
            result['observeResourceType'] = self.observe_resource_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.rule_display_name is not None:
            result['ruleDisplayName'] = self.rule_display_name

        if self.send is not None:
            result['send'] = self.send.to_map()

        if self.start_time is not None:
            result['startTime'] = self.start_time

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

        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')

        if m.get('bizSource') is not None:
            self.biz_source = m.get('bizSource')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('instanceDetail') is not None:
            self.instance_detail = m.get('instanceDetail')

        if m.get('instanceKey') is not None:
            self.instance_key = m.get('instanceKey')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('latestLevel') is not None:
            self.latest_level = m.get('latestLevel')

        if m.get('maxLevel') is not None:
            self.max_level = m.get('maxLevel')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('observeResourceGlobalScope') is not None:
            self.observe_resource_global_scope = m.get('observeResourceGlobalScope')

        if m.get('observeResourceList') is not None:
            self.observe_resource_list = m.get('observeResourceList')

        if m.get('observeResourceType') is not None:
            self.observe_resource_type = m.get('observeResourceType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('ruleDisplayName') is not None:
            self.rule_display_name = m.get('ruleDisplayName')

        if m.get('send') is not None:
            temp_model = main_models.AlertRuleSend()
            self.send = temp_model.from_map(m.get('send'))

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

