# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class ListActivatedAlertsResponseBody(DaraModel):
    def __init__(
        self,
        page: main_models.ListActivatedAlertsResponseBodyPage = None,
        request_id: str = None,
    ):
        self.page = page
        self.request_id = request_id

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = main_models.ListActivatedAlertsResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListActivatedAlertsResponseBodyPage(DaraModel):
    def __init__(
        self,
        alerts: List[main_models.ListActivatedAlertsResponseBodyPageAlerts] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.alerts = alerts
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.alerts:
            for v1 in self.alerts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Alerts'] = []
        if self.alerts is not None:
            for k1 in self.alerts:
                result['Alerts'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alerts = []
        if m.get('Alerts') is not None:
            for k1 in m.get('Alerts'):
                temp_model = main_models.ListActivatedAlertsResponseBodyPageAlerts()
                self.alerts.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListActivatedAlertsResponseBodyPageAlerts(DaraModel):
    def __init__(
        self,
        alert_id: str = None,
        alert_name: str = None,
        alert_type: str = None,
        count: int = None,
        create_time: int = None,
        dispatch_rules: List[main_models.ListActivatedAlertsResponseBodyPageAlertsDispatchRules] = None,
        ends_at: int = None,
        expand_fields: Dict[str, Any] = None,
        integration_name: str = None,
        integration_type: str = None,
        involved_object_kind: str = None,
        involved_object_name: str = None,
        message: str = None,
        severity: str = None,
        starts_at: int = None,
        status: str = None,
    ):
        self.alert_id = alert_id
        self.alert_name = alert_name
        self.alert_type = alert_type
        self.count = count
        self.create_time = create_time
        self.dispatch_rules = dispatch_rules
        self.ends_at = ends_at
        self.expand_fields = expand_fields
        self.integration_name = integration_name
        self.integration_type = integration_type
        self.involved_object_kind = involved_object_kind
        self.involved_object_name = involved_object_name
        self.message = message
        self.severity = severity
        self.starts_at = starts_at
        self.status = status

    def validate(self):
        if self.dispatch_rules:
            for v1 in self.dispatch_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.count is not None:
            result['Count'] = self.count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['DispatchRules'] = []
        if self.dispatch_rules is not None:
            for k1 in self.dispatch_rules:
                result['DispatchRules'].append(k1.to_map() if k1 else None)

        if self.ends_at is not None:
            result['EndsAt'] = self.ends_at

        if self.expand_fields is not None:
            result['ExpandFields'] = self.expand_fields

        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name

        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type

        if self.involved_object_kind is not None:
            result['InvolvedObjectKind'] = self.involved_object_kind

        if self.involved_object_name is not None:
            result['InvolvedObjectName'] = self.involved_object_name

        if self.message is not None:
            result['Message'] = self.message

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.starts_at is not None:
            result['StartsAt'] = self.starts_at

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.dispatch_rules = []
        if m.get('DispatchRules') is not None:
            for k1 in m.get('DispatchRules'):
                temp_model = main_models.ListActivatedAlertsResponseBodyPageAlertsDispatchRules()
                self.dispatch_rules.append(temp_model.from_map(k1))

        if m.get('EndsAt') is not None:
            self.ends_at = m.get('EndsAt')

        if m.get('ExpandFields') is not None:
            self.expand_fields = m.get('ExpandFields')

        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')

        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')

        if m.get('InvolvedObjectKind') is not None:
            self.involved_object_kind = m.get('InvolvedObjectKind')

        if m.get('InvolvedObjectName') is not None:
            self.involved_object_name = m.get('InvolvedObjectName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('StartsAt') is not None:
            self.starts_at = m.get('StartsAt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListActivatedAlertsResponseBodyPageAlertsDispatchRules(DaraModel):
    def __init__(
        self,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

