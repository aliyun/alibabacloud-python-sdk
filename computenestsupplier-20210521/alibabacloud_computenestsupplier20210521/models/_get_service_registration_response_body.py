# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class GetServiceRegistrationResponseBody(DaraModel):
    def __init__(
        self,
        comment: str = None,
        detail: main_models.GetServiceRegistrationResponseBodyDetail = None,
        finish_time: str = None,
        registration_id: str = None,
        request_id: str = None,
        service_id: str = None,
        service_info: main_models.GetServiceRegistrationResponseBodyServiceInfo = None,
        service_version: str = None,
        status: str = None,
        submit_time: str = None,
    ):
        # Comment from reviewer.
        self.comment = comment
        # The details of service audit.
        self.detail = detail
        # Finish time.
        self.finish_time = finish_time
        # Service registration ID.
        self.registration_id = registration_id
        # The request ID.
        self.request_id = request_id
        # The service ID.
        self.service_id = service_id
        # The service details.
        self.service_info = service_info
        # The service version.
        self.service_version = service_version
        # The status of service registration. Valid values:
        # 
        # *   Submitted
        # *   Approved
        # *   Rejected
        # *   Canceled
        # *   Executed
        self.status = status
        # Submit time.
        self.submit_time = submit_time

    def validate(self):
        if self.detail:
            self.detail.validate()
        if self.service_info:
            self.service_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_info is not None:
            result['ServiceInfo'] = self.service_info.to_map()

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Detail') is not None:
            temp_model = main_models.GetServiceRegistrationResponseBodyDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInfo') is not None:
            temp_model = main_models.GetServiceRegistrationResponseBodyServiceInfo()
            self.service_info = temp_model.from_map(m.get('ServiceInfo'))

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        return self

class GetServiceRegistrationResponseBodyServiceInfo(DaraModel):
    def __init__(
        self,
        service_type: str = None,
        trial_type: str = None,
        version_name: str = None,
    ):
        # The type of the service. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        self.service_type = service_type
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type
        # The version name.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.trial_type is not None:
            result['TrialType'] = self.trial_type

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class GetServiceRegistrationResponseBodyDetail(DaraModel):
    def __init__(
        self,
        at_risk: bool = None,
        has_related_artifact: bool = None,
        reports: str = None,
        template_diff_url: str = None,
    ):
        # Whether risk exists.
        self.at_risk = at_risk
        # Whether service is associated with artifact.
        self.has_related_artifact = has_related_artifact
        # The reports.
        self.reports = reports
        # The url of template diff file.
        self.template_diff_url = template_diff_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.at_risk is not None:
            result['AtRisk'] = self.at_risk

        if self.has_related_artifact is not None:
            result['HasRelatedArtifact'] = self.has_related_artifact

        if self.reports is not None:
            result['Reports'] = self.reports

        if self.template_diff_url is not None:
            result['TemplateDiffUrl'] = self.template_diff_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtRisk') is not None:
            self.at_risk = m.get('AtRisk')

        if m.get('HasRelatedArtifact') is not None:
            self.has_related_artifact = m.get('HasRelatedArtifact')

        if m.get('Reports') is not None:
            self.reports = m.get('Reports')

        if m.get('TemplateDiffUrl') is not None:
            self.template_diff_url = m.get('TemplateDiffUrl')

        return self

