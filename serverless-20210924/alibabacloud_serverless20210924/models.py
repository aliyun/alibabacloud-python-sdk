# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class ApplicationRepoSource(TeaModel):
    def __init__(
        self,
        owner: str = None,
        provider: str = None,
        repo: str = None,
    ):
        self.owner = owner
        self.provider = provider
        self.repo = repo

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner is not None:
            result['owner'] = self.owner
        if self.provider is not None:
            result['provider'] = self.provider
        if self.repo is not None:
            result['repo'] = self.repo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('repo') is not None:
            self.repo = m.get('repo')
        return self


class ApplicationTrigger(TeaModel):
    def __init__(
        self,
        branch: str = None,
        commit: str = None,
        on: str = None,
    ):
        self.branch = branch
        self.commit = commit
        self.on = on

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
        if self.on is not None:
            result['on'] = self.on
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commit') is not None:
            self.commit = m.get('commit')
        if m.get('on') is not None:
            self.on = m.get('on')
        return self


class Application(TeaModel):
    def __init__(
        self,
        auto_deploy: str = None,
        created_time: str = None,
        description: str = None,
        env_vars: Dict[str, Any] = None,
        last_release: Dict[str, Any] = None,
        name: str = None,
        output: Dict[str, Any] = None,
        parameters: Dict[str, Any] = None,
        repo_source: ApplicationRepoSource = None,
        role_arn: str = None,
        template: str = None,
        trigger: ApplicationTrigger = None,
        updated_time: str = None,
        work_dir: str = None,
    ):
        self.auto_deploy = auto_deploy
        self.created_time = created_time
        self.description = description
        self.env_vars = env_vars
        self.last_release = last_release
        self.name = name
        self.output = output
        self.parameters = parameters
        self.repo_source = repo_source
        self.role_arn = role_arn
        self.template = template
        self.trigger = trigger
        self.updated_time = updated_time
        self.work_dir = work_dir

    def validate(self):
        if self.repo_source:
            self.repo_source.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.env_vars is not None:
            result['envVars'] = self.env_vars
        if self.last_release is not None:
            result['lastRelease'] = self.last_release
        if self.name is not None:
            result['name'] = self.name
        if self.output is not None:
            result['output'] = self.output
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.repo_source is not None:
            result['repoSource'] = self.repo_source.to_map()
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.template is not None:
            result['template'] = self.template
        if self.trigger is not None:
            result['trigger'] = self.trigger.to_map()
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        if self.work_dir is not None:
            result['workDir'] = self.work_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('envVars') is not None:
            self.env_vars = m.get('envVars')
        if m.get('lastRelease') is not None:
            self.last_release = m.get('lastRelease')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('repoSource') is not None:
            temp_model = ApplicationRepoSource()
            self.repo_source = temp_model.from_map(m['repoSource'])
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('trigger') is not None:
            temp_model = ApplicationTrigger()
            self.trigger = temp_model.from_map(m['trigger'])
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        if m.get('workDir') is not None:
            self.work_dir = m.get('workDir')
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


class EnvironmentSpec(TeaModel):
    def __init__(
        self,
        region: str = None,
        role_arn: str = None,
        template: str = None,
        template_variables: Dict[str, Any] = None,
        template_version: int = None,
    ):
        self.region = region
        self.role_arn = role_arn
        self.template = template
        self.template_variables = template_variables
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
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
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('templateVariables') is not None:
            self.template_variables = m.get('templateVariables')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        return self


