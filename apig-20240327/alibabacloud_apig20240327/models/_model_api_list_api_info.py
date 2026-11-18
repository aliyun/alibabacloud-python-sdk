# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ModelApiListApiInfo(DaraModel):
    def __init__(
        self,
        agent_protocols: List[str] = None,
        ai_protocols: List[str] = None,
        auth_config: main_models.AuthConfig = None,
        base_path: str = None,
        creation_client_token: str = None,
        delete_status: str = None,
        deploy_cnt_map: Dict[str, main_models.ModelApiListApiInfoDeployCntMapValue] = None,
        deploy_configs: List[main_models.HttpApiDeployConfig] = None,
        deploy_error_message: str = None,
        description: str = None,
        domain_ids: List[str] = None,
        domain_infos: List[main_models.ModelApiDomainInfo] = None,
        enable_auth: bool = None,
        environment_id: str = None,
        environments: List[main_models.ModelApiListApiInfoEnvironments] = None,
        gateway_id: str = None,
        gateway_info: main_models.GatewayInfo = None,
        http_api_id: str = None,
        ingress_info: main_models.ModelApiListApiInfoIngressInfo = None,
        model_api_info: main_models.ModelApiListApiInfoModelApiInfo = None,
        model_card_runtime_diagnostics: List[main_models.ModelApiListApiInfoModelCardRuntimeDiagnostics] = None,
        model_category: str = None,
        name: str = None,
        policy_configs: List[main_models.ModelApiPolicyConfig] = None,
        protocols: List[str] = None,
        resource_group_id: str = None,
        status: str = None,
        type: str = None,
        version_info: main_models.HttpApiVersionInfo = None,
    ):
        # The collection of agent protocols for the model API.
        self.agent_protocols = agent_protocols
        # The API protocols created by scenario. APIs created by selecting models provide open paths through modelApiInfo.
        self.ai_protocols = ai_protocols
        # The API authentication configurations created by scenario.
        self.auth_config = auth_config
        # The API base path.
        self.base_path = base_path
        # The read-only association identifier for the creation request. It is returned only within approximately 24 hours after the first persistence and when the association with the same instance is unique after normal authentication. It is omitted when the identifier is historical, expired, or ambiguous. You cannot use this identifier to determine whether publishing or authorization is successful, nor does it replace the creation idempotency record.
        self.creation_client_token = creation_client_token
        # The optional read-only deletion status of the new model API. Deleting indicates that the deletion request is accepted but not completed. DeleteFailed indicates that the background deletion failed, and you can use the original clientToken to retry DeleteModelApi. This field is not returned for normal deployment and historical undeployment. The absence of this field does not indicate that the deletion is complete.
        self.delete_status = delete_status
        # The publish status of the API operation.
        self.deploy_cnt_map = deploy_cnt_map
        # The API deployment configurations and associated services created by scenario, provided as read-only list information.
        self.deploy_configs = deploy_configs
        # The read-only reason for deployment or deletion failure.
        self.deploy_error_message = deploy_error_message
        # The API description.
        self.description = description
        # The selected domain IDs.
        self.domain_ids = domain_ids
        # The read-only domain details and default domain flag.
        self.domain_infos = domain_infos
        # Specifies whether to enable authentication.
        self.enable_auth = enable_auth
        # The read-only default environment ID of the bound instance.
        self.environment_id = environment_id
        # The publish environment context of the API.
        self.environments = environments
        # The ID of the gateway instance to which the API belongs.
        self.gateway_id = gateway_id
        # The read-only information of the bound instance.
        self.gateway_info = gateway_info
        # The model API ID.
        self.http_api_id = http_api_id
        # The HTTP ingress API information.
        self.ingress_info = ingress_info
        # The public selection information of the model API.
        self.model_api_info = model_api_info
        # The read-only runtime diagnostics of the model card, derived from the original markers of the deployment configuration. This is used only for the readability and diagnosability of abnormal drafts.
        self.model_card_runtime_diagnostics = model_card_runtime_diagnostics
        # The model category of the model API.
        self.model_category = model_category
        # The API name.
        self.name = name
        # The inline configurations for AI request logs and AI security protection.
        self.policy_configs = policy_configs
        # The list of API protocols.
        self.protocols = protocols
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The deployment status on the bound instance. In the new version, Undeploying indicates that the deletion is in progress, and UndeployFailed indicates that the deletion failed. Refer to deleteStatus to determine whether the operation is a deletion.
        self.status = status
        # The API type.
        self.type = type
        # The API versioning information.
        self.version_info = version_info

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.deploy_cnt_map:
            for v1 in self.deploy_cnt_map.values():
                 if v1:
                    v1.validate()
        if self.deploy_configs:
            for v1 in self.deploy_configs:
                 if v1:
                    v1.validate()
        if self.domain_infos:
            for v1 in self.domain_infos:
                 if v1:
                    v1.validate()
        if self.environments:
            for v1 in self.environments:
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
        if self.version_info:
            self.version_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_protocols is not None:
            result['agentProtocols'] = self.agent_protocols

        if self.ai_protocols is not None:
            result['aiProtocols'] = self.ai_protocols

        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()

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

        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k1 in self.deploy_configs:
                result['deployConfigs'].append(k1.to_map() if k1 else None)

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

        result['environments'] = []
        if self.environments is not None:
            for k1 in self.environments:
                result['environments'].append(k1.to_map() if k1 else None)

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

        if m.get('aiProtocols') is not None:
            self.ai_protocols = m.get('aiProtocols')

        if m.get('authConfig') is not None:
            temp_model = main_models.AuthConfig()
            self.auth_config = temp_model.from_map(m.get('authConfig'))

        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')

        if m.get('creationClientToken') is not None:
            self.creation_client_token = m.get('creationClientToken')

        if m.get('deleteStatus') is not None:
            self.delete_status = m.get('deleteStatus')

        self.deploy_cnt_map = {}
        if m.get('deployCntMap') is not None:
            for k1, v1 in m.get('deployCntMap').items():
                temp_model = main_models.ModelApiListApiInfoDeployCntMapValue()
                self.deploy_cnt_map[k1] = temp_model.from_map(v1)

        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k1 in m.get('deployConfigs'):
                temp_model = main_models.HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k1))

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

        self.environments = []
        if m.get('environments') is not None:
            for k1 in m.get('environments'):
                temp_model = main_models.ModelApiListApiInfoEnvironments()
                self.environments.append(temp_model.from_map(k1))

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.GatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')

        if m.get('ingressInfo') is not None:
            temp_model = main_models.ModelApiListApiInfoIngressInfo()
            self.ingress_info = temp_model.from_map(m.get('ingressInfo'))

        if m.get('modelApiInfo') is not None:
            temp_model = main_models.ModelApiListApiInfoModelApiInfo()
            self.model_api_info = temp_model.from_map(m.get('modelApiInfo'))

        self.model_card_runtime_diagnostics = []
        if m.get('modelCardRuntimeDiagnostics') is not None:
            for k1 in m.get('modelCardRuntimeDiagnostics'):
                temp_model = main_models.ModelApiListApiInfoModelCardRuntimeDiagnostics()
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

