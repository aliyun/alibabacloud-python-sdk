# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        callable_agents_shrink: str = None,
        description: str = None,
        display_name: str = None,
        expected_version: int = None,
        expert_suites_shrink: str = None,
        metadata_shrink: str = None,
        model_shrink: str = None,
        name: str = None,
        publish_immediately: bool = None,
        skills_shrink: str = None,
        system_prompt: str = None,
        tools_shrink: str = None,
        visibility: str = None,
        visibility_scope_shrink: str = None,
    ):
        # The list of callable sub-agent references. For non-empty references, the referenced sub-agents must be visible. The agent cannot reference itself or form a call loop. Omit this parameter if no modification is required. Do not use an empty array to express general retention or clearing semantics.
        self.callable_agents_shrink = callable_agents_shrink
        # The description of the agent.
        self.description = description
        # The display name of the agent.
        self.display_name = display_name
        # The agent definition version used for concurrency control. We recommend explicitly specifying the AgentVersion you just obtained from GetAgent for each call. The update is rejected if the version does not match the current version on the server. To ensure compatibility with different deployment versions, do not rely on the server-side processing when this parameter is omitted.
        self.expected_version = expected_version
        # The list of expert suite references. If omitted, the existing references are retained. An explicit empty array clears the references. For official suites, specify only Source=OFFICIAL and SuiteId. Version, VersionSelector, or client artifact fields are not accepted. For custom suites, use SuiteId, and you can explicitly specify an existing integer Version.
        self.expert_suites_shrink = expert_suites_shrink
        # The extended metadata. If omitted, the existing metadata is retained. If provided, the business metadata is updated, and the server retains the protected system metadata.
        self.metadata_shrink = metadata_shrink
        # The model configuration.
        self.model_shrink = model_shrink
        # The name of the agent to be updated. Use the Name returned by GetAgent. This field is used to locate the target agent and is not used for renaming.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to publish the agent immediately after the update. If this parameter is set to true, the operation saves a new draft version before requesting publication. If this parameter is set to false or omitted, it saves only the definition. Saving and publishing are not atomic operations. If the operation fails, call GetAgent to read the current version before retrying to avoid blindly repeating the update.
        self.publish_immediately = publish_immediately
        # The list of skill references. Omit this parameter if no modification is required. Do not use an empty array to indicate retention or clearing. For official skills, specify only Source=OFFICIAL and SkillId. Name, Version, VersionSelector, or client artifact fields are not accepted. For custom skills, specify Name, and you can explicitly specify an existing integer Version.
        self.skills_shrink = skills_shrink
        # The system prompt.
        self.system_prompt = system_prompt
        # The list of tool references. Omit this parameter if no modification is required. The current new backend retains existing tools even for an empty array. A non-empty array replaces the references. Each item must include Kind and the corresponding configuration, and cannot include only Name. Replace the MCP service and tool names in the example with actual values available to the current identity.
        self.tools_shrink = tools_shrink
        # The visibility level.<br>TENANT: visible within the account.<br>PROJECT: visible to specified projects.<br>USER: visible to specified users.
        self.visibility = visibility
        # The visibility scope. The corresponding field is used based on the Visibility value.
        self.visibility_scope_shrink = visibility_scope_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callable_agents_shrink is not None:
            result['CallableAgents'] = self.callable_agents_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.expected_version is not None:
            result['ExpectedVersion'] = self.expected_version

        if self.expert_suites_shrink is not None:
            result['ExpertSuites'] = self.expert_suites_shrink

        if self.metadata_shrink is not None:
            result['Metadata'] = self.metadata_shrink

        if self.model_shrink is not None:
            result['Model'] = self.model_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.publish_immediately is not None:
            result['PublishImmediately'] = self.publish_immediately

        if self.skills_shrink is not None:
            result['Skills'] = self.skills_shrink

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        if self.tools_shrink is not None:
            result['Tools'] = self.tools_shrink

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.visibility_scope_shrink is not None:
            result['VisibilityScope'] = self.visibility_scope_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallableAgents') is not None:
            self.callable_agents_shrink = m.get('CallableAgents')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ExpectedVersion') is not None:
            self.expected_version = m.get('ExpectedVersion')

        if m.get('ExpertSuites') is not None:
            self.expert_suites_shrink = m.get('ExpertSuites')

        if m.get('Metadata') is not None:
            self.metadata_shrink = m.get('Metadata')

        if m.get('Model') is not None:
            self.model_shrink = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublishImmediately') is not None:
            self.publish_immediately = m.get('PublishImmediately')

        if m.get('Skills') is not None:
            self.skills_shrink = m.get('Skills')

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        if m.get('Tools') is not None:
            self.tools_shrink = m.get('Tools')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            self.visibility_scope_shrink = m.get('VisibilityScope')

        return self

