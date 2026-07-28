# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStackDeploymentsRequest(DaraModel):
    def __init__(
        self,
        config_version: str = None,
        deployment_name: str = None,
        deployment_no: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # The configuration version, such as v1. The initial value is v1. The version number increments each time the stack is updated or refreshed and the configuration changes.
        self.config_version = config_version
        # The deployment name.
        self.deployment_name = deployment_name
        # The deployment number. The deployment number of each stack starts from 1 and increments each time a deployment is triggered.
        self.deployment_no = deployment_no
        # The page number, starting from 1.
        self.page_number = page_number
        # The number of results per page. Default value: 20. Minimum value: 1. Maximum value: 200.
        self.page_size = page_size
        # The deployment status.
        # | Name | Description |
        # |------|------|
        # | Pending | The initial status after a deployment is created. |
        # | PriorityQueued | The deployment is queued by priority. |
        # | PlanQueued | The deployment is queued because no workflow is available after the deployment is created. |
        # | ApplyQueued | The deployment is queued because no workflow is available during execution. |
        # | Planning | The resource deployment is in the Plan phase. |
        # | Planned | The resource deployment has completed the Plan phase. |
        # | ConfigProactiveInProgress | A compliance pre-check is in progress. |
        # | ConfigProactiveSuccess | The compliance pre-check succeeded. |
        # | DetectInProgress | Drift detection is in progress. |
        # | ImportQueued | The deployment is queued because no workflow is available during the Import phase. |
        # | Importing | The resource deployment is in the Import phase. |
        # | Imported | The resource deployment has completed the Import phase. |
        # | StateQueued | The deployment is queued because no workflow is available during the state command execution. |
        # | Stating | The resource deployment is executing the state command. |
        # | Stated | The resource deployment has completed the state command execution. |
        # | Confirmed | The resource deployment has been confirmed after the Plan phase. |
        # | PlannedAndFinished | No differences were found after the Plan phase. The deployment is in a final status. |
        # | Applying | The resource deployment is in the Apply phase. |
        # | Applied | The resource deployment has completed the Apply phase. |
        # | Discarded | The resource deployment has been discarded and is in a final status. |
        # | Errored | The deployment encountered an error and is in a final status. |
        # | ConfigProactiveFailure | The compliance pre-check failed. |
        # | Canceled | The deployment has been canceled and is in a final status. |.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_version is not None:
            result['configVersion'] = self.config_version

        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name

        if self.deployment_no is not None:
            result['deploymentNo'] = self.deployment_no

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configVersion') is not None:
            self.config_version = m.get('configVersion')

        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')

        if m.get('deploymentNo') is not None:
            self.deployment_no = m.get('deploymentNo')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

