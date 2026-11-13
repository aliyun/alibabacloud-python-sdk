# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataQualityScanShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        compute_resource_shrink: str = None,
        description: str = None,
        hooks_shrink: str = None,
        name: str = None,
        owner: str = None,
        parameters_shrink: str = None,
        project_id: int = None,
        runtime_resource_shrink: str = None,
        spec: str = None,
        trigger_shrink: str = None,
    ):
        # The idempotency token.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The compute engine used when the data quality monitor runs. This parameter is optional. If it is not specified, the data source connection specified in the Spec is used.
        self.compute_resource_shrink = compute_resource_shrink
        # The description of the data quality monitor.
        self.description = description
        # The configuration for hooks that run after the data quality monitor finishes.
        self.hooks_shrink = hooks_shrink
        # The name of the data quality monitor.
        self.name = name
        # The user ID of the owner of the data quality monitor.
        self.owner = owner
        # The execution parameter definitions of the data quality monitor.
        self.parameters_shrink = parameters_shrink
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://dataworks.console.aliyun.com/overview) and go to the Workspace Management page to obtain the workspace ID. This parameter specifies the DataWorks workspace for the API call.
        self.project_id = project_id
        # The resource group used when the data quality monitor runs.
        self.runtime_resource_shrink = runtime_resource_shrink
        # The Spec code that defines the data quality monitor. For more information, see [Data quality spec configuration guide](https://help.aliyun.com/document_detail/2963394.html).
        self.spec = spec
        # The trigger settings of the data quality monitor.
        self.trigger_shrink = trigger_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compute_resource_shrink is not None:
            result['ComputeResource'] = self.compute_resource_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.hooks_shrink is not None:
            result['Hooks'] = self.hooks_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_resource_shrink is not None:
            result['RuntimeResource'] = self.runtime_resource_shrink

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.trigger_shrink is not None:
            result['Trigger'] = self.trigger_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ComputeResource') is not None:
            self.compute_resource_shrink = m.get('ComputeResource')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Hooks') is not None:
            self.hooks_shrink = m.get('Hooks')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            self.runtime_resource_shrink = m.get('RuntimeResource')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Trigger') is not None:
            self.trigger_shrink = m.get('Trigger')

        return self

