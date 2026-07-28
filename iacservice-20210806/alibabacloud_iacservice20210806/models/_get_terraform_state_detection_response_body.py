# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetTerraformStateDetectionResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetTerraformStateDetectionResponseBodyJob = None,
        request_id: str = None,
    ):
        # The job details.
        self.job = job
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job is not None:
            result['job'] = self.job.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('job') is not None:
            temp_model = main_models.GetTerraformStateDetectionResponseBodyJob()
            self.job = temp_model.from_map(m.get('job'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetTerraformStateDetectionResponseBodyJob(DaraModel):
    def __init__(
        self,
        changed_resources: List[main_models.GetTerraformStateDetectionResponseBodyJobChangedResources] = None,
        drifted_resources: List[main_models.GetTerraformStateDetectionResponseBodyJobDriftedResources] = None,
        error_message: str = None,
        identifier: str = None,
        status: str = None,
        type: str = None,
    ):
        # The collection of resources with state changes.
        self.changed_resources = changed_resources
        # The collection of resources with state drift.
        self.drifted_resources = drifted_resources
        # The error message.
        self.error_message = error_message
        # The task identifier. For a Stack task, the value is in the format of <$stackId>:<$deploymentName>. For a Task task, the value is <$TaskId>.
        self.identifier = identifier
        # The job status. Valid values:
        # 
        # - Pending: the initial status after the job is created.
        # - PlanQueued: the job is queued because no containers are available after the job is created.
        # - Planning: the resource job is in the Plan execution phase.
        # - Planned: the resource job has completed the Plan execution.
        # - PlannedAndFinished: no differences are found after the Plan execution is complete. The job is in a final status.
        # - Errored: the job execution encountered an error and entered a final status.
        self.status = status
        # The task type.
        self.type = type

    def validate(self):
        if self.changed_resources:
            for v1 in self.changed_resources:
                 if v1:
                    v1.validate()
        if self.drifted_resources:
            for v1 in self.drifted_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['changedResources'] = []
        if self.changed_resources is not None:
            for k1 in self.changed_resources:
                result['changedResources'].append(k1.to_map() if k1 else None)

        result['driftedResources'] = []
        if self.drifted_resources is not None:
            for k1 in self.drifted_resources:
                result['driftedResources'].append(k1.to_map() if k1 else None)

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.identifier is not None:
            result['identifier'] = self.identifier

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.changed_resources = []
        if m.get('changedResources') is not None:
            for k1 in m.get('changedResources'):
                temp_model = main_models.GetTerraformStateDetectionResponseBodyJobChangedResources()
                self.changed_resources.append(temp_model.from_map(k1))

        self.drifted_resources = []
        if m.get('driftedResources') is not None:
            for k1 in m.get('driftedResources'):
                temp_model = main_models.GetTerraformStateDetectionResponseBodyJobDriftedResources()
                self.drifted_resources.append(temp_model.from_map(k1))

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetTerraformStateDetectionResponseBodyJobDriftedResources(DaraModel):
    def __init__(
        self,
        attribute_drifts: List[main_models.GetTerraformStateDetectionResponseBodyJobDriftedResourcesAttributeDrifts] = None,
        drifted_type: str = None,
        resource_id: str = None,
        resource_identifier: str = None,
    ):
        # The collection of attribute drifts.
        self.attribute_drifts = attribute_drifts
        # The drift type.
        self.drifted_type = drifted_type
        # The Terraform resource ID.
        self.resource_id = resource_id
        # The identifier of the resource in the Terraform template. For a Stack task, the value is in the format of <$componetName>:<$resourceName>. For a Task task, the value is <$resourceName>.
        self.resource_identifier = resource_identifier

    def validate(self):
        if self.attribute_drifts:
            for v1 in self.attribute_drifts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['attributeDrifts'] = []
        if self.attribute_drifts is not None:
            for k1 in self.attribute_drifts:
                result['attributeDrifts'].append(k1.to_map() if k1 else None)

        if self.drifted_type is not None:
            result['driftedType'] = self.drifted_type

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_identifier is not None:
            result['resourceIdentifier'] = self.resource_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_drifts = []
        if m.get('attributeDrifts') is not None:
            for k1 in m.get('attributeDrifts'):
                temp_model = main_models.GetTerraformStateDetectionResponseBodyJobDriftedResourcesAttributeDrifts()
                self.attribute_drifts.append(temp_model.from_map(k1))

        if m.get('driftedType') is not None:
            self.drifted_type = m.get('driftedType')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceIdentifier') is not None:
            self.resource_identifier = m.get('resourceIdentifier')

        return self

class GetTerraformStateDetectionResponseBodyJobDriftedResourcesAttributeDrifts(DaraModel):
    def __init__(
        self,
        attribute_path: str = None,
        remote_value: str = None,
        state_value: str = None,
    ):
        # The attribute name.
        self.attribute_path = attribute_path
        # The server-side state value.
        self.remote_value = remote_value
        # The value stored in the state file.
        self.state_value = state_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_path is not None:
            result['attributePath'] = self.attribute_path

        if self.remote_value is not None:
            result['remoteValue'] = self.remote_value

        if self.state_value is not None:
            result['stateValue'] = self.state_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributePath') is not None:
            self.attribute_path = m.get('attributePath')

        if m.get('remoteValue') is not None:
            self.remote_value = m.get('remoteValue')

        if m.get('stateValue') is not None:
            self.state_value = m.get('stateValue')

        return self

class GetTerraformStateDetectionResponseBodyJobChangedResources(DaraModel):
    def __init__(
        self,
        attribute_changes: List[main_models.GetTerraformStateDetectionResponseBodyJobChangedResourcesAttributeChanges] = None,
        changed_type: str = None,
        has_drift: bool = None,
        resource_id: str = None,
        resource_identifier: str = None,
    ):
        # The collection of attribute changes.
        self.attribute_changes = attribute_changes
        # The change type.
        self.changed_type = changed_type
        # Indicates whether resource drift exists.
        self.has_drift = has_drift
        # The Terraform resource ID.
        self.resource_id = resource_id
        # The identifier of the resource in the Terraform template. For a Stack task, the value is in the format of <$componetName>:<$resourceName>. For a Task task, the value is <$resourceName>.
        self.resource_identifier = resource_identifier

    def validate(self):
        if self.attribute_changes:
            for v1 in self.attribute_changes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['attributeChanges'] = []
        if self.attribute_changes is not None:
            for k1 in self.attribute_changes:
                result['attributeChanges'].append(k1.to_map() if k1 else None)

        if self.changed_type is not None:
            result['changedType'] = self.changed_type

        if self.has_drift is not None:
            result['hasDrift'] = self.has_drift

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_identifier is not None:
            result['resourceIdentifier'] = self.resource_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_changes = []
        if m.get('attributeChanges') is not None:
            for k1 in m.get('attributeChanges'):
                temp_model = main_models.GetTerraformStateDetectionResponseBodyJobChangedResourcesAttributeChanges()
                self.attribute_changes.append(temp_model.from_map(k1))

        if m.get('changedType') is not None:
            self.changed_type = m.get('changedType')

        if m.get('hasDrift') is not None:
            self.has_drift = m.get('hasDrift')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceIdentifier') is not None:
            self.resource_identifier = m.get('resourceIdentifier')

        return self

class GetTerraformStateDetectionResponseBodyJobChangedResourcesAttributeChanges(DaraModel):
    def __init__(
        self,
        attribute_path: str = None,
        remote_value: str = None,
        template_value: str = None,
    ):
        # The attribute name.
        self.attribute_path = attribute_path
        # The server-side state value.
        self.remote_value = remote_value
        # The template-declared value.
        self.template_value = template_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_path is not None:
            result['attributePath'] = self.attribute_path

        if self.remote_value is not None:
            result['remoteValue'] = self.remote_value

        if self.template_value is not None:
            result['templateValue'] = self.template_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributePath') is not None:
            self.attribute_path = m.get('attributePath')

        if m.get('remoteValue') is not None:
            self.remote_value = m.get('remoteValue')

        if m.get('templateValue') is not None:
            self.template_value = m.get('templateValue')

        return self

