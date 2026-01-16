# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from ._acceleration_info import AccelerationInfo
from ._alias import Alias
from ._async_config import AsyncConfig
from ._async_task import AsyncTask
from ._async_task_event import AsyncTaskEvent
from ._auth_config import AuthConfig
from ._batch_window import BatchWindow
from ._cdntrigger_config import CDNTriggerConfig
from ._cert_config import CertConfig
from ._change_resource_group_input import ChangeResourceGroupInput
from ._change_resource_group_output import ChangeResourceGroupOutput
from ._concurrency_config import ConcurrencyConfig
from ._cookie_session_affinity_config import CookieSessionAffinityConfig
from ._create_alias_input import CreateAliasInput
from ._create_custom_domain_input import CreateCustomDomainInput
from ._create_function_input import CreateFunctionInput
from ._create_layer_version_input import CreateLayerVersionInput
from ._create_session_input import CreateSessionInput
from ._create_trigger_input import CreateTriggerInput
from ._create_vpc_binding_input import CreateVpcBindingInput
from ._custom_container_config import CustomContainerConfig
from ._custom_dns import CustomDNS
from ._custom_domain import CustomDomain
from ._custom_health_check_config import CustomHealthCheckConfig
from ._custom_runtime_config import CustomRuntimeConfig
from ._dnsoption import DNSOption
from ._dead_letter_queue import DeadLetterQueue
from ._delivery_option import DeliveryOption
from ._describe_regions_output import DescribeRegionsOutput
from ._destination import Destination
from ._destination_config import DestinationConfig
from ._elastic_config_status import ElasticConfigStatus
from ._equal_rule import EqualRule
from ._error import Error
from ._event_bridge_trigger_config import EventBridgeTriggerConfig
from ._event_sink_config import EventSinkConfig
from ._event_source_config import EventSourceConfig
from ._event_source_parameters import EventSourceParameters
from ._filter import Filter
from ._function import Function
from ._function_layer import FunctionLayer
from ._function_restriction import FunctionRestriction
from ._gpuconfig import GPUConfig
from ._get_instance_lifecycle_events_output import GetInstanceLifecycleEventsOutput
from ._get_resource_tags_output import GetResourceTagsOutput
from ._get_scaling_config_status_output import GetScalingConfigStatusOutput
from ._httptrigger import HTTPTrigger
from ._httptrigger_config import HTTPTriggerConfig
from ._header_field_session_affinity_config import HeaderFieldSessionAffinityConfig
from ._input_code_location import InputCodeLocation
from ._instance_event_item import InstanceEventItem
from ._instance_info import InstanceInfo
from ._instance_lifecycle_config import InstanceLifecycleConfig
from ._job_config import JobConfig
from ._key import Key
from ._layer import Layer
from ._lifecycle_hook import LifecycleHook
from ._list_aliases_output import ListAliasesOutput
from ._list_async_invoke_config_output import ListAsyncInvokeConfigOutput
from ._list_async_task_output import ListAsyncTaskOutput
from ._list_concurrency_configs_output import ListConcurrencyConfigsOutput
from ._list_custom_domain_output import ListCustomDomainOutput
from ._list_elastic_configs_output import ListElasticConfigsOutput
from ._list_functions_output import ListFunctionsOutput
from ._list_instances_output import ListInstancesOutput
from ._list_layer_version_output import ListLayerVersionOutput
from ._list_layers_output import ListLayersOutput
from ._list_provision_configs_output import ListProvisionConfigsOutput
from ._list_resident_resource_pools_output import ListResidentResourcePoolsOutput
from ._list_scaling_config_status_output import ListScalingConfigStatusOutput
from ._list_scaling_configs_output import ListScalingConfigsOutput
from ._list_sessions_output import ListSessionsOutput
from ._list_tag_resources_output import ListTagResourcesOutput
from ._list_tagged_resources_output import ListTaggedResourcesOutput
from ._list_triggers_output import ListTriggersOutput
from ._list_versions_output import ListVersionsOutput
from ._list_vpc_bindings_output import ListVpcBindingsOutput
from ._log_config import LogConfig
from ._mcpssesession_affinity_config import MCPSSESessionAffinityConfig
from ._mcpstreamable_session_affinity_config import MCPStreamableSessionAffinityConfig
from ._mnstopic_trigger_config import MNSTopicTriggerConfig
from ._nasconfig import NASConfig
from ._nasmount_config import NASMountConfig
from ._ossmount_config import OSSMountConfig
from ._ossmount_point import OSSMountPoint
from ._osstrigger_config import OSSTriggerConfig
from ._output_code_location import OutputCodeLocation
from ._output_func_code import OutputFuncCode
from ._path_config import PathConfig
from ._polar_fs_config import PolarFsConfig
from ._polar_fs_mount_config import PolarFsMountConfig
from ._provision_config import ProvisionConfig
from ._publish_version_input import PublishVersionInput
from ._put_async_invoke_config_input import PutAsyncInvokeConfigInput
from ._put_concurrency_input import PutConcurrencyInput
from ._put_elastic_config_input import PutElasticConfigInput
from ._put_provision_config_input import PutProvisionConfigInput
from ._put_scaling_config_input import PutScalingConfigInput
from ._put_scaling_config_output import PutScalingConfigOutput
from ._regex_rule import RegexRule
from ._registry_auth_config import RegistryAuthConfig
from ._registry_cert_config import RegistryCertConfig
from ._registry_config import RegistryConfig
from ._registry_network_config import RegistryNetworkConfig
from ._resident_config import ResidentConfig
from ._resident_resource_allocation import ResidentResourceAllocation
from ._resident_resource_allocation_status import ResidentResourceAllocationStatus
from ._resident_resource_capacity import ResidentResourceCapacity
from ._resident_resource_pool import ResidentResourcePool
from ._resource import Resource
from ._retry_strategy import RetryStrategy
from ._rewrite_config import RewriteConfig
from ._route_config import RouteConfig
from ._run_options import RunOptions
from ._slstrigger_config import SLSTriggerConfig
from ._slstrigger_log_config import SLSTriggerLogConfig
from ._scaling_config_status import ScalingConfigStatus
from ._scaling_policy import ScalingPolicy
from ._scaling_status import ScalingStatus
from ._scheduled_action import ScheduledAction
from ._scheduled_policy import ScheduledPolicy
from ._session import Session
from ._source_config import SourceConfig
from ._source_dtsparameters import SourceDTSParameters
from ._source_kafka_parameters import SourceKafkaParameters
from ._source_mnsparameters import SourceMNSParameters
from ._source_mqttparameters import SourceMQTTParameters
from ._source_rabbit_mqparameters import SourceRabbitMQParameters
from ._source_rocket_mqparameters import SourceRocketMQParameters
from ._tlsconfig import TLSConfig
from ._tag import Tag
from ._tag_resource import TagResource
from ._tag_resource_input import TagResourceInput
from ._tag_resources_input import TagResourcesInput
from ._target_tracking_policy import TargetTrackingPolicy
from ._timer_trigger_config import TimerTriggerConfig
from ._tracing_config import TracingConfig
from ._trigger import Trigger
from ._update_alias_input import UpdateAliasInput
from ._update_custom_domain_input import UpdateCustomDomainInput
from ._update_function_input import UpdateFunctionInput
from ._update_resident_resource_pool_input import UpdateResidentResourcePoolInput
from ._update_session_input import UpdateSessionInput
from ._update_trigger_input import UpdateTriggerInput
from ._vpcconfig import VPCConfig
from ._version import Version
from ._wafconfig import WAFConfig
from ._wildcard_rule import WildcardRule
from ._change_resource_group_request import ChangeResourceGroupRequest
from ._change_resource_group_response import ChangeResourceGroupResponse
from ._create_alias_request import CreateAliasRequest
from ._create_alias_response import CreateAliasResponse
from ._create_custom_domain_request import CreateCustomDomainRequest
from ._create_custom_domain_response import CreateCustomDomainResponse
from ._create_function_request import CreateFunctionRequest
from ._create_function_response import CreateFunctionResponse
from ._create_layer_version_request import CreateLayerVersionRequest
from ._create_layer_version_response import CreateLayerVersionResponse
from ._create_session_request import CreateSessionRequest
from ._create_session_response import CreateSessionResponse
from ._create_trigger_request import CreateTriggerRequest
from ._create_trigger_response import CreateTriggerResponse
from ._create_vpc_binding_request import CreateVpcBindingRequest
from ._create_vpc_binding_response import CreateVpcBindingResponse
from ._delete_alias_response import DeleteAliasResponse
from ._delete_async_invoke_config_request import DeleteAsyncInvokeConfigRequest
from ._delete_async_invoke_config_response import DeleteAsyncInvokeConfigResponse
from ._delete_concurrency_config_response import DeleteConcurrencyConfigResponse
from ._delete_custom_domain_response import DeleteCustomDomainResponse
from ._delete_function_response import DeleteFunctionResponse
from ._delete_function_version_response import DeleteFunctionVersionResponse
from ._delete_layer_version_response import DeleteLayerVersionResponse
from ._delete_provision_config_request import DeleteProvisionConfigRequest
from ._delete_provision_config_response import DeleteProvisionConfigResponse
from ._delete_scaling_config_request import DeleteScalingConfigRequest
from ._delete_scaling_config_response import DeleteScalingConfigResponse
from ._delete_session_request import DeleteSessionRequest
from ._delete_session_response import DeleteSessionResponse
from ._delete_trigger_response import DeleteTriggerResponse
from ._delete_vpc_binding_response import DeleteVpcBindingResponse
from ._describe_regions_request import DescribeRegionsRequest
from ._describe_regions_response import DescribeRegionsResponse
from ._disable_function_invocation_request import DisableFunctionInvocationRequest
from ._disable_function_invocation_response_body import DisableFunctionInvocationResponseBody
from ._disable_function_invocation_response import DisableFunctionInvocationResponse
from ._enable_function_invocation_response_body import EnableFunctionInvocationResponseBody
from ._enable_function_invocation_response import EnableFunctionInvocationResponse
from ._get_alias_response import GetAliasResponse
from ._get_async_invoke_config_request import GetAsyncInvokeConfigRequest
from ._get_async_invoke_config_response import GetAsyncInvokeConfigResponse
from ._get_async_task_request import GetAsyncTaskRequest
from ._get_async_task_response import GetAsyncTaskResponse
from ._get_concurrency_config_response import GetConcurrencyConfigResponse
from ._get_custom_domain_response import GetCustomDomainResponse
from ._get_function_request import GetFunctionRequest
from ._get_function_response import GetFunctionResponse
from ._get_function_code_request import GetFunctionCodeRequest
from ._get_function_code_response import GetFunctionCodeResponse
from ._get_layer_version_response import GetLayerVersionResponse
from ._get_layer_version_by_arn_response import GetLayerVersionByArnResponse
from ._get_provision_config_request import GetProvisionConfigRequest
from ._get_provision_config_response import GetProvisionConfigResponse
from ._get_scaling_config_request import GetScalingConfigRequest
from ._get_scaling_config_response import GetScalingConfigResponse
from ._get_session_request import GetSessionRequest
from ._get_session_response import GetSessionResponse
from ._get_trigger_response import GetTriggerResponse
from ._invoke_function_headers import InvokeFunctionHeaders
from ._invoke_function_request import InvokeFunctionRequest
from ._invoke_function_response import InvokeFunctionResponse
from ._list_aliases_request import ListAliasesRequest
from ._list_aliases_response import ListAliasesResponse
from ._list_async_invoke_configs_request import ListAsyncInvokeConfigsRequest
from ._list_async_invoke_configs_response import ListAsyncInvokeConfigsResponse
from ._list_async_tasks_request import ListAsyncTasksRequest
from ._list_async_tasks_response import ListAsyncTasksResponse
from ._list_concurrency_configs_request import ListConcurrencyConfigsRequest
from ._list_concurrency_configs_response import ListConcurrencyConfigsResponse
from ._list_custom_domains_request import ListCustomDomainsRequest
from ._list_custom_domains_response import ListCustomDomainsResponse
from ._list_function_versions_request import ListFunctionVersionsRequest
from ._list_function_versions_response import ListFunctionVersionsResponse
from ._list_functions_request import ListFunctionsRequest
from ._list_functions_shrink_request import ListFunctionsShrinkRequest
from ._list_functions_response import ListFunctionsResponse
from ._list_instances_request import ListInstancesRequest
from ._list_instances_shrink_request import ListInstancesShrinkRequest
from ._list_instances_response import ListInstancesResponse
from ._list_layer_versions_request import ListLayerVersionsRequest
from ._list_layer_versions_response import ListLayerVersionsResponse
from ._list_layers_request import ListLayersRequest
from ._list_layers_response import ListLayersResponse
from ._list_provision_configs_request import ListProvisionConfigsRequest
from ._list_provision_configs_response import ListProvisionConfigsResponse
from ._list_scaling_configs_request import ListScalingConfigsRequest
from ._list_scaling_configs_response import ListScalingConfigsResponse
from ._list_sessions_request import ListSessionsRequest
from ._list_sessions_response import ListSessionsResponse
from ._list_tag_resources_request import ListTagResourcesRequest
from ._list_tag_resources_shrink_request import ListTagResourcesShrinkRequest
from ._list_tag_resources_response import ListTagResourcesResponse
from ._list_triggers_request import ListTriggersRequest
from ._list_triggers_response import ListTriggersResponse
from ._list_vpc_bindings_response import ListVpcBindingsResponse
from ._publish_function_version_request import PublishFunctionVersionRequest
from ._publish_function_version_response import PublishFunctionVersionResponse
from ._put_async_invoke_config_request import PutAsyncInvokeConfigRequest
from ._put_async_invoke_config_response import PutAsyncInvokeConfigResponse
from ._put_concurrency_config_request import PutConcurrencyConfigRequest
from ._put_concurrency_config_response import PutConcurrencyConfigResponse
from ._put_layer_aclrequest import PutLayerACLRequest
from ._put_layer_aclresponse import PutLayerACLResponse
from ._put_provision_config_request import PutProvisionConfigRequest
from ._put_provision_config_response import PutProvisionConfigResponse
from ._put_scaling_config_request import PutScalingConfigRequest
from ._put_scaling_config_response import PutScalingConfigResponse
from ._stop_async_task_request import StopAsyncTaskRequest
from ._stop_async_task_response import StopAsyncTaskResponse
from ._tag_resources_request import TagResourcesRequest
from ._tag_resources_response import TagResourcesResponse
from ._untag_resources_request import UntagResourcesRequest
from ._untag_resources_shrink_request import UntagResourcesShrinkRequest
from ._untag_resources_response import UntagResourcesResponse
from ._update_alias_request import UpdateAliasRequest
from ._update_alias_response import UpdateAliasResponse
from ._update_custom_domain_request import UpdateCustomDomainRequest
from ._update_custom_domain_response import UpdateCustomDomainResponse
from ._update_function_request import UpdateFunctionRequest
from ._update_function_response import UpdateFunctionResponse
from ._update_session_request import UpdateSessionRequest
from ._update_session_response import UpdateSessionResponse
from ._update_trigger_request import UpdateTriggerRequest
from ._update_trigger_response import UpdateTriggerResponse
from ._describe_regions_output import DescribeRegionsOutputRegionsRegion
from ._describe_regions_output import DescribeRegionsOutputRegions
from ._list_tag_resources_request import ListTagResourcesRequestTag

