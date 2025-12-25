# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSmartClipTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        editing_config_shrink: str = None,
        extend_param: str = None,
        input_config_shrink: str = None,
        output_config_shrink: str = None,
        workspace_id: str = None,
    ):
        self.editing_config_shrink = editing_config_shrink
        self.extend_param = extend_param
        # This parameter is required.
        self.input_config_shrink = input_config_shrink
        self.output_config_shrink = output_config_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.editing_config_shrink is not None:
            result['EditingConfig'] = self.editing_config_shrink

        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param

        if self.input_config_shrink is not None:
            result['InputConfig'] = self.input_config_shrink

        if self.output_config_shrink is not None:
            result['OutputConfig'] = self.output_config_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingConfig') is not None:
            self.editing_config_shrink = m.get('EditingConfig')

        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')

        if m.get('InputConfig') is not None:
            self.input_config_shrink = m.get('InputConfig')

        if m.get('OutputConfig') is not None:
            self.output_config_shrink = m.get('OutputConfig')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

