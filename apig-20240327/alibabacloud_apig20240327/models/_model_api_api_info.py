# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ModelApiApiInfo(DaraModel):
    def __init__(
        self,
        agent_protocols: List[str] = None,
        base_path: str = None,
        creation_client_token: str = None,
        delete_status: str = None,
        deploy_cnt_map: Dict[str, main_models.ModelApiApiInfoDeployCntMapValue] = None,
        deploy_error_message: str = None,
        description: str = None,
        domain_ids: List[str] = None,
        domain_infos: List[main_models.ModelApiDomainInfo] = None,
        enable_auth: bool = None,
        environment_id: str = None,
        gateway_id: str = None,
        gateway_info: main_models.GatewayInfo = None,
        http_api_id: str = None,
        ingress_info: main_models.ModelApiApiInfoIngressInfo = None,
        model_api_info: main_models.ModelApiApiInfoModelApiInfo = None,
        model_card_runtime_diagnostics: List[main_models.ModelApiApiInfoModelCardRuntimeDiagnostics] = None,
        model_category: str = None,
        name: str = None,
        policy_configs: List[main_models.ModelApiPolicyConfig] = None,
        protocols: List[str] = None,
        published_endpoints: List[main_models.ModelApiApiInfoPublishedEndpoints] = None,
        resource_group_id: str = None,
        status: str = None,
        type: str = None,
        version_info: main_models.HttpApiVersionInfo = None,
    ):
        # The collection of agent protocols for the model API.
        self.agent_protocols = agent_protocols
        # The API base path.
        self.base_path = base_path
        # The read-only correlation identifier for creation requests. It is returned only when the association with the same instance is unique within approximately 24 hours after the first persistence following normal authentication. It is omitted for historical, expired, or ambiguous cases. This identifier cannot be used to determine the success of publishing or authorization, nor does it replace the creation of idempotent records.
        self.creation_client_token = creation_client_token
        # The deletion status of the new version model API. This field is read-only and optional. Deleting indicates that the deletion request is accepted but not yet completed. DeleteFailed indicates that the background deletion failed, and you can use the original clientToken to retry the DeleteModelApi operation. This field is not returned for normal publishing and historical undeployment. The absence of this field does not indicate that the deletion is complete.
        self.delete_status = delete_status
        # The publish status of the API operation.
        self.deploy_cnt_map = deploy_cnt_map
        # The reason for the deployment or deletion failure. This field is read-only.
        self.deploy_error_message = deploy_error_message
        # The API description.
        self.description = description
        # The selected domain IDs.
        self.domain_ids = domain_ids
        # The read-only domain name details and the default domain name flag.
        self.domain_infos = domain_infos
        # Specifies whether to enable authentication.
        self.enable_auth = enable_auth
        # The default environment ID of the bound instance. This field is read-only.
        self.environment_id = environment_id
        # The ID of the gateway instance to which the API belongs.
        self.gateway_id = gateway_id
        # The read-only information of the bound instance.
        self.gateway_info = gateway_info
        # The model API ID.
        self.http_api_id = http_api_id
        # The HTTP ingress API information.
        self.ingress_info = ingress_info
        # The model API public selection information.
        self.model_api_info = model_api_info
        # The read-only runtime diagnostic information for model cards, derived from the original markers of the deployment configuration. It is used only for the readability and diagnostics of abnormal drafts.
        self.model_card_runtime_diagnostics = model_card_runtime_diagnostics
        # The model category of the model API.
        self.model_category = model_category
        # The API name.
        self.name = name
        # The inline configurations for AI request logs and AI security protection.
        self.policy_configs = policy_configs
        # The list of API protocols.
        self.protocols = protocols
        # The collection of successfully published per-path executable models. This field is read-only. It is empty when a snapshot is missing, which does not represent consumer permission.
        self.published_endpoints = published_endpoints
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The publishing status on the bound instance. In the new version, the status is Undeploying when a deletion is in progress, and UndeployFailed when a deletion fails. To determine whether an operation is a deletion, refer to the deleteStatus field.
        self.status = status
        # The API type.
        self.type = type
        # The API versioning information.
        self.version_info = version_info

    def validate(self):
        if self.deploy_cnt_map:
            for v1 in self.deploy_cnt_map.values():
                 if v1:
                    v1.validate()
        if self.domain_infos:
            for v1 in self.domain_infos:
                 if v1:
                    v1.validate()
        if self.gateway_info:
            self.gateway_info.validate()
        if self.ingress_info:
            self.ingress_info.validate()
        if self.model_api_info:
            self.model_api_info.validate()
        if self.model_card_runtime_diagnostics:
            for v1 in self.model_card_runtime_diagnostics:
                 if v1:
                    v1.validate()
        if self.policy_configs:
            for v1 in self.policy_configs:
                 if v1:
                    v1.validate()
        if self.published_endpoints:
            for v1 in self.published_endpoints:
                 if v1:
                    v1.validate()
        if self.version_info:
            self.version_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_protocols is not None:
            result['agentProtocols'] = self.agent_protocols

        if self.base_path is not None:
            result['basePath'] = self.base_path

        if self.creation_client_token is not None:
            result['creationClientToken'] = self.creation_client_token

        if self.delete_status is not None:
            result['deleteStatus'] = self.delete_status

        result['deployCntMap'] = {}
        if self.deploy_cnt_map is not None:
            for k1, v1 in self.deploy_cnt_map.items():
                result['deployCntMap'][k1] = v1.to_map() if v1 else None

        if self.deploy_error_message is not None:
            result['deployErrorMessage'] = self.deploy_error_message

        if self.description is not None:
            result['description'] = self.description

        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids

        result['domainInfos'] = []
        if self.domain_infos is not None:
            for k1 in self.domain_infos:
                result['domainInfos'].append(k1.to_map() if k1 else None)

        if self.enable_auth is not None:
            result['enableAuth'] = self.enable_auth

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id

        if self.ingress_info is not None:
            result['ingressInfo'] = self.ingress_info.to_map()

        if self.model_api_info is not None:
            result['modelApiInfo'] = self.model_api_info.to_map()

        result['modelCardRuntimeDiagnostics'] = []
        if self.model_card_runtime_diagnostics is not None:
            for k1 in self.model_card_runtime_diagnostics:
                result['modelCardRuntimeDiagnostics'].append(k1.to_map() if k1 else None)

        if self.model_category is not None:
            result['modelCategory'] = self.model_category

        if self.name is not None:
            result['name'] = self.name

        result['policyConfigs'] = []
        if self.policy_configs is not None:
            for k1 in self.policy_configs:
                result['policyConfigs'].append(k1.to_map() if k1 else None)

        if self.protocols is not None:
            result['protocols'] = self.protocols

        result['publishedEndpoints'] = []
        if self.published_endpoints is not None:
            for k1 in self.published_endpoints:
                result['publishedEndpoints'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.version_info is not None:
            result['versionInfo'] = self.version_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentProtocols') is not None:
            self.agent_protocols = m.get('agentProtocols')

        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')

        if m.get('creationClientToken') is not None:
            self.creation_client_token = m.get('creationClientToken')

        if m.get('deleteStatus') is not None:
            self.delete_status = m.get('deleteStatus')

        self.deploy_cnt_map = {}
        if m.get('deployCntMap') is not None:
            for k1, v1 in m.get('deployCntMap').items():
                temp_model = main_models.ModelApiApiInfoDeployCntMapValue()
                self.deploy_cnt_map[k1] = temp_model.from_map(v1)

        if m.get('deployErrorMessage') is not None:
            self.deploy_error_message = m.get('deployErrorMessage')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')

        self.domain_infos = []
        if m.get('domainInfos') is not None:
            for k1 in m.get('domainInfos'):
                temp_model = main_models.ModelApiDomainInfo()
                self.domain_infos.append(temp_model.from_map(k1))

        if m.get('enableAuth') is not None:
            self.enable_auth = m.get('enableAuth')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.GatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')

        if m.get('ingressInfo') is not None:
            temp_model = main_models.ModelApiApiInfoIngressInfo()
            self.ingress_info = temp_model.from_map(m.get('ingressInfo'))

        if m.get('modelApiInfo') is not None:
            temp_model = main_models.ModelApiApiInfoModelApiInfo()
            self.model_api_info = temp_model.from_map(m.get('modelApiInfo'))

        self.model_card_runtime_diagnostics = []
        if m.get('modelCardRuntimeDiagnostics') is not None:
            for k1 in m.get('modelCardRuntimeDiagnostics'):
                temp_model = main_models.ModelApiApiInfoModelCardRuntimeDiagnostics()
                self.model_card_runtime_diagnostics.append(temp_model.from_map(k1))

        if m.get('modelCategory') is not None:
            self.model_category = m.get('modelCategory')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.policy_configs = []
        if m.get('policyConfigs') is not None:
            for k1 in m.get('policyConfigs'):
                temp_model = main_models.ModelApiPolicyConfig()
                self.policy_configs.append(temp_model.from_map(k1))

        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')

        self.published_endpoints = []
        if m.get('publishedEndpoints') is not None:
            for k1 in m.get('publishedEndpoints'):
                temp_model = main_models.ModelApiApiInfoPublishedEndpoints()
                self.published_endpoints.append(temp_model.from_map(k1))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('versionInfo') is not None:
            temp_model = main_models.HttpApiVersionInfo()
            self.version_info = temp_model.from_map(m.get('versionInfo'))

        return self

class ModelApiApiInfoPublishedEndpoints(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        model_card_ids: List[str] = None,
    ):
        # The name of the successfully published built-in endpoint.
        self.endpoint = endpoint
        # The collection of executable ModelCard IDs successfully published for this path.
        self.model_card_ids = model_card_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.model_card_ids is not None:
            result['modelCardIds'] = self.model_card_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('modelCardIds') is not None:
            self.model_card_ids = m.get('modelCardIds')

        return self

class ModelApiApiInfoModelCardRuntimeDiagnostics(DaraModel):
    def __init__(
        self,
        deploy_config_index: int = None,
        gateway_id: str = None,
        invalid_configuration: bool = None,
        reasons: List[str] = None,
    ):
        # The index of the corresponding deployment configuration.
        self.deploy_config_index = deploy_config_index
        # The gateway instance ID.
        self.gateway_id = gateway_id
        # Indicates whether the marker of the deployment configuration is invalid.
        self.invalid_configuration = invalid_configuration
        # The list of reasons for invalidity.
        self.reasons = reasons

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deploy_config_index is not None:
            result['deployConfigIndex'] = self.deploy_config_index

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.invalid_configuration is not None:
            result['invalidConfiguration'] = self.invalid_configuration

        if self.reasons is not None:
            result['reasons'] = self.reasons

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deployConfigIndex') is not None:
            self.deploy_config_index = m.get('deployConfigIndex')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('invalidConfiguration') is not None:
            self.invalid_configuration = m.get('invalidConfiguration')

        if m.get('reasons') is not None:
            self.reasons = m.get('reasons')

        return self

class ModelApiApiInfoModelApiInfo(DaraModel):
    def __init__(
        self,
        direct_supply_fallback_enabled: bool = None,
        exposure_mode: str = None,
        model_selection: main_models.ModelSelection = None,
        resolved_model_selection: main_models.ModelApiApiInfoModelApiInfoResolvedModelSelection = None,
        routing_mode: str = None,
    ):
        # The saved state of the direct supply fallback. A value of false indicates that it is disabled. This only reflects the saved configuration and does not indicate successful publishing or activation.
        self.direct_supply_fallback_enabled = direct_supply_fallback_enabled
        # The model exposure mode. Only SELECTED is supported in Phase 1.
        self.exposure_mode = exposure_mode
        # The model selection configuration.
        self.model_selection = model_selection
        # The read-only collection of publicly exposed models for the current configuration. It retains the modelSelection edit source, but the successful online collection is still subject to publishedEndpoints.
        self.resolved_model_selection = resolved_model_selection
        # The routing mode. Only Direct is supported in Phase 1.
        self.routing_mode = routing_mode

    def validate(self):
        if self.model_selection:
            self.model_selection.validate()
        if self.resolved_model_selection:
            self.resolved_model_selection.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direct_supply_fallback_enabled is not None:
            result['directSupplyFallbackEnabled'] = self.direct_supply_fallback_enabled

        if self.exposure_mode is not None:
            result['exposureMode'] = self.exposure_mode

        if self.model_selection is not None:
            result['modelSelection'] = self.model_selection.to_map()

        if self.resolved_model_selection is not None:
            result['resolvedModelSelection'] = self.resolved_model_selection.to_map()

        if self.routing_mode is not None:
            result['routingMode'] = self.routing_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directSupplyFallbackEnabled') is not None:
            self.direct_supply_fallback_enabled = m.get('directSupplyFallbackEnabled')

        if m.get('exposureMode') is not None:
            self.exposure_mode = m.get('exposureMode')

        if m.get('modelSelection') is not None:
            temp_model = main_models.ModelSelection()
            self.model_selection = temp_model.from_map(m.get('modelSelection'))

        if m.get('resolvedModelSelection') is not None:
            temp_model = main_models.ModelApiApiInfoModelApiInfoResolvedModelSelection()
            self.resolved_model_selection = temp_model.from_map(m.get('resolvedModelSelection'))

        if m.get('routingMode') is not None:
            self.routing_mode = m.get('routingMode')

        return self

class ModelApiApiInfoModelApiInfoResolvedModelSelection(DaraModel):
    def __init__(
        self,
        complete: bool = None,
        model_card_ids: List[str] = None,
    ):
        # Indicates whether the expanded collection of the current configuration is fully read. A fully empty group returns true and an empty array. Missing, invalid groups, or read failures return false. This does not reflect the online publishing or consumer permission status.
        self.complete = complete
        # The identities of the models selected for public exposure in the current configuration, stably sorted and deduplicated. Logical models retain their own IDs and do not include fallback-only targets or underlying execution cards of logical models. If complete is false, this is an empty array and must not be interpreted as zero models.
        self.model_card_ids = model_card_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete is not None:
            result['complete'] = self.complete

        if self.model_card_ids is not None:
            result['modelCardIds'] = self.model_card_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('complete') is not None:
            self.complete = m.get('complete')

        if m.get('modelCardIds') is not None:
            self.model_card_ids = m.get('modelCardIds')

        return self

class ModelApiApiInfoIngressInfo(DaraModel):
    def __init__(
        self,
        environment_info: main_models.ModelApiApiInfoIngressInfoEnvironmentInfo = None,
        ingress_class: str = None,
        k_8s_cluster_info: main_models.ModelApiApiInfoIngressInfoK8sClusterInfo = None,
        override_ingress_ip: bool = None,
        source_id: str = None,
        watch_namespace: str = None,
    ):
        # The environment context.
        self.environment_info = environment_info
        # The ingress class.
        self.ingress_class = ingress_class
        # The Kubernetes cluster information.
        self.k_8s_cluster_info = k_8s_cluster_info
        # Specifies whether to update the address in the ingress status.
        self.override_ingress_ip = override_ingress_ip
        # The source ID.
        self.source_id = source_id
        # The watched namespace.
        self.watch_namespace = watch_namespace

    def validate(self):
        if self.environment_info:
            self.environment_info.validate()
        if self.k_8s_cluster_info:
            self.k_8s_cluster_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()

        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class

        if self.k_8s_cluster_info is not None:
            result['k8sClusterInfo'] = self.k_8s_cluster_info.to_map()

        if self.override_ingress_ip is not None:
            result['overrideIngressIp'] = self.override_ingress_ip

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentInfo') is not None:
            temp_model = main_models.ModelApiApiInfoIngressInfoEnvironmentInfo()
            self.environment_info = temp_model.from_map(m.get('environmentInfo'))

        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')

        if m.get('k8sClusterInfo') is not None:
            temp_model = main_models.ModelApiApiInfoIngressInfoK8sClusterInfo()
            self.k_8s_cluster_info = temp_model.from_map(m.get('k8sClusterInfo'))

        if m.get('overrideIngressIp') is not None:
            self.override_ingress_ip = m.get('overrideIngressIp')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')

        return self

class ModelApiApiInfoIngressInfoK8sClusterInfo(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        return self

class ModelApiApiInfoIngressInfoEnvironmentInfo(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
    ):
        # The environment ID.
        self.environment_id = environment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        return self

