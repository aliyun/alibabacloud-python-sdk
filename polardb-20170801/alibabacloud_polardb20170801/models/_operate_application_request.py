# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateApplicationRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        component_types: str = None,
        group_names: str = None,
        operation: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The Ray component type. Supported only for the restart operation of Ray applications. The value is a comma-separated list of components. Valid components are head, jupyterlab, and grafana, which can be combined. worker or gpuworker is not accepted. To select workers, you must specify GroupNames. If only head is specified, other components are not actively restarted, but connections and jobs may be affected. To restore dependencies, explicitly add jupyterlab or select the entire cluster. When provided together with GroupNames, the union of both is used and deduplicated. If neither selection parameter is provided, all resident components are restarted, but scaled-out workers are not restarted. Explicit empty strings, pure whitespace, comma-only strings, unknown types, or non-Ray applications are rejected and do not fall back to a full-cluster operation. DisableHeadScheduling and EnableHeadScheduling always apply to the head of the entire application. Specifying this parameter for these operations is rejected.
        self.component_types = component_types
        # The Ray resident worker group name. Supported only for the restart operation of Ray applications. The value is a comma-separated list of exact workerGroup names, which are trimmed, deduplicated, and case-sensitive. Only resident CPU or GPU workers in the specified groups are restarted, excluding scaled-out workers. If only this parameter is specified, the head, other groups, or auxiliary components are not restarted. Unknown group names, explicit empty strings, pure whitespace, comma-only strings, or non-Ray applications are rejected. If any explicitly selected group exists but has no resident targets, the entire request is rejected and does not expand to scaled-out workers or a full-cluster operation. Full-cluster requests without selection parameters skip groups with no resident targets. DisableHeadScheduling and EnableHeadScheduling do not restart any workers. Specifying this parameter for these operations is rejected.
        self.group_names = group_names
        # The operation type.
        # 
        # * **restart**: Restart.
        # * **stop**: Stop.
        # * **start**: Start.
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.component_types is not None:
            result['ComponentTypes'] = self.component_types

        if self.group_names is not None:
            result['GroupNames'] = self.group_names

        if self.operation is not None:
            result['Operation'] = self.operation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ComponentTypes') is not None:
            self.component_types = m.get('ComponentTypes')

        if m.get('GroupNames') is not None:
            self.group_names = m.get('GroupNames')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        return self