__all__ = [
    AccelerationInfo,
    Alias,
    AsyncConfig,
    AsyncTask,
    AsyncTaskEvent,
    AuthConfig,
    BatchWindow,
    CDNTriggerConfig,
    CertConfig,
    ChangeResourceGroupInput,
    ChangeResourceGroupOutput,
    ConcurrencyConfig,
    CookieSessionAffinityConfig,
    CreateAliasInput,
    CreateCustomDomainInput,
    CreateFunctionInput,
    CreateLayerVersionInput,
    CreateSessionInput,
    CreateTriggerInput,
    CreateVpcBindingInput,
    CustomContainerConfig,
    CustomDNS,
    CustomDomain,
    CustomHealthCheckConfig,
    CustomRuntimeConfig,
    DNSOption,
    DeadLetterQueue,
    DeliveryOption,
    DescribeRegionsOutput,
    Destination,
    DestinationConfig,
    ElasticConfigStatus,
    EqualRule,
    Error,
    EventBridgeTriggerConfig,
    EventSinkConfig,
    EventSourceConfig,
    EventSourceParameters,
    Filter,
    Function,
    FunctionLayer,
    FunctionRestriction,
    GPUConfig,
    GetInstanceLifecycleEventsOutput,
    GetResourceTagsOutput,
    GetScalingConfigStatusOutput,
    HTTPTrigger,
    HTTPTriggerConfig,
    HeaderFieldSessionAffinityConfig,
    InputCodeLocation,
    InstanceEventItem,
    InstanceInfo,
    InstanceLifecycleConfig,
    JobConfig,
    Key,
    Layer,
    LifecycleHook,
    ListAliasesOutput,
    ListAsyncInvokeConfigOutput,
    ListAsyncTaskOutput,
    ListConcurrencyConfigsOutput,
    ListCustomDomainOutput,
    ListElasticConfigsOutput,
    ListFunctionsOutput,
    ListInstancesOutput,
    ListLayerVersionOutput,
    ListLayersOutput,
    ListProvisionConfigsOutput,
    ListResidentResourcePoolsOutput,
    ListScalingConfigStatusOutput,
    ListScalingConfigsOutput,
    ListSessionsOutput,
    ListTagResourcesOutput,
    ListTaggedResourcesOutput,
    ListTriggersOutput,
    ListVersionsOutput,
    ListVpcBindingsOutput,
    LogConfig,
    MCPSSESessionAffinityConfig,
    MCPStreamableSessionAffinityConfig,
    MNSTopicTriggerConfig,
    NASConfig,
    NASMountConfig,
    OSSMountConfig,
    OSSMountPoint,
    OSSTriggerConfig,
    OutputCodeLocation,
    OutputFuncCode,
    PathConfig,
    PolarFsConfig,
    PolarFsMountConfig,
    ProvisionConfig,
    PublishVersionInput,
    PutAsyncInvokeConfigInput,
    PutConcurrencyInput,
    PutElasticConfigInput,
    PutProvisionConfigInput,
    PutScalingConfigInput,
    PutScalingConfigOutput,
    RegexRule,
    RegistryAuthConfig,
    RegistryCertConfig,
    RegistryConfig,
    RegistryNetworkConfig,
    ResidentConfig,
    ResidentResourceAllocation,
    ResidentResourceAllocationStatus,
    ResidentResourceCapacity,
    ResidentResourcePool,
    Resource,
    RetryStrategy,
    RewriteConfig,
    RouteConfig,
    RunOptions,
    SLSTriggerConfig,
    SLSTriggerLogConfig,
    ScalingConfigStatus,
    ScalingPolicy,
    ScalingStatus,
    ScheduledAction,
    ScheduledPolicy,
    Session,
    SourceConfig,
    SourceDTSParameters,
    SourceKafkaParameters,
    SourceMNSParameters,
    SourceMQTTParameters,
    SourceRabbitMQParameters,
    SourceRocketMQParameters,
    TLSConfig,
    Tag,
    TagResource,
    TagResourceInput,
    TagResourcesInput,
    TargetTrackingPolicy,
    TimerTriggerConfig,
    TracingConfig,
    Trigger,
    UpdateAliasInput,
    UpdateCustomDomainInput,
    UpdateFunctionInput,
    UpdateResidentResourcePoolInput,
    UpdateSessionInput,
    UpdateTriggerInput,
    VPCConfig,
    Version,
    WAFConfig,
    WildcardRule,
    ChangeResourceGroupRequest,
    ChangeResourceGroupResponse,
    CreateAliasRequest,
    CreateAliasResponse,
    CreateCustomDomainRequest,
    CreateCustomDomainResponse,
    CreateFunctionRequest,
    CreateFunctionResponse,
    CreateLayerVersionRequest,
    CreateLayerVersionResponse,
    CreateSessionRequest,
    CreateSessionResponse,
    CreateTriggerRequest,
    CreateTriggerResponse,
    CreateVpcBindingRequest,
    CreateVpcBindingResponse,
    DeleteAliasResponse,
    DeleteAsyncInvokeConfigRequest,
    DeleteAsyncInvokeConfigResponse,
    DeleteConcurrencyConfigResponse,
    DeleteCustomDomainResponse,
    DeleteFunctionResponse,
    DeleteFunctionVersionResponse,
    DeleteLayerVersionResponse,
    DeleteProvisionConfigRequest,
    DeleteProvisionConfigResponse,
    DeleteScalingConfigRequest,
    DeleteScalingConfigResponse,
    DeleteSessionRequest,
    DeleteSessionResponse,
    DeleteTriggerResponse,
    DeleteVpcBindingResponse,
    DescribeRegionsRequest,
    DescribeRegionsResponse,
    DisableFunctionInvocationRequest,
    DisableFunctionInvocationResponseBody,
    DisableFunctionInvocationResponse,
    EnableFunctionInvocationResponseBody,
    EnableFunctionInvocationResponse,
    GetAliasResponse,
    GetAsyncInvokeConfigRequest,
    GetAsyncInvokeConfigResponse,
    GetAsyncTaskRequest,
    GetAsyncTaskResponse,
    GetConcurrencyConfigResponse,
    GetCustomDomainResponse,
    GetFunctionRequest,
    GetFunctionResponse,
    GetFunctionCodeRequest,
    GetFunctionCodeResponse,
    GetLayerVersionResponse,
    GetLayerVersionByArnResponse,
    GetProvisionConfigRequest,
    GetProvisionConfigResponse,
    GetScalingConfigRequest,
    GetScalingConfigResponse,
    GetSessionRequest,
    GetSessionResponse,
    GetTriggerResponse,
    InvokeFunctionHeaders,
    InvokeFunctionRequest,
    InvokeFunctionResponse,
    ListAliasesRequest,
    ListAliasesResponse,
    ListAsyncInvokeConfigsRequest,
    ListAsyncInvokeConfigsResponse,
    ListAsyncTasksRequest,
    ListAsyncTasksResponse,
    ListConcurrencyConfigsRequest,
    ListConcurrencyConfigsResponse,
    ListCustomDomainsRequest,
    ListCustomDomainsResponse,
    ListFunctionVersionsRequest,
    ListFunctionVersionsResponse,
    ListFunctionsRequest,
    ListFunctionsShrinkRequest,
    ListFunctionsResponse,
    ListInstancesRequest,
    ListInstancesShrinkRequest,
    ListInstancesResponse,
    ListLayerVersionsRequest,
    ListLayerVersionsResponse,
    ListLayersRequest,
    ListLayersResponse,
    ListProvisionConfigsRequest,
    ListProvisionConfigsResponse,
    ListScalingConfigsRequest,
    ListScalingConfigsResponse,
    ListSessionsRequest,
    ListSessionsResponse,
    ListTagResourcesRequest,
    ListTagResourcesShrinkRequest,
    ListTagResourcesResponse,
    ListTriggersRequest,
    ListTriggersResponse,
    ListVpcBindingsResponse,
    PublishFunctionVersionRequest,
    PublishFunctionVersionResponse,
    PutAsyncInvokeConfigRequest,
    PutAsyncInvokeConfigResponse,
    PutConcurrencyConfigRequest,
    PutConcurrencyConfigResponse,
    PutLayerACLRequest,
    PutLayerACLResponse,
    PutProvisionConfigRequest,
    PutProvisionConfigResponse,
    PutScalingConfigRequest,
    PutScalingConfigResponse,
    StopAsyncTaskRequest,
    StopAsyncTaskResponse,
    TagResourcesRequest,
    TagResourcesResponse,
    UntagResourcesRequest,
    UntagResourcesShrinkRequest,
    UntagResourcesResponse,
    UpdateAliasRequest,
    UpdateAliasResponse,
    UpdateCustomDomainRequest,
    UpdateCustomDomainResponse,
    UpdateFunctionRequest,
    UpdateFunctionResponse,
    UpdateSessionRequest,
    UpdateSessionResponse,
    UpdateTriggerRequest,
    UpdateTriggerResponse,
    DescribeRegionsOutputRegionsRegion,
    DescribeRegionsOutputRegions,
    ListTagResourcesRequestTag
]
