# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class GetIncidentInvestigationResponseBody(DaraModel):
    def __init__(
        self,
        incident_investigation: main_models.GetIncidentInvestigationResponseBodyIncidentInvestigation = None,
        request_id: str = None,
    ):
        # The AI investigation details of the incident. This field is empty if no matching investigation record is found.
        self.incident_investigation = incident_investigation
        # The request ID, which is used to locate and troubleshoot this call.
        self.request_id = request_id

    def validate(self):
        if self.incident_investigation:
            self.incident_investigation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.incident_investigation is not None:
            result['IncidentInvestigation'] = self.incident_investigation.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncidentInvestigation') is not None:
            temp_model = main_models.GetIncidentInvestigationResponseBodyIncidentInvestigation()
            self.incident_investigation = temp_model.from_map(m.get('IncidentInvestigation'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetIncidentInvestigationResponseBodyIncidentInvestigation(DaraModel):
    def __init__(
        self,
        incident_investigation_alert_name: str = None,
        incident_investigation_conclusion: str = None,
        incident_investigation_display_id: str = None,
        incident_investigation_end_time: int = None,
        incident_investigation_id: str = None,
        incident_investigation_output: str = None,
        incident_investigation_report: str = None,
        incident_investigation_start_time: int = None,
        incident_investigation_status: str = None,
        incident_investigation_summary: str = None,
        incident_uuid: str = None,
    ):
        # The name of the alert that triggered this AI investigation.
        self.incident_investigation_alert_name = incident_investigation_alert_name
        # The judgment conclusion of the AI investigation, corresponding to ai_judgement_conclusion in the report.
        self.incident_investigation_conclusion = incident_investigation_conclusion
        # The display ID of the AI investigation report. You can use this value as the IncidentInvestigationDisplayId parameter of this operation to query the report.
        self.incident_investigation_display_id = incident_investigation_display_id
        # The end time of the AI investigation, in seconds (UNIX timestamp). If the execution end time is not recorded, the last update time of the investigation record is used. This field is empty if neither time exists.
        self.incident_investigation_end_time = incident_investigation_end_time
        # The unique ID of the AI investigation report. You can use this value as the IncidentInvestigationId parameter of this operation to query the report.
        self.incident_investigation_id = incident_investigation_id
        # The output content of the AI investigation, in JSON-formatted string. This field can contain fields such as investigation_report (the investigation process and evidence body, which may use Markdown format). This field is empty if the corresponding output is not generated. Internal fields may change across report versions.
        self.incident_investigation_output = incident_investigation_output
        # The AI investigation report content, in JSON-formatted string. This field can contain fields such as judgement_category (judgment category), ai_judgement_conclusion (judgment conclusion), ai_summary (summary), attack process, and attack graph. The specific content may change across report versions.
        self.incident_investigation_report = incident_investigation_report
        # The start time of the AI investigation, in seconds (UNIX timestamp). If the execution start time is not recorded, the creation time of the investigation record is used. This field is empty if neither time exists.
        self.incident_investigation_start_time = incident_investigation_start_time
        # The judgment category of the AI investigation report, corresponding to judgement_category in the report. This field does not indicate the execution status of the asynchronous task. Valid values:
        # - real_attack: Real attack.
        # - blocked: Risk blocked.
        # - false_positive: Suspected false positive.
        # - insufficient_information_to_evaluate: Unable to determine.
        self.incident_investigation_status = incident_investigation_status
        # The summary of the AI investigation report, corresponding to ai_summary in the investigation results.
        self.incident_investigation_summary = incident_investigation_summary
        # The globally unique UUID of the incident.
        self.incident_uuid = incident_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.incident_investigation_alert_name is not None:
            result['IncidentInvestigationAlertName'] = self.incident_investigation_alert_name

        if self.incident_investigation_conclusion is not None:
            result['IncidentInvestigationConclusion'] = self.incident_investigation_conclusion

        if self.incident_investigation_display_id is not None:
            result['IncidentInvestigationDisplayId'] = self.incident_investigation_display_id

        if self.incident_investigation_end_time is not None:
            result['IncidentInvestigationEndTime'] = self.incident_investigation_end_time

        if self.incident_investigation_id is not None:
            result['IncidentInvestigationId'] = self.incident_investigation_id

        if self.incident_investigation_output is not None:
            result['IncidentInvestigationOutput'] = self.incident_investigation_output

        if self.incident_investigation_report is not None:
            result['IncidentInvestigationReport'] = self.incident_investigation_report

        if self.incident_investigation_start_time is not None:
            result['IncidentInvestigationStartTime'] = self.incident_investigation_start_time

        if self.incident_investigation_status is not None:
            result['IncidentInvestigationStatus'] = self.incident_investigation_status

        if self.incident_investigation_summary is not None:
            result['IncidentInvestigationSummary'] = self.incident_investigation_summary

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncidentInvestigationAlertName') is not None:
            self.incident_investigation_alert_name = m.get('IncidentInvestigationAlertName')

        if m.get('IncidentInvestigationConclusion') is not None:
            self.incident_investigation_conclusion = m.get('IncidentInvestigationConclusion')

        if m.get('IncidentInvestigationDisplayId') is not None:
            self.incident_investigation_display_id = m.get('IncidentInvestigationDisplayId')

        if m.get('IncidentInvestigationEndTime') is not None:
            self.incident_investigation_end_time = m.get('IncidentInvestigationEndTime')

        if m.get('IncidentInvestigationId') is not None:
            self.incident_investigation_id = m.get('IncidentInvestigationId')

        if m.get('IncidentInvestigationOutput') is not None:
            self.incident_investigation_output = m.get('IncidentInvestigationOutput')

        if m.get('IncidentInvestigationReport') is not None:
            self.incident_investigation_report = m.get('IncidentInvestigationReport')

        if m.get('IncidentInvestigationStartTime') is not None:
            self.incident_investigation_start_time = m.get('IncidentInvestigationStartTime')

        if m.get('IncidentInvestigationStatus') is not None:
            self.incident_investigation_status = m.get('IncidentInvestigationStatus')

        if m.get('IncidentInvestigationSummary') is not None:
            self.incident_investigation_summary = m.get('IncidentInvestigationSummary')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        return self

