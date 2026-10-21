# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListIncidentsResponseBody(DaraModel):
    def __init__(
        self,
        incidents: List[main_models.ListIncidentsResponseBodyIncidents] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of incidents.
        self.incidents = incidents
        # The maximum number of entries to read in this request.
        self.max_results = max_results
        # The pagination token used to retrieve the next page of results. Leave this parameter empty for the first request or when there are no more pages. If more pages exist, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The current page number for pagination.
        self.page_number = page_number
        # The number of entries to display per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.incidents:
            for v1 in self.incidents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Incidents'] = []
        if self.incidents is not None:
            for k1 in self.incidents:
                result['Incidents'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.incidents = []
        if m.get('Incidents') is not None:
            for k1 in m.get('Incidents'):
                temp_model = main_models.ListIncidentsResponseBodyIncidents()
                self.incidents.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIncidentsResponseBodyIncidents(DaraModel):
    def __init__(
        self,
        alert_infos: str = None,
        alert_sources: List[str] = None,
        attck_tactics: str = None,
        create_time: int = None,
        detection_rule_id: str = None,
        detection_rule_name: str = None,
        entity_infos: str = None,
        incident_description: str = None,
        incident_name: str = None,
        incident_remark: str = None,
        incident_status: int = None,
        incident_tags: str = None,
        incident_uuid: str = None,
        owner: str = None,
        owner_name: str = None,
        relate_alert_count: int = None,
        relate_asset_count: int = None,
        response_time: int = None,
        response_types: List[str] = None,
        threat_level: str = None,
        update_time: int = None,
    ):
        # The list of associated alert information.
        self.alert_infos = alert_infos
        # The list of alert source codes or modules.
        self.alert_sources = alert_sources
        # The list of MITRE ATT&CK tactics.
        self.attck_tactics = attck_tactics
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The ID of the detection rule.
        self.detection_rule_id = detection_rule_id
        # The name of the detection rule.
        self.detection_rule_name = detection_rule_name
        # The list of associated entity information.
        self.entity_infos = entity_infos
        # The description of the incident.
        self.incident_description = incident_description
        # The event name.
        self.incident_name = incident_name
        # The remark for the incident.
        self.incident_remark = incident_remark
        # The event status. Valid values:
        # - 0: Unhandled.
        # - 1: Handling.
        # - 5: Handling failed.
        # - 10: Handled.
        self.incident_status = incident_status
        # The event tags.
        self.incident_tags = incident_tags
        # The UUID of the incident.
        self.incident_uuid = incident_uuid
        # The UID of the account responsible for the event.
        self.owner = owner
        # The display name of the incident owner.
        self.owner_name = owner_name
        # The number of alerts associated with the incident.
        self.relate_alert_count = relate_alert_count
        # The number of assets associated with the incident.
        self.relate_asset_count = relate_asset_count
        # The response time, in milliseconds (ms).
        self.response_time = response_time
        # The list of response types. Valid values: auto, manual, ai.
        self.response_types = response_types
        # The threat level. Valid values:
        # - 5: Critical.
        # - 4: High.
        # - 3: Medium.
        # - 2: Low.
        # - 1: Informational.
        self.threat_level = threat_level
        # The update time. The value is a UNIX timestamp in milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_infos is not None:
            result['AlertInfos'] = self.alert_infos

        if self.alert_sources is not None:
            result['AlertSources'] = self.alert_sources

        if self.attck_tactics is not None:
            result['AttckTactics'] = self.attck_tactics

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id

        if self.detection_rule_name is not None:
            result['DetectionRuleName'] = self.detection_rule_name

        if self.entity_infos is not None:
            result['EntityInfos'] = self.entity_infos

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

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.relate_alert_count is not None:
            result['RelateAlertCount'] = self.relate_alert_count

        if self.relate_asset_count is not None:
            result['RelateAssetCount'] = self.relate_asset_count

        if self.response_time is not None:
            result['ResponseTime'] = self.response_time

        if self.response_types is not None:
            result['ResponseTypes'] = self.response_types

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertInfos') is not None:
            self.alert_infos = m.get('AlertInfos')

        if m.get('AlertSources') is not None:
            self.alert_sources = m.get('AlertSources')

        if m.get('AttckTactics') is not None:
            self.attck_tactics = m.get('AttckTactics')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')

        if m.get('DetectionRuleName') is not None:
            self.detection_rule_name = m.get('DetectionRuleName')

        if m.get('EntityInfos') is not None:
            self.entity_infos = m.get('EntityInfos')

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

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('RelateAlertCount') is not None:
            self.relate_alert_count = m.get('RelateAlertCount')

        if m.get('RelateAssetCount') is not None:
            self.relate_asset_count = m.get('RelateAssetCount')

        if m.get('ResponseTime') is not None:
            self.response_time = m.get('ResponseTime')

        if m.get('ResponseTypes') is not None:
            self.response_types = m.get('ResponseTypes')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