class ModelApiListApiInfoModelCardRuntimeDiagnostics(DaraModel):
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

class ModelApiListApiInfoModelApiInfo(DaraModel):
    def __init__(
        self,
        direct_supply_fallback_enabled: bool = None,
        exposure_mode: str = None,
        model_selection: main_models.ModelSelection = None,
        resolved_model_selection: main_models.ModelApiListApiInfoModelApiInfoResolvedModelSelection = None,
        routing_mode: str = None,
    ):
        # The save state of the direct supply fallback. A value of false indicates that it is disabled. This only reflects the saved configuration and does not indicate successful release or activation.
        self.direct_supply_fallback_enabled = direct_supply_fallback_enabled
        # The model exposure mode. Only SELECTED is supported in the first phase.
        self.exposure_mode = exposure_mode
        # The model selection configuration.
        self.model_selection = model_selection
        # The read-only public model collection for the current configuration. If complete is false, the collection is unknown, and partial members must not be used as the full count.
        self.resolved_model_selection = resolved_model_selection
        # The routing mode. Only Direct is supported in the first phase.
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
            temp_model = main_models.ModelApiListApiInfoModelApiInfoResolvedModelSelection()
            self.resolved_model_selection = temp_model.from_map(m.get('resolvedModelSelection'))

        if m.get('routingMode') is not None:
            self.routing_mode = m.get('routingMode')

        return self

class ModelApiListApiInfoModelApiInfoResolvedModelSelection(DaraModel):
    def __init__(
        self,
        complete: bool = None,
        model_card_ids: List[str] = None,
    ):
        # Indicates whether the group expansion collection for the current configuration is completely read. A complete empty group returns true and an empty array. A missing, invalid group, or read failure returns false. This does not represent the online release or consumer permission status.
        self.complete = complete
        # The model card IDs of the publicly selected models for the current configuration, stably sorted and deduplicated. Logical models retain their own IDs, excluding fallback-only targets or underlying execution cards of logical models. If complete is false, this is an empty array and must not be interpreted as zero models.
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

class ModelApiListApiInfoIngressInfo(DaraModel):
    def __init__(
        self,
        environment_info: main_models.ModelApiListApiInfoIngressInfoEnvironmentInfo = None,
        ingress_class: str = None,
        k_8s_cluster_info: main_models.ModelApiListApiInfoIngressInfoK8sClusterInfo = None,
        override_ingress_ip: bool = None,
        source_id: str = None,
        watch_namespace: str = None,
    ):
        # The environment context.
        self.environment_info = environment_info
        # The ingress class being listened to.
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
            temp_model = main_models.ModelApiListApiInfoIngressInfoEnvironmentInfo()
            self.environment_info = temp_model.from_map(m.get('environmentInfo'))

        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')

        if m.get('k8sClusterInfo') is not None:
            temp_model = main_models.ModelApiListApiInfoIngressInfoK8sClusterInfo()
            self.k_8s_cluster_info = temp_model.from_map(m.get('k8sClusterInfo'))

        if m.get('overrideIngressIp') is not None:
            self.override_ingress_ip = m.get('overrideIngressIp')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')

        return self

