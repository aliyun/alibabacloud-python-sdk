# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDetectionRuleRequest(DaraModel):
    def __init__(
        self,
        alert_att_ck: str = None,
        alert_att_ck_mapping: str = None,
        alert_description: str = None,
        alert_level: str = None,
        alert_level_mapping: str = None,
        alert_name: str = None,
        alert_schema_id: str = None,
        alert_tactic_id: str = None,
        alert_threshold_count: int = None,
        alert_threshold_group: str = None,
        alert_threshold_period: str = None,
        alert_type: str = None,
        alert_type_mapping: str = None,
        detection_expression_content: str = None,
        detection_expression_type: str = None,
        detection_rule_description: str = None,
        detection_rule_id: str = None,
        detection_rule_name: str = None,
        detection_rule_status: str = None,
        detection_rule_type: str = None,
        entity_mappings: str = None,
        incident_aggregation_expression: str = None,
        incident_aggregation_type: str = None,
        lang: str = None,
        log_category_id: str = None,
        log_schema_id: str = None,
        playbook_parameters: str = None,
        playbook_uuid: str = None,
        region_id: str = None,
        schedule_begin_time: int = None,
        schedule_expression: str = None,
        schedule_max_retries: int = None,
        schedule_max_timeout: int = None,
        schedule_type: str = None,
        schedule_window: str = None,
    ):
        self.alert_att_ck = alert_att_ck
        self.alert_att_ck_mapping = alert_att_ck_mapping
        self.alert_description = alert_description
        self.alert_level = alert_level
        self.alert_level_mapping = alert_level_mapping
        self.alert_name = alert_name
        self.alert_schema_id = alert_schema_id
        self.alert_tactic_id = alert_tactic_id
        self.alert_threshold_count = alert_threshold_count
        self.alert_threshold_group = alert_threshold_group
        self.alert_threshold_period = alert_threshold_period
        self.alert_type = alert_type
        self.alert_type_mapping = alert_type_mapping
        self.detection_expression_content = detection_expression_content
        self.detection_expression_type = detection_expression_type
        self.detection_rule_description = detection_rule_description
        # This parameter is required.
        self.detection_rule_id = detection_rule_id
        self.detection_rule_name = detection_rule_name
        self.detection_rule_status = detection_rule_status
        # This parameter is required.
        self.detection_rule_type = detection_rule_type
        self.entity_mappings = entity_mappings
        self.incident_aggregation_expression = incident_aggregation_expression
        self.incident_aggregation_type = incident_aggregation_type
        self.lang = lang
        self.log_category_id = log_category_id
        self.log_schema_id = log_schema_id
        self.playbook_parameters = playbook_parameters
        self.playbook_uuid = playbook_uuid
        self.region_id = region_id
        self.schedule_begin_time = schedule_begin_time
        self.schedule_expression = schedule_expression
        self.schedule_max_retries = schedule_max_retries
        self.schedule_max_timeout = schedule_max_timeout
        self.schedule_type = schedule_type
        self.schedule_window = schedule_window

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_att_ck is not None:
            result['AlertAttCk'] = self.alert_att_ck

        if self.alert_att_ck_mapping is not None:
            result['AlertAttCkMapping'] = self.alert_att_ck_mapping

        if self.alert_description is not None:
            result['AlertDescription'] = self.alert_description

        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level

        if self.alert_level_mapping is not None:
            result['AlertLevelMapping'] = self.alert_level_mapping

        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.alert_schema_id is not None:
            result['AlertSchemaId'] = self.alert_schema_id

        if self.alert_tactic_id is not None:
            result['AlertTacticId'] = self.alert_tactic_id

        if self.alert_threshold_count is not None:
            result['AlertThresholdCount'] = self.alert_threshold_count

        if self.alert_threshold_group is not None:
            result['AlertThresholdGroup'] = self.alert_threshold_group

        if self.alert_threshold_period is not None:
            result['AlertThresholdPeriod'] = self.alert_threshold_period

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.alert_type_mapping is not None:
            result['AlertTypeMapping'] = self.alert_type_mapping

        if self.detection_expression_content is not None:
            result['DetectionExpressionContent'] = self.detection_expression_content

        if self.detection_expression_type is not None:
            result['DetectionExpressionType'] = self.detection_expression_type

        if self.detection_rule_description is not None:
            result['DetectionRuleDescription'] = self.detection_rule_description

        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id

        if self.detection_rule_name is not None:
            result['DetectionRuleName'] = self.detection_rule_name

        if self.detection_rule_status is not None:
            result['DetectionRuleStatus'] = self.detection_rule_status

        if self.detection_rule_type is not None:
            result['DetectionRuleType'] = self.detection_rule_type

        if self.entity_mappings is not None:
            result['EntityMappings'] = self.entity_mappings

        if self.incident_aggregation_expression is not None:
            result['IncidentAggregationExpression'] = self.incident_aggregation_expression

        if self.incident_aggregation_type is not None:
            result['IncidentAggregationType'] = self.incident_aggregation_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_category_id is not None:
            result['LogCategoryId'] = self.log_category_id

        if self.log_schema_id is not None:
            result['LogSchemaId'] = self.log_schema_id

        if self.playbook_parameters is not None:
            result['PlaybookParameters'] = self.playbook_parameters

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.schedule_begin_time is not None:
            result['ScheduleBeginTime'] = self.schedule_begin_time

        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression

        if self.schedule_max_retries is not None:
            result['ScheduleMaxRetries'] = self.schedule_max_retries

        if self.schedule_max_timeout is not None:
            result['ScheduleMaxTimeout'] = self.schedule_max_timeout

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.schedule_window is not None:
            result['ScheduleWindow'] = self.schedule_window

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertAttCk') is not None:
            self.alert_att_ck = m.get('AlertAttCk')

        if m.get('AlertAttCkMapping') is not None:
            self.alert_att_ck_mapping = m.get('AlertAttCkMapping')

        if m.get('AlertDescription') is not None:
            self.alert_description = m.get('AlertDescription')

        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('AlertLevelMapping') is not None:
            self.alert_level_mapping = m.get('AlertLevelMapping')

        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('AlertSchemaId') is not None:
            self.alert_schema_id = m.get('AlertSchemaId')

        if m.get('AlertTacticId') is not None:
            self.alert_tactic_id = m.get('AlertTacticId')

        if m.get('AlertThresholdCount') is not None:
            self.alert_threshold_count = m.get('AlertThresholdCount')

        if m.get('AlertThresholdGroup') is not None:
            self.alert_threshold_group = m.get('AlertThresholdGroup')

        if m.get('AlertThresholdPeriod') is not None:
            self.alert_threshold_period = m.get('AlertThresholdPeriod')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AlertTypeMapping') is not None:
            self.alert_type_mapping = m.get('AlertTypeMapping')

        if m.get('DetectionExpressionContent') is not None:
            self.detection_expression_content = m.get('DetectionExpressionContent')

        if m.get('DetectionExpressionType') is not None:
            self.detection_expression_type = m.get('DetectionExpressionType')

        if m.get('DetectionRuleDescription') is not None:
            self.detection_rule_description = m.get('DetectionRuleDescription')

        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')

        if m.get('DetectionRuleName') is not None:
            self.detection_rule_name = m.get('DetectionRuleName')

        if m.get('DetectionRuleStatus') is not None:
            self.detection_rule_status = m.get('DetectionRuleStatus')

        if m.get('DetectionRuleType') is not None:
            self.detection_rule_type = m.get('DetectionRuleType')

        if m.get('EntityMappings') is not None:
            self.entity_mappings = m.get('EntityMappings')

        if m.get('IncidentAggregationExpression') is not None:
            self.incident_aggregation_expression = m.get('IncidentAggregationExpression')

        if m.get('IncidentAggregationType') is not None:
            self.incident_aggregation_type = m.get('IncidentAggregationType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogCategoryId') is not None:
            self.log_category_id = m.get('LogCategoryId')

        if m.get('LogSchemaId') is not None:
            self.log_schema_id = m.get('LogSchemaId')

        if m.get('PlaybookParameters') is not None:
            self.playbook_parameters = m.get('PlaybookParameters')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScheduleBeginTime') is not None:
            self.schedule_begin_time = m.get('ScheduleBeginTime')

        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')

        if m.get('ScheduleMaxRetries') is not None:
            self.schedule_max_retries = m.get('ScheduleMaxRetries')

        if m.get('ScheduleMaxTimeout') is not None:
            self.schedule_max_timeout = m.get('ScheduleMaxTimeout')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('ScheduleWindow') is not None:
            self.schedule_window = m.get('ScheduleWindow')

        return self

