# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateApprovalProcessShrinkRequest(DaraModel):
    def __init__(
        self,
        approval_type: int = None,
        description: str = None,
        event_label: str = None,
        external_config: str = None,
        match_schema_configs_shrink: str = None,
        match_schemas_shrink: str = None,
        process_id: str = None,
        process_name: str = None,
        process_nodes: List[List[str]] = None,
    ):
        # The approval type. Valid values: 0 (built-in approval), 1 (DingTalk approval), 2 (WeCom approval), and 3 (Lark approval). Default value: 0.
        self.approval_type = approval_type
        # The description of the approval process. The description must be 1 to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), hyphens (-), and spaces.
        self.description = description
        # The event callback identifier. When the approval type is 1 (DingTalk approval) or 3 (Lark approval), this parameter is used to generate the event callback URL for the external platform. You can pass a complete callback URL, and the server retains only the part after the callback path prefix.
        self.event_label = event_label
        # The integration configuration for the external approval platform. This parameter is required when the approval type is 1 (DingTalk approval) or 3 (Lark approval). It includes integration parameters such as appKey and appSecret, and must be passed as a JSON string.
        self.external_config = external_config
        # The external approval template configurations. Configure the approval template ID, external approval process ID, and field mappings based on the policy type. This parameter is used only when ApprovalType is set to 1 (DingTalk approval), 2 (WeCom approval), or 3 (Lark approval). If this parameter is not passed, the existing template associations of the approval process are cleared. The approval templates associated with business policies cannot be cleared.
        self.match_schema_configs_shrink = match_schema_configs_shrink
        # The matched approval templates.
        self.match_schemas_shrink = match_schemas_shrink
        # The ID of the approval process.
        # 
        # This parameter is required.
        self.process_id = process_id
        # The name of the approval process. The name must be 1 to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-).
        self.process_name = process_name
        # The list of approval nodes. You can define up to 5 approval nodes.
        self.process_nodes = process_nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.description is not None:
            result['Description'] = self.description

        if self.event_label is not None:
            result['EventLabel'] = self.event_label

        if self.external_config is not None:
            result['ExternalConfig'] = self.external_config

        if self.match_schema_configs_shrink is not None:
            result['MatchSchemaConfigs'] = self.match_schema_configs_shrink

        if self.match_schemas_shrink is not None:
            result['MatchSchemas'] = self.match_schemas_shrink

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_nodes is not None:
            result['ProcessNodes'] = self.process_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventLabel') is not None:
            self.event_label = m.get('EventLabel')

        if m.get('ExternalConfig') is not None:
            self.external_config = m.get('ExternalConfig')

        if m.get('MatchSchemaConfigs') is not None:
            self.match_schema_configs_shrink = m.get('MatchSchemaConfigs')

        if m.get('MatchSchemas') is not None:
            self.match_schemas_shrink = m.get('MatchSchemas')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessNodes') is not None:
            self.process_nodes = m.get('ProcessNodes')

        return self

