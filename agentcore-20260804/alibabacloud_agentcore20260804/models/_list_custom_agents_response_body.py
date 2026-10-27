# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListCustomAgentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListCustomAgentsResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The request result code. The value is SUCCESS when the request is successful.
        self.code = code
        # The HTTP status code of the current request. The value is 200 when the request is successful.
        self.http_status_code = http_status_code
        # The list of custom agent summaries on the current page. To query the complete configuration and the execution result of the latest version, call the GetCustomAgent operation.
        self.items = items
        # The maximum number of results returned per page for the current query.
        self.max_results = max_results
        # The message that describes the processing result of the request. The value is success if the request succeeds.
        self.message = message
        # The opaque token used to query the next page. An empty value indicates that no more pages exist. Pass this token as is in subsequent requests.
        self.next_token = next_token
        # The unique identifier of the request, used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was processed successfully. A value of true indicates success. A successful creation, update, or deletion does not mean that the background operation is complete.
        self.success = success
        # The total number of custom agents that meet the query conditions in the specified workspace.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListCustomAgentsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListCustomAgentsResponseBodyItems(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        artifact: main_models.ListCustomAgentsResponseBodyItemsArtifact = None,
        code_package_info: main_models.ListCustomAgentsResponseBodyItemsCodePackageInfo = None,
        create_mode: str = None,
        created_at: str = None,
        deploy_type: str = None,
        description: str = None,
        latest_spec_version: int = None,
        name: str = None,
        protocol: List[main_models.ListCustomAgentsResponseBodyItemsProtocol] = None,
        runtime: str = None,
        status: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The unique identifier of the custom agent. You can obtain this ID from the response of the CreateCustomAgent or ListCustomAgents operation.
        self.agent_id = agent_id
        # The agent artifact.
        self.artifact = artifact
        # The currently saved code package information.
        self.code_package_info = code_package_info
        # The creation method of the agent. The value is CUSTOM for custom agents.
        self.create_mode = create_mode
        # The time when the agent was created. The time is in ISO 8601 format. The trailing Z indicates the UTC time zone. Fractional seconds may be included.
        self.created_at = created_at
        # The deployment method of the agent. Custom agents are deployed and managed by the platform. The value is MANAGED for custom agents.
        self.deploy_type = deploy_type
        # The description of the agent\\"s purpose.
        self.description = description
        # The latest configuration version number. Updates with the same configuration may retain the original version number. This field does not indicate that the configuration has taken effect.
        self.latest_spec_version = latest_spec_version
        # The name of the custom agent.
        self.name = name
        # The list of invocation protocol configurations for the agent.
        self.protocol = protocol
        # The compute specifications of the agent. Valid values: INTERACTIVE, STANDARD, and HEAVY.
        self.runtime = runtime
        # The overall status of the agent. Valid values: Creating, Running, Failed, Updating, Deleting, and Deleted. To query the execution progress of the latest configuration, call the GetCustomAgent operation.
        self.status = status
        # The time when the agent was last updated. The time is in ISO 8601 format. The trailing Z indicates the UTC time zone. Fractional seconds may be included.
        self.updated_at = updated_at
        # The ID of the workspace to which the custom agent belongs.
        self.workspace_id = workspace_id

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.code_package_info:
            self.code_package_info.validate()
        if self.protocol:
            for v1 in self.protocol:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()

        if self.code_package_info is not None:
            result['codePackageInfo'] = self.code_package_info.to_map()

        if self.create_mode is not None:
            result['createMode'] = self.create_mode

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.deploy_type is not None:
            result['deployType'] = self.deploy_type

        if self.description is not None:
            result['description'] = self.description

        if self.latest_spec_version is not None:
            result['latestSpecVersion'] = self.latest_spec_version

        if self.name is not None:
            result['name'] = self.name

        result['protocol'] = []
        if self.protocol is not None:
            for k1 in self.protocol:
                result['protocol'].append(k1.to_map() if k1 else None)

        if self.runtime is not None:
            result['runtime'] = self.runtime

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('artifact') is not None:
            temp_model = main_models.ListCustomAgentsResponseBodyItemsArtifact()
            self.artifact = temp_model.from_map(m.get('artifact'))

        if m.get('codePackageInfo') is not None:
            temp_model = main_models.ListCustomAgentsResponseBodyItemsCodePackageInfo()
            self.code_package_info = temp_model.from_map(m.get('codePackageInfo'))

        if m.get('createMode') is not None:
            self.create_mode = m.get('createMode')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('deployType') is not None:
            self.deploy_type = m.get('deployType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('latestSpecVersion') is not None:
            self.latest_spec_version = m.get('latestSpecVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.protocol = []
        if m.get('protocol') is not None:
            for k1 in m.get('protocol'):
                temp_model = main_models.ListCustomAgentsResponseBodyItemsProtocol()
                self.protocol.append(temp_model.from_map(k1))

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListCustomAgentsResponseBodyItemsProtocol(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        paths: List[main_models.ListCustomAgentsResponseBodyItemsProtocolPaths] = None,
        type: str = None,
    ):
        # The request header configuration for the current protocol. The key is the header name and the value is a string.
        self.headers = headers
        # The list of API paths corresponding to the current protocol.
        self.paths = paths
        # The invoke Protocol Type. Valid values: agui (AG-UI protocol), openai-chat-completion (OpenAI Chat Completions compatible protocol), and custom (custom protocol).
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.paths:
            for v1 in self.paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        result['paths'] = []
        if self.paths is not None:
            for k1 in self.paths:
                result['paths'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        self.paths = []
        if m.get('paths') is not None:
            for k1 in m.get('paths'):
                temp_model = main_models.ListCustomAgentsResponseBodyItemsProtocolPaths()
                self.paths.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListCustomAgentsResponseBodyItemsProtocolPaths(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # The purpose description of the current API path.
        self.description = description
        # The API path corresponding to the current protocol.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListCustomAgentsResponseBodyItemsCodePackageInfo(DaraModel):
    def __init__(
        self,
        crc_64: str = None,
        etag: str = None,
        file_name: str = None,
        file_size: int = None,
        format: str = None,
    ):
        # The CRC64 value of the code package object.
        self.crc_64 = crc_64
        # The ETag of the code package object.
        self.etag = etag
        # The original file name of the code package.
        self.file_name = file_name
        # The compressed size of the code package.
        self.file_size = file_size
        # The format of the code package.
        self.format = format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crc_64 is not None:
            result['crc64'] = self.crc_64

        if self.etag is not None:
            result['etag'] = self.etag

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.format is not None:
            result['format'] = self.format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crc64') is not None:
            self.crc_64 = m.get('crc64')

        if m.get('etag') is not None:
            self.etag = m.get('etag')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('format') is not None:
            self.format = m.get('format')

        return self

class ListCustomAgentsResponseBodyItemsArtifact(DaraModel):
    def __init__(
        self,
        code: main_models.ListCustomAgentsResponseBodyItemsArtifactCode = None,
        container: main_models.ListCustomAgentsResponseBodyItemsArtifactContainer = None,
        port: int = None,
    ):
        # The code package deployment configuration. This parameter is mutually exclusive with container. The code package uses the ZIP or TAR.GZ format. Dependencies are packaged by the user. The platform does not install dependencies or perform online builds.
        self.code = code
        # The container image deployment configuration.
        self.container = container
        # The listening port of the agent service.
        # 
        # This parameter is required.
        self.port = port

    def validate(self):
        if self.code:
            self.code.validate()
        if self.container:
            self.container.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code.to_map()

        if self.container is not None:
            result['container'] = self.container.to_map()

        if self.port is not None:
            result['port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            temp_model = main_models.ListCustomAgentsResponseBodyItemsArtifactCode()
            self.code = temp_model.from_map(m.get('code'))

        if m.get('container') is not None:
            temp_model = main_models.ListCustomAgentsResponseBodyItemsArtifactContainer()
            self.container = temp_model.from_map(m.get('container'))

        if m.get('port') is not None:
            self.port = m.get('port')

        return self

class ListCustomAgentsResponseBodyItemsArtifactContainer(DaraModel):
    def __init__(
        self,
        entrypoint: str = None,
        instance_id: str = None,
        namespace: str = None,
        repo: str = None,
        tag: str = None,
        type: str = None,
    ):
        # The custom container startup command and parameters. If this parameter is not configured, the default startup method of the image is used.
        self.entrypoint = entrypoint
        # The ID of the Container Registry Enterprise instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The namespace of the Container Registry instance.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The name of the Container Registry image repository.
        # 
        # This parameter is required.
        self.repo = repo
        # The tag of the image.
        # 
        # This parameter is required.
        self.tag = tag
        # The source type of the container image.
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
        if self.entrypoint is not None:
            result['entrypoint'] = self.entrypoint

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.repo is not None:
            result['repo'] = self.repo

        if self.tag is not None:
            result['tag'] = self.tag

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entrypoint') is not None:
            self.entrypoint = m.get('entrypoint')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('repo') is not None:
            self.repo = m.get('repo')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListCustomAgentsResponseBodyItemsArtifactCode(DaraModel):
    def __init__(
        self,
        entrypoint: str = None,
        language_runtime: str = None,
        source_uri: str = None,
    ):
        # The startup command for the code package. This parameter is required in code package mode. The working directory is the root directory of the extracted code, which is /code. Example: python main.py. Quotes and escape characters are supported. Environment variables, pipes, and logical operations are not automatically expanded. For complex commands, use a script within the package.
        # 
        # This parameter is required.
        self.entrypoint = entrypoint
        # The identifier of the code runtime environment in the currently saved configuration. The runtime image uses a saved snapshot. Adding a new version to the directory does not automatically change the existing configuration.
        # 
        # This parameter is required.
        self.language_runtime = language_runtime
        # The fixed oss:// address of the platform code package referenced by the currently saved configuration. This address does not include the signature parameters of the source HTTPS link. You can use this address to reuse an existing code package. To download the content, call the GetAgentCodePackageDownloadUrl operation.
        # 
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entrypoint is not None:
            result['entrypoint'] = self.entrypoint

        if self.language_runtime is not None:
            result['languageRuntime'] = self.language_runtime

        if self.source_uri is not None:
            result['sourceUri'] = self.source_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entrypoint') is not None:
            self.entrypoint = m.get('entrypoint')

        if m.get('languageRuntime') is not None:
            self.language_runtime = m.get('languageRuntime')

        if m.get('sourceUri') is not None:
            self.source_uri = m.get('sourceUri')

        return self

