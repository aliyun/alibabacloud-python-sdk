# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class Checkout(TeaModel):
    def __init__(
        self,
        ref: str = None,
        remote: str = None,
    ):
        self.ref = ref
        self.remote = remote

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ref is not None:
            result['ref'] = self.ref
        if self.remote is not None:
            result['remote'] = self.remote
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ref') is not None:
            self.ref = m.get('ref')
        if m.get('remote') is not None:
            self.remote = m.get('remote')
        return self


class CodeupEventPayload(TeaModel):
    def __init__(
        self,
        original_payload: bytes = None,
    ):
        self.original_payload = original_payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_payload is not None:
            result['originalPayload'] = self.original_payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalPayload') is not None:
            self.original_payload = m.get('originalPayload')
        return self


class Condition(TeaModel):
    def __init__(
        self,
        expression: str = None,
    ):
        self.expression = expression

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['expression'] = self.expression
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expression') is not None:
            self.expression = m.get('expression')
        return self


class GitAccount(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        uri: str = None,
    ):
        self.avatar = avatar
        self.display_name = display_name
        self.id = id
        self.name = name
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class GitLabConfig(TeaModel):
    def __init__(
        self,
        token: str = None,
        uri: str = None,
    ):
        self.token = token
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['token'] = self.token
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class ConnectionSpec(TeaModel):
    def __init__(
        self,
        account: GitAccount = None,
        gitlab_config: GitLabConfig = None,
        platform: str = None,
    ):
        self.account = account
        self.gitlab_config = gitlab_config
        # This parameter is required.
        self.platform = platform

    def validate(self):
        if self.account:
            self.account.validate()
        if self.gitlab_config:
            self.gitlab_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['account'] = self.account.to_map()
        if self.gitlab_config is not None:
            result['gitlabConfig'] = self.gitlab_config.to_map()
        if self.platform is not None:
            result['platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account') is not None:
            temp_model = GitAccount()
            self.account = temp_model.from_map(m['account'])
        if m.get('gitlabConfig') is not None:
            temp_model = GitLabConfig()
            self.gitlab_config = temp_model.from_map(m['gitlabConfig'])
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        return self


class Installation(TeaModel):
    def __init__(
        self,
        action_uri: str = None,
        message: str = None,
        stage: str = None,
    ):
        self.action_uri = action_uri
        self.message = message
        self.stage = stage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_uri is not None:
            result['actionUri'] = self.action_uri
        if self.message is not None:
            result['message'] = self.message
        if self.stage is not None:
            result['stage'] = self.stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionUri') is not None:
            self.action_uri = m.get('actionUri')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('stage') is not None:
            self.stage = m.get('stage')
        return self


class ConnectionStatus(TeaModel):
    def __init__(
        self,
        installation: Installation = None,
    ):
        self.installation = installation

    def validate(self):
        if self.installation:
            self.installation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.installation is not None:
            result['installation'] = self.installation.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('installation') is not None:
            temp_model = Installation()
            self.installation = temp_model.from_map(m['installation'])
        return self


