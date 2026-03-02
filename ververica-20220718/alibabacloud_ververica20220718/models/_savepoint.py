# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Savepoint(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        deployment_id: str = None,
        description: str = None,
        job_id: str = None,
        modified_at: int = None,
        namespace: str = None,
        native_format: bool = None,
        savepoint_id: str = None,
        savepoint_location: str = None,
        savepoint_origin: str = None,
        status: main_models.SavepointStatus = None,
        stop_with_drain_enabled: bool = None,
    ):
        # The time when the savepoint was created.
        self.created_at = created_at
        # The deployment ID.
        self.deployment_id = deployment_id
        # The description of the savepoint.
        self.description = description
        # The job ID.
        self.job_id = job_id
        # The time when the savepoint was last modified.
        self.modified_at = modified_at
        # The name of the namespace.
        self.namespace = namespace
        # Specifies whether the savepoint is in native format.
        self.native_format = native_format
        # The savepoint ID.
        self.savepoint_id = savepoint_id
        # The storage URL of the savepoint.
        self.savepoint_location = savepoint_location
        # The method that is used to create a savepoint.
        # 
        # *   `USER_REQUEST`: The savepoint is manually created.
        # *   `STOP_WITH_SAVEPOINT`: The savepoint is created when you cancel the deployment.
        # *   `RETAINED_CHECKPOINT`: The savepoint is created based on the returned checkpoint.
        self.savepoint_origin = savepoint_origin
        # The status of the savepoint.
        self.status = status
        # Specifies whether to use the stop-with-drain mode.
        self.stop_with_drain_enabled = stop_with_drain_enabled

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.description is not None:
            result['description'] = self.description

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.native_format is not None:
            result['nativeFormat'] = self.native_format

        if self.savepoint_id is not None:
            result['savepointId'] = self.savepoint_id

        if self.savepoint_location is not None:
            result['savepointLocation'] = self.savepoint_location

        if self.savepoint_origin is not None:
            result['savepointOrigin'] = self.savepoint_origin

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.stop_with_drain_enabled is not None:
            result['stopWithDrainEnabled'] = self.stop_with_drain_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('nativeFormat') is not None:
            self.native_format = m.get('nativeFormat')

        if m.get('savepointId') is not None:
            self.savepoint_id = m.get('savepointId')

        if m.get('savepointLocation') is not None:
            self.savepoint_location = m.get('savepointLocation')

        if m.get('savepointOrigin') is not None:
            self.savepoint_origin = m.get('savepointOrigin')

        if m.get('status') is not None:
            temp_model = main_models.SavepointStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('stopWithDrainEnabled') is not None:
            self.stop_with_drain_enabled = m.get('stopWithDrainEnabled')

        return self

