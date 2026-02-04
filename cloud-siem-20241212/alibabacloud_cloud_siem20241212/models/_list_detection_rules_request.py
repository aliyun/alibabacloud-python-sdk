# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDetectionRulesRequest(DaraModel):
    def __init__(
        self,
        alert_att_ck: str = None,
        alert_level: str = None,
        alert_tactic_id: str = None,
        alert_type: str = None,
        detection_expression_type: str = None,
        detection_rule_id: str = None,
        detection_rule_ids: List[str] = None,
        detection_rule_name: str = None,
        detection_rule_status: str = None,
        detection_rule_type: str = None,
        incident_aggregation_type: str = None,
        lang: str = None,
        log_category_id: str = None,
        log_schema_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order_direction: str = None,
        order_field_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.alert_att_ck = alert_att_ck
        self.alert_level = alert_level
        self.alert_tactic_id = alert_tactic_id
        self.alert_type = alert_type
        self.detection_expression_type = detection_expression_type
        self.detection_rule_id = detection_rule_id
        self.detection_rule_ids = detection_rule_ids
        self.detection_rule_name = detection_rule_name
        self.detection_rule_status = detection_rule_status
        self.detection_rule_type = detection_rule_type
        self.incident_aggregation_type = incident_aggregation_type
        self.lang = lang
        self.log_category_id = log_category_id
        self.log_schema_id = log_schema_id
        self.max_results = max_results
        self.next_token = next_token
        self.order_direction = order_direction
        self.order_field_name = order_field_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_att_ck is not None:
            result['AlertAttCk'] = self.alert_att_ck

        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level

        if self.alert_tactic_id is not None:
            result['AlertTacticId'] = self.alert_tactic_id

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.detection_expression_type is not None:
            result['DetectionExpressionType'] = self.detection_expression_type

        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id

        if self.detection_rule_ids is not None:
            result['DetectionRuleIds'] = self.detection_rule_ids

        if self.detection_rule_name is not None:
            result['DetectionRuleName'] = self.detection_rule_name

        if self.detection_rule_status is not None:
            result['DetectionRuleStatus'] = self.detection_rule_status

        if self.detection_rule_type is not None:
            result['DetectionRuleType'] = self.detection_rule_type

        if self.incident_aggregation_type is not None:
            result['IncidentAggregationType'] = self.incident_aggregation_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_category_id is not None:
            result['LogCategoryId'] = self.log_category_id

        if self.log_schema_id is not None:
            result['LogSchemaId'] = self.log_schema_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction

        if self.order_field_name is not None:
            result['OrderFieldName'] = self.order_field_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertAttCk') is not None:
            self.alert_att_ck = m.get('AlertAttCk')

        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('AlertTacticId') is not None:
            self.alert_tactic_id = m.get('AlertTacticId')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('DetectionExpressionType') is not None:
            self.detection_expression_type = m.get('DetectionExpressionType')

        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')

        if m.get('DetectionRuleIds') is not None:
            self.detection_rule_ids = m.get('DetectionRuleIds')

        if m.get('DetectionRuleName') is not None:
            self.detection_rule_name = m.get('DetectionRuleName')

        if m.get('DetectionRuleStatus') is not None:
            self.detection_rule_status = m.get('DetectionRuleStatus')

        if m.get('DetectionRuleType') is not None:
            self.detection_rule_type = m.get('DetectionRuleType')

        if m.get('IncidentAggregationType') is not None:
            self.incident_aggregation_type = m.get('IncidentAggregationType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogCategoryId') is not None:
            self.log_category_id = m.get('LogCategoryId')

        if m.get('LogSchemaId') is not None:
            self.log_schema_id = m.get('LogSchemaId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')

        if m.get('OrderFieldName') is not None:
            self.order_field_name = m.get('OrderFieldName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

