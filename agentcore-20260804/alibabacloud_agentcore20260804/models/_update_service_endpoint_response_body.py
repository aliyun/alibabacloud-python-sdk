# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateServiceEndpointResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateServiceEndpointResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code of the request. The value is SUCCESS if the request is successful.
        self.code = code
        # The service endpoint information returned after the update is accepted. This includes the binding target, saved authentication and elasticity configurations, and current status. The endpoint may still be updating.
        self.data = data
        # The HTTP status code of the request. The value is 200 if the request is successful.
        self.http_status_code = http_status_code
        # The response message of the request. The value is success if the request is successful.
        self.message = message
        # The unique identifier of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful. A value of true indicates that the update request is accepted, but does not mean that the deployment or endpoint change is complete. You must check data.status and data.accessUrls to confirm the result.
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
            temp_model = main_models.UpdateServiceEndpointResponseBodyData()
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

class UpdateServiceEndpointResponseBodyData(DaraModel):
    def __init__(
        self,
        access_urls: List[main_models.UpdateServiceEndpointResponseBodyDataAccessUrls] = None,
        authentication: main_models.UpdateServiceEndpointResponseBodyDataAuthentication = None,
        created_at: str = None,
        current_instances: int = None,
        effective_public_access_enabled: bool = None,
        elasticity_policy: main_models.UpdateServiceEndpointResponseBodyDataElasticityPolicy = None,
        endpoint_type: str = None,
        name: str = None,
        public_access_enabled: bool = None,
        region_id: str = None,
        service_endpoint_id: str = None,
        status: str = None,
        status_reason: str = None,
        target: main_models.UpdateServiceEndpointResponseBodyDataTarget = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The list of access URLs for the service endpoint.
        self.access_urls = access_urls
        # The authentication configuration of the service endpoint.
        self.authentication = authentication
        # The creation time in UTC format compliant with RFC 3339.
        self.created_at = created_at
        # Read-only. The Get operation queries RM sandboxPhaseCounts.RUNNING by endpoint runtimeKey. The Create and Update operations return null. The value is a non-negative integer. If the statistics are unavailable, null is returned. The value is not replaced by the base upper and lower limits, target quantity, or READY status. Unavailable statistics do not block submission.
        self.current_instances = current_instances
        # The effective public access setting derived from combining publicAccessEnabled with the workspace-level public access limit. This parameter returns true only when both settings allow public access. This value only indicates the policy target and does not mean that the public endpoint has been fully published. For the actual status, refer to accessUrls and status.
        self.effective_public_access_enabled = effective_public_access_enabled
        # The elasticity configuration used for edit backfill, which is not the current effective upper and lower limits or the actual number of instances. The Get operation preferentially returns the saved configuration. If no configuration is saved, an endpoint that supports elasticity backfills the base values from the expected runtime frozen configuration or the bound version configuration when the runtime is not established. Successful publication is not required. If the source is temporarily unavailable or no applicable configuration exists, the value is null, but the status and statusReason are still returned. The Create and Update operations return only the saved configuration. If no configuration is saved, the value is null. The historical base capacity can exceed 100 and is not truncated when read.
        self.elasticity_policy = elasticity_policy
        # The service endpoint type. Valid values:
        # - DEFAULT: The default endpoint created and maintained by the platform.
        # - NAMED: The named endpoint explicitly created by the user.
        self.endpoint_type = endpoint_type
        # The service endpoint name. The name must be unique within the workspace and 1 to 128 characters in length.
        self.name = name
        # The expected public access setting configured by the user for the service endpoint. For historical service endpoints that have not been configured, this parameter returns true. This value only indicates the configuration expectation. For the actual availability of the public endpoint, refer to accessUrls and status.
        self.public_access_enabled = public_access_enabled
        # The region ID of the service endpoint.
        self.region_id = region_id
        # The service endpoint ID.
        self.service_endpoint_id = service_endpoint_id
        # The service endpoint status. Valid values: CREATING, READY, UPDATING, DEGRADED, DISABLED, and DELETING.
        self.status = status
        # The reason for the service endpoint status. The specific reason is returned when the status is abnormal.
        self.status_reason = status_reason
        # The target routing configuration of the service endpoint.
        self.target = target
        # The time of the last modification in UTC format compliant with RFC 3339.
        self.updated_at = updated_at
        # The workspace ID.
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
                temp_model = main_models.UpdateServiceEndpointResponseBodyDataAccessUrls()
                self.access_urls.append(temp_model.from_map(k1))

        if m.get('authentication') is not None:
            temp_model = main_models.UpdateServiceEndpointResponseBodyDataAuthentication()
            self.authentication = temp_model.from_map(m.get('authentication'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('currentInstances') is not None:
            self.current_instances = m.get('currentInstances')

        if m.get('effectivePublicAccessEnabled') is not None:
            self.effective_public_access_enabled = m.get('effectivePublicAccessEnabled')

        if m.get('elasticityPolicy') is not None:
            temp_model = main_models.UpdateServiceEndpointResponseBodyDataElasticityPolicy()
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
            temp_model = main_models.UpdateServiceEndpointResponseBodyDataTarget()
            self.target = temp_model.from_map(m.get('target'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class UpdateServiceEndpointResponseBodyDataTarget(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        collaboration_component: str = None,
        resource_binding_id: str = None,
        target_type: str = None,
    ):
        # The target agent ID. This parameter is returned when the target type is AGENT_VERSION.
        self.agent_id = agent_id
        # The target agent version. This parameter is returned when the target type is AGENT_VERSION.
        self.agent_version = agent_version
        # The collaboration component type. This parameter is returned when the target type is TEAM_COLLABORATION.
        self.collaboration_component = collaboration_component
        # The workspace resource binding ID associated with the target collaboration component. This parameter is returned when the target type is TEAM_COLLABORATION.
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

class UpdateServiceEndpointResponseBodyDataElasticityPolicy(DaraModel):
    def __init__(
        self,
        dynamic_policy: main_models.UpdateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicy = None,
        enabled: bool = None,
        max_sandbox_count: int = None,
        min_sandbox_count: int = None,
    ):
        # The saved dynamic configuration. If the base configuration before the requirement is published lacks the dynamicPolicy parameter, it is supplemented with enabled=false and policies=[].
        self.dynamic_policy = dynamic_policy
        # Specifies whether to enable the overall automatic elasticity mode. This parameter is independent of dynamicPolicy.enabled. If omitted during an update, the original value is retained.
        self.enabled = enabled
        # The saved or backfilled base maximum number of instances, which is not less than minSandboxCount. The historical value can exceed 100 and is not truncated when read. The base value is used when dynamic scaling is disabled or no candidates are available.
        self.max_sandbox_count = max_sandbox_count
        # The saved or backfilled base minimum number of instances, which is a non-negative integer and not greater than maxSandboxCount. The historical value can exceed 100 and is not truncated when read. A newly written complete configuration must still meet the 0 to 100 range.
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
            temp_model = main_models.UpdateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicy()
            self.dynamic_policy = temp_model.from_map(m.get('dynamicPolicy'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('maxSandboxCount') is not None:
            self.max_sandbox_count = m.get('maxSandboxCount')

        if m.get('minSandboxCount') is not None:
            self.min_sandbox_count = m.get('minSandboxCount')

        return self

class UpdateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicy(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        policies: List[main_models.UpdateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPolicies] = None,
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
                temp_model = main_models.UpdateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPolicies()
                self.policies.append(temp_model.from_map(k1))

        return self

class UpdateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPolicies(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        id: str = None,
        priority: int = None,
        repeat: str = None,
        start_time: str = None,
        time_points: List[main_models.UpdateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPoliciesTimePoints] = None,
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
                temp_model = main_models.UpdateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPoliciesTimePoints()
                self.time_points.append(temp_model.from_map(k1))

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        if m.get('validity') is not None:
            self.validity = m.get('validity')

        return self

class UpdateServiceEndpointResponseBodyDataElasticityPolicyDynamicPolicyPoliciesTimePoints(DaraModel):
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

class UpdateServiceEndpointResponseBodyDataAuthentication(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The authentication method. Valid values:
        # - NONE: No authentication is required.
        # - API_KEY: Authentication is performed by passing the API key in the x-api-key request header.
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

class UpdateServiceEndpointResponseBodyDataAccessUrls(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        status: str = None,
        status_reason: str = None,
        url: str = None,
    ):
        # The access URL type. Valid values: INTERNET and VPC.
        self.access_type = access_type
        # The access URL status. Valid values: CREATING, READY, and DEGRADED.
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

