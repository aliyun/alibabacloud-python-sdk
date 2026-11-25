# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class TypedAIAsset(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        agent_id: str = None,
        config_path: str = None,
        description: str = None,
        endpoint: str = None,
        endpoint_type: str = None,
        first_seen: str = None,
        form: str = None,
        id: str = None,
        identity_identifiers: main_models.TypedAIAssetIdentityIdentifiers = None,
        install_path: str = None,
        instance_local_id: str = None,
        last_check_time: str = None,
        last_detect_task_id: str = None,
        last_seen: str = None,
        matched_rules: List[str] = None,
        mcp_id: str = None,
        product_code: str = None,
        provider_id: str = None,
        provider_name: str = None,
        provider_name_cn: str = None,
        provider_name_en: str = None,
        provider_type: str = None,
        recognition_evidence: main_models.TypedAIAssetRecognitionEvidence = None,
        recognition_status: str = None,
        risk_info: main_models.TypedAIAssetRiskInfo = None,
        risk_level: str = None,
        scan_id: str = None,
        source_type: str = None,
        standard_sha_256: str = None,
        transport: str = None,
        vendor: int = None,
        version: str = None,
    ):
        # The access method for the MCP. Valid values: local_process for local processes, remote_service for remote services, and unknown for undetermined methods.
        self.access_type = access_type
        # The database primary key of the agent instance associated with the leaf asset, returned as a decimal numeric string. The value can be 0 when no agent is associated, and it can also be 0 in the details of the agent itself. This field is not returned in aggregated lists.
        self.agent_id = agent_id
        # The configuration path where the LLM, MCP, or tool declaration is located. This is not a skill package identifier. It is returned in instance details but not in aggregated lists.
        self.config_path = config_path
        # The description text collected for an MCP, tool, or skill. This is not returned if missing. Aggregated lists only return descriptions that are consistent within the group.
        self.description = description
        # The configured service endpoint for an LLM model service or remote MCP. Local stdio MCPs may not have this field. Its presence does not indicate a successful connection or actual invocation.
        self.endpoint = endpoint
        # The classification of the LLM service endpoint. Valid values: official for official services, third_party for third-party services, and unknown for undetermined services. This classification does not represent a security detection conclusion.
        self.endpoint_type = endpoint_type
        # The time when the asset instance was first observed. The value is a database datetime string that may include six decimal places for seconds, without a unified time zone indicator. This field is not returned in aggregated lists.
        self.first_seen = first_seen
        # The installation form of the agent, such as desktop_app, ide_extension, cli, or sdk. This is not the endpoint operating system such as Windows or macOS. The specific value is subject to the instance recognition result.
        self.form = form
        # The database primary key of the table where the asset instance is located, returned as a decimal numeric string to prevent precision loss of large integers. This is not the asset aggregation key AssetKey, and this instance field is not returned in aggregated lists.
        self.id = id
        # The collected product identity clues and their categorization by identifier type. These are used for auxiliary identification and do not indicate that signatures, publishers, or file contents have been authenticated through security authentication.
        self.identity_identifiers = identity_identifiers
        # The installation path of the agent instance. This field is used only for instance details and is not returned in aggregated lists. It is not applicable to other asset types.
        self.install_path = install_path
        # The instance identity installed or declared within the endpoint, calculated by the script based on the asset type, ownership, and location. The identity scope must still include the tenant and endpoint, and it cannot be used as a globally unique ID across endpoints. This field is not returned in aggregation lists.
        self.instance_local_id = instance_local_id
        # The time of the last successful detection for the current skill content. This field is empty or not returned if no saved successful detection record exists. The value is a database datetime string without a unified time zone indicator. This field is not returned in aggregated lists.
        self.last_check_time = last_check_time
        # The database ID of the latest detection task associated with the current skill content, returned as a decimal numeric string. The value can be 0 if no task is associated. The presence of a task ID does not indicate that the detection is complete. This field is not returned in aggregated lists.
        self.last_detect_task_id = last_detect_task_id
        # The time when the asset instance was last actually observed. The value is a database datetime string that may include six decimal places for seconds. This is not the page query time. This field is not returned in aggregated lists.
        self.last_seen = last_seen
        # The array of static recognition basis tags matched by the agent, which can include model_call, tool_call, autonomous_execution, state_management, and agent_declaration. This does not indicate that the agent was actually executed or passed security certification.
        self.matched_rules = matched_rules
        # The database primary key of the MCP instance associated with the tool, returned as a decimal numeric string. The value can be 0 when no MCP is associated, and this field is not applicable to other asset types. This field is not returned in aggregated lists.
        self.mcp_id = mcp_id
        # The product code of the agent. The specific value is subject to the product catalog in the recognition rules. This field is not returned when it is not applicable, unidentified, or inconsistent across aggregated attributes.
        self.product_code = product_code
        # The provider identifier matched based on the service endpoint and provider directory. This may not be returned if no match is found and is not the product code of the associated agent.
        self.provider_id = provider_id
        # The provider display name of the tool. This is generated from the associated MCP, agent, or declaration source and is not a proof of security or trust.
        self.provider_name = provider_name
        # The Chinese display name of the service provider. The directory name is prioritized. The name parsed from the service endpoint may be used if no match is found. The presence of this field does not indicate that the service provider is identified.
        self.provider_name_cn = provider_name_cn
        # The English display name of the service provider. The directory name is prioritized. The name parsed from the service endpoint may be used if no match is found. The presence of this field does not indicate that the service provider is identified.
        self.provider_name_en = provider_name_en
        # The declared provider type of the tool. Valid values: mcp, agent, software, file, or unknown. This describes the declaration source and does not represent the actual caller, authorization status, or vendor identity.
        self.provider_type = provider_type
        # The static recognition basis of the agent, which lists the source paths and evidence text grouped by recognition tags. This is not a runtime audit record, and instance-level evidence is not returned in aggregated lists.
        self.recognition_evidence = recognition_evidence
        # The product recognition status of the agent. identified indicates recognized, unidentified indicates pending recognition, and conflict indicates a recognition conflict. This status does not indicate whether the asset is secure.
        self.recognition_status = recognition_status
        # The counts of high, medium, and low-risk items saved for the current skill content. This may be empty or not returned when no detection results are available. A missing value cannot be interpreted as a zero risk count or an indication of security.
        self.risk_info = risk_info
        # The final risk level saved for the current skill content. This is not returned when no detection conclusion is available. The value high is provided only as a format example and does not serve as a new enumeration constraint.
        self.risk_level = risk_level
        # The scan batch identifier of the most recent scan where the instance was actually observed. This is not a database primary key or asset content hash. This field is not returned in aggregated lists.
        self.scan_id = scan_id
        # The source channel classification of the skill. The default value for current collection and storage is unknown. The unknown value cannot be inferred as an official or community source.
        self.source_type = source_type
        # The SHA-256 hash of the complete skill package bytes. The format is a 64-character lowercase hexadecimal string without the sha256: prefix. The current script uses the skill-canonical-zip-v1 specification for compression. This is not equivalent to the installation instance ID and does not indicate that the package has been inspected or is secure.
        self.standard_sha_256 = standard_sha_256
        # The transport protocol declared in the MCP configuration. The collected value is retained as-is, such as stdio, sse, or streamable_http. This cannot be used to determine whether the service is running or has been invoked.
        self.transport = transport
        # The vendor code for the collected and stored skill. The current default value is 1000. This cannot be used to infer a specific vendor or security status.
        self.vendor = vendor
        # The collected installation version of the agent. This field is not returned when the version is not collected. In aggregated lists, this field is returned only when the versions of all instances in the group are identical and not empty.
        self.version = version

    def validate(self):
        if self.identity_identifiers:
            self.identity_identifiers.validate()
        if self.recognition_evidence:
            self.recognition_evidence.validate()
        if self.risk_info:
            self.risk_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.config_path is not None:
            result['ConfigPath'] = self.config_path

        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.first_seen is not None:
            result['FirstSeen'] = self.first_seen

        if self.form is not None:
            result['Form'] = self.form

        if self.id is not None:
            result['Id'] = self.id

        if self.identity_identifiers is not None:
            result['IdentityIdentifiers'] = self.identity_identifiers.to_map()

        if self.install_path is not None:
            result['InstallPath'] = self.install_path

        if self.instance_local_id is not None:
            result['InstanceLocalId'] = self.instance_local_id

        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        if self.last_detect_task_id is not None:
            result['LastDetectTaskId'] = self.last_detect_task_id

        if self.last_seen is not None:
            result['LastSeen'] = self.last_seen

        if self.matched_rules is not None:
            result['MatchedRules'] = self.matched_rules

        if self.mcp_id is not None:
            result['McpId'] = self.mcp_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.provider_name_cn is not None:
            result['ProviderNameCn'] = self.provider_name_cn

        if self.provider_name_en is not None:
            result['ProviderNameEn'] = self.provider_name_en

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

        if self.recognition_evidence is not None:
            result['RecognitionEvidence'] = self.recognition_evidence.to_map()

        if self.recognition_status is not None:
            result['RecognitionStatus'] = self.recognition_status

        if self.risk_info is not None:
            result['RiskInfo'] = self.risk_info.to_map()

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.scan_id is not None:
            result['ScanId'] = self.scan_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.standard_sha_256 is not None:
            result['StandardSha256'] = self.standard_sha_256

        if self.transport is not None:
            result['Transport'] = self.transport

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ConfigPath') is not None:
            self.config_path = m.get('ConfigPath')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('FirstSeen') is not None:
            self.first_seen = m.get('FirstSeen')

        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdentityIdentifiers') is not None:
            temp_model = main_models.TypedAIAssetIdentityIdentifiers()
            self.identity_identifiers = temp_model.from_map(m.get('IdentityIdentifiers'))

        if m.get('InstallPath') is not None:
            self.install_path = m.get('InstallPath')

        if m.get('InstanceLocalId') is not None:
            self.instance_local_id = m.get('InstanceLocalId')

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('LastDetectTaskId') is not None:
            self.last_detect_task_id = m.get('LastDetectTaskId')

        if m.get('LastSeen') is not None:
            self.last_seen = m.get('LastSeen')

        if m.get('MatchedRules') is not None:
            self.matched_rules = m.get('MatchedRules')

        if m.get('McpId') is not None:
            self.mcp_id = m.get('McpId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('ProviderNameCn') is not None:
            self.provider_name_cn = m.get('ProviderNameCn')

        if m.get('ProviderNameEn') is not None:
            self.provider_name_en = m.get('ProviderNameEn')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        if m.get('RecognitionEvidence') is not None:
            temp_model = main_models.TypedAIAssetRecognitionEvidence()
            self.recognition_evidence = temp_model.from_map(m.get('RecognitionEvidence'))

        if m.get('RecognitionStatus') is not None:
            self.recognition_status = m.get('RecognitionStatus')

        if m.get('RiskInfo') is not None:
            temp_model = main_models.TypedAIAssetRiskInfo()
            self.risk_info = temp_model.from_map(m.get('RiskInfo'))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('ScanId') is not None:
            self.scan_id = m.get('ScanId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StandardSha256') is not None:
            self.standard_sha_256 = m.get('StandardSha256')

        if m.get('Transport') is not None:
            self.transport = m.get('Transport')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class TypedAIAssetRiskInfo(DaraModel):
    def __init__(
        self,
        high_risk_cnt: int = None,
        low_risk_cnt: int = None,
        medium_risk_cnt: int = None,
    ):
        # The number of high-risk items in the currently saved detection results. This is interpreted as an actual count only when detection results are available.
        self.high_risk_cnt = high_risk_cnt
        # The number of low-risk items in the currently saved detection results. A value of zero indicates no low-risk items in the results but does not indicate overall security.
        self.low_risk_cnt = low_risk_cnt
        # The number of medium-risk items in the currently saved detection results. A value of zero indicates no medium-risk items in the results but does not indicate the absence of other risks.
        self.medium_risk_cnt = medium_risk_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.high_risk_cnt is not None:
            result['highRiskCnt'] = self.high_risk_cnt

        if self.low_risk_cnt is not None:
            result['lowRiskCnt'] = self.low_risk_cnt

        if self.medium_risk_cnt is not None:
            result['mediumRiskCnt'] = self.medium_risk_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('highRiskCnt') is not None:
            self.high_risk_cnt = m.get('highRiskCnt')

        if m.get('lowRiskCnt') is not None:
            self.low_risk_cnt = m.get('lowRiskCnt')

        if m.get('mediumRiskCnt') is not None:
            self.medium_risk_cnt = m.get('mediumRiskCnt')

        return self

class TypedAIAssetRecognitionEvidence(DaraModel):
    def __init__(
        self,
        agent_declaration: List[main_models.TypedAIAssetRecognitionEvidenceAgentDeclaration] = None,
        autonomous_execution: List[main_models.TypedAIAssetRecognitionEvidenceAutonomousExecution] = None,
        model_call: List[main_models.TypedAIAssetRecognitionEvidenceModelCall] = None,
        state_management: List[main_models.TypedAIAssetRecognitionEvidenceStateManagement] = None,
        tool_call: List[main_models.TypedAIAssetRecognitionEvidenceToolCall] = None,
    ):
        # The array of evidence for explicit declarations of agent roles, capabilities, or usage methods. The declaration content itself does not constitute security certification.
        self.agent_declaration = agent_declaration
        # The array of static evidence related to autonomous task execution or agent loops. This does not indicate that actual execution was observed during this scan.
        self.autonomous_execution = autonomous_execution
        # The array of static evidence related to model clients, requests, or configurations. This does not indicate that model requests were actually sent.
        self.model_call = model_call
        # The array of static evidence related to sessions, memory, or state management. This does not prove actual data persistence or runtime behavior.
        self.state_management = state_management
        # The array of static evidence related to tool declarations or code to invoke tools. This does not indicate that the tools were actually executed.
        self.tool_call = tool_call

    def validate(self):
        if self.agent_declaration:
            for v1 in self.agent_declaration:
                 if v1:
                    v1.validate()
        if self.autonomous_execution:
            for v1 in self.autonomous_execution:
                 if v1:
                    v1.validate()
        if self.model_call:
            for v1 in self.model_call:
                 if v1:
                    v1.validate()
        if self.state_management:
            for v1 in self.state_management:
                 if v1:
                    v1.validate()
        if self.tool_call:
            for v1 in self.tool_call:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['agent_declaration'] = []
        if self.agent_declaration is not None:
            for k1 in self.agent_declaration:
                result['agent_declaration'].append(k1.to_map() if k1 else None)

        result['autonomous_execution'] = []
        if self.autonomous_execution is not None:
            for k1 in self.autonomous_execution:
                result['autonomous_execution'].append(k1.to_map() if k1 else None)

        result['model_call'] = []
        if self.model_call is not None:
            for k1 in self.model_call:
                result['model_call'].append(k1.to_map() if k1 else None)

        result['state_management'] = []
        if self.state_management is not None:
            for k1 in self.state_management:
                result['state_management'].append(k1.to_map() if k1 else None)

        result['tool_call'] = []
        if self.tool_call is not None:
            for k1 in self.tool_call:
                result['tool_call'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_declaration = []
        if m.get('agent_declaration') is not None:
            for k1 in m.get('agent_declaration'):
                temp_model = main_models.TypedAIAssetRecognitionEvidenceAgentDeclaration()
                self.agent_declaration.append(temp_model.from_map(k1))

        self.autonomous_execution = []
        if m.get('autonomous_execution') is not None:
            for k1 in m.get('autonomous_execution'):
                temp_model = main_models.TypedAIAssetRecognitionEvidenceAutonomousExecution()
                self.autonomous_execution.append(temp_model.from_map(k1))

        self.model_call = []
        if m.get('model_call') is not None:
            for k1 in m.get('model_call'):
                temp_model = main_models.TypedAIAssetRecognitionEvidenceModelCall()
                self.model_call.append(temp_model.from_map(k1))

        self.state_management = []
        if m.get('state_management') is not None:
            for k1 in m.get('state_management'):
                temp_model = main_models.TypedAIAssetRecognitionEvidenceStateManagement()
                self.state_management.append(temp_model.from_map(k1))

        self.tool_call = []
        if m.get('tool_call') is not None:
            for k1 in m.get('tool_call'):
                temp_model = main_models.TypedAIAssetRecognitionEvidenceToolCall()
                self.tool_call.append(temp_model.from_map(k1))

        return self

class TypedAIAssetRecognitionEvidenceToolCall(DaraModel):
    def __init__(
        self,
        content: str = None,
        source_path: str = None,
    ):
        # The collected declaration text related to the recognition basis. This is currently used mainly for agent_declaration, and other recognition evidence may not return content. This should not be interpreted as an actual execution log.
        self.content = content
        # The local file or configuration path where the recognition evidence is located. This is used to display and locate static clues, and is not a server-side downloadable URL.
        self.source_path = source_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.source_path is not None:
            result['source_path'] = self.source_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('source_path') is not None:
            self.source_path = m.get('source_path')

        return self

class TypedAIAssetRecognitionEvidenceStateManagement(DaraModel):
    def __init__(
        self,
        content: str = None,
        source_path: str = None,
    ):
        # The collected declaration text related to the recognition basis. This is currently used mainly for agent_declaration, and other recognition evidence may not return content. This should not be interpreted as an actual execution log.
        self.content = content
        # The local file or configuration path where the recognition evidence is located. This is used to display and locate static clues, and is not a server-side downloadable URL.
        self.source_path = source_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.source_path is not None:
            result['source_path'] = self.source_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('source_path') is not None:
            self.source_path = m.get('source_path')

        return self

class TypedAIAssetRecognitionEvidenceModelCall(DaraModel):
    def __init__(
        self,
        content: str = None,
        source_path: str = None,
    ):
        # The collected declaration text related to the recognition basis. This is currently used mainly for agent_declaration, and other recognition evidence may not return content. This should not be interpreted as an actual execution log.
        self.content = content
        # The local file or configuration path where the recognition evidence is located. This is used to display and locate static clues, and is not a server-side downloadable URL.
        self.source_path = source_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.source_path is not None:
            result['source_path'] = self.source_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('source_path') is not None:
            self.source_path = m.get('source_path')

        return self

class TypedAIAssetRecognitionEvidenceAutonomousExecution(DaraModel):
    def __init__(
        self,
        content: str = None,
        source_path: str = None,
    ):
        # The collected declaration text related to the recognition basis. This is currently used mainly for agent_declaration, and other recognition evidence may not return content. This should not be interpreted as an actual execution log.
        self.content = content
        # The local file or configuration path where the recognition evidence is located. This is used to display and locate static clues, and is not a server-side downloadable URL.
        self.source_path = source_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.source_path is not None:
            result['source_path'] = self.source_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('source_path') is not None:
            self.source_path = m.get('source_path')

        return self

class TypedAIAssetRecognitionEvidenceAgentDeclaration(DaraModel):
    def __init__(
        self,
        content: str = None,
        source_path: str = None,
    ):
        # The collected declaration text related to the recognition basis. This is currently used mainly for agent_declaration, and other recognition evidence may not return content. This should not be interpreted as an actual execution log.
        self.content = content
        # The local file or configuration path where the recognition evidence is located. This is used to display and locate static clues, and is not a server-side downloadable URL.
        self.source_path = source_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.source_path is not None:
            result['source_path'] = self.source_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('source_path') is not None:
            self.source_path = m.get('source_path')

        return self

class TypedAIAssetIdentityIdentifiers(DaraModel):
    def __init__(
        self,
        desktop_manifest_name: List[str] = None,
        jetbrains_plugin_id: List[str] = None,
        macos_bundle_id: List[str] = None,
        npm_package: List[str] = None,
        pe_product_identity: List[main_models.TypedAIAssetIdentityIdentifiersPeProductIdentity] = None,
        pypi_package: List[str] = None,
        vscode_extension_id: List[str] = None,
        windows_appx_identity: List[main_models.TypedAIAssetIdentityIdentifiersWindowsAppxIdentity] = None,
        windows_package_family_name: List[str] = None,
    ):
        # The array of application names declared in desktop application manifests.
        self.desktop_manifest_name = desktop_manifest_name
        # The array of plugin IDs declared in JetBrains plugin manifests.
        self.jetbrains_plugin_id = jetbrains_plugin_id
        # The array of macOS application bundle identifiers. These describe collected product identity clues and do not indicate that signatures are verified.
        self.macos_bundle_id = macos_bundle_id
        # The array of npm package names. Scoped packages retain the @scope/name format.
        self.npm_package = npm_package
        # The array of product name and company name combinations in Windows PE version resources. These are not file hashes or verified signature identities.
        self.pe_product_identity = pe_product_identity
        # The array of Python package distribution names. These are used for product identity identification and are not a list of import module names.
        self.pypi_package = pypi_package
        # The array of VS Code extension identifiers. Each is typically the publisher name and extension name connected by a dot.
        self.vscode_extension_id = vscode_extension_id
        # The array of Windows AppX/MSIX manifest identities. Each item provides both the package name and publisher. This does not indicate that the publisher signature is verified.
        self.windows_appx_identity = windows_appx_identity
        # The array of Windows application package family names. Each includes the package name and publisher identifier suffix and is not the application installation path.
        self.windows_package_family_name = windows_package_family_name

    def validate(self):
        if self.pe_product_identity:
            for v1 in self.pe_product_identity:
                 if v1:
                    v1.validate()
        if self.windows_appx_identity:
            for v1 in self.windows_appx_identity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_manifest_name is not None:
            result['desktop_manifest_name'] = self.desktop_manifest_name

        if self.jetbrains_plugin_id is not None:
            result['jetbrains_plugin_id'] = self.jetbrains_plugin_id

        if self.macos_bundle_id is not None:
            result['macos_bundle_id'] = self.macos_bundle_id

        if self.npm_package is not None:
            result['npm_package'] = self.npm_package

        result['pe_product_identity'] = []
        if self.pe_product_identity is not None:
            for k1 in self.pe_product_identity:
                result['pe_product_identity'].append(k1.to_map() if k1 else None)

        if self.pypi_package is not None:
            result['pypi_package'] = self.pypi_package

        if self.vscode_extension_id is not None:
            result['vscode_extension_id'] = self.vscode_extension_id

        result['windows_appx_identity'] = []
        if self.windows_appx_identity is not None:
            for k1 in self.windows_appx_identity:
                result['windows_appx_identity'].append(k1.to_map() if k1 else None)

        if self.windows_package_family_name is not None:
            result['windows_package_family_name'] = self.windows_package_family_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desktop_manifest_name') is not None:
            self.desktop_manifest_name = m.get('desktop_manifest_name')

        if m.get('jetbrains_plugin_id') is not None:
            self.jetbrains_plugin_id = m.get('jetbrains_plugin_id')

        if m.get('macos_bundle_id') is not None:
            self.macos_bundle_id = m.get('macos_bundle_id')

        if m.get('npm_package') is not None:
            self.npm_package = m.get('npm_package')

        self.pe_product_identity = []
        if m.get('pe_product_identity') is not None:
            for k1 in m.get('pe_product_identity'):
                temp_model = main_models.TypedAIAssetIdentityIdentifiersPeProductIdentity()
                self.pe_product_identity.append(temp_model.from_map(k1))

        if m.get('pypi_package') is not None:
            self.pypi_package = m.get('pypi_package')

        if m.get('vscode_extension_id') is not None:
            self.vscode_extension_id = m.get('vscode_extension_id')

        self.windows_appx_identity = []
        if m.get('windows_appx_identity') is not None:
            for k1 in m.get('windows_appx_identity'):
                temp_model = main_models.TypedAIAssetIdentityIdentifiersWindowsAppxIdentity()
                self.windows_appx_identity.append(temp_model.from_map(k1))

        if m.get('windows_package_family_name') is not None:
            self.windows_package_family_name = m.get('windows_package_family_name')

        return self

class TypedAIAssetIdentityIdentifiersWindowsAppxIdentity(DaraModel):
    def __init__(
        self,
        name: str = None,
        publisher: str = None,
    ):
        # The original package name of the Identity.Name in a Windows AppX/MSIX manifest.
        self.name = name
        # The publisher string of the Identity.Publisher in a Windows AppX/MSIX manifest. This is not equivalent to the signature verification result.
        self.publisher = publisher

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.publisher is not None:
            result['publisher'] = self.publisher

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('publisher') is not None:
            self.publisher = m.get('publisher')

        return self

class TypedAIAssetIdentityIdentifiersPeProductIdentity(DaraModel):
    def __init__(
        self,
        company_name: str = None,
        product_name: str = None,
    ):
        # The CompanyName field in a Windows PE version resource. This is not a certified vendor identity.
        self.company_name = company_name
        # The ProductName field in a Windows PE version resource.
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_name is not None:
            result['company_name'] = self.company_name

        if self.product_name is not None:
            result['product_name'] = self.product_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('company_name') is not None:
            self.company_name = m.get('company_name')

        if m.get('product_name') is not None:
            self.product_name = m.get('product_name')

        return self

