# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateServiceEndpointRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateServiceEndpointRequestBody = None,
        client_token: str = None,
    ):
        # The service endpoint configurations to be modified in this request. Submit the supported modifiable name, bound version, invocation authentication configuration, elastic policy, or public network inbound switch based on the endpoint type. Router and hybrid ingress endpoints cannot be renamed. DEFAULT endpoints do not accept name or authentication configuration updates. When updating the elastic policy, you must specify both updateElasticity=true and clientToken.
        self.body = body
        # The client token. This parameter is required when updateElasticity is set to true and is verified by the server. Reuse the token and the original request for the same retry. Use a new token if the logical content changes. Passing different content with the same token returns InvalidParameter. The token must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), colons (:), and hyphens (-). The scope is the tenant and workspace. The receipt is retained for 7 days from the time of successful acceptance. Replays do not extend the retention period. After expiration, it is verified again as a new submission.
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
            temp_model = main_models.UpdateServiceEndpointRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateServiceEndpointRequestBody(DaraModel):
    def __init__(
        self,
        agent_version: str = None,
        authentication: main_models.UpdateServiceEndpointRequestBodyAuthentication = None,
        elasticity_policy: main_models.UpdateServiceEndpointRequestBodyElasticityPolicy = None,
        name: str = None,
        public_access_enabled: bool = None,
        update_elasticity: bool = None,
    ):
        # If not specified, the original binding is retained. If specified, it must be an exact source version that has been successfully deployed for the agent. Otherwise, ServiceEndpointTargetNotReady is returned. When rebinding a DEFAULT service endpoint of the GATEWAY_API type, ServiceEndpointTargetNotReady is also returned if the original gateway runtime instance is unavailable.
        self.agent_version = agent_version
        # Updates the invocation authentication configuration saved for the service endpoint, specified by type. If not specified, the original configuration is retained. This field is prohibited for DEFAULT endpoints. For AGENT_VERSION endpoints of non-EDGE agents, the actual API key verification is determined by the current inbound authentication configuration of the agent. The management API for updating the service endpoint still uses AccessKey (AK) or Security Token Service (STS) authentication and Resource Access Management (RAM) authorization.
        self.authentication = authentication
        # Accepted only when updateElasticity is set to true. Omitting subfields indicates that the original values are retained. The basic minSandboxCount and maxSandboxCount must be submitted in pairs. dynamicPolicy.enabled and policies can be updated separately. If policies is provided, it replaces the entire list. To clear the list, you must ensure that the final dynamicPolicy.enabled is set to false. elasticityPolicy and dynamicPolicy do not accept null, and an empty patch is invalid. Only Router service endpoints and DEFAULT service endpoints of the GATEWAY_API_WITH_VPC_INGRESS or GATEWAY_API_WITH_PUBLIC_INGRESS type support elasticity updates. The server merges, verifies, and saves the complete configuration, and does not backfill basic values with the current capacity. The final basic min and max values must be between 0 and 100. If the historical basic capacity exceeds the limit, you must submit valid basic min and max values even if you only modify the dynamic policy. Silent truncation is not allowed.
        self.elasticity_policy = elasticity_policy
        # Used to modify existing named endpoints that support renaming. If omitted, the original name is retained. Router and hybrid ingress endpoints do not support renaming. You can only omit this parameter or pass the original name. This field is prohibited for DEFAULT endpoints.
        self.name = name
        # Specifies whether to enable public network inbound access for the service endpoint. If not specified, the original value is retained. If set to true or false, the value is replaced. Explicitly passing null or a non-Boolean value returns InvalidParameter, and no restore inheritance semantics are provided. Modifying only this field triggers an ingress revision only and does not redeploy the runtime instance. Whether public network access is actually enabled is also subject to the public network inbound limit of the workspace. For more information, see effectivePublicAccessEnabled in the response.
        self.public_access_enabled = public_access_enabled
        # Specifies whether to explicitly update the elastic configuration in this request. If omitted or set to false, the elasticityPolicy carried in this request is ignored, and the saved configuration is retained. If set to true, a valid and non-empty elasticityPolicy patch and clientToken must be provided. This parameter is not persisted, returned, or passed through to the resource manager (RM), and no default value is set. Omit this parameter during normal editing and version rebinding.
        self.update_elasticity = update_elasticity

    def validate(self):
        if self.authentication:
            self.authentication.validate()
        if self.elasticity_policy:
            self.elasticity_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_version is not None:
            result['agentVersion'] = self.agent_version

        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()

        if self.elasticity_policy is not None:
            result['elasticityPolicy'] = self.elasticity_policy.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.public_access_enabled is not None:
            result['publicAccessEnabled'] = self.public_access_enabled

        if self.update_elasticity is not None:
            result['updateElasticity'] = self.update_elasticity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentVersion') is not None:
            self.agent_version = m.get('agentVersion')

        if m.get('authentication') is not None:
            temp_model = main_models.UpdateServiceEndpointRequestBodyAuthentication()
            self.authentication = temp_model.from_map(m.get('authentication'))

        if m.get('elasticityPolicy') is not None:
            temp_model = main_models.UpdateServiceEndpointRequestBodyElasticityPolicy()
            self.elasticity_policy = temp_model.from_map(m.get('elasticityPolicy'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('publicAccessEnabled') is not None:
            self.public_access_enabled = m.get('publicAccessEnabled')

        if m.get('updateElasticity') is not None:
            self.update_elasticity = m.get('updateElasticity')

        return self

class UpdateServiceEndpointRequestBodyElasticityPolicy(DaraModel):
    def __init__(
        self,
        dynamic_policy: main_models.UpdateServiceEndpointRequestBodyElasticityPolicyDynamicPolicy = None,
        enabled: bool = None,
        max_sandbox_count: int = None,
        min_sandbox_count: int = None,
    ):
        # The dynamic policy configuration. It must be fully provided during creation. If omitted during an update, the original configuration is retained. If provided, it is merged by field and does not accept null. The response returns the saved complete configuration. If no historical dynamic configuration exists, it is normalized to enabled=false and policies=[].
        self.dynamic_policy = dynamic_policy
        # Specifies whether to enable the overall automatic elasticity mode. This parameter is independent of dynamicPolicy.enabled. If omitted during an update, the original value is retained.
        self.enabled = enabled
        # The saved basic maximum number of instances. Valid values: 0 to 100. The value cannot be less than minSandboxCount. The basic upper and lower limits are used when dynamic elasticity is disabled or no candidates are available.
        self.max_sandbox_count = max_sandbox_count
        # The saved basic minimum number of instances. Valid values: 0 to 100. The value cannot be greater than maxSandboxCount. It must be submitted in pairs with maxSandboxCount during an update. If both are omitted, the original values are retained. It does not override dynamic results when dynamic candidates are available.
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
            temp_model = main_models.UpdateServiceEndpointRequestBodyElasticityPolicyDynamicPolicy()
            self.dynamic_policy = temp_model.from_map(m.get('dynamicPolicy'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('maxSandboxCount') is not None:
            self.max_sandbox_count = m.get('maxSandboxCount')

        if m.get('minSandboxCount') is not None:
            self.min_sandbox_count = m.get('minSandboxCount')

        return self

class UpdateServiceEndpointRequestBodyElasticityPolicyDynamicPolicy(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        policies: List[main_models.UpdateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPolicies] = None,
    ):
        # Specifies whether to enable dynamic policies. This parameter is required during creation. If omitted during an update, the original value is retained. Disabling it retains existing policies and restores the basic upper and lower limits. Re-enabling it triggers immediate calculation. When it is finally enabled, policies cannot be empty.
        self.enabled = enabled
        # The complete list of dynamic policies. This parameter is required during creation. If omitted during an update, the original list is retained. If provided, it replaces the entire list and is not merged by ID. To clear the list, you must ensure that the final enabled is set to false. Each item must be complete. Conditional requirements and cross-field constraints are verified by the server. The display order does not indicate priority.
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
                temp_model = main_models.UpdateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPolicies()
                self.policies.append(temp_model.from_map(k1))

        return self

class UpdateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPolicies(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        id: str = None,
        priority: int = None,
        repeat: str = None,
        start_time: str = None,
        time_points: List[main_models.UpdateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPoliciesTimePoints] = None,
        time_zone: str = None,
        validity: str = None,
    ):
        # The end time of the validity period. This parameter is required only when validity is set to range. The format is the same as startTime, and the seconds are fixed at 00. It must be later than startTime. The interval does not include the end time. If validity is set to forever, the start and end times must be omitted. Valid dates and cross-field constraints are verified by the console.
        self.end_time = end_time
        # The policy identifier. This parameter is required and must be unique and stable within the endpoint. It is generated by the frontend when added, and retained during editing and retries.
        self.id = id
        # The policy priority. This parameter is required. Valid values: 5 (regular) and 10 (high priority). The default selection for a new policy is regular. You must explicitly provide this parameter upon submission, and no default value is set for the API. When the final dynamicPolicy.enabled is set to true, the validity periods of high-priority policies cannot overlap, but end-to-end connection is allowed. Long-term high-priority policies can overlap with other high-priority policies. When disabled, overlapping drafts can be saved, and the final configuration is verified when re-enabled. The validity of other fields and trigger conflicts within the policy are always verified. You must explicitly provide priority.
        self.priority = priority
        # The repeat period. This parameter is required. Valid values: daily (every day), weekly (every week), and monthly (every month). Only submit the fields corresponding to the specified period.
        self.repeat = repeat
        # The start time of the validity period. This parameter is required only when validity is set to range. Format: YYYY-MM-DDTHH:mm:ss in the policy time zone, without a time zone offset. The seconds are fixed at 00. The interval includes the start time. When editing, existing past start times are retained, and updates or retries are not rejected because the start time is earlier than the current time.
        self.start_time = start_time
        # The periodic trigger time points. This parameter is required and cannot be empty. Each item must be complete. The day of the week or day of the month is configured independently for each item. Within the same policy, daily policies conflict if the time is the same. weekly and monthly policies conflict only when the time is the same and the date sets intersect. This is verified by the console.
        self.time_points = time_points
        # The policy time zone. This parameter is required and must be a valid IANA time zone. All dates and times in this policy are interpreted in this time zone.
        self.time_zone = time_zone
        # The policy validity period type. This parameter is required. Valid values: forever (long-term validity) and range (short-term validity). After expiration, the policy and its trigger results exit the current calculation, and the remaining policies are recalculated. If no candidates are available, the basic values are restored. The saved configuration is not automatically deleted.
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
                temp_model = main_models.UpdateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPoliciesTimePoints()
                self.time_points.append(temp_model.from_map(k1))

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        if m.get('validity') is not None:
            self.validity = m.get('validity')

        return self

class UpdateServiceEndpointRequestBodyElasticityPolicyDynamicPolicyPoliciesTimePoints(DaraModel):
    def __init__(
        self,
        max_instances: int = None,
        min_instances: int = None,
        month_days: List[int] = None,
        time: str = None,
        weekdays: List[int] = None,
    ):
        # The target maximum number of instances. This parameter is required. Valid values: 1 to 100.
        self.max_instances = max_instances
        # The target minimum number of instances. This parameter is required. Valid values: 0 to 100. The value cannot be greater than maxInstances in the same item.
        self.min_instances = min_instances
        # The days of the month. This parameter is required only for each trigger point of monthly policies. It cannot be empty and must be deduplicated. Valid values are integers from 1 to 31. Each row is selected independently. If a date does not exist in a specific month, the policy is not triggered and is not postponed to the end of the month. This parameter must be omitted for other periods.
        self.month_days = month_days
        # The trigger time. This parameter is required. Format: HH:mm:ss. It is interpreted in the time zone of the associated policy, accurate to the minute, and the seconds are fixed at 00.
        self.time = time
        # The days of the week. This parameter is required only for each trigger point of weekly policies. It cannot be empty and must be deduplicated. Valid values are integers from 1 to 7, where 1 represents Monday and 7 represents Sunday. Each row is selected independently. This parameter must be omitted for other periods.
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

class UpdateServiceEndpointRequestBodyAuthentication(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The saved invocation authentication type. Valid values:
        # - NONE: Configured to not use the endpoint API key.
        # - API_KEY: Configured to use the endpoint API key.
        # For AGENT_VERSION endpoints of non-EDGE agents, the actual API key verification is determined by the current inbound authentication configuration of the agent and cannot be determined solely based on this field. You must provide type when passing authentication.
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

