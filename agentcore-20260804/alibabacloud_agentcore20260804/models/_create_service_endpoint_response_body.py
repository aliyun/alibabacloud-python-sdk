# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateServiceEndpointResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateServiceEndpointResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code of the request. The value is SUCCESS if the request is successful.
        self.code = code
        # The service endpoint information returned after a successful creation, including the binding target, saved authentication and elasticity configurations, and current status. The endpoint may still be in the creating state.
        self.data = data
        # The HTTP status code of the request. The value is 200 if the request is successful.
        self.http_status_code = http_status_code
        # The response message of the request. The value is success if the request is successful.
        self.message = message
        # The unique identifier of the request, used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful. A value of true indicates that the creation request is accepted, but it does not mean that the endpoint deployment is complete. To confirm the deployment result, check data.status and data.accessUrls.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateServiceEndpointResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateServiceEndpointResponseBodyData(DaraModel):
    def __init__(
        self,
        access_urls: List[main_models.CreateServiceEndpointResponseBodyDataAccessUrls] = None,
        authentication: main_models.CreateServiceEndpointResponseBodyDataAuthentication = None,
        created_at: str = None,
        current_instances: int = None,
        effective_public_access_enabled: bool = None,
        elasticity_policy: main_models.CreateServiceEndpointResponseBodyDataElasticityPolicy = None,
        endpoint_type: str = None,
        name: str = None,
        public_access_enabled: bool = None,
        region_id: str = None,
        service_endpoint_id: str = None,
        status: str = None,
        status_reason: str = None,
        target: main_models.CreateServiceEndpointResponseBodyDataTarget = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The list of access URLs for the service endpoint.
        self.access_urls = access_urls
        # The authentication configuration of the service endpoint.
        self.authentication = authentication
        # The creation time in UTC format compliant with RFC 3339.
        self.created_at = created_at
        # The current number of instances. This parameter is read-only. The Get operation queries RM sandboxPhaseCounts.RUNNING based on the endpoint runtimeKey. The Create and Update operations return null. The value is a non-negative integer. If the statistics are unavailable, null is returned. This parameter is not replaced by the base upper and lower limits, target quantity, or READY status. Unavailable statistics do not block submission.
        self.current_instances = current_instances
        # The combined result of publicAccessEnabled and the workspace-level public access limit. The value is true only when both allow public access. This value only indicates the policy target and does not mean that the public endpoint has been fully provisioned. For the actual status, refer to accessUrls and status.
        self.effective_public_access_enabled = effective_public_access_enabled
        # The configuration used for edit backfill, which is not the currently effective upper and lower limits or the actual number of instances. The Get operation preferentially returns the saved configuration. If no configuration is saved, an endpoint that supports elasticity backfills the base values from the expected runtime frozen configuration or the bound version configuration when the runtime is not yet established, without requiring a successful publication. The value is null when the source is temporarily unavailable or no applicable configuration exists, but the status and statusReason are still returned. The Create and Update operations return only the saved configuration, and the value is null if no configuration is saved. The historical base capacity may exceed 100, and the read value is not truncated.
        self.elasticity_policy = elasticity_policy
        # The type of the service endpoint. Valid values:
        # - DEFAULT: The default endpoint created and maintained by the platform.
        # - NAMED: The named endpoint explicitly created by the user.
        self.endpoint_type = endpoint_type
        # The name of the service endpoint. The name must be unique within the workspace and be 1 to 128 characters in length.
        self.name = name
        # The expected public access setting configured by the user on the service endpoint. For historical service endpoints that have not been configured, this parameter returns true. This value only indicates the configuration expectation. To check whether the actual public endpoint is available, refer to accessUrls and status.
        self.public_access_enabled = public_access_enabled
        # The ID of the region where the service endpoint resides.
        self.region_id = region_id
        # The ID of the service endpoint.
        self.service_endpoint_id = service_endpoint_id
        # The status of the service endpoint. Valid values: CREATING, READY, UPDATING, DEGRADED, DISABLED, and DELETING.
        self.status = status
        # The reason for the service endpoint status. The specific reason is returned when the status is abnormal.
        self.status_reason = status_reason
        # The target routing configuration of the service endpoint.
        self.target = target
        # The time of the last modification in UTC format compliant with RFC 3339.
        self.updated_at = updated_at
        # The ID of the workspace.
        self.workspace_id = workspace_id

    def validate(self):
        if self.access_urls:
            for v1 in self.access_urls:
                 if v1:
                    v1.validate()
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
        result['accessUrls'] = []
        if self.access_urls is not None:
            for k1 in self.access_urls:
                result['accessUrls'].append(k1.to_map() if k1 else None)

        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.current_instances is not None:
            result['currentInstances'] = self.current_instances

        if self.effective_public_access_enabled is not None:
            result['effectivePublicAccessEnabled'] = self.effective_public_access_enabled

        if self.elasticity_policy is not None:
            result['elasticityPolicy'] = self.elasticity_policy.to_map()

        if self.endpoint_type is not None:
            result['endpointType'] = self.endpoint_type

        if self.name is not None:
            result['name'] = self.name

        if self.public_access_enabled is not None:
            result['publicAccessEnabled'] = self.public_access_enabled

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.service_endpoint_id is not None:
            result['serviceEndpointId'] = self.service_endpoint_id

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.target is not None:
            result['target'] = self.target.to_map()

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_urls = []
        if m.get('accessUrls') is not None:
            for k1 in m.get('accessUrls'):
                temp_model = main_models.CreateServiceEndpointResponseBodyDataAccessUrls()
                self.access_urls.append(temp_model.from_map(k1))

        if m.get('authentication') is not None:
            temp_model = main_models.CreateServiceEndpointResponseBodyDataAuthentication()
            self.authentication = temp_model.from_map(m.get('authentication'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('currentInstances') is not None:
            self.current_instances = m.get('currentInstances')

        if m.get('effectivePublicAccessEnabled') is not None:
            self.effective_public_access_enabled = m.get('effectivePublicAccessEnabled')

        if m.get('elasticityPolicy') is not None:
            temp_model = main_models.CreateServiceEndpointResponseBodyDataElasticityPolicy()
            self.elasticity_policy = temp_model.from_map(m.get('elasticityPolicy'))

        if m.get('endpointType') is not None:
            self.endpoint_type = m.get('endpointType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('publicAccessEnabled') is not None:
            self.public_access_enabled = m.get('publicAccessEnabled')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('serviceEndpointId') is not None:
            self.service_endpoint_id = m.get('serviceEndpointId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('target') is not None:
            temp_model = main_models.CreateServiceEndpointResponseBodyDataTarget()
            self.target = temp_model.from_map(m.get('target'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CreateServiceEndpointResponseBodyDataTarget(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        collaboration_component: str = None,
        resource_binding_id: str = None,
        target_type: str = None,
    ):
        # The ID of the target agent. This parameter is returned when the target type is AGENT_VERSION.
        self.agent_id = agent_id
        # The version number of the target agent. This parameter is returned when the target type is AGENT_VERSION.
        self.agent_version = agent_version
        # The type of the collaboration component. This parameter is returned when the target type is TEAM_COLLABORATION.
        self.collaboration_component = collaboration_component
        # The ID of the workspace resource binding associated with the target collaboration component. This parameter is returned when the target type is TEAM_COLLABORATION.
        self.resource_binding_id = resource_binding_id
        # The target type. Valid values: AGENT_VERSION and TEAM_COLLABORATION.
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

class CreateServiceEndpointResponseBodyDataElasticityPolicy(DaraModel):
    def __init__(
        self,
        dynamic_policy: main_models.CreateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicy = None,
        enabled: bool = None,
        max_sandbox_count: int = None,
        min_sandbox_count: int = None,
    ):
        # The saved dynamic configuration. If the base configuration before the requirement goes online lacks dynamicPolicy, it is supplemented with enabled=false and policies=[].
        self.dynamic_policy = dynamic_policy
        # Indicates whether the elasticity policy is enabled. This parameter is independent of dynamicPolicy.enabled. If this parameter is omitted during an update, the original value is retained.
        self.enabled = enabled
        # The saved or backfilled base maximum number of instances, which is not less than minSandboxCount. The historical value may exceed 100, and the read value is not truncated. The base value is used when dynamic scaling is disabled or no candidates are available.
        self.max_sandbox_count = max_sandbox_count
        # The saved or backfilled base minimum number of instances, which is a non-negative integer and not greater than maxSandboxCount. The historical value may exceed 100, and the read value is not truncated. A newly written complete configuration must still meet the requirement of 0 to 100.
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
            temp_model = main_models.CreateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicy()
            self.dynamic_policy = temp_model.from_map(m.get('dynamicPolicy'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('maxSandboxCount') is not None:
            self.max_sandbox_count = m.get('maxSandboxCount')

        if m.get('minSandboxCount') is not None:
            self.min_sandbox_count = m.get('minSandboxCount')

        return self

class CreateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicy(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        policies: List[main_models.CreateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPolicies] = None,
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
                temp_model = main_models.CreateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPolicies()
                self.policies.append(temp_model.from_map(k1))

        return self

class CreateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPolicies(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        id: str = None,
        priority: int = None,
        repeat: str = None,
        start_time: str = None,
        time_points: List[main_models.CreateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPoliciesTimePoints] = None,
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
                temp_model = main_models.CreateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPoliciesTimePoints()
                self.time_points.append(temp_model.from_map(k1))

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        if m.get('validity') is not None:
            self.validity = m.get('validity')

        return self

class CreateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPoliciesTimePoints(DaraModel):
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

class CreateServiceEndpointResponseBodyDataAuthentication(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The authentication method. Valid values:
        # - NONE: No authentication is required.
        # - API_KEY: Authentication is performed by passing an API key in the x-api-key request header.
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

class CreateServiceEndpointResponseBodyDataAccessUrls(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        status: str = None,
        status_reason: str = None,
        url: str = None,
    ):
        # The type of the access URL. Valid values: INTERNET and VPC.
        self.access_type = access_type
        # The status of the access URL. Valid values: CREATING, READY, and DEGRADED.
        self.status = status
        # The reason for the access URL status. The specific reason is returned when the status is abnormal.
        self.status_reason = status_reason
        # The access URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['accessType'] = self.access_type

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessType') is not None:
            self.access_type = m.get('accessType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

