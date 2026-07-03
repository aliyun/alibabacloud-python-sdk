# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class GetIncidentResponseBody(DaraModel):
    def __init__(
        self,
        incident: main_models.GetIncidentResponseBodyIncident = None,
        request_id: str = None,
    ):
        # The event information.
        self.incident = incident
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.incident:
            self.incident.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.incident is not None:
            result['Incident'] = self.incident.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Incident') is not None:
            temp_model = main_models.GetIncidentResponseBodyIncident()
            self.incident = temp_model.from_map(m.get('Incident'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetIncidentResponseBodyIncident(DaraModel):
    def __init__(
        self,
        attck_tactics: Any = None,
        create_time: int = None,
        detection_rule_id: str = None,
        incident_aggregation_type: str = None,
        incident_description: str = None,
        incident_name: str = None,
        incident_remark: str = None,
        incident_status: int = None,
        incident_tags: str = None,
        incident_uuid: str = None,
        owner: str = None,
        relate_alert_count: int = None,
        relate_asset_count: int = None,
        relate_data_source_ids: Any = None,
        relate_user_ids: Any = None,
        response_time: int = None,
        threat_level: str = None,
        threat_score: str = None,
        update_time: int = None,
    ):
        # The count of attack stages associated with the event alerts.
        self.attck_tactics = attck_tactics
        # The creation time.
        self.create_time = create_time
        # The ID of the detection rule.
        self.detection_rule_id = detection_rule_id
        # The event summaries type. Valid values:
        # 
        # - none: no event is generated.
        # - graph_compute: graph computing (supported by predefined rules).
        # - expert: expert rule.
        # - passthrough: alerting pass-through (one-to-one).
        # - window: same-type aggregation (window).
        self.incident_aggregation_type = incident_aggregation_type
        # The description of the event.
        self.incident_description = incident_description
        # The name of the event.
        self.incident_name = incident_name
        # The remarks of the event.
        self.incident_remark = incident_remark
        # The status of the event. Valid values:
        # - 0: unhandled.
        # - 1: handling.
        # - 5: handling failed.
        # - 10: handled.
        self.incident_status = incident_status
        # The tags of the event.
        self.incident_tags = incident_tags
        # The UUID of the event.
        self.incident_uuid = incident_uuid
        # The owner of the event.
        self.owner = owner
        # The number of alerts associated with the event.
        self.relate_alert_count = relate_alert_count
        # The number of assets associated with the event.
        self.relate_asset_count = relate_asset_count
        # The list of associated data sources.
        self.relate_data_source_ids = relate_data_source_ids
        # The list of user IDs associated with the event.
        self.relate_user_ids = relate_user_ids
        # The response time. Unit: milliseconds (ms).
        self.response_time = response_time
        # The threat level. Valid values:
        # - 5: critical.
        # - 4: high.
        # - 3: medium.
        # - 2: low.
        # - 1: informational.
        self.threat_level = threat_level
        # The threat score of the event. Valid values: 0 to 100. A higher score indicates a higher risk level.
        self.threat_score = threat_score
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attck_tactics is not None:
            result['AttckTactics'] = self.attck_tactics

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id

        if self.incident_aggregation_type is not None:
            result['IncidentAggregationType'] = self.incident_aggregation_type

        if self.incident_description is not None:
            result['IncidentDescription'] = self.incident_description

        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name

        if self.incident_remark is not None:
            result['IncidentRemark'] = self.incident_remark

        if self.incident_status is not None:
            result['IncidentStatus'] = self.incident_status

        if self.incident_tags is not None:
            result['IncidentTags'] = self.incident_tags

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.relate_alert_count is not None:
            result['RelateAlertCount'] = self.relate_alert_count

        if self.relate_asset_count is not None:
            result['RelateAssetCount'] = self.relate_asset_count

        if self.relate_data_source_ids is not None:
            result['RelateDataSourceIds'] = self.relate_data_source_ids

        if self.relate_user_ids is not None:
            result['RelateUserIds'] = self.relate_user_ids

        if self.response_time is not None:
            result['ResponseTime'] = self.response_time

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.threat_score is not None:
            result['ThreatScore'] = self.threat_score

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttckTactics') is not None:
            self.attck_tactics = m.get('AttckTactics')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')

        if m.get('IncidentAggregationType') is not None:
            self.incident_aggregation_type = m.get('IncidentAggregationType')

        if m.get('IncidentDescription') is not None:
            self.incident_description = m.get('IncidentDescription')

        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')

        if m.get('IncidentRemark') is not None:
            self.incident_remark = m.get('IncidentRemark')

        if m.get('IncidentStatus') is not None:
            self.incident_status = m.get('IncidentStatus')

        if m.get('IncidentTags') is not None:
            self.incident_tags = m.get('IncidentTags')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RelateAlertCount') is not None:
            self.relate_alert_count = m.get('RelateAlertCount')

        if m.get('RelateAssetCount') is not None:
            self.relate_asset_count = m.get('RelateAssetCount')

        if m.get('RelateDataSourceIds') is not None:
            self.relate_data_source_ids = m.get('RelateDataSourceIds')

        if m.get('RelateUserIds') is not None:
            self.relate_user_ids = m.get('RelateUserIds')

        if m.get('ResponseTime') is not None:
            self.response_time = m.get('ResponseTime')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('ThreatScore') is not None:
            self.threat_score = m.get('ThreatScore')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