class EnvironmentStatus(TeaModel):
    def __init__(
        self,
        message: str = None,
        observed_generation: int = None,
        observed_time: str = None,
        output: Dict[str, Any] = None,
        phase: str = None,
    ):
        self.message = message
        self.observed_generation = observed_generation
        self.observed_time = observed_time
        self.output = output
        self.phase = phase

    def validate(self):
        pass

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
        if self.output is not None:
            result['output'] = self.output
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class Environment(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        deletion_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        name: str = None,
        spec: EnvironmentSpec = None,
        status: EnvironmentStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.deletion_time = deletion_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.name = name
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
        if self.name is not None:
            result['name'] = self.name
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
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = EnvironmentSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = EnvironmentStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class EnvironmentRevision(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        environment_generation: int = None,
        environment_name: str = None,
        kind: str = None,
        spec: EnvironmentSpec = None,
        status: EnvironmentStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.environment_generation = environment_generation
        self.environment_name = environment_name
        self.kind = kind
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
        if self.environment_generation is not None:
            result['environmentGeneration'] = self.environment_generation
        if self.environment_name is not None:
            result['environmentName'] = self.environment_name
        if self.kind is not None:
            result['kind'] = self.kind
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
        if m.get('environmentGeneration') is not None:
            self.environment_generation = m.get('environmentGeneration')
        if m.get('environmentName') is not None:
            self.environment_name = m.get('environmentName')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('spec') is not None:
            temp_model = EnvironmentSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = EnvironmentStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class InputVariable(TeaModel):
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


class OutputValue(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sensitive: bool = None,
    ):
        self.description = description
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


class PipelineSpec(TeaModel):
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


class PipelineStatus(TeaModel):
    def __init__(
        self,
        phase: str = None,
    ):
        self.phase = phase

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        context_schema: Dict[str, Any] = None,
        tasks: List[TaskExec] = None,
    ):
        self.context = context
        self.context_schema = context_schema
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
        if self.context_schema is not None:
            result['contextSchema'] = self.context_schema
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
        if m.get('contextSchema') is not None:
            self.context_schema = m.get('contextSchema')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = TaskExec()
                self.tasks.append(temp_model.from_map(k))
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


class ReleaseCodeVersion(TeaModel):
    def __init__(
        self,
        branch: str = None,
        commit: str = None,
    ):
        self.branch = branch
        self.commit = commit

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commit') is not None:
            self.commit = m.get('commit')
        return self


class Release(TeaModel):
    def __init__(
        self,
        app_config: Dict[str, Any] = None,
        code_version: ReleaseCodeVersion = None,
        created_time: str = None,
        description: str = None,
        output: Dict[str, Any] = None,
        status: str = None,
        version_id: int = None,
    ):
        self.app_config = app_config
        self.code_version = code_version
        self.created_time = created_time
        self.description = description
        self.output = output
        self.status = status
        self.version_id = version_id

    def validate(self):
        if self.code_version:
            self.code_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_config is not None:
            result['appConfig'] = self.app_config
        if self.code_version is not None:
            result['codeVersion'] = self.code_version.to_map()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.output is not None:
            result['output'] = self.output
        if self.status is not None:
            result['status'] = self.status
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appConfig') is not None:
            self.app_config = m.get('appConfig')
        if m.get('codeVersion') is not None:
            temp_model = ReleaseCodeVersion()
            self.code_version = temp_model.from_map(m['codeVersion'])
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class RepoSource(TeaModel):
    def __init__(
        self,
        owner: str = None,
        provider: str = None,
        repo: str = None,
    ):
        self.owner = owner
        self.provider = provider
        self.repo = repo

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner is not None:
            result['owner'] = self.owner
        if self.provider is not None:
            result['provider'] = self.provider
        if self.repo is not None:
            result['repo'] = self.repo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('repo') is not None:
            self.repo = m.get('repo')
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
        self.environment = environment
        self.role_arn = role_arn
        self.template = template
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


class ServiceStatus(TeaModel):
    def __init__(
        self,
        message: str = None,
        observed_generation: int = None,
        observed_time: str = None,
        output: Dict[str, Any] = None,
        phase: str = None,
    ):
        self.message = message
        self.observed_generation = observed_generation
        self.observed_time = observed_time
        self.output = output
        self.phase = phase

    def validate(self):
        pass

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
        if self.output is not None:
            result['output'] = self.output
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class Service(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        deletion_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        name: str = None,
        spec: ServiceSpec = None,
        status: ServiceStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.deletion_time = deletion_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.name = name
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
        if self.name is not None:
            result['name'] = self.name
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
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = ServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = ServiceStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ServiceRevision(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        kind: str = None,
        service_generation: int = None,
        service_name: str = None,
        spec: ServiceSpec = None,
        status: EnvironmentStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.kind = kind
        self.service_generation = service_generation
        self.service_name = service_name
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
        if self.kind is not None:
            result['kind'] = self.kind
        if self.service_generation is not None:
            result['serviceGeneration'] = self.service_generation
        if self.service_name is not None:
            result['serviceName'] = self.service_name
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
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('serviceGeneration') is not None:
            self.service_generation = m.get('serviceGeneration')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('spec') is not None:
            temp_model = ServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = EnvironmentStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class Status(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
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
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StsCredentials(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        expiration_time: str = None,
        kind: str = None,
        secret_access_key: str = None,
        token: str = None,
    ):
        self.access_key_id = access_key_id
        self.expiration_time = expiration_time
        self.kind = kind
        self.secret_access_key = secret_access_key
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        if self.kind is not None:
            result['kind'] = self.kind
        if self.secret_access_key is not None:
            result['secretAccessKey'] = self.secret_access_key
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('secretAccessKey') is not None:
            self.secret_access_key = m.get('secretAccessKey')
        if m.get('token') is not None:
            self.token = m.get('token')
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


class TaskStatus(TeaModel):
    def __init__(
        self,
        execution_details: List[str] = None,
        phase: str = None,
        status_generation: int = None,
    ):
        self.execution_details = execution_details
        self.phase = phase
        self.status_generation = status_generation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_details is not None:
            result['executionDetails'] = self.execution_details
        if self.phase is not None:
            result['phase'] = self.phase
        if self.status_generation is not None:
            result['statusGeneration'] = self.status_generation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executionDetails') is not None:
            self.execution_details = m.get('executionDetails')
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
        context_schema: Dict[str, Any] = None,
        description: str = None,
        execute_condition: Condition = None,
        worker: TaskWorker = None,
    ):
        self.context = context
        self.context_schema = context_schema
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
        if self.context_schema is not None:
            result['contextSchema'] = self.context_schema
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
        if m.get('contextSchema') is not None:
            self.context_schema = m.get('contextSchema')
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


class TemplateSpec(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        ram_policy: str = None,
        type: str = None,
    ):
        self.content = content
        self.content_type = content_type
        self.ram_policy = ram_policy
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.ram_policy is not None:
            result['ramPolicy'] = self.ram_policy
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('ramPolicy') is not None:
            self.ram_policy = m.get('ramPolicy')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class TemplateStatus(TeaModel):
    def __init__(
        self,
        message: str = None,
        observed_generation: int = None,
        observed_time: str = None,
        outputs: List[OutputValue] = None,
        phase: str = None,
        variables: List[InputVariable] = None,
    ):
        self.message = message
        self.observed_generation = observed_generation
        self.observed_time = observed_time
        self.outputs = outputs
        self.phase = phase
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
        if self.message is not None:
            result['message'] = self.message
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.observed_time is not None:
            result['observedTime'] = self.observed_time
        result['outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['outputs'].append(k.to_map() if k else None)
        if self.phase is not None:
            result['phase'] = self.phase
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        self.outputs = []
        if m.get('outputs') is not None:
            for k in m.get('outputs'):
                temp_model = OutputValue()
                self.outputs.append(temp_model.from_map(k))
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = InputVariable()
                self.variables.append(temp_model.from_map(k))
        return self


class Template(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        deletion_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        name: str = None,
        spec: TemplateSpec = None,
        status: TemplateStatus = None,
        uid: str = None,
        version: int = None,
    ):
        self.created_time = created_time
        self.deletion_time = deletion_time
        self.description = description
        self.generation = generation
        self.kind = kind
        self.name = name
        self.spec = spec
        self.status = status
        self.uid = uid
        self.version = version

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
        if self.name is not None:
            result['name'] = self.name
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
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
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = TemplateSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = TemplateStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class TemplateRevision(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        kind: str = None,
        spec: TemplateSpec = None,
        status: TemplateStatus = None,
        template_generation: int = None,
        template_name: str = None,
        template_version: int = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.kind = kind
        self.spec = spec
        self.status = status
        self.template_generation = template_generation
        self.template_name = template_name
        self.template_version = template_version
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
        if self.kind is not None:
            result['kind'] = self.kind
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.template_generation is not None:
            result['templateGeneration'] = self.template_generation
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.template_version is not None:
            result['templateVersion'] = self.template_version
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('spec') is not None:
            temp_model = TemplateSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = TemplateStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('templateGeneration') is not None:
            self.template_generation = m.get('templateGeneration')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class TriggerConfig(TeaModel):
    def __init__(
        self,
        branch: str = None,
        commit: str = None,
        on: str = None,
    ):
        self.branch = branch
        self.commit = commit
        self.on = on

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
        if self.on is not None:
            result['on'] = self.on
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commit') is not None:
            self.commit = m.get('commit')
        if m.get('on') is not None:
            self.on = m.get('on')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        auto_deploy: bool = None,
        description: str = None,
        env_vars: Dict[str, str] = None,
        name: str = None,
        parameters: Dict[str, str] = None,
        repo_source: RepoSource = None,
        role_arn: str = None,
        template: str = None,
        trigger: TriggerConfig = None,
    ):
        self.auto_deploy = auto_deploy
        self.description = description
        self.env_vars = env_vars
        self.name = name
        self.parameters = parameters
        self.repo_source = repo_source
        self.role_arn = role_arn
        self.template = template
        self.trigger = trigger

    def validate(self):
        if self.repo_source:
            self.repo_source.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy
        if self.description is not None:
            result['description'] = self.description
        if self.env_vars is not None:
            result['envVars'] = self.env_vars
        if self.name is not None:
            result['name'] = self.name
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.repo_source is not None:
            result['repoSource'] = self.repo_source.to_map()
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.template is not None:
            result['template'] = self.template
        if self.trigger is not None:
            result['trigger'] = self.trigger.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('envVars') is not None:
            self.env_vars = m.get('envVars')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('repoSource') is not None:
            temp_model = RepoSource()
            self.repo_source = temp_model.from_map(m['repoSource'])
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('trigger') is not None:
            temp_model = TriggerConfig()
            self.trigger = temp_model.from_map(m['trigger'])
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Application = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = Application()
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class CreateReleaseRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateReleaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Release = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = Release()
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: str = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        version: int = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Status = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = Status()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Application = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = Application()
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class GetReleaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Release = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = Release()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Service = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = Service()
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        version: int = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Template = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = Template()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentRevisionsRequest(TeaModel):
    def __init__(
        self,
        environment_name: str = None,
    ):
        self.environment_name = environment_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_name is not None:
            result['environmentName'] = self.environment_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentName') is not None:
            self.environment_name = m.get('environmentName')
        return self


class ListEnvironmentRevisionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[EnvironmentRevision] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
                temp_model = EnvironmentRevision()
                self.body.append(temp_model.from_map(k))
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[Environment] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
                temp_model = Environment()
                self.body.append(temp_model.from_map(k))
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListServiceRevisionsRequest(TeaModel):
    def __init__(
        self,
        service_name: str = None,
    ):
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class ListServiceRevisionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[ServiceRevision] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
                temp_model = ServiceRevision()
                self.body.append(temp_model.from_map(k))
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[Service] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
                temp_model = Service()
                self.body.append(temp_model.from_map(k))
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListTemplateRevisionsRequest(TeaModel):
    def __init__(
        self,
        template_name: str = None,
        template_version: int = None,
    ):
        self.template_name = template_name
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.template_version is not None:
            result['templateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        return self


class ListTemplateRevisionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[TemplateRevision] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
                temp_model = TemplateRevision()
                self.body.append(temp_model.from_map(k))
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[Template] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
                temp_model = Template()
                self.body.append(temp_model.from_map(k))
        return self


class PutEnvironmentRequest(TeaModel):
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class PutServiceRequest(TeaModel):
    def __init__(
        self,
        body: Service = None,
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
            temp_model = Service()
            self.body = temp_model.from_map(m['body'])
        return self


class PutServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Service = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = Service()
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class PutTemplateRequest(TeaModel):
    def __init__(
        self,
        body: Template = None,
        version: int = None,
    ):
        self.body = body
        self.version = version

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
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Template()
            self.body = temp_model.from_map(m['body'])
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class PutTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Template = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = Template()
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class UpdateApplicationRequest(TeaModel):
    def __init__(
        self,
        body: Application = None,
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
            temp_model = Application()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Application = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = Application()
            self.body = temp_model.from_map(m['body'])
        return self


