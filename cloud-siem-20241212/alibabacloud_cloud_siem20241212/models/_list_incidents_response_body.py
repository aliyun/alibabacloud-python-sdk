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
        self.incidents = incidents
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
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
        create_time: int = None,
        detection_rule_id: str = None,
        incident_name: str = None,
        incident_remark: str = None,
        incident_status: int = None,
        incident_tags: str = None,
        incident_uuid: str = None,
        owner: str = None,
        relate_alert_count: int = None,
        relate_asset_count: int = None,
        threat_level: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.detection_rule_id = detection_rule_id
        self.incident_name = incident_name
        self.incident_remark = incident_remark
        self.incident_status = incident_status
        self.incident_tags = incident_tags
        self.incident_uuid = incident_uuid
        self.owner = owner
        self.relate_alert_count = relate_alert_count
        self.relate_asset_count = relate_asset_count
        self.threat_level = threat_level
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id

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

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')

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

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

