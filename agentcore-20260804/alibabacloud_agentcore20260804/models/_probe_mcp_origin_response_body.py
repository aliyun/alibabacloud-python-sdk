# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ProbeMcpOriginResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ProbeMcpOriginResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code of the API operation. SUCCESS indicates that the operation completed normally. For the origin server result, see data.status.
        self.code = code
        # The read-only, one-time, and bounded probe result. It is not persisted and is not associated with subsequently created MCPs.
        self.data = data
        # The HTTP status code of the POP API request.
        self.http_status_code = http_status_code
        # The processing result of the API operation, excluding the original response from the origin server.
        self.message = message
        # The ID used to correlate this API call.
        self.request_id = request_id
        # Indicates whether the API operation was processed successfully. This means that authorization, parameter validation, and execution mechanisms completed normally, which does not equate to a successful origin server check.
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
            temp_model = main_models.ProbeMcpOriginResponseBodyData()
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

class ProbeMcpOriginResponseBodyData(DaraModel):
    def __init__(
        self,
        coverage: main_models.ProbeMcpOriginResponseBodyDataCoverage = None,
        error: main_models.ProbeMcpOriginResponseBodyDataError = None,
        http_result: main_models.ProbeMcpOriginResponseBodyDataHttpResult = None,
        observations: List[main_models.ProbeMcpOriginResponseBodyDataObservations] = None,
        probe_id: str = None,
        probed_at: str = None,
        recommendation: main_models.ProbeMcpOriginResponseBodyDataRecommendation = None,
        selected_configuration: main_models.ProbeMcpOriginResponseBodyDataSelectedConfiguration = None,
        stage: str = None,
        status: str = None,
        tools: List[main_models.ProbeMcpOriginResponseBodyDataTools] = None,
        tools_complete: bool = None,
        tools_status: str = None,
        warnings: List[main_models.ProbeMcpOriginResponseBodyDataWarnings] = None,
    ):
        # The check coverage. It describes the target, protocol, or HTTP request conditions for this check and does not prove that the formal gateway and other APIs are available.
        self.coverage = coverage
        # Indicates origin server failures. This field is empty upon success. Origin server 401 errors or connection failures are not uniformly mapped to API exceptions.
        self.error = error
        # The HTTP check result. This is returned only for the HTTP type. The definition and actual request status are separated. This is null for direct connections. A 2xx status code only proves the success of this request and does not prove that business functions or other APIs are available.
        self.http_result = http_result
        # The declared and actual test results for controlled endpoints of a single origin server. This is an empty array for the HTTP type.
        self.observations = observations
        # The ID used only to correlate desensitized logs. It is not used for queries, authorization, binding MCPs, or reusing check evidence.
        self.probe_id = probe_id
        # The observation time in ISO 8601 UTC format.
        self.probed_at = probed_at
        # The recommended protocol combination. It only includes verified combinations that the platform can access. This is empty when no combinations are available or for the HTTP type.
        self.recommendation = recommendation
        # The combination actually used for tool queries. Specifying this does not mean verification passed. This is empty for the HTTP type.
        self.selected_configuration = selected_configuration
        # The stage of the check. Valid values: AUTHORIZE, VALIDATE, RATE_LIMIT, NETWORK, NETWORK_CONTEXT, CONNECT, DISCOVER, INITIALIZE, SESSION_CHECK, TOOLS_LIST, HTTP_DEFINITION, HTTP_REQUEST, CLEANUP, EXECUTION, or COMPLETE.
        self.stage = stage
        # The check result of the origin server. Valid values: SUCCESS, PARTIAL, or FAILED. SUCCESS indicates that the protocol check passed but no capabilities were declared or no tools capability exists. A completely empty tool list also passes. PARTIAL indicates that the tool query failed or was truncated. For HTTP, PARTIAL indicates that only the definition was checked or required evidence is unknown.
        self.status = status
        # The restricted metadata list for this check. Tools are not executed. An empty array is returned if tools are not declared, the list is completely empty, or the type is HTTP. Refer to toolsStatus and toolsComplete for judgment.
        self.tools = tools
        # Indicates whether the tool list is complete. The value is true for COMPLETE or EMPTY, and false for TRUNCATED. The value is null if not queried, not declared, or failed. Completeness cannot be determined solely by an empty array.
        self.tools_complete = tools_complete
        # The tool query status. Valid values: NOT_RUN, NOT_DECLARED, EMPTY, COMPLETE, TRUNCATED, or FAILED. If tools are not declared, the value is NOT_DECLARED and tools/list is not executed. For the HTTP type, the value is NOT_RUN.
        self.tools_status = tools_status
        # The coverage and completeness limitations of this check.
        self.warnings = warnings

    def validate(self):
        if self.coverage:
            self.coverage.validate()
        if self.error:
            self.error.validate()
        if self.http_result:
            self.http_result.validate()
        if self.observations:
            for v1 in self.observations:
                 if v1:
                    v1.validate()
        if self.recommendation:
            self.recommendation.validate()
        if self.selected_configuration:
            self.selected_configuration.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()
        if self.warnings:
            for v1 in self.warnings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coverage is not None:
            result['coverage'] = self.coverage.to_map()

        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.http_result is not None:
            result['httpResult'] = self.http_result.to_map()

        result['observations'] = []
        if self.observations is not None:
            for k1 in self.observations:
                result['observations'].append(k1.to_map() if k1 else None)

        if self.probe_id is not None:
            result['probeId'] = self.probe_id

        if self.probed_at is not None:
            result['probedAt'] = self.probed_at

        if self.recommendation is not None:
            result['recommendation'] = self.recommendation.to_map()

        if self.selected_configuration is not None:
            result['selectedConfiguration'] = self.selected_configuration.to_map()

        if self.stage is not None:
            result['stage'] = self.stage

        if self.status is not None:
            result['status'] = self.status

        result['tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['tools'].append(k1.to_map() if k1 else None)

        if self.tools_complete is not None:
            result['toolsComplete'] = self.tools_complete

        if self.tools_status is not None:
            result['toolsStatus'] = self.tools_status

        result['warnings'] = []
        if self.warnings is not None:
            for k1 in self.warnings:
                result['warnings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('coverage') is not None:
            temp_model = main_models.ProbeMcpOriginResponseBodyDataCoverage()
            self.coverage = temp_model.from_map(m.get('coverage'))

        if m.get('error') is not None:
            temp_model = main_models.ProbeMcpOriginResponseBodyDataError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('httpResult') is not None:
            temp_model = main_models.ProbeMcpOriginResponseBodyDataHttpResult()
            self.http_result = temp_model.from_map(m.get('httpResult'))

        self.observations = []
        if m.get('observations') is not None:
            for k1 in m.get('observations'):
                temp_model = main_models.ProbeMcpOriginResponseBodyDataObservations()
                self.observations.append(temp_model.from_map(k1))

        if m.get('probeId') is not None:
            self.probe_id = m.get('probeId')

        if m.get('probedAt') is not None:
            self.probed_at = m.get('probedAt')

        if m.get('recommendation') is not None:
            temp_model = main_models.ProbeMcpOriginResponseBodyDataRecommendation()
            self.recommendation = temp_model.from_map(m.get('recommendation'))

        if m.get('selectedConfiguration') is not None:
            temp_model = main_models.ProbeMcpOriginResponseBodyDataSelectedConfiguration()
            self.selected_configuration = temp_model.from_map(m.get('selectedConfiguration'))

        if m.get('stage') is not None:
            self.stage = m.get('stage')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.ProbeMcpOriginResponseBodyDataTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('toolsComplete') is not None:
            self.tools_complete = m.get('toolsComplete')

        if m.get('toolsStatus') is not None:
            self.tools_status = m.get('toolsStatus')

        self.warnings = []
        if m.get('warnings') is not None:
            for k1 in m.get('warnings'):
                temp_model = main_models.ProbeMcpOriginResponseBodyDataWarnings()
                self.warnings.append(temp_model.from_map(k1))

        return self

class ProbeMcpOriginResponseBodyDataWarnings(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The structured identifier for the detection limitation.
        self.code = code
        # Explains limitations such as UNKNOWN, not executed, or truncated. This excludes credentials and original responses.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class ProbeMcpOriginResponseBodyDataTools(DaraModel):
    def __init__(
        self,
        input_schema: str = None,
        output_schema: str = None,
        tool_description: str = None,
        tool_name: str = None,
    ):
        # The input schema defined by the protocol, represented as a JSON string.
        self.input_schema = input_schema
        # The output schema defined by the protocol, represented as a JSON string.
        self.output_schema = output_schema
        # The untrusted description text returned by the origin server. It is escaped when displayed and is not executed as an instruction.
        self.tool_description = tool_description
        # The declared name of the tool. Only metadata is displayed.
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_schema is not None:
            result['inputSchema'] = self.input_schema

        if self.output_schema is not None:
            result['outputSchema'] = self.output_schema

        if self.tool_description is not None:
            result['toolDescription'] = self.tool_description

        if self.tool_name is not None:
            result['toolName'] = self.tool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputSchema') is not None:
            self.input_schema = m.get('inputSchema')

        if m.get('outputSchema') is not None:
            self.output_schema = m.get('outputSchema')

        if m.get('toolDescription') is not None:
            self.tool_description = m.get('toolDescription')

        if m.get('toolName') is not None:
            self.tool_name = m.get('toolName')

        return self

class ProbeMcpOriginResponseBodyDataSelectedConfiguration(DaraModel):
    def __init__(
        self,
        backend_mcp_protocol: str = None,
        origin_protocol_version: str = None,
        protocol: str = None,
    ):
        # The backend MCP protocol policy. Valid values: legacy or modern.
        self.backend_mcp_protocol = backend_mcp_protocol
        # The actual negotiated or selected and verified origin server MCP date version in YYYY-MM-DD format. This is null when not confirmed. It only displays the origin server protocol date metadata. It can be specified during creation and modified during updates. If omitted during an update, the current value is retained. It does not control backend requests or the external protocol of the gateway.
        self.origin_protocol_version = origin_protocol_version
        # The protocol. Valid values: SSE or StreamableHTTP. The modern policy is only combined with StreamableHTTP.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_mcp_protocol is not None:
            result['backendMcpProtocol'] = self.backend_mcp_protocol

        if self.origin_protocol_version is not None:
            result['originProtocolVersion'] = self.origin_protocol_version

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendMcpProtocol') is not None:
            self.backend_mcp_protocol = m.get('backendMcpProtocol')

        if m.get('originProtocolVersion') is not None:
            self.origin_protocol_version = m.get('originProtocolVersion')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class ProbeMcpOriginResponseBodyDataRecommendation(DaraModel):
    def __init__(
        self,
        backend_mcp_protocol: str = None,
        origin_protocol_version: str = None,
        protocol: str = None,
    ):
        # The backend MCP protocol policy. Valid values: legacy or modern.
        self.backend_mcp_protocol = backend_mcp_protocol
        # The actual negotiated or selected and verified origin server MCP date version in YYYY-MM-DD format. This is null when not confirmed. It only displays the origin server protocol date metadata. It can be specified during creation and modified during updates. If omitted during an update, the current value is retained. It does not control backend requests or the external protocol of the gateway.
        self.origin_protocol_version = origin_protocol_version
        # The protocol. Valid values: SSE or StreamableHTTP. The modern policy is only combined with StreamableHTTP.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_mcp_protocol is not None:
            result['backendMcpProtocol'] = self.backend_mcp_protocol

        if self.origin_protocol_version is not None:
            result['originProtocolVersion'] = self.origin_protocol_version

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendMcpProtocol') is not None:
            self.backend_mcp_protocol = m.get('backendMcpProtocol')

        if m.get('originProtocolVersion') is not None:
            self.origin_protocol_version = m.get('originProtocolVersion')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class ProbeMcpOriginResponseBodyDataObservations(DaraModel):
    def __init__(
        self,
        backend_mcp_protocol: str = None,
        declared: bool = None,
        declared_versions: List[str] = None,
        endpoint: str = None,
        negotiated_version: str = None,
        protocol: str = None,
        session_mode: str = None,
        verification_status: str = None,
    ):
        # The backend MCP protocol policy. Valid values: legacy or modern.
        self.backend_mcp_protocol = backend_mcp_protocol
        # Indicates whether the origin server declares support for this combination. This is empty when there is no declaration evidence.
        self.declared = declared
        # The list of declared versions. It retains only the date versions actually declared by the origin server and does not infer the full set from a single negotiation.
        self.declared_versions = declared_versions
        # The desensitized origin server or controlled subsequent endpoint. Sensitive query parameters are not returned.
        self.endpoint = endpoint
        # The negotiated version. For legacy, it is the negotiated version. For modern, it is the selected and verified date version. This is empty when not confirmed.
        self.negotiated_version = negotiated_version
        # The protocol. Valid values: SSE or StreamableHTTP. The modern policy is only combined with StreamableHTTP.
        self.protocol = protocol
        # The session mode. Valid values: STATEFUL, STATELESS, NOT_APPLICABLE, or UNKNOWN. A direct legacy connection without a session is not automatically judged as failed.
        self.session_mode = session_mode
        # The protocol verification status. Valid values: VERIFIED, UNSUPPORTED, FAILED, or UNKNOWN. UNSUPPORTED requires protocol evidence.
        self.verification_status = verification_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_mcp_protocol is not None:
            result['backendMcpProtocol'] = self.backend_mcp_protocol

        if self.declared is not None:
            result['declared'] = self.declared

        if self.declared_versions is not None:
            result['declaredVersions'] = self.declared_versions

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.negotiated_version is not None:
            result['negotiatedVersion'] = self.negotiated_version

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.session_mode is not None:
            result['sessionMode'] = self.session_mode

        if self.verification_status is not None:
            result['verificationStatus'] = self.verification_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendMcpProtocol') is not None:
            self.backend_mcp_protocol = m.get('backendMcpProtocol')

        if m.get('declared') is not None:
            self.declared = m.get('declared')

        if m.get('declaredVersions') is not None:
            self.declared_versions = m.get('declaredVersions')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('negotiatedVersion') is not None:
            self.negotiated_version = m.get('negotiatedVersion')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('sessionMode') is not None:
            self.session_mode = m.get('sessionMode')

        if m.get('verificationStatus') is not None:
            self.verification_status = m.get('verificationStatus')

        return self

class ProbeMcpOriginResponseBodyDataHttpResult(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        definition_status: str = None,
        http_status_code: int = None,
    ):
        # The connection status of the target. Valid values: PASSED, FAILED, NOT_RUN, or UNKNOWN. This is judged only based on the actual target connection evidence for this check.
        self.connection_status = connection_status
        # The check result of the API definition. Valid values: PASSED, FAILED, or NOT_RUN. The value is NOT_RUN when no OpenAPI specification is available.
        self.definition_status = definition_status
        # The actual HTTP status code received. This is empty if the request was not executed or no response was received.
        self.http_status_code = http_status_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['connectionStatus'] = self.connection_status

        if self.definition_status is not None:
            result['definitionStatus'] = self.definition_status

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectionStatus') is not None:
            self.connection_status = m.get('connectionStatus')

        if m.get('definitionStatus') is not None:
            self.definition_status = m.get('definitionStatus')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        return self

class ProbeMcpOriginResponseBodyDataError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        retryable: bool = None,
        source: str = None,
        stage: str = None,
    ):
        # Returns only bounded diagnostic codes. The original error body from the origin server is not returned.
        self.code = code
        # The trimmed and redacted diagnostic information. This excludes credentials or original responses.
        self.message = message
        # Indicates whether the operation is suitable for retry under a restricted policy. This does not trigger automatic retries.
        self.retryable = retryable
        # The error source, which can be MAGIC, ROUTER, NETWORK, ORIGIN, or UNKNOWN. This is determined solely based on actual evidence.
        self.source = source
        # The detection or publishing stage where the error occurred.
        self.stage = stage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.retryable is not None:
            result['retryable'] = self.retryable

        if self.source is not None:
            result['source'] = self.source

        if self.stage is not None:
            result['stage'] = self.stage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryable') is not None:
            self.retryable = m.get('retryable')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('stage') is not None:
            self.stage = m.get('stage')

        return self

class ProbeMcpOriginResponseBodyDataCoverage(DaraModel):
    def __init__(
        self,
        backend_mcp_protocol: str = None,
        header_names: List[str] = None,
        method: str = None,
        path: str = None,
        protocol: str = None,
        target: str = None,
        via_gateway: bool = None,
    ):
        # The evidence-verified legacy or modern protocol. This field is empty during HTTP interface checks.
        self.backend_mcp_protocol = backend_mcp_protocol
        # Returns only non-sensitive names and excludes internal platform routing or network identities.
        self.header_names = header_names
        # The selected HTTP method for this check. This field is empty for direct connections.
        self.method = method
        # The redacted summary of the selected HTTP path for this check. This field is empty for direct connections.
        self.path = path
        # The evidence-verified MCP transport. This field is empty during HTTP interface checks.
        self.protocol = protocol
        # The summary of the origin server target for this check. It does not contain sensitive query parameters or credentials.
        self.target = target
        # The origin server check before creation is fixed to false, which does not indicate that the resource is ready.
        self.via_gateway = via_gateway

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_mcp_protocol is not None:
            result['backendMcpProtocol'] = self.backend_mcp_protocol

        if self.header_names is not None:
            result['headerNames'] = self.header_names

        if self.method is not None:
            result['method'] = self.method

        if self.path is not None:
            result['path'] = self.path

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.target is not None:
            result['target'] = self.target

        if self.via_gateway is not None:
            result['viaGateway'] = self.via_gateway

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendMcpProtocol') is not None:
            self.backend_mcp_protocol = m.get('backendMcpProtocol')

        if m.get('headerNames') is not None:
            self.header_names = m.get('headerNames')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('viaGateway') is not None:
            self.via_gateway = m.get('viaGateway')

        return self

