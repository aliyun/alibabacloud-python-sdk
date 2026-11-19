# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateServiceEndpointRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateServiceEndpointRequestBody = None,
        client_token: str = None,
    ):
        # The name, routing target, and invocation authentication configuration of the service endpoint to be created, along with the optional initial elasticity configuration and public access switch.
        self.body = body
        # Required when elasticity initialization is included. It is verified by the server. The same token and original request are reused for the same retry. If the logical content changes, a new token is used. The same token with different content returns InvalidParameter. The token must be 1 to 128 characters in length and can contain letters, digits, and the following special characters: . _ : -. The scope is the tenant and workspace. The receipt is retained for 7 days from the time of successful acceptance. Replays do not extend the retention period. After expiration, it is verified again as a new submission.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateServiceEndpointRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateServiceEndpointRequestBody(DaraModel):
    def __init__(
        self,
        authentication: main_models.CreateServiceEndpointRequestBodyAuthentication = None,
        elasticity_policy: main_models.CreateServiceEndpointRequestBodyElasticityPolicy = None,
        name: str = None,
        public_access_enabled: bool = None,
        target: main_models.CreateServiceEndpointRequestBodyTarget = None,
    ):
        # Sets the invocation authentication configuration saved for the service endpoint, specified by type. For AGENT_VERSION endpoints of non-EDGE agents, the actual API key verification is determined by the current inbound authentication configuration of the agent. The management operation for creating service endpoints still uses AccessKey or STS authentication and RAM authorization.
        # 
        # This parameter is required.
        self.authentication = authentication
        # Explicitly provided when creating a service endpoint with elasticity capabilities. The capability scope follows existing rules. Null or partial patches are not accepted. It must include enabled, the basic minSandboxCount and maxSandboxCount, and the complete dynamicPolicy. The basic upper and lower limits are both 0 to 100, and min must be less than or equal to max. To disable dynamic scaling without policies, pass enabled=false and policies=[]. When elasticity initialization is included, clientToken must be provided, and updateElasticity is not passed. Conditional requirements and cross-field constraints are verified by the server.
        self.elasticity_policy = elasticity_policy
        # The name of the named service endpoint to be created. For the Router type, the name must be 1 to 128 characters in length and can contain lowercase letters, digits, underscores, and hyphens. It must start with a letter or a digit, cannot use the reserved name default, and must be unique within the same agent. The names of Router and hybrid ingress endpoints cannot be changed after creation.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to enable public network inbound access for the service endpoint. If omitted, it is initialized to true. If true or false is passed, the passed value is saved. An explicit null or non-boolean value returns InvalidParameter. Whether public network access is actually enabled is also subject to the public network inbound access limit of the workspace. For more information, see effectivePublicAccessEnabled in the response.
        self.public_access_enabled = public_access_enabled
        # Specifies the agent and its version associated with the service endpoint. The routing targets for collaboration components are maintained internally by the platform.
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        if self.authentication:
            self.authentication.validate()
        if self.elasticity_policy:
            self.elasticity_policy.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()

        if self.elasticity_policy is not None:
            result['elasticityPolicy'] = self.elasticity_policy.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.public_access_enabled is not None:
            result['publicAccessEnabled'] = self.public_access_enabled

        if self.target is not None:
            result['target'] = self.target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication') is not None:
            temp_model = main_models.CreateServiceEndpointRequestBodyAuthentication()
            self.authentication = temp_model.from_map(m.get('authentication'))

        if m.get('elasticityPolicy') is not None:
            temp_model = main_models.CreateServiceEndpointRequestBodyElasticityPolicy()
            self.elasticity_policy = temp_model.from_map(m.get('elasticityPolicy'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('publicAccessEnabled') is not None:
            self.public_access_enabled = m.get('publicAccessEnabled')

        if m.get('target') is not None:
            temp_model = main_models.CreateServiceEndpointRequestBodyTarget()
            self.target = temp_model.from_map(m.get('target'))

        return self

class CreateServiceEndpointRequestBodyTarget(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        collaboration_component: str = None,
        resource_binding_id: str = None,
        target_type: str = None,
    ):
        # The ID of the agent associated with the AGENT_VERSION routing target. The agent is located in the workspace specified in the request.
        self.agent_id = agent_id
        # The version of the agent associated with the AGENT_VERSION routing target. Use the agentVersion returned by CreateAgentVersion or ListAgentVersions, which is different from the version name versionName.
        self.agent_version = agent_version
        # The component associated with the TEAM_COLLABORATION routing target. MATRIX_CLIENT indicates the Matrix client ingress, MATRIX_FEDERATION indicates the Matrix federation ingress, and ELEMENT_WEB indicates the Element Web ingress. Service endpoints for collaboration components are created internally by the platform. Do not pass this field when publicly creating an AGENT_VERSION endpoint.
        self.collaboration_component = collaboration_component
        # The ID of the resource binding associated with the TEAM_COLLABORATION routing target. It is maintained internally by the platform and generated in the format of wrb- followed by a 32-character hexadecimal UUID. Do not pass this field when publicly creating an AGENT_VERSION endpoint.
        self.resource_binding_id = resource_binding_id
        # The public create operation only supports AGENT_VERSION, which indicates routing to a specified agent version. TEAM_COLLABORATION indicates a collaboration component. Service endpoints for collaboration components are created internally by the platform.
        # 
        # This parameter is required.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_version is not None:
            result['agentVersion'] = self.agent_version

        if self.collaboration_component is not None:
            result['collaborationComponent'] = self.collaboration_component

        if self.resource_binding_id is not None:
            result['resourceBindingId'] = self.resource_binding_id

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentVersion') is not None:
            self.agent_version = m.get('agentVersion')

        if m.get('collaborationComponent') is not None:
            self.collaboration_component = m.get('collaborationComponent')

        if m.get('resourceBindingId') is not None:
            self.resource_binding_id = m.get('resourceBindingId')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

class CreateServiceEndpointRequestBodyElasticityPolicy(DaraModel):
    def __init__(
        self,
        dynamic_policy: main_models.CreateServiceEndpointRequestBodyElasticityPolicyDynamicPolicy = None,
        enabled: bool = None,
        max_sandbox_count: int = None,
        min_sandbox_count: int = None,
    ):
        # Required. It must include enabled and policies, and is verified by the server. It is independent of the overall automatic elasticity switch.
        self.dynamic_policy = dynamic_policy
        # Specifies whether to enable the entire automatic elasticity mode. It must be provided when elasticityPolicy is passed and is verified by the server.
        self.enabled = enabled
        # Specifies whether to enable the entire automatic elasticity mode. It must be provided when elasticityPolicy is passed and is verified by the server.
        self.max_sandbox_count = max_sandbox_count
        # Specifies whether to enable the entire automatic elasticity mode. It must be provided when elasticityPolicy is passed and is verified by the server.
        self.min_sandbox_count = min_sandbox_count

    def validate(self):
        if self.dynamic_policy:
            self.dynamic_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_policy is not None:
            result['dynamicPolicy'] = self.dynamic_policy.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.max_sandbox_count is not None:
            result['maxSandboxCount'] = self.max_sandbox_count

        if self.min_sandbox_count is not None:
            result['minSandboxCount'] = self.min_sandbox_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dynamicPolicy') is not None:
            temp_model = main_models.CreateServiceEndpointRequestBodyElasticityPolicyDynamicPolicy()
            self.dynamic_policy = temp_model.from_map(m.get('dynamicPolicy'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('maxSandboxCount') is not None:
            self.max_sandbox_count = m.get('maxSandboxCount')

        if m.get('minSandboxCount') is not None:
            self.min_sandbox_count = m.get('minSandboxCount')

        return self

class CreateServiceEndpointRequestBodyElasticityPolicyDynamicPolicy(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        policies: List[main_models.CreateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPolicies] = None,
    ):
        # Specifies whether to enable dynamic policies. Required during creation. If omitted during an update, the original value is retained. Disabling it retains existing policies and restores the basic upper and lower limits. Re-enabling it triggers immediate calculation. When finally enabled, policies must not be empty.
        self.enabled = enabled
        # Required during creation. If omitted during an update, the original list is retained. If passed, the entire list is replaced and not merged by ID. To clear the list, you must also ensure that the final enabled value is false. Each item must be complete. Conditional requirements and cross-field constraints are verified by the server. The display order does not indicate priority.
        self.policies = policies

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['policies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.policies = []
        if m.get('policies') is not None:
            for k1 in m.get('policies'):
                temp_model = main_models.CreateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPolicies()
                self.policies.append(temp_model.from_map(k1))

        return self

class CreateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPolicies(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        id: str = None,
        priority: int = None,
        repeat: str = None,
        start_time: str = None,
        time_points: List[main_models.CreateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPoliciesTimePoints] = None,
        time_zone: str = None,
        validity: str = None,
    ):
        # Required only when validity is set to range. The format is the same as startTime, the seconds are fixed at 00, and it must be later than startTime. The interval does not include the end time. For forever, the start and end times must be omitted. Valid dates and cross-field constraints are verified by the console.
        self.end_time = end_time
        # Required. It must be unique and stable within the endpoint. It is generated by the frontend when added, and retained during editing and retries.
        self.id = id
        # Required. 5 indicates normal, and 10 indicates high priority. New policies default to normal. It must be explicitly provided during submission, and no default value is set for the operation. When the final dynamicPolicy.enabled is true, the validity periods of high-priority policies must not overlap, but end-to-end connection is allowed. Long-term high-priority policies can overlap with other high-priority policies. When disabled, overlapping drafts can be saved, and the final configuration is verified when re-enabled. The validity of other fields and trigger conflicts within the policy are always verified. The priority must be explicitly provided.
        self.priority = priority
        # Required. daily means every day, weekly means every week, and monthly means every month. Only submit the fields corresponding to the cycle.
        self.repeat = repeat
        # Required only when validity is set to range. The format is YYYY-MM-DDTHH:mm:ss in the policy time zone, without a time zone offset, and the seconds are fixed at 00. The interval includes the start time. Editing retains the existing past start time and does not reject updates or retries because it is earlier than the current time.
        self.start_time = start_time
        # Required and non-empty. Each item must be complete. The day of the week or day of the month is configured independently for each item. Within the same policy, daily policies conflict if the time is the same. Weekly and monthly policies conflict only if the time is the same and the date sets intersect. This is verified by the console.
        self.time_points = time_points
        # Required. A valid IANA time zone. All dates and times in this policy are interpreted in this time zone.
        self.time_zone = time_zone
        # Required. forever indicates long-term validity, and range indicates short-term validity. After expiration, the policy and its trigger results exit the current calculation, and the remaining policies are recalculated. If there are no candidates, the basic values are restored, and the saved configurations are not automatically deleted.
        self.validity = validity

    def validate(self):
        if self.time_points:
            for v1 in self.time_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.id is not None:
            result['id'] = self.id

        if self.priority is not None:
            result['priority'] = self.priority

        if self.repeat is not None:
            result['repeat'] = self.repeat

        if self.start_time is not None:
            result['startTime'] = self.start_time

        result['timePoints'] = []
        if self.time_points is not None:
            for k1 in self.time_points:
                result['timePoints'].append(k1.to_map() if k1 else None)

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        if self.validity is not None:
            result['validity'] = self.validity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('repeat') is not None:
            self.repeat = m.get('repeat')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        self.time_points = []
        if m.get('timePoints') is not None:
            for k1 in m.get('timePoints'):
                temp_model = main_models.CreateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPoliciesTimePoints()
                self.time_points.append(temp_model.from_map(k1))

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        if m.get('validity') is not None:
            self.validity = m.get('validity')

        return self

class CreateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPoliciesTimePoints(DaraModel):
    def __init__(
        self,
        max_instances: int = None,
        min_instances: int = None,
        month_days: List[int] = None,
        time: str = None,
        weekdays: List[int] = None,
    ):
        # Required. The value ranges from 1 to 100.
        self.max_instances = max_instances
        # Required. The value ranges from 0 to 100 and must not be greater than maxInstances in the same item.
        self.min_instances = min_instances
        # Required only for each trigger point of monthly. It must be non-empty and deduplicated. The values are integers from 1 to 31. Each row is selected independently. If a date does not exist in a month, it is not triggered and is not postponed to the end of the month. It must be omitted for other cycles.
        self.month_days = month_days
        # Required. The format is HH:mm:ss. It is interpreted in the time zone of the policy, accurate to the minute, and the seconds are fixed at 00.
        self.time = time
        # Required only for each trigger point of weekly. It must be non-empty and deduplicated. The values are integers from 1 to 7, where 1 indicates Monday and 7 indicates Sunday. Each row is selected independently. It must be omitted for other cycles.
        self.weekdays = weekdays

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_instances is not None:
            result['maxInstances'] = self.max_instances

        if self.min_instances is not None:
            result['minInstances'] = self.min_instances

        if self.month_days is not None:
            result['monthDays'] = self.month_days

        if self.time is not None:
            result['time'] = self.time

        if self.weekdays is not None:
            result['weekdays'] = self.weekdays

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxInstances') is not None:
            self.max_instances = m.get('maxInstances')

        if m.get('minInstances') is not None:
            self.min_instances = m.get('minInstances')

        if m.get('monthDays') is not None:
            self.month_days = m.get('monthDays')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('weekdays') is not None:
            self.weekdays = m.get('weekdays')

        return self

class CreateServiceEndpointRequestBodyAuthentication(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The saved invocation authentication type. NONE indicates that the endpoint API key is not used. API_KEY indicates that the endpoint API key is used. For AGENT_VERSION endpoints of non-EDGE agents, the actual API key verification is determined by the current inbound authentication configuration of the agent and cannot be determined solely based on this field.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