class Connection(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        resource_version: int = None,
        spec: ConnectionSpec = None,
        status: ConnectionStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.resource_version = resource_version
        # This parameter is required.
        self.spec = spec
        self.status = status
        self.uid = uid

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = ConnectionSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = ConnectionStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class Context(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ContextSchema(TeaModel):
    def __init__(
        self,
        description: str = None,
        hint: str = None,
        name: str = None,
        required: bool = None,
        type: str = None,
    ):
        self.description = description
        self.hint = hint
        self.name = name
        self.required = required
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.hint is not None:
            result['hint'] = self.hint
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('hint') is not None:
            self.hint = m.get('hint')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InfraStackSpecTemplateSpec(TeaModel):
    def __init__(
        self,
        content: str = None,
        engine: str = None,
    ):
        self.content = content
        self.engine = engine

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.engine is not None:
            result['engine'] = self.engine
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        return self


class InfraStackSpec(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        role_arn: str = None,
        template_name: str = None,
        template_spec: InfraStackSpecTemplateSpec = None,
        template_variables: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        self.role_arn = role_arn
        self.template_name = template_name
        self.template_spec = template_spec
        self.template_variables = template_variables

    def validate(self):
        if self.template_spec:
            self.template_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionID'] = self.region_id
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.template_spec is not None:
            result['templateSpec'] = self.template_spec.to_map()
        if self.template_variables is not None:
            result['templateVariables'] = self.template_variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionID') is not None:
            self.region_id = m.get('regionID')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('templateSpec') is not None:
            temp_model = InfraStackSpecTemplateSpec()
            self.template_spec = temp_model.from_map(m['templateSpec'])
        if m.get('templateVariables') is not None:
            self.template_variables = m.get('templateVariables')
        return self


class RepositoryConfig(TeaModel):
    def __init__(
        self,
        branch_name: str = None,
        manifest: str = None,
        repository_name: str = None,
    ):
        # This parameter is required.
        self.branch_name = branch_name
        self.manifest = manifest
        # This parameter is required.
        self.repository_name = repository_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_name is not None:
            result['branchName'] = self.branch_name
        if self.manifest is not None:
            result['manifest'] = self.manifest
        if self.repository_name is not None:
            result['repositoryName'] = self.repository_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branchName') is not None:
            self.branch_name = m.get('branchName')
        if m.get('manifest') is not None:
            self.manifest = m.get('manifest')
        if m.get('repositoryName') is not None:
            self.repository_name = m.get('repositoryName')
        return self


class TemplateConfig(TeaModel):
    def __init__(
        self,
        parameters: Dict[str, Any] = None,
        template_name: str = None,
    ):
        self.parameters = parameters
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.template_name is not None:
            result['templateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        return self


class EnvironmentSpecServiceOverlay(TeaModel):
    def __init__(
        self,
        components: Dict[str, Any] = None,
        resources: Dict[str, Any] = None,
    ):
        self.components = components
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.components is not None:
            result['components'] = self.components
        if self.resources is not None:
            result['resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('components') is not None:
            self.components = m.get('components')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        return self


class EnvironmentSpec(TeaModel):
    def __init__(
        self,
        alias: str = None,
        infra_stack_config: InfraStackSpec = None,
        is_auto_deploy: bool = None,
        repository_config: RepositoryConfig = None,
        role_arn: str = None,
        service_overlay: EnvironmentSpecServiceOverlay = None,
        template_config: TemplateConfig = None,
        type: str = None,
    ):
        self.alias = alias
        self.infra_stack_config = infra_stack_config
        self.is_auto_deploy = is_auto_deploy
        self.repository_config = repository_config
        self.role_arn = role_arn
        self.service_overlay = service_overlay
        self.template_config = template_config
        self.type = type

    def validate(self):
        if self.infra_stack_config:
            self.infra_stack_config.validate()
        if self.repository_config:
            self.repository_config.validate()
        if self.service_overlay:
            self.service_overlay.validate()
        if self.template_config:
            self.template_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.infra_stack_config is not None:
            result['infraStackConfig'] = self.infra_stack_config.to_map()
        if self.is_auto_deploy is not None:
            result['isAutoDeploy'] = self.is_auto_deploy
        if self.repository_config is not None:
            result['repositoryConfig'] = self.repository_config.to_map()
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.service_overlay is not None:
            result['serviceOverlay'] = self.service_overlay.to_map()
        if self.template_config is not None:
            result['templateConfig'] = self.template_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('infraStackConfig') is not None:
            temp_model = InfraStackSpec()
            self.infra_stack_config = temp_model.from_map(m['infraStackConfig'])
        if m.get('isAutoDeploy') is not None:
            self.is_auto_deploy = m.get('isAutoDeploy')
        if m.get('repositoryConfig') is not None:
            temp_model = RepositoryConfig()
            self.repository_config = temp_model.from_map(m['repositoryConfig'])
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('serviceOverlay') is not None:
            temp_model = EnvironmentSpecServiceOverlay()
            self.service_overlay = temp_model.from_map(m['serviceOverlay'])
        if m.get('templateConfig') is not None:
            temp_model = TemplateConfig()
            self.template_config = temp_model.from_map(m['templateConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ResourceDriftChange(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        after: Any = None,
        before: Any = None,
    ):
        self.actions = actions
        self.after = after
        self.before = before

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.after is not None:
            result['after'] = self.after
        if self.before is not None:
            result['before'] = self.before
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('after') is not None:
            self.after = m.get('after')
        if m.get('before') is not None:
            self.before = m.get('before')
        return self


class ResourceDrift(TeaModel):
    def __init__(
        self,
        address: str = None,
        change: ResourceDriftChange = None,
        mode: str = None,
        name: str = None,
        type: str = None,
    ):
        self.address = address
        self.change = change
        self.mode = mode
        self.name = name
        self.type = type

    def validate(self):
        if self.change:
            self.change.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.change is not None:
            result['change'] = self.change.to_map()
        if self.mode is not None:
            result['mode'] = self.mode
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('change') is not None:
            temp_model = ResourceDriftChange()
            self.change = temp_model.from_map(m['change'])
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ResourceDetail(TeaModel):
    def __init__(
        self,
        address: str = None,
        attribute_values: Dict[str, Any] = None,
        mode: str = None,
        name: str = None,
        type: str = None,
    ):
        self.address = address
        self.attribute_values = attribute_values
        self.mode = mode
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.attribute_values is not None:
            result['attributeValues'] = self.attribute_values
        if self.mode is not None:
            result['mode'] = self.mode
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('attributeValues') is not None:
            self.attribute_values = m.get('attributeValues')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InfraStackResourceState(TeaModel):
    def __init__(
        self,
        resource_drifts: List[ResourceDrift] = None,
        resources: List[ResourceDetail] = None,
    ):
        self.resource_drifts = resource_drifts
        self.resources = resources

    def validate(self):
        if self.resource_drifts:
            for k in self.resource_drifts:
                if k:
                    k.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['resourceDrifts'] = []
        if self.resource_drifts is not None:
            for k in self.resource_drifts:
                result['resourceDrifts'].append(k.to_map() if k else None)
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_drifts = []
        if m.get('resourceDrifts') is not None:
            for k in m.get('resourceDrifts'):
                temp_model = ResourceDrift()
                self.resource_drifts.append(temp_model.from_map(k))
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = ResourceDetail()
                self.resources.append(temp_model.from_map(k))
        return self


class TerraformOutputValue(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sensitive: bool = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
        self.sensitive = sensitive

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.sensitive is not None:
            result['sensitive'] = self.sensitive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')
        return self


class TerraformInputVariable(TeaModel):
    def __init__(
        self,
        default_json: str = None,
        description: str = None,
        name: str = None,
        nullable: bool = None,
        sensitive: bool = None,
        type: str = None,
    ):
        self.default_json = default_json
        self.description = description
        # This parameter is required.
        self.name = name
        self.nullable = nullable
        self.sensitive = sensitive
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_json is not None:
            result['defaultJson'] = self.default_json
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.nullable is not None:
            result['nullable'] = self.nullable
        if self.sensitive is not None:
            result['sensitive'] = self.sensitive
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultJson') is not None:
            self.default_json = m.get('defaultJson')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InfraStackStatusTemplateStatus(TeaModel):
    def __init__(
        self,
        outputs: List[TerraformOutputValue] = None,
        variables: List[TerraformInputVariable] = None,
    ):
        # This parameter is required.
        self.outputs = outputs
        # This parameter is required.
        self.variables = variables

    def validate(self):
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['outputs'].append(k.to_map() if k else None)
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outputs = []
        if m.get('outputs') is not None:
            for k in m.get('outputs'):
                temp_model = TerraformOutputValue()
                self.outputs.append(temp_model.from_map(k))
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = TerraformInputVariable()
                self.variables.append(temp_model.from_map(k))
        return self


class InfraStackStatus(TeaModel):
    def __init__(
        self,
        message: str = None,
        observed_generation: int = None,
        observed_time: str = None,
        phase: str = None,
        resource_state: InfraStackResourceState = None,
        template_outputs: Dict[str, Any] = None,
        template_status: InfraStackStatusTemplateStatus = None,
    ):
        self.message = message
        self.observed_generation = observed_generation
        self.observed_time = observed_time
        self.phase = phase
        self.resource_state = resource_state
        self.template_outputs = template_outputs
        self.template_status = template_status

    def validate(self):
        if self.resource_state:
            self.resource_state.validate()
        if self.template_status:
            self.template_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.observed_time is not None:
            result['observedTime'] = self.observed_time
        if self.phase is not None:
            result['phase'] = self.phase
        if self.resource_state is not None:
            result['resourceState'] = self.resource_state.to_map()
        if self.template_outputs is not None:
            result['templateOutputs'] = self.template_outputs
        if self.template_status is not None:
            result['templateStatus'] = self.template_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('resourceState') is not None:
            temp_model = InfraStackResourceState()
            self.resource_state = temp_model.from_map(m['resourceState'])
        if m.get('templateOutputs') is not None:
            self.template_outputs = m.get('templateOutputs')
        if m.get('templateStatus') is not None:
            temp_model = InfraStackStatusTemplateStatus()
            self.template_status = temp_model.from_map(m['templateStatus'])
        return self


class GitEventSnapshot(TeaModel):
    def __init__(
        self,
        branch: str = None,
        commit_id: str = None,
        tag: str = None,
    ):
        self.branch = branch
        self.commit_id = commit_id
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch
        if self.commit_id is not None:
            result['commitID'] = self.commit_id
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commitID') is not None:
            self.commit_id = m.get('commitID')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class TaskExecError(TeaModel):
    def __init__(
        self,
        code: str = None,
        extra_info: str = None,
        message: str = None,
        request_id: str = None,
        title: str = None,
    ):
        self.code = code
        self.extra_info = extra_info
        self.message = message
        self.request_id = request_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class RepositorySpec(TeaModel):
    def __init__(
        self,
        clone_url: str = None,
        connection_name: str = None,
        display_name: str = None,
        id: int = None,
        owner: str = None,
        platform: str = None,
        web_url: str = None,
    ):
        # This parameter is required.
        self.clone_url = clone_url
        # This parameter is required.
        self.connection_name = connection_name
        self.display_name = display_name
        self.id = id
        self.owner = owner
        self.platform = platform
        self.web_url = web_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clone_url is not None:
            result['cloneUrl'] = self.clone_url
        if self.connection_name is not None:
            result['connectionName'] = self.connection_name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.owner is not None:
            result['owner'] = self.owner
        if self.platform is not None:
            result['platform'] = self.platform
        if self.web_url is not None:
            result['webUrl'] = self.web_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloneUrl') is not None:
            self.clone_url = m.get('cloneUrl')
        if m.get('connectionName') is not None:
            self.connection_name = m.get('connectionName')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('webUrl') is not None:
            self.web_url = m.get('webUrl')
        return self


class ReleaseDetail(TeaModel):
    def __init__(
        self,
        biz_status: str = None,
        env_name: str = None,
        finished_time: str = None,
        git_event_snapshot: GitEventSnapshot = None,
        latest_task_exec_error: TaskExecError = None,
        message: str = None,
        pipeline_name: str = None,
        pipeline_trigger_event_name: str = None,
        release_outputs: Dict[str, Any] = None,
        repository_snapshot: RepositorySpec = None,
        template_config_snapshot: TemplateConfig = None,
    ):
        self.biz_status = biz_status
        self.env_name = env_name
        self.finished_time = finished_time
        self.git_event_snapshot = git_event_snapshot
        self.latest_task_exec_error = latest_task_exec_error
        self.message = message
        self.pipeline_name = pipeline_name
        self.pipeline_trigger_event_name = pipeline_trigger_event_name
        self.release_outputs = release_outputs
        self.repository_snapshot = repository_snapshot
        self.template_config_snapshot = template_config_snapshot

    def validate(self):
        if self.git_event_snapshot:
            self.git_event_snapshot.validate()
        if self.latest_task_exec_error:
            self.latest_task_exec_error.validate()
        if self.repository_snapshot:
            self.repository_snapshot.validate()
        if self.template_config_snapshot:
            self.template_config_snapshot.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_status is not None:
            result['bizStatus'] = self.biz_status
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.git_event_snapshot is not None:
            result['gitEventSnapshot'] = self.git_event_snapshot.to_map()
        if self.latest_task_exec_error is not None:
            result['latestTaskExecError'] = self.latest_task_exec_error.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name
        if self.pipeline_trigger_event_name is not None:
            result['pipelineTriggerEventName'] = self.pipeline_trigger_event_name
        if self.release_outputs is not None:
            result['releaseOutputs'] = self.release_outputs
        if self.repository_snapshot is not None:
            result['repositorySnapshot'] = self.repository_snapshot.to_map()
        if self.template_config_snapshot is not None:
            result['templateConfigSnapshot'] = self.template_config_snapshot.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizStatus') is not None:
            self.biz_status = m.get('bizStatus')
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('gitEventSnapshot') is not None:
            temp_model = GitEventSnapshot()
            self.git_event_snapshot = temp_model.from_map(m['gitEventSnapshot'])
        if m.get('latestTaskExecError') is not None:
            temp_model = TaskExecError()
            self.latest_task_exec_error = temp_model.from_map(m['latestTaskExecError'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')
        if m.get('pipelineTriggerEventName') is not None:
            self.pipeline_trigger_event_name = m.get('pipelineTriggerEventName')
        if m.get('releaseOutputs') is not None:
            self.release_outputs = m.get('releaseOutputs')
        if m.get('repositorySnapshot') is not None:
            temp_model = RepositorySpec()
            self.repository_snapshot = temp_model.from_map(m['repositorySnapshot'])
        if m.get('templateConfigSnapshot') is not None:
            temp_model = TemplateConfig()
            self.template_config_snapshot = temp_model.from_map(m['templateConfigSnapshot'])
        return self


class EnvironmentStatus(TeaModel):
    def __init__(
        self,
        infra_stack_status: InfraStackStatus = None,
        latest_release_detail: ReleaseDetail = None,
        observed_generation: int = None,
        observed_time: str = None,
    ):
        self.infra_stack_status = infra_stack_status
        self.latest_release_detail = latest_release_detail
        self.observed_generation = observed_generation
        self.observed_time = observed_time

    def validate(self):
        if self.infra_stack_status:
            self.infra_stack_status.validate()
        if self.latest_release_detail:
            self.latest_release_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.infra_stack_status is not None:
            result['infraStackStatus'] = self.infra_stack_status.to_map()
        if self.latest_release_detail is not None:
            result['latestReleaseDetail'] = self.latest_release_detail.to_map()
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.observed_time is not None:
            result['observedTime'] = self.observed_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('infraStackStatus') is not None:
            temp_model = InfraStackStatus()
            self.infra_stack_status = temp_model.from_map(m['infraStackStatus'])
        if m.get('latestReleaseDetail') is not None:
            temp_model = ReleaseDetail()
            self.latest_release_detail = temp_model.from_map(m['latestReleaseDetail'])
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        return self


class Environment(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        project_name: str = None,
        resource_version: int = None,
        spec: EnvironmentSpec = None,
        status: EnvironmentStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.project_name = project_name
        self.resource_version = resource_version
        # This parameter is required.
        self.spec = spec
        self.status = status
        self.uid = uid

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = EnvironmentSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = EnvironmentStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class PullRequestFilter(TeaModel):
    def __init__(
        self,
        source_branch: str = None,
        target_branch: str = None,
        types: List[str] = None,
    ):
        self.source_branch = source_branch
        self.target_branch = target_branch
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_branch is not None:
            result['sourceBranch'] = self.source_branch
        if self.target_branch is not None:
            result['targetBranch'] = self.target_branch
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceBranch') is not None:
            self.source_branch = m.get('sourceBranch')
        if m.get('targetBranch') is not None:
            self.target_branch = m.get('targetBranch')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class PushFilter(TeaModel):
    def __init__(
        self,
        branch: str = None,
        tag: str = None,
    ):
        self.branch = branch
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class EventFilterConfig(TeaModel):
    def __init__(
        self,
        pull_request: PullRequestFilter = None,
        push: PushFilter = None,
    ):
        self.pull_request = pull_request
        self.push = push

    def validate(self):
        if self.pull_request:
            self.pull_request.validate()
        if self.push:
            self.push.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_request is not None:
            result['pullRequest'] = self.pull_request.to_map()
        if self.push is not None:
            result['push'] = self.push.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullRequest') is not None:
            temp_model = PullRequestFilter()
            self.pull_request = temp_model.from_map(m['pullRequest'])
        if m.get('push') is not None:
            temp_model = PushFilter()
            self.push = temp_model.from_map(m['push'])
        return self


class GiteeEventPayload(TeaModel):
    def __init__(
        self,
        original_payload: bytes = None,
    ):
        self.original_payload = original_payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_payload is not None:
            result['originalPayload'] = self.original_payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalPayload') is not None:
            self.original_payload = m.get('originalPayload')
        return self


class GithubEventPayload(TeaModel):
    def __init__(
        self,
        original_payload: bytes = None,
    ):
        self.original_payload = original_payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_payload is not None:
            result['originalPayload'] = self.original_payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalPayload') is not None:
            self.original_payload = m.get('originalPayload')
        return self


class GitlabEventPayload(TeaModel):
    def __init__(
        self,
        original_payload: bytes = None,
    ):
        self.original_payload = original_payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_payload is not None:
            result['originalPayload'] = self.original_payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalPayload') is not None:
            self.original_payload = m.get('originalPayload')
        return self


class ManualEventPayload(TeaModel):
    def __init__(
        self,
        branch: str = None,
        commit_id: str = None,
        tag: str = None,
        template_config: TemplateConfig = None,
    ):
        self.branch = branch
        self.commit_id = commit_id
        self.tag = tag
        self.template_config = template_config

    def validate(self):
        if self.template_config:
            self.template_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch
        if self.commit_id is not None:
            result['commitID'] = self.commit_id
        if self.tag is not None:
            result['tag'] = self.tag
        if self.template_config is not None:
            result['templateConfig'] = self.template_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commitID') is not None:
            self.commit_id = m.get('commitID')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('templateConfig') is not None:
            temp_model = TemplateConfig()
            self.template_config = temp_model.from_map(m['templateConfig'])
        return self


class EventPayload(TeaModel):
    def __init__(
        self,
        codeup: CodeupEventPayload = None,
        gitee: GiteeEventPayload = None,
        github: GithubEventPayload = None,
        gitlab: GitlabEventPayload = None,
        manual: ManualEventPayload = None,
    ):
        self.codeup = codeup
        self.gitee = gitee
        self.github = github
        self.gitlab = gitlab
        self.manual = manual

    def validate(self):
        if self.codeup:
            self.codeup.validate()
        if self.gitee:
            self.gitee.validate()
        if self.github:
            self.github.validate()
        if self.gitlab:
            self.gitlab.validate()
        if self.manual:
            self.manual.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codeup is not None:
            result['codeup'] = self.codeup.to_map()
        if self.gitee is not None:
            result['gitee'] = self.gitee.to_map()
        if self.github is not None:
            result['github'] = self.github.to_map()
        if self.gitlab is not None:
            result['gitlab'] = self.gitlab.to_map()
        if self.manual is not None:
            result['manual'] = self.manual.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeup') is not None:
            temp_model = CodeupEventPayload()
            self.codeup = temp_model.from_map(m['codeup'])
        if m.get('gitee') is not None:
            temp_model = GiteeEventPayload()
            self.gitee = temp_model.from_map(m['gitee'])
        if m.get('github') is not None:
            temp_model = GithubEventPayload()
            self.github = temp_model.from_map(m['github'])
        if m.get('gitlab') is not None:
            temp_model = GitlabEventPayload()
            self.gitlab = temp_model.from_map(m['gitlab'])
        if m.get('manual') is not None:
            temp_model = ManualEventPayload()
            self.manual = temp_model.from_map(m['manual'])
        return self


class OAuthCredential(TeaModel):
    def __init__(
        self,
        created_time: int = None,
        expiration: int = None,
        refresh_token: str = None,
        scope: str = None,
        token: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.created_time = created_time
        # This parameter is required.
        self.expiration = expiration
        self.refresh_token = refresh_token
        self.scope = scope
        # This parameter is required.
        self.token = token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.refresh_token is not None:
            result['refreshToken'] = self.refresh_token
        if self.scope is not None:
            result['scope'] = self.scope
        if self.token is not None:
            result['token'] = self.token
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('refreshToken') is not None:
            self.refresh_token = m.get('refreshToken')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RunAfter(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class TaskExec(TeaModel):
    def __init__(
        self,
        context: Context = None,
        name: str = None,
        run_afters: List[RunAfter] = None,
        task_template: str = None,
    ):
        self.context = context
        self.name = name
        self.run_afters = run_afters
        self.task_template = task_template

    def validate(self):
        if self.context:
            self.context.validate()
        if self.run_afters:
            for k in self.run_afters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.name is not None:
            result['name'] = self.name
        result['runAfters'] = []
        if self.run_afters is not None:
            for k in self.run_afters:
                result['runAfters'].append(k.to_map() if k else None)
        if self.task_template is not None:
            result['taskTemplate'] = self.task_template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = Context()
            self.context = temp_model.from_map(m['context'])
        if m.get('name') is not None:
            self.name = m.get('name')
        self.run_afters = []
        if m.get('runAfters') is not None:
            for k in m.get('runAfters'):
                temp_model = RunAfter()
                self.run_afters.append(temp_model.from_map(k))
        if m.get('taskTemplate') is not None:
            self.task_template = m.get('taskTemplate')
        return self


class PipelineTemplateSpec(TeaModel):
    def __init__(
        self,
        context: Context = None,
        tasks: List[TaskExec] = None,
    ):
        self.context = context
        self.tasks = tasks

    def validate(self):
        if self.context:
            self.context.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = Context()
            self.context = temp_model.from_map(m['context'])
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = TaskExec()
                self.tasks.append(temp_model.from_map(k))
        return self


class PipelineSpec(TeaModel):
    def __init__(
        self,
        context: Context = None,
        template_name: str = None,
        template_spec: PipelineTemplateSpec = None,
    ):
        self.context = context
        self.template_name = template_name
        self.template_spec = template_spec

    def validate(self):
        if self.context:
            self.context.validate()
        if self.template_spec:
            self.template_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.template_spec is not None:
            result['templateSpec'] = self.template_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = Context()
            self.context = temp_model.from_map(m['context'])
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('templateSpec') is not None:
            temp_model = PipelineTemplateSpec()
            self.template_spec = temp_model.from_map(m['templateSpec'])
        return self


class PipelineStatus(TeaModel):
    def __init__(
        self,
        latest_exec_error: TaskExecError = None,
        phase: str = None,
    ):
        self.latest_exec_error = latest_exec_error
        self.phase = phase

    def validate(self):
        if self.latest_exec_error:
            self.latest_exec_error.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latest_exec_error is not None:
            result['latestExecError'] = self.latest_exec_error.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latestExecError') is not None:
            temp_model = TaskExecError()
            self.latest_exec_error = temp_model.from_map(m['latestExecError'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class Pipeline(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        deletion_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        resource_version: int = None,
        spec: PipelineSpec = None,
        status: PipelineStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.deletion_time = deletion_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.resource_version = resource_version
        self.spec = spec
        self.status = status
        self.uid = uid

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = PipelineSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = PipelineStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class PipelineTemplate(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        deletion_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        resource_version: int = None,
        spec: PipelineTemplateSpec = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.deletion_time = deletion_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.resource_version = resource_version
        self.spec = spec
        self.uid = uid

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = PipelineTemplateSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class Variable(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class RunPipelineConfig(TeaModel):
    def __init__(
        self,
        pipeline_spec: PipelineSpec = None,
        variables: List[Variable] = None,
        yaml_file_content: str = None,
        yaml_file_path: str = None,
    ):
        self.pipeline_spec = pipeline_spec
        self.variables = variables
        self.yaml_file_content = yaml_file_content
        self.yaml_file_path = yaml_file_path

    def validate(self):
        if self.pipeline_spec:
            self.pipeline_spec.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_spec is not None:
            result['pipelineSpec'] = self.pipeline_spec.to_map()
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        if self.yaml_file_content is not None:
            result['yamlFileContent'] = self.yaml_file_content
        if self.yaml_file_path is not None:
            result['yamlFilePath'] = self.yaml_file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pipelineSpec') is not None:
            temp_model = PipelineSpec()
            self.pipeline_spec = temp_model.from_map(m['pipelineSpec'])
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = Variable()
                self.variables.append(temp_model.from_map(k))
        if m.get('yamlFileContent') is not None:
            self.yaml_file_content = m.get('yamlFileContent')
        if m.get('yamlFilePath') is not None:
            self.yaml_file_path = m.get('yamlFilePath')
        return self


class PipelineTriggerSpec(TeaModel):
    def __init__(
        self,
        event_filter: EventFilterConfig = None,
        role_arn: str = None,
        run_pipeline: RunPipelineConfig = None,
    ):
        # This parameter is required.
        self.event_filter = event_filter
        self.role_arn = role_arn
        self.run_pipeline = run_pipeline

    def validate(self):
        if self.event_filter:
            self.event_filter.validate()
        if self.run_pipeline:
            self.run_pipeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_filter is not None:
            result['eventFilter'] = self.event_filter.to_map()
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.run_pipeline is not None:
            result['runPipeline'] = self.run_pipeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventFilter') is not None:
            temp_model = EventFilterConfig()
            self.event_filter = temp_model.from_map(m['eventFilter'])
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('runPipeline') is not None:
            temp_model = RunPipelineConfig()
            self.run_pipeline = temp_model.from_map(m['runPipeline'])
        return self


class PipelineTrigger(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        deletion_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        project_name: str = None,
        resource_version: int = None,
        spec: PipelineTriggerSpec = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.deletion_time = deletion_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_name = project_name
        self.resource_version = resource_version
        self.spec = spec
        self.uid = uid

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = PipelineTriggerSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class PipelineTriggerEventSpec(TeaModel):
    def __init__(
        self,
        payload: EventPayload = None,
        trigger_name: str = None,
    ):
        self.payload = payload
        self.trigger_name = trigger_name

    def validate(self):
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload is not None:
            result['payload'] = self.payload.to_map()
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('payload') is not None:
            temp_model = EventPayload()
            self.payload = temp_model.from_map(m['payload'])
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        return self


class PipelineTriggerEventStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        fired_pipeline_name: str = None,
        release_detail: ReleaseDetail = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.fired_pipeline_name = fired_pipeline_name
        self.release_detail = release_detail
        self.status = status

    def validate(self):
        if self.release_detail:
            self.release_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.fired_pipeline_name is not None:
            result['firedPipelineName'] = self.fired_pipeline_name
        if self.release_detail is not None:
            result['releaseDetail'] = self.release_detail.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('firedPipelineName') is not None:
            self.fired_pipeline_name = m.get('firedPipelineName')
        if m.get('releaseDetail') is not None:
            temp_model = ReleaseDetail()
            self.release_detail = temp_model.from_map(m['releaseDetail'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class PipelineTriggerEvent(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        deletion_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        resource_version: int = None,
        spec: PipelineTriggerEventSpec = None,
        status: PipelineTriggerEventStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.deletion_time = deletion_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.resource_version = resource_version
        self.spec = spec
        self.status = status
        self.uid = uid

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = PipelineTriggerEventSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = PipelineTriggerEventStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ProjectSpec(TeaModel):
    def __init__(
        self,
        role_arn: str = None,
        template_config: TemplateConfig = None,
        token: str = None,
    ):
        self.role_arn = role_arn
        self.template_config = template_config
        self.token = token

    def validate(self):
        if self.template_config:
            self.template_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.template_config is not None:
            result['templateConfig'] = self.template_config.to_map()
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('templateConfig') is not None:
            temp_model = TemplateConfig()
            self.template_config = temp_model.from_map(m['templateConfig'])
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class ProjectStatus(TeaModel):
    def __init__(
        self,
        latest_release_detail: ReleaseDetail = None,
        observed_generation: int = None,
        observed_time: str = None,
    ):
        self.latest_release_detail = latest_release_detail
        self.observed_generation = observed_generation
        self.observed_time = observed_time

    def validate(self):
        if self.latest_release_detail:
            self.latest_release_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latest_release_detail is not None:
            result['latestReleaseDetail'] = self.latest_release_detail.to_map()
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.observed_time is not None:
            result['observedTime'] = self.observed_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latestReleaseDetail') is not None:
            temp_model = ReleaseDetail()
            self.latest_release_detail = temp_model.from_map(m['latestReleaseDetail'])
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        return self


class Project(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        resource_version: int = None,
        spec: ProjectSpec = None,
        status: ProjectStatus = None,
        uid: str = None,
        updated_time: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.resource_version = resource_version
        self.spec = spec
        self.status = status
        self.uid = uid
        self.updated_time = updated_time

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = ProjectSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = ProjectStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self


class Repository(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        resource_version: int = None,
        spec: RepositorySpec = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.resource_version = resource_version
        # This parameter is required.
        self.spec = spec
        self.uid = uid

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = RepositorySpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ServiceSpec(TeaModel):
    def __init__(
        self,
        environment: str = None,
        role_arn: str = None,
        template: str = None,
        template_variables: Dict[str, Any] = None,
        template_version: int = None,
    ):
        # This parameter is required.
        self.environment = environment
        self.role_arn = role_arn
        # This parameter is required.
        self.template = template
        # This parameter is required.
        self.template_variables = template_variables
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['environment'] = self.environment
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.template is not None:
            result['template'] = self.template
        if self.template_variables is not None:
            result['templateVariables'] = self.template_variables
        if self.template_version is not None:
            result['templateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environment') is not None:
            self.environment = m.get('environment')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('templateVariables') is not None:
            self.template_variables = m.get('templateVariables')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        return self


class TaskSpec(TeaModel):
    def __init__(
        self,
        context: Context = None,
        template_name: str = None,
    ):
        self.context = context
        self.template_name = template_name

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.template_name is not None:
            result['templateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = Context()
            self.context = temp_model.from_map(m['context'])
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        return self


class TaskInvocation(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        invocation_id: str = None,
        invocation_target: str = None,
        output: str = None,
        request_id: str = None,
        sls_log_store: str = None,
        sls_project: str = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.invocation_id = invocation_id
        self.invocation_target = invocation_target
        self.output = output
        self.request_id = request_id
        self.sls_log_store = sls_log_store
        self.sls_project = sls_project
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceID'] = self.instance_id
        if self.invocation_id is not None:
            result['invocationID'] = self.invocation_id
        if self.invocation_target is not None:
            result['invocationTarget'] = self.invocation_target
        if self.output is not None:
            result['output'] = self.output
        if self.request_id is not None:
            result['requestID'] = self.request_id
        if self.sls_log_store is not None:
            result['slsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['slsProject'] = self.sls_project
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')
        if m.get('invocationID') is not None:
            self.invocation_id = m.get('invocationID')
        if m.get('invocationTarget') is not None:
            self.invocation_target = m.get('invocationTarget')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        if m.get('slsLogStore') is not None:
            self.sls_log_store = m.get('slsLogStore')
        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class TaskStatus(TeaModel):
    def __init__(
        self,
        execution_details: List[str] = None,
        invocations: List[TaskInvocation] = None,
        latest_exec_error: TaskExecError = None,
        phase: str = None,
        status_generation: int = None,
    ):
        self.execution_details = execution_details
        self.invocations = invocations
        self.latest_exec_error = latest_exec_error
        self.phase = phase
        self.status_generation = status_generation

    def validate(self):
        if self.invocations:
            for k in self.invocations:
                if k:
                    k.validate()
        if self.latest_exec_error:
            self.latest_exec_error.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_details is not None:
            result['executionDetails'] = self.execution_details
        result['invocations'] = []
        if self.invocations is not None:
            for k in self.invocations:
                result['invocations'].append(k.to_map() if k else None)
        if self.latest_exec_error is not None:
            result['latestExecError'] = self.latest_exec_error.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.status_generation is not None:
            result['statusGeneration'] = self.status_generation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executionDetails') is not None:
            self.execution_details = m.get('executionDetails')
        self.invocations = []
        if m.get('invocations') is not None:
            for k in m.get('invocations'):
                temp_model = TaskInvocation()
                self.invocations.append(temp_model.from_map(k))
        if m.get('latestExecError') is not None:
            temp_model = TaskExecError()
            self.latest_exec_error = temp_model.from_map(m['latestExecError'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('statusGeneration') is not None:
            self.status_generation = m.get('statusGeneration')
        return self


class Task(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        deletion_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        resource_version: int = None,
        spec: TaskSpec = None,
        status: TaskStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.deletion_time = deletion_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.resource_version = resource_version
        self.spec = spec
        self.status = status
        self.uid = uid

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = TaskSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = TaskStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class TaskWorker(TeaModel):
    def __init__(
        self,
        preset_worker: str = None,
    ):
        self.preset_worker = preset_worker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preset_worker is not None:
            result['presetWorker'] = self.preset_worker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('presetWorker') is not None:
            self.preset_worker = m.get('presetWorker')
        return self


class TaskTemplateSpec(TeaModel):
    def __init__(
        self,
        context: Context = None,
        description: str = None,
        execute_condition: Condition = None,
        worker: TaskWorker = None,
    ):
        self.context = context
        self.description = description
        self.execute_condition = execute_condition
        self.worker = worker

    def validate(self):
        if self.context:
            self.context.validate()
        if self.execute_condition:
            self.execute_condition.validate()
        if self.worker:
            self.worker.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.execute_condition is not None:
            result['executeCondition'] = self.execute_condition.to_map()
        if self.worker is not None:
            result['worker'] = self.worker.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = Context()
            self.context = temp_model.from_map(m['context'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executeCondition') is not None:
            temp_model = Condition()
            self.execute_condition = temp_model.from_map(m['executeCondition'])
        if m.get('worker') is not None:
            temp_model = TaskWorker()
            self.worker = temp_model.from_map(m['worker'])
        return self


class TaskTemplate(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        deletion_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        resource_version: int = None,
        spec: TaskTemplateSpec = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.deletion_time = deletion_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.resource_version = resource_version
        self.spec = spec
        self.uid = uid

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = TaskTemplateSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ActivateConnectionRequest(TeaModel):
    def __init__(
        self,
        account: GitAccount = None,
        credential: OAuthCredential = None,
    ):
        self.account = account
        self.credential = credential

    def validate(self):
        if self.account:
            self.account.validate()
        if self.credential:
            self.credential.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['account'] = self.account.to_map()
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account') is not None:
            temp_model = GitAccount()
            self.account = temp_model.from_map(m['account'])
        if m.get('credential') is not None:
            temp_model = OAuthCredential()
            self.credential = temp_model.from_map(m['credential'])
        return self


class ActivateConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Connection = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Connection()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Pipeline = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Task = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnectionRequest(TeaModel):
    def __init__(
        self,
        body: Connection = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Connection()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Connection = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Connection()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentRequest(TeaModel):
    def __init__(
        self,
        body: Environment = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Environment = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineRequest(TeaModel):
    def __init__(
        self,
        body: Pipeline = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Pipeline = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineTemplateRequest(TeaModel):
    def __init__(
        self,
        body: PipelineTemplate = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PipelineTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PipelineTemplate = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineTriggerRequest(TeaModel):
    def __init__(
        self,
        body: PipelineTrigger = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PipelineTrigger()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PipelineTrigger = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTrigger()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineTriggerEventRequest(TeaModel):
    def __init__(
        self,
        body: PipelineTriggerEvent = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PipelineTriggerEvent()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineTriggerEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PipelineTriggerEvent = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTriggerEvent()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        body: Project = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Project()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Project = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Project()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryRequest(TeaModel):
    def __init__(
        self,
        body: Repository = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Repository()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Repository = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Repository()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskRequest(TeaModel):
    def __init__(
        self,
        body: Task = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Task = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskTemplateRequest(TeaModel):
    def __init__(
        self,
        body: TaskTemplate = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TaskTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TaskTemplate = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TaskTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnectionRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
    ):
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class DeleteConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeletePipelineTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeletePipelineTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePipelineTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePipelineTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePipelineTriggerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeletePipelineTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePipelineTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePipelineTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePipelineTriggerEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeletePipelineTriggerEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePipelineTriggerEventResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePipelineTriggerEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
    ):
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTaskTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteTaskTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTaskTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTaskTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchConnectionCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OAuthCredential = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OAuthCredential()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchRepositoryCheckoutRequest(TeaModel):
    def __init__(
        self,
        branch: str = None,
        commit: str = None,
        tag: str = None,
    ):
        self.branch = branch
        self.commit = commit
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch
        if self.commit is not None:
            result['commit'] = self.commit
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commit') is not None:
            self.commit = m.get('commit')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class FetchRepositoryCheckoutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Checkout = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Checkout()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Connection = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Connection()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Environment = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Pipeline = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PipelineTemplate = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PipelineTrigger = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTrigger()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineTriggerEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PipelineTriggerEvent = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTriggerEvent()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Project = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Project()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Repository = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Repository()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Task = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TaskTemplate = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TaskTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector = label_selector
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListConnectionsShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector_shrink = label_selector_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Connection] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Connection()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConnectionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector = label_selector
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnvironmentsShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector_shrink = label_selector_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnvironmentsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Environment] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Environment()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnvironmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineTemplatesRequest(TeaModel):
    def __init__(
        self,
        label_selector: List[str] = None,
    ):
        self.label_selector = label_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListPipelineTemplatesShrinkRequest(TeaModel):
    def __init__(
        self,
        label_selector_shrink: str = None,
    ):
        self.label_selector_shrink = label_selector_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        return self


class ListPipelineTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[PipelineTemplate] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = PipelineTemplate()
                self.body.append(temp_model.from_map(k))
        return self


class ListPipelineTriggerEventsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector = label_selector
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListPipelineTriggerEventsShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector_shrink = label_selector_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListPipelineTriggerEventsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[PipelineTriggerEvent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = PipelineTriggerEvent()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListPipelineTriggerEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPipelineTriggerEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPipelineTriggerEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineTriggersRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector = label_selector
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListPipelineTriggersShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector_shrink = label_selector_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListPipelineTriggersResponseBody(TeaModel):
    def __init__(
        self,
        data: List[PipelineTrigger] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = PipelineTrigger()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListPipelineTriggersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPipelineTriggersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPipelineTriggersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelinesRequest(TeaModel):
    def __init__(
        self,
        label_selector: List[str] = None,
    ):
        self.label_selector = label_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListPipelinesShrinkRequest(TeaModel):
    def __init__(
        self,
        label_selector_shrink: str = None,
    ):
        self.label_selector_shrink = label_selector_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        return self


class ListPipelinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[Pipeline] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Pipeline()
                self.body.append(temp_model.from_map(k))
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector = label_selector
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListProjectsShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector_shrink = label_selector_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Project] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Project()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoriesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector = label_selector
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListRepositoriesShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        label_selector_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.label_selector_shrink = label_selector_shrink
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListRepositoriesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Repository] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Repository()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListRepositoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRepositoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskTemplatesRequest(TeaModel):
    def __init__(
        self,
        label_selector: List[str] = None,
    ):
        self.label_selector = label_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListTaskTemplatesShrinkRequest(TeaModel):
    def __init__(
        self,
        label_selector_shrink: str = None,
    ):
        self.label_selector_shrink = label_selector_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        return self


class ListTaskTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[TaskTemplate] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = TaskTemplate()
                self.body.append(temp_model.from_map(k))
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        label_selector: List[str] = None,
    ):
        self.label_selector = label_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(
        self,
        label_selector_shrink: str = None,
    ):
        self.label_selector_shrink = label_selector_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[Task] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Task()
                self.body.append(temp_model.from_map(k))
        return self


class PutEnvironmentRequest(TeaModel):
    def __init__(
        self,
        body: Environment = None,
        force: bool = None,
    ):
        self.body = body
        self.force = force

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Environment = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class PutPipelineStatusRequest(TeaModel):
    def __init__(
        self,
        body: Pipeline = None,
        force: bool = None,
    ):
        self.body = body
        self.force = force

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutPipelineStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Pipeline = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class PutPipelineTemplateRequest(TeaModel):
    def __init__(
        self,
        body: PipelineTemplate = None,
        force: bool = None,
    ):
        self.body = body
        self.force = force

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PipelineTemplate()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutPipelineTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PipelineTemplate = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class PutPipelineTriggerRequest(TeaModel):
    def __init__(
        self,
        body: PipelineTrigger = None,
        force: bool = None,
    ):
        self.body = body
        self.force = force

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PipelineTrigger()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutPipelineTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PipelineTrigger = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTrigger()
            self.body = temp_model.from_map(m['body'])
        return self


class PutProjectRequest(TeaModel):
    def __init__(
        self,
        body: Project = None,
        force: bool = None,
    ):
        self.body = body
        self.force = force

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Project()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Project = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Project()
            self.body = temp_model.from_map(m['body'])
        return self


class PutTaskStatusRequest(TeaModel):
    def __init__(
        self,
        body: Task = None,
        force: bool = None,
    ):
        self.body = body
        self.force = force

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Task = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class PutTaskTemplateRequest(TeaModel):
    def __init__(
        self,
        body: TaskTemplate = None,
        force: bool = None,
    ):
        self.body = body
        self.force = force

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TaskTemplate()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutTaskTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TaskTemplate = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TaskTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Connection = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Connection()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Task = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Task = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class StartPipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Pipeline = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Task = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentRequest(TeaModel):
    def __init__(
        self,
        body: Environment = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Environment = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelineTriggerRequest(TeaModel):
    def __init__(
        self,
        body: PipelineTrigger = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PipelineTrigger()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelineTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PipelineTrigger = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTrigger()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        body: Project = None,
        force: bool = None,
    ):
        self.body = body
        self.force = force

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Project()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Project = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Project()
            self.body = temp_model.from_map(m['body'])
        return self