class ModelApiListApiInfoIngressInfoK8sClusterInfo(DaraModel):
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

class ModelApiListApiInfoIngressInfoEnvironmentInfo(DaraModel):
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

class ModelApiListApiInfoEnvironments(DaraModel):
    def __init__(
        self,
        alias: str = None,
        backend_scene: str = None,
        backend_type: str = None,
        custom_domains: List[main_models.HttpApiDomainInfo] = None,
        deploy_error_message: str = None,
        deploy_status: str = None,
        environment_id: str = None,
        gateway_info: main_models.ModelApiListApiInfoEnvironmentsGatewayInfo = None,
        name: str = None,
        service_configs: List[main_models.ModelApiListApiInfoEnvironmentsServiceConfigs] = None,
        sub_domains: List[main_models.ModelApiListApiInfoEnvironmentsSubDomains] = None,
    ):
        # The alias of the environment.
        self.alias = alias
        # The release scenario.
        self.backend_scene = backend_scene
        # The backend type.
        self.backend_type = backend_type
        # The custom domain name information published by the user.
        self.custom_domains = custom_domains
        # The read-only reason for the release failure.
        self.deploy_error_message = deploy_error_message
        # The release status of the API in the current environment.
        self.deploy_status = deploy_status
        # The ID of the environment.
        self.environment_id = environment_id
        # The gateway instance information to which the current environment belongs.
        self.gateway_info = gateway_info
        # The name of the environment.
        self.name = name
        # The existing service configurations.
        self.service_configs = service_configs
        # The list of default domain names for the environment.
        self.sub_domains = sub_domains

    def validate(self):
        if self.custom_domains:
            for v1 in self.custom_domains:
                 if v1:
                    v1.validate()
        if self.gateway_info:
            self.gateway_info.validate()
        if self.service_configs:
            for v1 in self.service_configs:
                 if v1:
                    v1.validate()
        if self.sub_domains:
            for v1 in self.sub_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene

        if self.backend_type is not None:
            result['backendType'] = self.backend_type

        result['customDomains'] = []
        if self.custom_domains is not None:
            for k1 in self.custom_domains:
                result['customDomains'].append(k1.to_map() if k1 else None)

        if self.deploy_error_message is not None:
            result['deployErrorMessage'] = self.deploy_error_message

        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        result['subDomains'] = []
        if self.sub_domains is not None:
            for k1 in self.sub_domains:
                result['subDomains'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')

        if m.get('backendType') is not None:
            self.backend_type = m.get('backendType')

        self.custom_domains = []
        if m.get('customDomains') is not None:
            for k1 in m.get('customDomains'):
                temp_model = main_models.HttpApiDomainInfo()
                self.custom_domains.append(temp_model.from_map(k1))

        if m.get('deployErrorMessage') is not None:
            self.deploy_error_message = m.get('deployErrorMessage')

        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.ModelApiListApiInfoEnvironmentsGatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.ModelApiListApiInfoEnvironmentsServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k1 in m.get('subDomains'):
                temp_model = main_models.ModelApiListApiInfoEnvironmentsSubDomains()
                self.sub_domains.append(temp_model.from_map(k1))

        return self

class ModelApiListApiInfoEnvironmentsSubDomains(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        network_type: str = None,
        protocol: str = None,
    ):
        # The ID of the domain name.
        self.domain_id = domain_id
        # The domain name.
        self.name = name
        # The network type.
        self.network_type = network_type
        # The access protocol.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.name is not None:
            result['name'] = self.name

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class ModelApiListApiInfoEnvironmentsServiceConfigs(DaraModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: main_models.HttpApiBackendMatchConditions = None,
        name: str = None,
        port: str = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        # The ID of the service.
        self.gateway_service_id = gateway_service_id
        # The match conditions.
        self.match = match
        # The name of the service.
        self.name = name
        # The service port.
        self.port = port
        # The protocol.
        self.protocol = protocol
        # The ID of the service.
        self.service_id = service_id
        # The service version.
        self.version = version
        # The weight.
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.version is not None:
            result['version'] = self.version

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayServiceId') is not None:
            self.gateway_service_id = m.get('gatewayServiceId')

        if m.get('match') is not None:
            temp_model = main_models.HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class ModelApiListApiInfoEnvironmentsGatewayInfo(DaraModel):
    def __init__(
        self,
        gateway_edition: str = None,
        gateway_id: str = None,
        name: str = None,
    ):
        # The edition of the gateway instance. Valid values: Professional, Serverless, MultiTenantServerless, and Unknown.
        self.gateway_edition = gateway_edition
        # The gateway instance ID.
        self.gateway_id = gateway_id
        # The name of the gateway instance.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_edition is not None:
            result['gatewayEdition'] = self.gateway_edition

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayEdition') is not None:
            self.gateway_edition = m.get('gatewayEdition')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

