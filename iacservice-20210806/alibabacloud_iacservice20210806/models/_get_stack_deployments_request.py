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
        # The name of the deployment.
        self.deployment_name = deployment_name
        # The deployment number. The deployment number of each stack starts from 1 and increments each time a deployment is successfully triggered.
        self.deployment_no = deployment_no
        # The page number. Pages start from 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20. Minimum value: 1. Maximum value: 200.
        self.page_size = page_size
        # The deployment status. Valid values:
        # | Name | Description |
        # |------|------|
        # | Pending | The initial status after the deployment is created. |
        # | PriorityQueued | The deployment is queued with priority. |
        # | PlanQueued | The deployment is queued and waiting for an available workflow after it is created. |
        # | ApplyQueued | The deployment is queued and waiting for an available workflow during execution. |
        # | Planning | The deployment is in the plan phase. |
        # | Planned | The deployment has completed the plan phase. |
        # | ConfigProactiveInProgress | The compliance precheck is in progress. |
        # | ConfigProactiveSuccess | The compliance precheck is successful. |
        # | DetectInProgress | Drift detection is in progress. |
        # | ImportQueued | The deployment is queued and waiting for an available workflow during the import phase. |
        # | Importing | The deployment is in the import phase. |
        # | Imported | The deployment has completed the import phase. |
        # | StateQueued | The deployment is queued and waiting for an available workflow during the state command execution. |
        # | Stating | The deployment is executing the state command. |
        # | Stated | The deployment has completed the execution of the state command. |
        # | Confirmed | The deployment is confirmed after the plan phase. |
        # | PlannedAndFinished | The deployment is in the final state because no differences are found after the plan phase. |
        # | Applying | The deployment is in the apply phase. |
        # | Applied | The deployment has completed the apply phase. |
        # | Discarded | The deployment is discarded and enters the final state. |
        # | Errored | An error occurred during the deployment execution, and the deployment enters the final state. |
        # | ConfigProactiveFailure | The compliance precheck failed. |
        # | Canceled | The deployment execution is canceled, and the deployment enters the final state. |
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

