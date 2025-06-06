# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class ArtifactSpec(TeaModel):
    def __init__(
        self,
        runtime: str = None,
        type: str = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.runtime = runtime
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.type is not None:
            result['type'] = self.type
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class ArtifactStatus(TeaModel):
    def __init__(
        self,
        arn: str = None,
        checksum: str = None,
        size: int = None,
    ):
        self.arn = arn
        self.checksum = checksum
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['arn'] = self.arn
        if self.checksum is not None:
            result['checksum'] = self.checksum
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class Artifact(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        resource_version: int = None,
        spec: ArtifactSpec = None,
        status: ArtifactStatus = None,
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
            temp_model = ArtifactSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = ArtifactStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self


class ArtifactCode(TeaModel):
    def __init__(
        self,
        checksum: str = None,
        url: str = None,
    ):
        self.checksum = checksum
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['checksum'] = self.checksum
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ArtifactMeta(TeaModel):
    def __init__(
        self,
        checksum: str = None,
        name: str = None,
    ):
        self.checksum = checksum
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['checksum'] = self.checksum
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ArtifactTempBucketTokenCredentials(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        return self


class ArtifactTempBucketToken(TeaModel):
    def __init__(
        self,
        credentials: ArtifactTempBucketTokenCredentials = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        oss_region: str = None,
    ):
        self.credentials = credentials
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.oss_region = oss_region

    def validate(self):
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credentials is not None:
            result['credentials'] = self.credentials.to_map()
        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name
        if self.oss_region is not None:
            result['ossRegion'] = self.oss_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentials') is not None:
            temp_model = ArtifactTempBucketTokenCredentials()
            self.credentials = temp_model.from_map(m['credentials'])
        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')
        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')
        if m.get('ossRegion') is not None:
            self.oss_region = m.get('ossRegion')
        return self


class BranchFilter(TeaModel):
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


class BuildCacheConfig(TeaModel):
    def __init__(
        self,
        key_path: Dict[str, Any] = None,
        paths: List[str] = None,
    ):
        self.key_path = key_path
        self.paths = paths

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_path is not None:
            result['keyPath'] = self.key_path
        if self.paths is not None:
            result['paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyPath') is not None:
            self.key_path = m.get('keyPath')
        if m.get('paths') is not None:
            self.paths = m.get('paths')
        return self


class DefaultBuilderConfig(TeaModel):
    def __init__(
        self,
        cache: BuildCacheConfig = None,
        languages: List[str] = None,
        root_path: str = None,
        steps: List[Any] = None,
    ):
        self.cache = cache
        self.languages = languages
        self.root_path = root_path
        self.steps = steps

    def validate(self):
        if self.cache:
            self.cache.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache is not None:
            result['cache'] = self.cache.to_map()
        if self.languages is not None:
            result['languages'] = self.languages
        if self.root_path is not None:
            result['rootPath'] = self.root_path
        if self.steps is not None:
            result['steps'] = self.steps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cache') is not None:
            temp_model = BuildCacheConfig()
            self.cache = temp_model.from_map(m['cache'])
        if m.get('languages') is not None:
            self.languages = m.get('languages')
        if m.get('rootPath') is not None:
            self.root_path = m.get('rootPath')
        if m.get('steps') is not None:
            self.steps = m.get('steps')
        return self


class BuildConfig(TeaModel):
    def __init__(
        self,
        default: DefaultBuilderConfig = None,
    ):
        self.default = default

    def validate(self):
        if self.default:
            self.default.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default is not None:
            result['default'] = self.default.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default') is not None:
            temp_model = DefaultBuilderConfig()
            self.default = temp_model.from_map(m['default'])
        return self


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


class CodeVersionReference(TeaModel):
    def __init__(
        self,
        branch: str = None,
        commit_id: str = None,
    ):
        self.branch = branch
        self.commit_id = commit_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commitID') is not None:
            self.commit_id = m.get('commitID')
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
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        spec: ConnectionSpec = None,
        status: ConnectionStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
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
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
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
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
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


class DeleteModelOutput(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployCustomContainerAsyncOutput(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployCustomContainerInputAsyncInvokeConfigDestinationConfigOnFailure(TeaModel):
    def __init__(
        self,
        destination: str = None,
    ):
        self.destination = destination

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['destination'] = self.destination
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destination') is not None:
            self.destination = m.get('destination')
        return self


class DeployCustomContainerInputAsyncInvokeConfigDestinationConfigOnSuccess(TeaModel):
    def __init__(
        self,
        destination: str = None,
    ):
        self.destination = destination

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['destination'] = self.destination
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destination') is not None:
            self.destination = m.get('destination')
        return self


class DeployCustomContainerInputAsyncInvokeConfigDestinationConfig(TeaModel):
    def __init__(
        self,
        on_failure: DeployCustomContainerInputAsyncInvokeConfigDestinationConfigOnFailure = None,
        on_success: DeployCustomContainerInputAsyncInvokeConfigDestinationConfigOnSuccess = None,
    ):
        self.on_failure = on_failure
        self.on_success = on_success

    def validate(self):
        if self.on_failure:
            self.on_failure.validate()
        if self.on_success:
            self.on_success.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_failure is not None:
            result['onFailure'] = self.on_failure.to_map()
        if self.on_success is not None:
            result['onSuccess'] = self.on_success.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onFailure') is not None:
            temp_model = DeployCustomContainerInputAsyncInvokeConfigDestinationConfigOnFailure()
            self.on_failure = temp_model.from_map(m['onFailure'])
        if m.get('onSuccess') is not None:
            temp_model = DeployCustomContainerInputAsyncInvokeConfigDestinationConfigOnSuccess()
            self.on_success = temp_model.from_map(m['onSuccess'])
        return self


class DeployCustomContainerInputAsyncInvokeConfig(TeaModel):
    def __init__(
        self,
        async_task: bool = None,
        destination_config: DeployCustomContainerInputAsyncInvokeConfigDestinationConfig = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
    ):
        self.async_task = async_task
        self.destination_config = destination_config
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        self.max_async_retry_attempts = max_async_retry_attempts

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task is not None:
            result['asyncTask'] = self.async_task
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncTask') is not None:
            self.async_task = m.get('asyncTask')
        if m.get('destinationConfig') is not None:
            temp_model = DeployCustomContainerInputAsyncInvokeConfigDestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        return self


class DeployCustomContainerInputConcurrencyConfig(TeaModel):
    def __init__(
        self,
        reserved_concurrency: int = None,
    ):
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class DeployCustomContainerInputCustomContainerConfigHealthCheckConfig(TeaModel):
    def __init__(
        self,
        failure_threshold: int = None,
        http_get_url: str = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        timeout_seconds: int = None,
    ):
        self.failure_threshold = failure_threshold
        self.http_get_url = http_get_url
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure_threshold is not None:
            result['failureThreshold'] = self.failure_threshold
        if self.http_get_url is not None:
            result['httpGetUrl'] = self.http_get_url
        if self.initial_delay_seconds is not None:
            result['initialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['successThreshold'] = self.success_threshold
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failureThreshold') is not None:
            self.failure_threshold = m.get('failureThreshold')
        if m.get('httpGetUrl') is not None:
            self.http_get_url = m.get('httpGetUrl')
        if m.get('initialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('initialDelaySeconds')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        if m.get('successThreshold') is not None:
            self.success_threshold = m.get('successThreshold')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class DeployCustomContainerInputCustomContainerConfigInstanceLifecycleConfigInitializer(TeaModel):
    def __init__(
        self,
        handler: str = None,
        timeout: int = None,
    ):
        self.handler = handler
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class DeployCustomContainerInputCustomContainerConfigInstanceLifecycleConfigPreStop(TeaModel):
    def __init__(
        self,
        handler: str = None,
        timeout: int = None,
    ):
        self.handler = handler
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class DeployCustomContainerInputCustomContainerConfigInstanceLifecycleConfig(TeaModel):
    def __init__(
        self,
        initializer: DeployCustomContainerInputCustomContainerConfigInstanceLifecycleConfigInitializer = None,
        pre_stop: DeployCustomContainerInputCustomContainerConfigInstanceLifecycleConfigPreStop = None,
    ):
        self.initializer = initializer
        self.pre_stop = pre_stop

    def validate(self):
        if self.initializer:
            self.initializer.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initializer is not None:
            result['initializer'] = self.initializer.to_map()
        if self.pre_stop is not None:
            result['preStop'] = self.pre_stop.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('initializer') is not None:
            temp_model = DeployCustomContainerInputCustomContainerConfigInstanceLifecycleConfigInitializer()
            self.initializer = temp_model.from_map(m['initializer'])
        if m.get('preStop') is not None:
            temp_model = DeployCustomContainerInputCustomContainerConfigInstanceLifecycleConfigPreStop()
            self.pre_stop = temp_model.from_map(m['preStop'])
        return self


class DeployCustomContainerInputCustomContainerConfig(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
        entrypoint: List[str] = None,
        health_check_config: DeployCustomContainerInputCustomContainerConfigHealthCheckConfig = None,
        image: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: DeployCustomContainerInputCustomContainerConfigInstanceLifecycleConfig = None,
        port: int = None,
        role: str = None,
    ):
        self.command = command
        self.entrypoint = entrypoint
        self.health_check_config = health_check_config
        self.image = image
        self.instance_concurrency = instance_concurrency
        self.instance_lifecycle_config = instance_lifecycle_config
        self.port = port
        self.role = role

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['command'] = self.command
        if self.entrypoint is not None:
            result['entrypoint'] = self.entrypoint
        if self.health_check_config is not None:
            result['healthCheckConfig'] = self.health_check_config.to_map()
        if self.image is not None:
            result['image'] = self.image
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.port is not None:
            result['port'] = self.port
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('entrypoint') is not None:
            self.entrypoint = m.get('entrypoint')
        if m.get('healthCheckConfig') is not None:
            temp_model = DeployCustomContainerInputCustomContainerConfigHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['healthCheckConfig'])
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = DeployCustomContainerInputCustomContainerConfigInstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class DeployCustomContainerInputGpuConfig(TeaModel):
    def __init__(
        self,
        gpu_memory_size: int = None,
        gpu_type: str = None,
    ):
        self.gpu_memory_size = gpu_memory_size
        self.gpu_type = gpu_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        return self


class DeployCustomContainerInputHttpTriggerTriggerConfig(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        disable_urlinternet: bool = None,
        dsable_urlinternet: bool = None,
        methods: List[str] = None,
    ):
        self.auth_type = auth_type
        self.disable_urlinternet = disable_urlinternet
        self.dsable_urlinternet = dsable_urlinternet
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet
        if self.dsable_urlinternet is not None:
            result['dsableURLInternet'] = self.dsable_urlinternet
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')
        if m.get('dsableURLInternet') is not None:
            self.dsable_urlinternet = m.get('dsableURLInternet')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class DeployCustomContainerInputHttpTrigger(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
        trigger_config: DeployCustomContainerInputHttpTriggerTriggerConfig = None,
    ):
        self.qualifier = qualifier
        self.trigger_config = trigger_config

    def validate(self):
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('triggerConfig') is not None:
            temp_model = DeployCustomContainerInputHttpTriggerTriggerConfig()
            self.trigger_config = temp_model.from_map(m['triggerConfig'])
        return self


class DeployCustomContainerInputLogConfig(TeaModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        self.enable_instance_metrics = enable_instance_metrics
        self.enable_request_metrics = enable_request_metrics
        self.log_begin_rule = log_begin_rule
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics
        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics
        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')
        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')
        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class ModelConfig(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        framework: str = None,
        model: str = None,
        multi_model_config: List['ModelConfig'] = None,
        path: str = None,
        prefix: str = None,
        region: str = None,
        reversion: str = None,
        token: str = None,
        type: str = None,
    ):
        self.bucket = bucket
        self.framework = framework
        self.model = model
        self.multi_model_config = multi_model_config
        self.path = path
        self.prefix = prefix
        self.region = region
        self.reversion = reversion
        self.token = token
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.multi_model_config:
            for k in self.multi_model_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.framework is not None:
            result['framework'] = self.framework
        if self.model is not None:
            result['model'] = self.model
        result['multiModelConfig'] = []
        if self.multi_model_config is not None:
            for k in self.multi_model_config:
                result['multiModelConfig'].append(k.to_map() if k else None)
        if self.path is not None:
            result['path'] = self.path
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.region is not None:
            result['region'] = self.region
        if self.reversion is not None:
            result['reversion'] = self.reversion
        if self.token is not None:
            result['token'] = self.token
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('framework') is not None:
            self.framework = m.get('framework')
        if m.get('model') is not None:
            self.model = m.get('model')
        self.multi_model_config = []
        if m.get('multiModelConfig') is not None:
            for k in m.get('multiModelConfig'):
                temp_model = ModelConfig()
                self.multi_model_config.append(temp_model.from_map(k))
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('reversion') is not None:
            self.reversion = m.get('reversion')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DeployCustomContainerInputModelConfig(TeaModel):
    def __init__(
        self,
        framework: str = None,
        multi_model_config: List[ModelConfig] = None,
        prefix: str = None,
        source_type: str = None,
        src_model_scope_model_id: str = None,
        src_model_scope_model_revision: str = None,
        src_model_scope_token: str = None,
        src_oss_bucket: str = None,
        src_oss_path: str = None,
        src_oss_region: str = None,
        sync_strategy: str = None,
    ):
        self.framework = framework
        self.multi_model_config = multi_model_config
        self.prefix = prefix
        self.source_type = source_type
        self.src_model_scope_model_id = src_model_scope_model_id
        self.src_model_scope_model_revision = src_model_scope_model_revision
        self.src_model_scope_token = src_model_scope_token
        self.src_oss_bucket = src_oss_bucket
        self.src_oss_path = src_oss_path
        self.src_oss_region = src_oss_region
        self.sync_strategy = sync_strategy

    def validate(self):
        if self.multi_model_config:
            for k in self.multi_model_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.framework is not None:
            result['framework'] = self.framework
        result['multiModelConfig'] = []
        if self.multi_model_config is not None:
            for k in self.multi_model_config:
                result['multiModelConfig'].append(k.to_map() if k else None)
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.src_model_scope_model_id is not None:
            result['srcModelScopeModelID'] = self.src_model_scope_model_id
        if self.src_model_scope_model_revision is not None:
            result['srcModelScopeModelRevision'] = self.src_model_scope_model_revision
        if self.src_model_scope_token is not None:
            result['srcModelScopeToken'] = self.src_model_scope_token
        if self.src_oss_bucket is not None:
            result['srcOssBucket'] = self.src_oss_bucket
        if self.src_oss_path is not None:
            result['srcOssPath'] = self.src_oss_path
        if self.src_oss_region is not None:
            result['srcOssRegion'] = self.src_oss_region
        if self.sync_strategy is not None:
            result['syncStrategy'] = self.sync_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('framework') is not None:
            self.framework = m.get('framework')
        self.multi_model_config = []
        if m.get('multiModelConfig') is not None:
            for k in m.get('multiModelConfig'):
                temp_model = ModelConfig()
                self.multi_model_config.append(temp_model.from_map(k))
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('srcModelScopeModelID') is not None:
            self.src_model_scope_model_id = m.get('srcModelScopeModelID')
        if m.get('srcModelScopeModelRevision') is not None:
            self.src_model_scope_model_revision = m.get('srcModelScopeModelRevision')
        if m.get('srcModelScopeToken') is not None:
            self.src_model_scope_token = m.get('srcModelScopeToken')
        if m.get('srcOssBucket') is not None:
            self.src_oss_bucket = m.get('srcOssBucket')
        if m.get('srcOssPath') is not None:
            self.src_oss_path = m.get('srcOssPath')
        if m.get('srcOssRegion') is not None:
            self.src_oss_region = m.get('srcOssRegion')
        if m.get('syncStrategy') is not None:
            self.sync_strategy = m.get('syncStrategy')
        return self


class DeployCustomContainerInputNasConfig(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[str] = None,
        user_id: int = None,
    ):
        self.group_id = group_id
        self.mount_points = mount_points
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.mount_points is not None:
            result['mountPoints'] = self.mount_points
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('mountPoints') is not None:
            self.mount_points = m.get('mountPoints')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeployCustomContainerInputOssMountConfigMountPoints(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        endpoint: str = None,
        mount_dir: str = None,
        read_only: bool = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path
        self.endpoint = endpoint
        self.mount_dir = mount_dir
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self


class DeployCustomContainerInputOssMountConfig(TeaModel):
    def __init__(
        self,
        mount_points: List[DeployCustomContainerInputOssMountConfigMountPoints] = None,
    ):
        self.mount_points = mount_points

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['mountPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k in m.get('mountPoints'):
                temp_model = DeployCustomContainerInputOssMountConfigMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        return self


class DeployCustomContainerInputProvisionConfigScheduledActions(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.schedule_expression = schedule_expression
        self.start_time = start_time
        self.target = target
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class DeployCustomContainerInputProvisionConfig(TeaModel):
    def __init__(
        self,
        always_allocate_gpu: bool = None,
        scheduled_actions: List[DeployCustomContainerInputProvisionConfigScheduledActions] = None,
        target: int = None,
    ):
        self.always_allocate_gpu = always_allocate_gpu
        self.scheduled_actions = scheduled_actions
        self.target = target

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_gpu is not None:
            result['alwaysAllocateGPU'] = self.always_allocate_gpu
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateGPU') is not None:
            self.always_allocate_gpu = m.get('alwaysAllocateGPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = DeployCustomContainerInputProvisionConfigScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class DeployCustomContainerInputVpcConfig(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class DeployCustomContainerInput(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        async_invoke_config: DeployCustomContainerInputAsyncInvokeConfig = None,
        concurrency_config: DeployCustomContainerInputConcurrencyConfig = None,
        cpu: float = None,
        custom_container_config: DeployCustomContainerInputCustomContainerConfig = None,
        description: str = None,
        disk_size: int = None,
        env_name: str = None,
        environment_variables: Dict[str, Any] = None,
        gpu_config: DeployCustomContainerInputGpuConfig = None,
        http_trigger: DeployCustomContainerInputHttpTrigger = None,
        log_config: DeployCustomContainerInputLogConfig = None,
        memory_size: int = None,
        model_config: DeployCustomContainerInputModelConfig = None,
        name: str = None,
        nas_config: DeployCustomContainerInputNasConfig = None,
        original_name: str = None,
        oss_mount_config: DeployCustomContainerInputOssMountConfig = None,
        project_name: str = None,
        provision_config: DeployCustomContainerInputProvisionConfig = None,
        region: str = None,
        report_status_url: str = None,
        role: str = None,
        timeout: int = None,
        trace_id: str = None,
        vpc_config: DeployCustomContainerInputVpcConfig = None,
    ):
        self.account_id = account_id
        self.async_invoke_config = async_invoke_config
        self.concurrency_config = concurrency_config
        self.cpu = cpu
        self.custom_container_config = custom_container_config
        self.description = description
        self.disk_size = disk_size
        self.env_name = env_name
        self.environment_variables = environment_variables
        self.gpu_config = gpu_config
        self.http_trigger = http_trigger
        self.log_config = log_config
        self.memory_size = memory_size
        self.model_config = model_config
        # This parameter is required.
        self.name = name
        self.nas_config = nas_config
        self.original_name = original_name
        self.oss_mount_config = oss_mount_config
        self.project_name = project_name
        self.provision_config = provision_config
        self.region = region
        self.report_status_url = report_status_url
        # This parameter is required.
        self.role = role
        self.timeout = timeout
        self.trace_id = trace_id
        self.vpc_config = vpc_config

    def validate(self):
        if self.async_invoke_config:
            self.async_invoke_config.validate()
        if self.concurrency_config:
            self.concurrency_config.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.http_trigger:
            self.http_trigger.validate()
        if self.log_config:
            self.log_config.validate()
        if self.model_config:
            self.model_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.provision_config:
            self.provision_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountID'] = self.account_id
        if self.async_invoke_config is not None:
            result['asyncInvokeConfig'] = self.async_invoke_config.to_map()
        if self.concurrency_config is not None:
            result['concurrencyConfig'] = self.concurrency_config.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.http_trigger is not None:
            result['httpTrigger'] = self.http_trigger.to_map()
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.original_name is not None:
            result['originalName'] = self.original_name
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.provision_config is not None:
            result['provisionConfig'] = self.provision_config.to_map()
        if self.region is not None:
            result['region'] = self.region
        if self.report_status_url is not None:
            result['reportStatusURL'] = self.report_status_url
        if self.role is not None:
            result['role'] = self.role
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountID') is not None:
            self.account_id = m.get('accountID')
        if m.get('asyncInvokeConfig') is not None:
            temp_model = DeployCustomContainerInputAsyncInvokeConfig()
            self.async_invoke_config = temp_model.from_map(m['asyncInvokeConfig'])
        if m.get('concurrencyConfig') is not None:
            temp_model = DeployCustomContainerInputConcurrencyConfig()
            self.concurrency_config = temp_model.from_map(m['concurrencyConfig'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('customContainerConfig') is not None:
            temp_model = DeployCustomContainerInputCustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuConfig') is not None:
            temp_model = DeployCustomContainerInputGpuConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('httpTrigger') is not None:
            temp_model = DeployCustomContainerInputHttpTrigger()
            self.http_trigger = temp_model.from_map(m['httpTrigger'])
        if m.get('logConfig') is not None:
            temp_model = DeployCustomContainerInputLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('modelConfig') is not None:
            temp_model = DeployCustomContainerInputModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nasConfig') is not None:
            temp_model = DeployCustomContainerInputNasConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('originalName') is not None:
            self.original_name = m.get('originalName')
        if m.get('ossMountConfig') is not None:
            temp_model = DeployCustomContainerInputOssMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('provisionConfig') is not None:
            temp_model = DeployCustomContainerInputProvisionConfig()
            self.provision_config = temp_model.from_map(m['provisionConfig'])
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('reportStatusURL') is not None:
            self.report_status_url = m.get('reportStatusURL')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('vpcConfig') is not None:
            temp_model = DeployCustomContainerInputVpcConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class DeployCustomContainerOutputData(TeaModel):
    def __init__(
        self,
        deployment_task_id: str = None,
        error_message: str = None,
        finished: bool = None,
        nas_config_str: str = None,
        service_name: str = None,
        trace_id: str = None,
        url_internet: str = None,
        url_intranet: str = None,
        vpc_config_str: str = None,
    ):
        self.deployment_task_id = deployment_task_id
        self.error_message = error_message
        self.finished = finished
        self.nas_config_str = nas_config_str
        self.service_name = service_name
        self.trace_id = trace_id
        self.url_internet = url_internet
        self.url_intranet = url_intranet
        self.vpc_config_str = vpc_config_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_task_id is not None:
            result['deploymentTaskID'] = self.deployment_task_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.finished is not None:
            result['finished'] = self.finished
        if self.nas_config_str is not None:
            result['nasConfigStr'] = self.nas_config_str
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.trace_id is not None:
            result['traceID'] = self.trace_id
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        if self.vpc_config_str is not None:
            result['vpcConfigStr'] = self.vpc_config_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentTaskID') is not None:
            self.deployment_task_id = m.get('deploymentTaskID')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('nasConfigStr') is not None:
            self.nas_config_str = m.get('nasConfigStr')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('traceID') is not None:
            self.trace_id = m.get('traceID')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        if m.get('vpcConfigStr') is not None:
            self.vpc_config_str = m.get('vpcConfigStr')
        return self


class DeployCustomContainerOutput(TeaModel):
    def __init__(
        self,
        data: DeployCustomContainerOutputData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeployCustomContainerOutputData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployEnvironmentOptions(TeaModel):
    def __init__(
        self,
        services: List[str] = None,
    ):
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.services is not None:
            result['services'] = self.services
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('services') is not None:
            self.services = m.get('services')
        return self


class DeployHuggingFaceModelAsyncOutput(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployHuggingFaceModelInputConcurrencyConfig(TeaModel):
    def __init__(
        self,
        reserved_concurrency: int = None,
    ):
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class DeployHuggingFaceModelInputGpuConfig(TeaModel):
    def __init__(
        self,
        gpu_memory_size: int = None,
        gpu_type: str = None,
    ):
        self.gpu_memory_size = gpu_memory_size
        self.gpu_type = gpu_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        return self


class DeployHuggingFaceModelInputHttpTriggerTriggerConfig(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        disable_urlinternet: bool = None,
        dsable_urlinternet: bool = None,
        methods: List[str] = None,
    ):
        self.auth_type = auth_type
        self.disable_urlinternet = disable_urlinternet
        self.dsable_urlinternet = dsable_urlinternet
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet
        if self.dsable_urlinternet is not None:
            result['dsableURLInternet'] = self.dsable_urlinternet
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')
        if m.get('dsableURLInternet') is not None:
            self.dsable_urlinternet = m.get('dsableURLInternet')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class DeployHuggingFaceModelInputHttpTrigger(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
        trigger_config: DeployHuggingFaceModelInputHttpTriggerTriggerConfig = None,
    ):
        self.qualifier = qualifier
        self.trigger_config = trigger_config

    def validate(self):
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('triggerConfig') is not None:
            temp_model = DeployHuggingFaceModelInputHttpTriggerTriggerConfig()
            self.trigger_config = temp_model.from_map(m['triggerConfig'])
        return self


class DeployHuggingFaceModelInputLogConfig(TeaModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        self.enable_instance_metrics = enable_instance_metrics
        self.enable_request_metrics = enable_request_metrics
        self.log_begin_rule = log_begin_rule
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics
        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics
        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')
        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')
        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class DeployHuggingFaceModelInputModelConfigFmkHuggingFaceConfig(TeaModel):
    def __init__(
        self,
        framework: str = None,
        task: str = None,
    ):
        self.framework = framework
        self.task = task

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.framework is not None:
            result['framework'] = self.framework
        if self.task is not None:
            result['task'] = self.task
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('framework') is not None:
            self.framework = m.get('framework')
        if m.get('task') is not None:
            self.task = m.get('task')
        return self


class DeployHuggingFaceModelInputModelConfig(TeaModel):
    def __init__(
        self,
        fmk_hugging_face_config: DeployHuggingFaceModelInputModelConfigFmkHuggingFaceConfig = None,
        framework: str = None,
        multi_model_config: List[ModelConfig] = None,
        prefix: str = None,
        source_type: str = None,
        src_model_scope_model_id: str = None,
        src_model_scope_model_revision: str = None,
        src_model_scope_token: str = None,
        src_oss_bucket: str = None,
        src_oss_path: str = None,
        src_oss_region: str = None,
        sync_strategy: str = None,
    ):
        self.fmk_hugging_face_config = fmk_hugging_face_config
        self.framework = framework
        self.multi_model_config = multi_model_config
        self.prefix = prefix
        self.source_type = source_type
        self.src_model_scope_model_id = src_model_scope_model_id
        self.src_model_scope_model_revision = src_model_scope_model_revision
        self.src_model_scope_token = src_model_scope_token
        self.src_oss_bucket = src_oss_bucket
        self.src_oss_path = src_oss_path
        self.src_oss_region = src_oss_region
        self.sync_strategy = sync_strategy

    def validate(self):
        if self.fmk_hugging_face_config:
            self.fmk_hugging_face_config.validate()
        if self.multi_model_config:
            for k in self.multi_model_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fmk_hugging_face_config is not None:
            result['fmkHuggingFaceConfig'] = self.fmk_hugging_face_config.to_map()
        if self.framework is not None:
            result['framework'] = self.framework
        result['multiModelConfig'] = []
        if self.multi_model_config is not None:
            for k in self.multi_model_config:
                result['multiModelConfig'].append(k.to_map() if k else None)
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.src_model_scope_model_id is not None:
            result['srcModelScopeModelID'] = self.src_model_scope_model_id
        if self.src_model_scope_model_revision is not None:
            result['srcModelScopeModelRevision'] = self.src_model_scope_model_revision
        if self.src_model_scope_token is not None:
            result['srcModelScopeToken'] = self.src_model_scope_token
        if self.src_oss_bucket is not None:
            result['srcOssBucket'] = self.src_oss_bucket
        if self.src_oss_path is not None:
            result['srcOssPath'] = self.src_oss_path
        if self.src_oss_region is not None:
            result['srcOssRegion'] = self.src_oss_region
        if self.sync_strategy is not None:
            result['syncStrategy'] = self.sync_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fmkHuggingFaceConfig') is not None:
            temp_model = DeployHuggingFaceModelInputModelConfigFmkHuggingFaceConfig()
            self.fmk_hugging_face_config = temp_model.from_map(m['fmkHuggingFaceConfig'])
        if m.get('framework') is not None:
            self.framework = m.get('framework')
        self.multi_model_config = []
        if m.get('multiModelConfig') is not None:
            for k in m.get('multiModelConfig'):
                temp_model = ModelConfig()
                self.multi_model_config.append(temp_model.from_map(k))
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('srcModelScopeModelID') is not None:
            self.src_model_scope_model_id = m.get('srcModelScopeModelID')
        if m.get('srcModelScopeModelRevision') is not None:
            self.src_model_scope_model_revision = m.get('srcModelScopeModelRevision')
        if m.get('srcModelScopeToken') is not None:
            self.src_model_scope_token = m.get('srcModelScopeToken')
        if m.get('srcOssBucket') is not None:
            self.src_oss_bucket = m.get('srcOssBucket')
        if m.get('srcOssPath') is not None:
            self.src_oss_path = m.get('srcOssPath')
        if m.get('srcOssRegion') is not None:
            self.src_oss_region = m.get('srcOssRegion')
        if m.get('syncStrategy') is not None:
            self.sync_strategy = m.get('syncStrategy')
        return self


class DeployHuggingFaceModelInputNasConfig(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[str] = None,
        user_id: int = None,
    ):
        self.group_id = group_id
        self.mount_points = mount_points
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.mount_points is not None:
            result['mountPoints'] = self.mount_points
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('mountPoints') is not None:
            self.mount_points = m.get('mountPoints')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeployHuggingFaceModelInputProvisionConfigScheduledActions(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.schedule_expression = schedule_expression
        self.start_time = start_time
        self.target = target
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class DeployHuggingFaceModelInputProvisionConfig(TeaModel):
    def __init__(
        self,
        always_allocate_gpu: bool = None,
        scheduled_actions: List[DeployHuggingFaceModelInputProvisionConfigScheduledActions] = None,
        target: int = None,
    ):
        self.always_allocate_gpu = always_allocate_gpu
        self.scheduled_actions = scheduled_actions
        self.target = target

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_gpu is not None:
            result['alwaysAllocateGPU'] = self.always_allocate_gpu
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateGPU') is not None:
            self.always_allocate_gpu = m.get('alwaysAllocateGPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = DeployHuggingFaceModelInputProvisionConfigScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class DeployHuggingFaceModelInputVpcConfig(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class DeployHuggingFaceModelInput(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        concurrency_config: DeployHuggingFaceModelInputConcurrencyConfig = None,
        cpu: float = None,
        description: str = None,
        disk_size: int = None,
        env_name: str = None,
        environment_variables: Dict[str, Any] = None,
        gpu_config: DeployHuggingFaceModelInputGpuConfig = None,
        http_trigger: DeployHuggingFaceModelInputHttpTrigger = None,
        image_name: str = None,
        instance_concurrency: int = None,
        log_config: DeployHuggingFaceModelInputLogConfig = None,
        memory_size: int = None,
        model_config: DeployHuggingFaceModelInputModelConfig = None,
        name: str = None,
        nas_config: DeployHuggingFaceModelInputNasConfig = None,
        original_name: str = None,
        project_name: str = None,
        provision_config: DeployHuggingFaceModelInputProvisionConfig = None,
        region: str = None,
        report_status_url: str = None,
        role: str = None,
        timeout: int = None,
        trace_id: str = None,
        vpc_config: DeployHuggingFaceModelInputVpcConfig = None,
    ):
        self.account_id = account_id
        self.concurrency_config = concurrency_config
        self.cpu = cpu
        self.description = description
        self.disk_size = disk_size
        self.env_name = env_name
        self.environment_variables = environment_variables
        self.gpu_config = gpu_config
        self.http_trigger = http_trigger
        self.image_name = image_name
        self.instance_concurrency = instance_concurrency
        self.log_config = log_config
        self.memory_size = memory_size
        self.model_config = model_config
        # This parameter is required.
        self.name = name
        self.nas_config = nas_config
        self.original_name = original_name
        self.project_name = project_name
        self.provision_config = provision_config
        self.region = region
        self.report_status_url = report_status_url
        # This parameter is required.
        self.role = role
        self.timeout = timeout
        self.trace_id = trace_id
        self.vpc_config = vpc_config

    def validate(self):
        if self.concurrency_config:
            self.concurrency_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.http_trigger:
            self.http_trigger.validate()
        if self.log_config:
            self.log_config.validate()
        if self.model_config:
            self.model_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.provision_config:
            self.provision_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountID'] = self.account_id
        if self.concurrency_config is not None:
            result['concurrencyConfig'] = self.concurrency_config.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.http_trigger is not None:
            result['httpTrigger'] = self.http_trigger.to_map()
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.original_name is not None:
            result['originalName'] = self.original_name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.provision_config is not None:
            result['provisionConfig'] = self.provision_config.to_map()
        if self.region is not None:
            result['region'] = self.region
        if self.report_status_url is not None:
            result['reportStatusURL'] = self.report_status_url
        if self.role is not None:
            result['role'] = self.role
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountID') is not None:
            self.account_id = m.get('accountID')
        if m.get('concurrencyConfig') is not None:
            temp_model = DeployHuggingFaceModelInputConcurrencyConfig()
            self.concurrency_config = temp_model.from_map(m['concurrencyConfig'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuConfig') is not None:
            temp_model = DeployHuggingFaceModelInputGpuConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('httpTrigger') is not None:
            temp_model = DeployHuggingFaceModelInputHttpTrigger()
            self.http_trigger = temp_model.from_map(m['httpTrigger'])
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('logConfig') is not None:
            temp_model = DeployHuggingFaceModelInputLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('modelConfig') is not None:
            temp_model = DeployHuggingFaceModelInputModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nasConfig') is not None:
            temp_model = DeployHuggingFaceModelInputNasConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('originalName') is not None:
            self.original_name = m.get('originalName')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('provisionConfig') is not None:
            temp_model = DeployHuggingFaceModelInputProvisionConfig()
            self.provision_config = temp_model.from_map(m['provisionConfig'])
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('reportStatusURL') is not None:
            self.report_status_url = m.get('reportStatusURL')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('vpcConfig') is not None:
            temp_model = DeployHuggingFaceModelInputVpcConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class DeployHuggingFaceModelOutputData(TeaModel):
    def __init__(
        self,
        deployment_task_id: str = None,
        error_message: str = None,
        finished: bool = None,
        service_name: str = None,
        task_type: str = None,
        trace_id: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        self.deployment_task_id = deployment_task_id
        self.error_message = error_message
        self.finished = finished
        self.service_name = service_name
        self.task_type = task_type
        self.trace_id = trace_id
        self.url_internet = url_internet
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_task_id is not None:
            result['deploymentTaskID'] = self.deployment_task_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.finished is not None:
            result['finished'] = self.finished
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.trace_id is not None:
            result['traceID'] = self.trace_id
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentTaskID') is not None:
            self.deployment_task_id = m.get('deploymentTaskID')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('traceID') is not None:
            self.trace_id = m.get('traceID')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class DeployHuggingFaceModelOutput(TeaModel):
    def __init__(
        self,
        data: DeployHuggingFaceModelOutputData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeployHuggingFaceModelOutputData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployModelScopeModelAsyncOutput(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployModelScopeModelInputConcurrencyConfig(TeaModel):
    def __init__(
        self,
        reserved_concurrency: int = None,
    ):
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class DeployModelScopeModelInputGpuConfig(TeaModel):
    def __init__(
        self,
        gpu_memory_size: int = None,
        gpu_type: str = None,
    ):
        self.gpu_memory_size = gpu_memory_size
        self.gpu_type = gpu_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        return self


class DeployModelScopeModelInputHttpTriggerTriggerConfig(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        disable_urlinternet: bool = None,
        dsable_urlinternet: bool = None,
        methods: List[str] = None,
    ):
        self.auth_type = auth_type
        self.disable_urlinternet = disable_urlinternet
        self.dsable_urlinternet = dsable_urlinternet
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet
        if self.dsable_urlinternet is not None:
            result['dsableURLInternet'] = self.dsable_urlinternet
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')
        if m.get('dsableURLInternet') is not None:
            self.dsable_urlinternet = m.get('dsableURLInternet')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class DeployModelScopeModelInputHttpTrigger(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
        trigger_config: DeployModelScopeModelInputHttpTriggerTriggerConfig = None,
    ):
        self.qualifier = qualifier
        self.trigger_config = trigger_config

    def validate(self):
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('triggerConfig') is not None:
            temp_model = DeployModelScopeModelInputHttpTriggerTriggerConfig()
            self.trigger_config = temp_model.from_map(m['triggerConfig'])
        return self


class DeployModelScopeModelInputLogConfig(TeaModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        self.enable_instance_metrics = enable_instance_metrics
        self.enable_request_metrics = enable_request_metrics
        self.log_begin_rule = log_begin_rule
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics
        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics
        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')
        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')
        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class DeployModelScopeModelInputModelConfig(TeaModel):
    def __init__(
        self,
        framework: str = None,
        multi_model_config: List[ModelConfig] = None,
        prefix: str = None,
        source_type: str = None,
        src_model_scope_model_id: str = None,
        src_model_scope_model_revision: str = None,
        src_model_scope_token: str = None,
        src_oss_bucket: str = None,
        src_oss_path: str = None,
        src_oss_region: str = None,
        sync_strategy: str = None,
    ):
        self.framework = framework
        self.multi_model_config = multi_model_config
        self.prefix = prefix
        self.source_type = source_type
        self.src_model_scope_model_id = src_model_scope_model_id
        self.src_model_scope_model_revision = src_model_scope_model_revision
        self.src_model_scope_token = src_model_scope_token
        self.src_oss_bucket = src_oss_bucket
        self.src_oss_path = src_oss_path
        self.src_oss_region = src_oss_region
        self.sync_strategy = sync_strategy

    def validate(self):
        if self.multi_model_config:
            for k in self.multi_model_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.framework is not None:
            result['framework'] = self.framework
        result['multiModelConfig'] = []
        if self.multi_model_config is not None:
            for k in self.multi_model_config:
                result['multiModelConfig'].append(k.to_map() if k else None)
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.src_model_scope_model_id is not None:
            result['srcModelScopeModelID'] = self.src_model_scope_model_id
        if self.src_model_scope_model_revision is not None:
            result['srcModelScopeModelRevision'] = self.src_model_scope_model_revision
        if self.src_model_scope_token is not None:
            result['srcModelScopeToken'] = self.src_model_scope_token
        if self.src_oss_bucket is not None:
            result['srcOssBucket'] = self.src_oss_bucket
        if self.src_oss_path is not None:
            result['srcOssPath'] = self.src_oss_path
        if self.src_oss_region is not None:
            result['srcOssRegion'] = self.src_oss_region
        if self.sync_strategy is not None:
            result['syncStrategy'] = self.sync_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('framework') is not None:
            self.framework = m.get('framework')
        self.multi_model_config = []
        if m.get('multiModelConfig') is not None:
            for k in m.get('multiModelConfig'):
                temp_model = ModelConfig()
                self.multi_model_config.append(temp_model.from_map(k))
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('srcModelScopeModelID') is not None:
            self.src_model_scope_model_id = m.get('srcModelScopeModelID')
        if m.get('srcModelScopeModelRevision') is not None:
            self.src_model_scope_model_revision = m.get('srcModelScopeModelRevision')
        if m.get('srcModelScopeToken') is not None:
            self.src_model_scope_token = m.get('srcModelScopeToken')
        if m.get('srcOssBucket') is not None:
            self.src_oss_bucket = m.get('srcOssBucket')
        if m.get('srcOssPath') is not None:
            self.src_oss_path = m.get('srcOssPath')
        if m.get('srcOssRegion') is not None:
            self.src_oss_region = m.get('srcOssRegion')
        if m.get('syncStrategy') is not None:
            self.sync_strategy = m.get('syncStrategy')
        return self


class DeployModelScopeModelInputNasConfig(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[str] = None,
        user_id: int = None,
    ):
        self.group_id = group_id
        self.mount_points = mount_points
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.mount_points is not None:
            result['mountPoints'] = self.mount_points
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('mountPoints') is not None:
            self.mount_points = m.get('mountPoints')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeployModelScopeModelInputProvisionConfigScheduledActions(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.schedule_expression = schedule_expression
        self.start_time = start_time
        self.target = target
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class DeployModelScopeModelInputProvisionConfig(TeaModel):
    def __init__(
        self,
        always_allocate_gpu: bool = None,
        scheduled_actions: List[DeployModelScopeModelInputProvisionConfigScheduledActions] = None,
        target: int = None,
    ):
        self.always_allocate_gpu = always_allocate_gpu
        self.scheduled_actions = scheduled_actions
        self.target = target

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_gpu is not None:
            result['alwaysAllocateGPU'] = self.always_allocate_gpu
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateGPU') is not None:
            self.always_allocate_gpu = m.get('alwaysAllocateGPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = DeployModelScopeModelInputProvisionConfigScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class DeployModelScopeModelInputVpcConfig(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class DeployModelScopeModelInput(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        concurrency_config: DeployModelScopeModelInputConcurrencyConfig = None,
        cpu: float = None,
        description: str = None,
        disk_size: int = None,
        env_name: str = None,
        environment_variables: Dict[str, Any] = None,
        gpu_config: DeployModelScopeModelInputGpuConfig = None,
        http_trigger: DeployModelScopeModelInputHttpTrigger = None,
        image_name: str = None,
        instance_concurrency: int = None,
        log_config: DeployModelScopeModelInputLogConfig = None,
        memory_size: int = None,
        model_config: DeployModelScopeModelInputModelConfig = None,
        name: str = None,
        nas_config: DeployModelScopeModelInputNasConfig = None,
        original_name: str = None,
        project_name: str = None,
        provision_config: DeployModelScopeModelInputProvisionConfig = None,
        region: str = None,
        report_status_url: str = None,
        role: str = None,
        timeout: int = None,
        trace_id: str = None,
        vpc_config: DeployModelScopeModelInputVpcConfig = None,
    ):
        self.account_id = account_id
        self.concurrency_config = concurrency_config
        self.cpu = cpu
        self.description = description
        self.disk_size = disk_size
        self.env_name = env_name
        self.environment_variables = environment_variables
        self.gpu_config = gpu_config
        self.http_trigger = http_trigger
        self.image_name = image_name
        self.instance_concurrency = instance_concurrency
        self.log_config = log_config
        self.memory_size = memory_size
        self.model_config = model_config
        # This parameter is required.
        self.name = name
        self.nas_config = nas_config
        self.original_name = original_name
        self.project_name = project_name
        self.provision_config = provision_config
        self.region = region
        self.report_status_url = report_status_url
        # This parameter is required.
        self.role = role
        self.timeout = timeout
        self.trace_id = trace_id
        self.vpc_config = vpc_config

    def validate(self):
        if self.concurrency_config:
            self.concurrency_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.http_trigger:
            self.http_trigger.validate()
        if self.log_config:
            self.log_config.validate()
        if self.model_config:
            self.model_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.provision_config:
            self.provision_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountID'] = self.account_id
        if self.concurrency_config is not None:
            result['concurrencyConfig'] = self.concurrency_config.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.http_trigger is not None:
            result['httpTrigger'] = self.http_trigger.to_map()
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.original_name is not None:
            result['originalName'] = self.original_name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.provision_config is not None:
            result['provisionConfig'] = self.provision_config.to_map()
        if self.region is not None:
            result['region'] = self.region
        if self.report_status_url is not None:
            result['reportStatusURL'] = self.report_status_url
        if self.role is not None:
            result['role'] = self.role
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountID') is not None:
            self.account_id = m.get('accountID')
        if m.get('concurrencyConfig') is not None:
            temp_model = DeployModelScopeModelInputConcurrencyConfig()
            self.concurrency_config = temp_model.from_map(m['concurrencyConfig'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuConfig') is not None:
            temp_model = DeployModelScopeModelInputGpuConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('httpTrigger') is not None:
            temp_model = DeployModelScopeModelInputHttpTrigger()
            self.http_trigger = temp_model.from_map(m['httpTrigger'])
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('logConfig') is not None:
            temp_model = DeployModelScopeModelInputLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('modelConfig') is not None:
            temp_model = DeployModelScopeModelInputModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nasConfig') is not None:
            temp_model = DeployModelScopeModelInputNasConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('originalName') is not None:
            self.original_name = m.get('originalName')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('provisionConfig') is not None:
            temp_model = DeployModelScopeModelInputProvisionConfig()
            self.provision_config = temp_model.from_map(m['provisionConfig'])
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('reportStatusURL') is not None:
            self.report_status_url = m.get('reportStatusURL')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('vpcConfig') is not None:
            temp_model = DeployModelScopeModelInputVpcConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class DeployModelScopeModelOutputData(TeaModel):
    def __init__(
        self,
        deployment_task_id: str = None,
        error_message: str = None,
        finished: bool = None,
        service_name: str = None,
        task_type: str = None,
        trace_id: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        self.deployment_task_id = deployment_task_id
        self.error_message = error_message
        self.finished = finished
        self.service_name = service_name
        self.task_type = task_type
        self.trace_id = trace_id
        self.url_internet = url_internet
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_task_id is not None:
            result['deploymentTaskID'] = self.deployment_task_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.finished is not None:
            result['finished'] = self.finished
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.trace_id is not None:
            result['traceID'] = self.trace_id
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentTaskID') is not None:
            self.deployment_task_id = m.get('deploymentTaskID')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('traceID') is not None:
            self.trace_id = m.get('traceID')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class DeployModelScopeModelOutput(TeaModel):
    def __init__(
        self,
        data: DeployModelScopeModelOutputData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeployModelScopeModelOutputData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployOllamaModelAsyncOutput(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployOllamaModelInputConcurrencyConfig(TeaModel):
    def __init__(
        self,
        reserved_concurrency: int = None,
    ):
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class DeployOllamaModelInputGpuConfig(TeaModel):
    def __init__(
        self,
        gpu_memory_size: int = None,
        gpu_type: str = None,
    ):
        self.gpu_memory_size = gpu_memory_size
        self.gpu_type = gpu_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        return self


class DeployOllamaModelInputHttpTriggerTriggerConfig(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        disable_urlinternet: bool = None,
        dsable_urlinternet: bool = None,
        methods: List[str] = None,
    ):
        self.auth_type = auth_type
        self.disable_urlinternet = disable_urlinternet
        self.dsable_urlinternet = dsable_urlinternet
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet
        if self.dsable_urlinternet is not None:
            result['dsableURLInternet'] = self.dsable_urlinternet
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')
        if m.get('dsableURLInternet') is not None:
            self.dsable_urlinternet = m.get('dsableURLInternet')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class DeployOllamaModelInputHttpTrigger(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
        trigger_config: DeployOllamaModelInputHttpTriggerTriggerConfig = None,
    ):
        self.qualifier = qualifier
        self.trigger_config = trigger_config

    def validate(self):
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('triggerConfig') is not None:
            temp_model = DeployOllamaModelInputHttpTriggerTriggerConfig()
            self.trigger_config = temp_model.from_map(m['triggerConfig'])
        return self


class DeployOllamaModelInputLogConfig(TeaModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        self.enable_instance_metrics = enable_instance_metrics
        self.enable_request_metrics = enable_request_metrics
        self.log_begin_rule = log_begin_rule
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics
        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics
        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')
        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')
        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class DeployOllamaModelInputModelConfigFmkOllamaConfig(TeaModel):
    def __init__(
        self,
        min_p: float = None,
        mirostat: int = None,
        mirostat_eta: float = None,
        mirostat_tau: float = None,
        model_name: str = None,
        modelfile_adapter: str = None,
        modelfile_additional_froms_string: str = None,
        modelfile_full_text_postfix: str = None,
        modelfile_params: str = None,
        modelfile_system: str = None,
        modelfile_template: str = None,
        num_ctx: int = None,
        num_predict: int = None,
        quantize: str = None,
        repeat_last_n: int = None,
        repeat_penalty: float = None,
        seed: int = None,
        single_model_file: str = None,
        splited_model_start_file: str = None,
        stop: str = None,
        stream: bool = None,
        temperature: float = None,
        tfs_z: float = None,
        top_k: int = None,
        top_p: float = None,
    ):
        self.min_p = min_p
        self.mirostat = mirostat
        self.mirostat_eta = mirostat_eta
        self.mirostat_tau = mirostat_tau
        self.model_name = model_name
        self.modelfile_adapter = modelfile_adapter
        self.modelfile_additional_froms_string = modelfile_additional_froms_string
        self.modelfile_full_text_postfix = modelfile_full_text_postfix
        self.modelfile_params = modelfile_params
        self.modelfile_system = modelfile_system
        self.modelfile_template = modelfile_template
        self.num_ctx = num_ctx
        self.num_predict = num_predict
        self.quantize = quantize
        self.repeat_last_n = repeat_last_n
        self.repeat_penalty = repeat_penalty
        self.seed = seed
        self.single_model_file = single_model_file
        self.splited_model_start_file = splited_model_start_file
        self.stop = stop
        self.stream = stream
        self.temperature = temperature
        self.tfs_z = tfs_z
        self.top_k = top_k
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.min_p is not None:
            result['minP'] = self.min_p
        if self.mirostat is not None:
            result['mirostat'] = self.mirostat
        if self.mirostat_eta is not None:
            result['mirostatEta'] = self.mirostat_eta
        if self.mirostat_tau is not None:
            result['mirostatTau'] = self.mirostat_tau
        if self.model_name is not None:
            result['modelName'] = self.model_name
        if self.modelfile_adapter is not None:
            result['modelfileAdapter'] = self.modelfile_adapter
        if self.modelfile_additional_froms_string is not None:
            result['modelfileAdditionalFromsString'] = self.modelfile_additional_froms_string
        if self.modelfile_full_text_postfix is not None:
            result['modelfileFullTextPostfix'] = self.modelfile_full_text_postfix
        if self.modelfile_params is not None:
            result['modelfileParams'] = self.modelfile_params
        if self.modelfile_system is not None:
            result['modelfileSystem'] = self.modelfile_system
        if self.modelfile_template is not None:
            result['modelfileTemplate'] = self.modelfile_template
        if self.num_ctx is not None:
            result['numCtx'] = self.num_ctx
        if self.num_predict is not None:
            result['numPredict'] = self.num_predict
        if self.quantize is not None:
            result['quantize'] = self.quantize
        if self.repeat_last_n is not None:
            result['repeatLastN'] = self.repeat_last_n
        if self.repeat_penalty is not None:
            result['repeatPenalty'] = self.repeat_penalty
        if self.seed is not None:
            result['seed'] = self.seed
        if self.single_model_file is not None:
            result['singleModelFile'] = self.single_model_file
        if self.splited_model_start_file is not None:
            result['splitedModelStartFile'] = self.splited_model_start_file
        if self.stop is not None:
            result['stop'] = self.stop
        if self.stream is not None:
            result['stream'] = self.stream
        if self.temperature is not None:
            result['temperature'] = self.temperature
        if self.tfs_z is not None:
            result['tfsZ'] = self.tfs_z
        if self.top_k is not None:
            result['topK'] = self.top_k
        if self.top_p is not None:
            result['topP'] = self.top_p
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('minP') is not None:
            self.min_p = m.get('minP')
        if m.get('mirostat') is not None:
            self.mirostat = m.get('mirostat')
        if m.get('mirostatEta') is not None:
            self.mirostat_eta = m.get('mirostatEta')
        if m.get('mirostatTau') is not None:
            self.mirostat_tau = m.get('mirostatTau')
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')
        if m.get('modelfileAdapter') is not None:
            self.modelfile_adapter = m.get('modelfileAdapter')
        if m.get('modelfileAdditionalFromsString') is not None:
            self.modelfile_additional_froms_string = m.get('modelfileAdditionalFromsString')
        if m.get('modelfileFullTextPostfix') is not None:
            self.modelfile_full_text_postfix = m.get('modelfileFullTextPostfix')
        if m.get('modelfileParams') is not None:
            self.modelfile_params = m.get('modelfileParams')
        if m.get('modelfileSystem') is not None:
            self.modelfile_system = m.get('modelfileSystem')
        if m.get('modelfileTemplate') is not None:
            self.modelfile_template = m.get('modelfileTemplate')
        if m.get('numCtx') is not None:
            self.num_ctx = m.get('numCtx')
        if m.get('numPredict') is not None:
            self.num_predict = m.get('numPredict')
        if m.get('quantize') is not None:
            self.quantize = m.get('quantize')
        if m.get('repeatLastN') is not None:
            self.repeat_last_n = m.get('repeatLastN')
        if m.get('repeatPenalty') is not None:
            self.repeat_penalty = m.get('repeatPenalty')
        if m.get('seed') is not None:
            self.seed = m.get('seed')
        if m.get('singleModelFile') is not None:
            self.single_model_file = m.get('singleModelFile')
        if m.get('splitedModelStartFile') is not None:
            self.splited_model_start_file = m.get('splitedModelStartFile')
        if m.get('stop') is not None:
            self.stop = m.get('stop')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        if m.get('tfsZ') is not None:
            self.tfs_z = m.get('tfsZ')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        if m.get('topP') is not None:
            self.top_p = m.get('topP')
        return self


class DeployOllamaModelInputModelConfig(TeaModel):
    def __init__(
        self,
        fmk_ollama_config: DeployOllamaModelInputModelConfigFmkOllamaConfig = None,
        framework: str = None,
        multi_model_config: List[ModelConfig] = None,
        prefix: str = None,
        source_type: str = None,
        src_model_scope_model_id: str = None,
        src_model_scope_model_revision: str = None,
        src_model_scope_token: str = None,
        src_oss_bucket: str = None,
        src_oss_path: str = None,
        src_oss_region: str = None,
        sync_strategy: str = None,
    ):
        self.fmk_ollama_config = fmk_ollama_config
        self.framework = framework
        self.multi_model_config = multi_model_config
        self.prefix = prefix
        self.source_type = source_type
        self.src_model_scope_model_id = src_model_scope_model_id
        self.src_model_scope_model_revision = src_model_scope_model_revision
        self.src_model_scope_token = src_model_scope_token
        self.src_oss_bucket = src_oss_bucket
        self.src_oss_path = src_oss_path
        self.src_oss_region = src_oss_region
        self.sync_strategy = sync_strategy

    def validate(self):
        if self.fmk_ollama_config:
            self.fmk_ollama_config.validate()
        if self.multi_model_config:
            for k in self.multi_model_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fmk_ollama_config is not None:
            result['fmkOllamaConfig'] = self.fmk_ollama_config.to_map()
        if self.framework is not None:
            result['framework'] = self.framework
        result['multiModelConfig'] = []
        if self.multi_model_config is not None:
            for k in self.multi_model_config:
                result['multiModelConfig'].append(k.to_map() if k else None)
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.src_model_scope_model_id is not None:
            result['srcModelScopeModelID'] = self.src_model_scope_model_id
        if self.src_model_scope_model_revision is not None:
            result['srcModelScopeModelRevision'] = self.src_model_scope_model_revision
        if self.src_model_scope_token is not None:
            result['srcModelScopeToken'] = self.src_model_scope_token
        if self.src_oss_bucket is not None:
            result['srcOssBucket'] = self.src_oss_bucket
        if self.src_oss_path is not None:
            result['srcOssPath'] = self.src_oss_path
        if self.src_oss_region is not None:
            result['srcOssRegion'] = self.src_oss_region
        if self.sync_strategy is not None:
            result['syncStrategy'] = self.sync_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fmkOllamaConfig') is not None:
            temp_model = DeployOllamaModelInputModelConfigFmkOllamaConfig()
            self.fmk_ollama_config = temp_model.from_map(m['fmkOllamaConfig'])
        if m.get('framework') is not None:
            self.framework = m.get('framework')
        self.multi_model_config = []
        if m.get('multiModelConfig') is not None:
            for k in m.get('multiModelConfig'):
                temp_model = ModelConfig()
                self.multi_model_config.append(temp_model.from_map(k))
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('srcModelScopeModelID') is not None:
            self.src_model_scope_model_id = m.get('srcModelScopeModelID')
        if m.get('srcModelScopeModelRevision') is not None:
            self.src_model_scope_model_revision = m.get('srcModelScopeModelRevision')
        if m.get('srcModelScopeToken') is not None:
            self.src_model_scope_token = m.get('srcModelScopeToken')
        if m.get('srcOssBucket') is not None:
            self.src_oss_bucket = m.get('srcOssBucket')
        if m.get('srcOssPath') is not None:
            self.src_oss_path = m.get('srcOssPath')
        if m.get('srcOssRegion') is not None:
            self.src_oss_region = m.get('srcOssRegion')
        if m.get('syncStrategy') is not None:
            self.sync_strategy = m.get('syncStrategy')
        return self


class DeployOllamaModelInputNasConfig(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[str] = None,
        user_id: int = None,
    ):
        self.group_id = group_id
        self.mount_points = mount_points
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.mount_points is not None:
            result['mountPoints'] = self.mount_points
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('mountPoints') is not None:
            self.mount_points = m.get('mountPoints')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeployOllamaModelInputProvisionConfigScheduledActions(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.schedule_expression = schedule_expression
        self.start_time = start_time
        self.target = target
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class DeployOllamaModelInputProvisionConfig(TeaModel):
    def __init__(
        self,
        always_allocate_gpu: bool = None,
        scheduled_actions: List[DeployOllamaModelInputProvisionConfigScheduledActions] = None,
        target: int = None,
    ):
        self.always_allocate_gpu = always_allocate_gpu
        self.scheduled_actions = scheduled_actions
        self.target = target

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_gpu is not None:
            result['alwaysAllocateGPU'] = self.always_allocate_gpu
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateGPU') is not None:
            self.always_allocate_gpu = m.get('alwaysAllocateGPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = DeployOllamaModelInputProvisionConfigScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class DeployOllamaModelInputVpcConfig(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class DeployOllamaModelInput(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        concurrency_config: DeployOllamaModelInputConcurrencyConfig = None,
        cpu: float = None,
        description: str = None,
        disk_size: int = None,
        env_name: str = None,
        environment_variables: Dict[str, Any] = None,
        gpu_config: DeployOllamaModelInputGpuConfig = None,
        http_trigger: DeployOllamaModelInputHttpTrigger = None,
        image_name: str = None,
        instance_concurrency: int = None,
        log_config: DeployOllamaModelInputLogConfig = None,
        memory_size: int = None,
        model_config: DeployOllamaModelInputModelConfig = None,
        name: str = None,
        nas_config: DeployOllamaModelInputNasConfig = None,
        original_name: str = None,
        project_name: str = None,
        provision_config: DeployOllamaModelInputProvisionConfig = None,
        region: str = None,
        report_status_url: str = None,
        role: str = None,
        timeout: int = None,
        trace_id: str = None,
        vpc_config: DeployOllamaModelInputVpcConfig = None,
    ):
        self.account_id = account_id
        self.concurrency_config = concurrency_config
        self.cpu = cpu
        self.description = description
        self.disk_size = disk_size
        self.env_name = env_name
        self.environment_variables = environment_variables
        self.gpu_config = gpu_config
        self.http_trigger = http_trigger
        self.image_name = image_name
        self.instance_concurrency = instance_concurrency
        self.log_config = log_config
        self.memory_size = memory_size
        self.model_config = model_config
        # This parameter is required.
        self.name = name
        self.nas_config = nas_config
        self.original_name = original_name
        self.project_name = project_name
        self.provision_config = provision_config
        self.region = region
        self.report_status_url = report_status_url
        # This parameter is required.
        self.role = role
        self.timeout = timeout
        self.trace_id = trace_id
        self.vpc_config = vpc_config

    def validate(self):
        if self.concurrency_config:
            self.concurrency_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.http_trigger:
            self.http_trigger.validate()
        if self.log_config:
            self.log_config.validate()
        if self.model_config:
            self.model_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.provision_config:
            self.provision_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountID'] = self.account_id
        if self.concurrency_config is not None:
            result['concurrencyConfig'] = self.concurrency_config.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.http_trigger is not None:
            result['httpTrigger'] = self.http_trigger.to_map()
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.original_name is not None:
            result['originalName'] = self.original_name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.provision_config is not None:
            result['provisionConfig'] = self.provision_config.to_map()
        if self.region is not None:
            result['region'] = self.region
        if self.report_status_url is not None:
            result['reportStatusURL'] = self.report_status_url
        if self.role is not None:
            result['role'] = self.role
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountID') is not None:
            self.account_id = m.get('accountID')
        if m.get('concurrencyConfig') is not None:
            temp_model = DeployOllamaModelInputConcurrencyConfig()
            self.concurrency_config = temp_model.from_map(m['concurrencyConfig'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuConfig') is not None:
            temp_model = DeployOllamaModelInputGpuConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('httpTrigger') is not None:
            temp_model = DeployOllamaModelInputHttpTrigger()
            self.http_trigger = temp_model.from_map(m['httpTrigger'])
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('logConfig') is not None:
            temp_model = DeployOllamaModelInputLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('modelConfig') is not None:
            temp_model = DeployOllamaModelInputModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nasConfig') is not None:
            temp_model = DeployOllamaModelInputNasConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('originalName') is not None:
            self.original_name = m.get('originalName')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('provisionConfig') is not None:
            temp_model = DeployOllamaModelInputProvisionConfig()
            self.provision_config = temp_model.from_map(m['provisionConfig'])
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('reportStatusURL') is not None:
            self.report_status_url = m.get('reportStatusURL')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('vpcConfig') is not None:
            temp_model = DeployOllamaModelInputVpcConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class DeployOllamaModelOutputData(TeaModel):
    def __init__(
        self,
        deployment_task_id: str = None,
        error_message: str = None,
        finished: bool = None,
        model_name: str = None,
        service_name: str = None,
        trace_id: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        self.deployment_task_id = deployment_task_id
        self.error_message = error_message
        self.finished = finished
        self.model_name = model_name
        self.service_name = service_name
        self.trace_id = trace_id
        self.url_internet = url_internet
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_task_id is not None:
            result['deploymentTaskID'] = self.deployment_task_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.finished is not None:
            result['finished'] = self.finished
        if self.model_name is not None:
            result['modelName'] = self.model_name
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.trace_id is not None:
            result['traceID'] = self.trace_id
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentTaskID') is not None:
            self.deployment_task_id = m.get('deploymentTaskID')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('traceID') is not None:
            self.trace_id = m.get('traceID')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class DeployOllamaModelOutput(TeaModel):
    def __init__(
        self,
        data: DeployOllamaModelOutputData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeployOllamaModelOutputData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeploySGLangModelAsyncOutput(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeploySGLangModelInputConcurrencyConfig(TeaModel):
    def __init__(
        self,
        reserved_concurrency: int = None,
    ):
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class DeploySGLangModelInputGpuConfig(TeaModel):
    def __init__(
        self,
        gpu_memory_size: int = None,
        gpu_type: str = None,
    ):
        self.gpu_memory_size = gpu_memory_size
        self.gpu_type = gpu_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        return self


class DeploySGLangModelInputHttpTriggerTriggerConfig(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        disable_urlinternet: bool = None,
        dsable_urlinternet: bool = None,
        methods: List[str] = None,
    ):
        self.auth_type = auth_type
        self.disable_urlinternet = disable_urlinternet
        self.dsable_urlinternet = dsable_urlinternet
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet
        if self.dsable_urlinternet is not None:
            result['dsableURLInternet'] = self.dsable_urlinternet
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')
        if m.get('dsableURLInternet') is not None:
            self.dsable_urlinternet = m.get('dsableURLInternet')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class DeploySGLangModelInputHttpTrigger(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
        trigger_config: DeploySGLangModelInputHttpTriggerTriggerConfig = None,
    ):
        self.qualifier = qualifier
        self.trigger_config = trigger_config

    def validate(self):
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('triggerConfig') is not None:
            temp_model = DeploySGLangModelInputHttpTriggerTriggerConfig()
            self.trigger_config = temp_model.from_map(m['triggerConfig'])
        return self


class DeploySGLangModelInputLogConfig(TeaModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        self.enable_instance_metrics = enable_instance_metrics
        self.enable_request_metrics = enable_request_metrics
        self.log_begin_rule = log_begin_rule
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics
        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics
        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')
        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')
        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class DeploySGLangModelInputModelConfigFmkSGLangConfig(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        chat_template: str = None,
        dtype: str = None,
        full_text_postfix: str = None,
        load_format: str = None,
        max_running_requests: int = None,
        max_total_tokens: int = None,
        mem_fraction_static: float = None,
        quantization: str = None,
        served_model_name: str = None,
    ):
        self.api_key = api_key
        self.chat_template = chat_template
        self.dtype = dtype
        self.full_text_postfix = full_text_postfix
        self.load_format = load_format
        self.max_running_requests = max_running_requests
        self.max_total_tokens = max_total_tokens
        self.mem_fraction_static = mem_fraction_static
        self.quantization = quantization
        self.served_model_name = served_model_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['apiKey'] = self.api_key
        if self.chat_template is not None:
            result['chatTemplate'] = self.chat_template
        if self.dtype is not None:
            result['dtype'] = self.dtype
        if self.full_text_postfix is not None:
            result['fullTextPostfix'] = self.full_text_postfix
        if self.load_format is not None:
            result['loadFormat'] = self.load_format
        if self.max_running_requests is not None:
            result['maxRunningRequests'] = self.max_running_requests
        if self.max_total_tokens is not None:
            result['maxTotalTokens'] = self.max_total_tokens
        if self.mem_fraction_static is not None:
            result['memFractionStatic'] = self.mem_fraction_static
        if self.quantization is not None:
            result['quantization'] = self.quantization
        if self.served_model_name is not None:
            result['servedModelName'] = self.served_model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')
        if m.get('chatTemplate') is not None:
            self.chat_template = m.get('chatTemplate')
        if m.get('dtype') is not None:
            self.dtype = m.get('dtype')
        if m.get('fullTextPostfix') is not None:
            self.full_text_postfix = m.get('fullTextPostfix')
        if m.get('loadFormat') is not None:
            self.load_format = m.get('loadFormat')
        if m.get('maxRunningRequests') is not None:
            self.max_running_requests = m.get('maxRunningRequests')
        if m.get('maxTotalTokens') is not None:
            self.max_total_tokens = m.get('maxTotalTokens')
        if m.get('memFractionStatic') is not None:
            self.mem_fraction_static = m.get('memFractionStatic')
        if m.get('quantization') is not None:
            self.quantization = m.get('quantization')
        if m.get('servedModelName') is not None:
            self.served_model_name = m.get('servedModelName')
        return self


class DeploySGLangModelInputModelConfig(TeaModel):
    def __init__(
        self,
        fmk_sglang_config: DeploySGLangModelInputModelConfigFmkSGLangConfig = None,
        framework: str = None,
        multi_model_config: List[ModelConfig] = None,
        prefix: str = None,
        source_type: str = None,
        src_model_scope_model_id: str = None,
        src_model_scope_model_revision: str = None,
        src_model_scope_token: str = None,
        src_oss_bucket: str = None,
        src_oss_path: str = None,
        src_oss_region: str = None,
        sync_strategy: str = None,
    ):
        self.fmk_sglang_config = fmk_sglang_config
        self.framework = framework
        self.multi_model_config = multi_model_config
        self.prefix = prefix
        self.source_type = source_type
        self.src_model_scope_model_id = src_model_scope_model_id
        self.src_model_scope_model_revision = src_model_scope_model_revision
        self.src_model_scope_token = src_model_scope_token
        self.src_oss_bucket = src_oss_bucket
        self.src_oss_path = src_oss_path
        self.src_oss_region = src_oss_region
        self.sync_strategy = sync_strategy

    def validate(self):
        if self.fmk_sglang_config:
            self.fmk_sglang_config.validate()
        if self.multi_model_config:
            for k in self.multi_model_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fmk_sglang_config is not None:
            result['fmkSGLangConfig'] = self.fmk_sglang_config.to_map()
        if self.framework is not None:
            result['framework'] = self.framework
        result['multiModelConfig'] = []
        if self.multi_model_config is not None:
            for k in self.multi_model_config:
                result['multiModelConfig'].append(k.to_map() if k else None)
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.src_model_scope_model_id is not None:
            result['srcModelScopeModelID'] = self.src_model_scope_model_id
        if self.src_model_scope_model_revision is not None:
            result['srcModelScopeModelRevision'] = self.src_model_scope_model_revision
        if self.src_model_scope_token is not None:
            result['srcModelScopeToken'] = self.src_model_scope_token
        if self.src_oss_bucket is not None:
            result['srcOssBucket'] = self.src_oss_bucket
        if self.src_oss_path is not None:
            result['srcOssPath'] = self.src_oss_path
        if self.src_oss_region is not None:
            result['srcOssRegion'] = self.src_oss_region
        if self.sync_strategy is not None:
            result['syncStrategy'] = self.sync_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fmkSGLangConfig') is not None:
            temp_model = DeploySGLangModelInputModelConfigFmkSGLangConfig()
            self.fmk_sglang_config = temp_model.from_map(m['fmkSGLangConfig'])
        if m.get('framework') is not None:
            self.framework = m.get('framework')
        self.multi_model_config = []
        if m.get('multiModelConfig') is not None:
            for k in m.get('multiModelConfig'):
                temp_model = ModelConfig()
                self.multi_model_config.append(temp_model.from_map(k))
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('srcModelScopeModelID') is not None:
            self.src_model_scope_model_id = m.get('srcModelScopeModelID')
        if m.get('srcModelScopeModelRevision') is not None:
            self.src_model_scope_model_revision = m.get('srcModelScopeModelRevision')
        if m.get('srcModelScopeToken') is not None:
            self.src_model_scope_token = m.get('srcModelScopeToken')
        if m.get('srcOssBucket') is not None:
            self.src_oss_bucket = m.get('srcOssBucket')
        if m.get('srcOssPath') is not None:
            self.src_oss_path = m.get('srcOssPath')
        if m.get('srcOssRegion') is not None:
            self.src_oss_region = m.get('srcOssRegion')
        if m.get('syncStrategy') is not None:
            self.sync_strategy = m.get('syncStrategy')
        return self


class DeploySGLangModelInputNasConfigMountPoints(TeaModel):
    def __init__(
        self,
        enable_tls: bool = None,
        mount_dir: str = None,
        server_addr: str = None,
    ):
        self.enable_tls = enable_tls
        self.mount_dir = mount_dir
        self.server_addr = server_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tls is not None:
            result['enableTLS'] = self.enable_tls
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir
        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableTLS') is not None:
            self.enable_tls = m.get('enableTLS')
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')
        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')
        return self


class DeploySGLangModelInputNasConfig(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[DeploySGLangModelInputNasConfigMountPoints] = None,
        user_id: int = None,
    ):
        self.group_id = group_id
        self.mount_points = mount_points
        self.user_id = user_id

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['mountPoints'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k in m.get('mountPoints'):
                temp_model = DeploySGLangModelInputNasConfigMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeploySGLangModelInputProvisionConfigScheduledActions(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.schedule_expression = schedule_expression
        self.start_time = start_time
        self.target = target
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class DeploySGLangModelInputProvisionConfig(TeaModel):
    def __init__(
        self,
        always_allocate_gpu: bool = None,
        scheduled_actions: List[DeploySGLangModelInputProvisionConfigScheduledActions] = None,
        target: int = None,
    ):
        self.always_allocate_gpu = always_allocate_gpu
        self.scheduled_actions = scheduled_actions
        self.target = target

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_gpu is not None:
            result['alwaysAllocateGPU'] = self.always_allocate_gpu
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateGPU') is not None:
            self.always_allocate_gpu = m.get('alwaysAllocateGPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = DeploySGLangModelInputProvisionConfigScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class DeploySGLangModelInputVpcConfig(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class DeploySGLangModelInput(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        concurrency_config: DeploySGLangModelInputConcurrencyConfig = None,
        cpu: float = None,
        description: str = None,
        disk_size: int = None,
        env_name: str = None,
        environment_variables: Dict[str, Any] = None,
        gpu_config: DeploySGLangModelInputGpuConfig = None,
        http_trigger: DeploySGLangModelInputHttpTrigger = None,
        image_name: str = None,
        instance_concurrency: int = None,
        log_config: DeploySGLangModelInputLogConfig = None,
        memory_size: int = None,
        model_config: DeploySGLangModelInputModelConfig = None,
        name: str = None,
        nas_config: DeploySGLangModelInputNasConfig = None,
        original_name: str = None,
        project_name: str = None,
        provision_config: DeploySGLangModelInputProvisionConfig = None,
        region: str = None,
        report_status_url: str = None,
        role: str = None,
        timeout: int = None,
        trace_id: str = None,
        vpc_config: DeploySGLangModelInputVpcConfig = None,
    ):
        self.account_id = account_id
        self.concurrency_config = concurrency_config
        self.cpu = cpu
        self.description = description
        self.disk_size = disk_size
        self.env_name = env_name
        self.environment_variables = environment_variables
        self.gpu_config = gpu_config
        self.http_trigger = http_trigger
        self.image_name = image_name
        self.instance_concurrency = instance_concurrency
        self.log_config = log_config
        self.memory_size = memory_size
        self.model_config = model_config
        # This parameter is required.
        self.name = name
        self.nas_config = nas_config
        self.original_name = original_name
        self.project_name = project_name
        self.provision_config = provision_config
        self.region = region
        self.report_status_url = report_status_url
        # This parameter is required.
        self.role = role
        self.timeout = timeout
        self.trace_id = trace_id
        self.vpc_config = vpc_config

    def validate(self):
        if self.concurrency_config:
            self.concurrency_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.http_trigger:
            self.http_trigger.validate()
        if self.log_config:
            self.log_config.validate()
        if self.model_config:
            self.model_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.provision_config:
            self.provision_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountID'] = self.account_id
        if self.concurrency_config is not None:
            result['concurrencyConfig'] = self.concurrency_config.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.http_trigger is not None:
            result['httpTrigger'] = self.http_trigger.to_map()
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.original_name is not None:
            result['originalName'] = self.original_name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.provision_config is not None:
            result['provisionConfig'] = self.provision_config.to_map()
        if self.region is not None:
            result['region'] = self.region
        if self.report_status_url is not None:
            result['reportStatusURL'] = self.report_status_url
        if self.role is not None:
            result['role'] = self.role
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountID') is not None:
            self.account_id = m.get('accountID')
        if m.get('concurrencyConfig') is not None:
            temp_model = DeploySGLangModelInputConcurrencyConfig()
            self.concurrency_config = temp_model.from_map(m['concurrencyConfig'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuConfig') is not None:
            temp_model = DeploySGLangModelInputGpuConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('httpTrigger') is not None:
            temp_model = DeploySGLangModelInputHttpTrigger()
            self.http_trigger = temp_model.from_map(m['httpTrigger'])
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('logConfig') is not None:
            temp_model = DeploySGLangModelInputLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('modelConfig') is not None:
            temp_model = DeploySGLangModelInputModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nasConfig') is not None:
            temp_model = DeploySGLangModelInputNasConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('originalName') is not None:
            self.original_name = m.get('originalName')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('provisionConfig') is not None:
            temp_model = DeploySGLangModelInputProvisionConfig()
            self.provision_config = temp_model.from_map(m['provisionConfig'])
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('reportStatusURL') is not None:
            self.report_status_url = m.get('reportStatusURL')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('vpcConfig') is not None:
            temp_model = DeploySGLangModelInputVpcConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class DeploySGLangModelOutputData(TeaModel):
    def __init__(
        self,
        deployment_task_id: str = None,
        error_message: str = None,
        finished: bool = None,
        model_name: str = None,
        service_name: str = None,
        trace_id: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        self.deployment_task_id = deployment_task_id
        self.error_message = error_message
        self.finished = finished
        self.model_name = model_name
        self.service_name = service_name
        self.trace_id = trace_id
        self.url_internet = url_internet
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_task_id is not None:
            result['deploymentTaskID'] = self.deployment_task_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.finished is not None:
            result['finished'] = self.finished
        if self.model_name is not None:
            result['modelName'] = self.model_name
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.trace_id is not None:
            result['traceID'] = self.trace_id
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentTaskID') is not None:
            self.deployment_task_id = m.get('deploymentTaskID')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('traceID') is not None:
            self.trace_id = m.get('traceID')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class DeploySGLangModelOutput(TeaModel):
    def __init__(
        self,
        data: DeploySGLangModelOutputData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeploySGLangModelOutputData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployTensorRtModelAsyncOutput(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployTensorRtModelInputConcurrencyConfig(TeaModel):
    def __init__(
        self,
        reserved_concurrency: int = None,
    ):
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class DeployTensorRtModelInputGpuConfig(TeaModel):
    def __init__(
        self,
        gpu_memory_size: int = None,
        gpu_type: str = None,
    ):
        self.gpu_memory_size = gpu_memory_size
        self.gpu_type = gpu_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        return self


class DeployTensorRtModelInputHttpTriggerTriggerConfig(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        disable_urlinternet: bool = None,
        dsable_urlinternet: bool = None,
        methods: List[str] = None,
    ):
        self.auth_type = auth_type
        self.disable_urlinternet = disable_urlinternet
        self.dsable_urlinternet = dsable_urlinternet
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet
        if self.dsable_urlinternet is not None:
            result['dsableURLInternet'] = self.dsable_urlinternet
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')
        if m.get('dsableURLInternet') is not None:
            self.dsable_urlinternet = m.get('dsableURLInternet')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class DeployTensorRtModelInputHttpTrigger(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
        trigger_config: DeployTensorRtModelInputHttpTriggerTriggerConfig = None,
    ):
        self.qualifier = qualifier
        self.trigger_config = trigger_config

    def validate(self):
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('triggerConfig') is not None:
            temp_model = DeployTensorRtModelInputHttpTriggerTriggerConfig()
            self.trigger_config = temp_model.from_map(m['triggerConfig'])
        return self


class DeployTensorRtModelInputLogConfig(TeaModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        self.enable_instance_metrics = enable_instance_metrics
        self.enable_request_metrics = enable_request_metrics
        self.log_begin_rule = log_begin_rule
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics
        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics
        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')
        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')
        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class DeployTensorRtModelInputModelConfig(TeaModel):
    def __init__(
        self,
        framework: str = None,
        multi_model_config: List[ModelConfig] = None,
        prefix: str = None,
        source_type: str = None,
        src_model_scope_model_id: str = None,
        src_model_scope_model_revision: str = None,
        src_model_scope_token: str = None,
        src_oss_bucket: str = None,
        src_oss_path: str = None,
        src_oss_region: str = None,
        sync_strategy: str = None,
    ):
        self.framework = framework
        self.multi_model_config = multi_model_config
        self.prefix = prefix
        self.source_type = source_type
        self.src_model_scope_model_id = src_model_scope_model_id
        self.src_model_scope_model_revision = src_model_scope_model_revision
        self.src_model_scope_token = src_model_scope_token
        self.src_oss_bucket = src_oss_bucket
        self.src_oss_path = src_oss_path
        self.src_oss_region = src_oss_region
        self.sync_strategy = sync_strategy

    def validate(self):
        if self.multi_model_config:
            for k in self.multi_model_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.framework is not None:
            result['framework'] = self.framework
        result['multiModelConfig'] = []
        if self.multi_model_config is not None:
            for k in self.multi_model_config:
                result['multiModelConfig'].append(k.to_map() if k else None)
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.src_model_scope_model_id is not None:
            result['srcModelScopeModelID'] = self.src_model_scope_model_id
        if self.src_model_scope_model_revision is not None:
            result['srcModelScopeModelRevision'] = self.src_model_scope_model_revision
        if self.src_model_scope_token is not None:
            result['srcModelScopeToken'] = self.src_model_scope_token
        if self.src_oss_bucket is not None:
            result['srcOssBucket'] = self.src_oss_bucket
        if self.src_oss_path is not None:
            result['srcOssPath'] = self.src_oss_path
        if self.src_oss_region is not None:
            result['srcOssRegion'] = self.src_oss_region
        if self.sync_strategy is not None:
            result['syncStrategy'] = self.sync_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('framework') is not None:
            self.framework = m.get('framework')
        self.multi_model_config = []
        if m.get('multiModelConfig') is not None:
            for k in m.get('multiModelConfig'):
                temp_model = ModelConfig()
                self.multi_model_config.append(temp_model.from_map(k))
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('srcModelScopeModelID') is not None:
            self.src_model_scope_model_id = m.get('srcModelScopeModelID')
        if m.get('srcModelScopeModelRevision') is not None:
            self.src_model_scope_model_revision = m.get('srcModelScopeModelRevision')
        if m.get('srcModelScopeToken') is not None:
            self.src_model_scope_token = m.get('srcModelScopeToken')
        if m.get('srcOssBucket') is not None:
            self.src_oss_bucket = m.get('srcOssBucket')
        if m.get('srcOssPath') is not None:
            self.src_oss_path = m.get('srcOssPath')
        if m.get('srcOssRegion') is not None:
            self.src_oss_region = m.get('srcOssRegion')
        if m.get('syncStrategy') is not None:
            self.sync_strategy = m.get('syncStrategy')
        return self


class DeployTensorRtModelInputNasConfigMountPoints(TeaModel):
    def __init__(
        self,
        enable_tls: bool = None,
        mount_dir: str = None,
        server_addr: str = None,
    ):
        self.enable_tls = enable_tls
        self.mount_dir = mount_dir
        self.server_addr = server_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tls is not None:
            result['enableTLS'] = self.enable_tls
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir
        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableTLS') is not None:
            self.enable_tls = m.get('enableTLS')
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')
        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')
        return self


class DeployTensorRtModelInputNasConfig(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[DeployTensorRtModelInputNasConfigMountPoints] = None,
        user_id: int = None,
    ):
        self.group_id = group_id
        self.mount_points = mount_points
        self.user_id = user_id

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['mountPoints'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k in m.get('mountPoints'):
                temp_model = DeployTensorRtModelInputNasConfigMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeployTensorRtModelInputProvisionConfigScheduledActions(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.schedule_expression = schedule_expression
        self.start_time = start_time
        self.target = target
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class DeployTensorRtModelInputProvisionConfig(TeaModel):
    def __init__(
        self,
        always_allocate_gpu: bool = None,
        scheduled_actions: List[DeployTensorRtModelInputProvisionConfigScheduledActions] = None,
        target: int = None,
    ):
        self.always_allocate_gpu = always_allocate_gpu
        self.scheduled_actions = scheduled_actions
        self.target = target

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_gpu is not None:
            result['alwaysAllocateGPU'] = self.always_allocate_gpu
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateGPU') is not None:
            self.always_allocate_gpu = m.get('alwaysAllocateGPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = DeployTensorRtModelInputProvisionConfigScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class DeployTensorRtModelInputVpcConfig(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class DeployTensorRtModelInput(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        concurrency_config: DeployTensorRtModelInputConcurrencyConfig = None,
        cpu: float = None,
        description: str = None,
        disk_size: int = None,
        env_name: str = None,
        environment_variables: Dict[str, Any] = None,
        gpu_config: DeployTensorRtModelInputGpuConfig = None,
        http_trigger: DeployTensorRtModelInputHttpTrigger = None,
        image_name: str = None,
        instance_concurrency: int = None,
        log_config: DeployTensorRtModelInputLogConfig = None,
        memory_size: int = None,
        model_config: DeployTensorRtModelInputModelConfig = None,
        name: str = None,
        nas_config: DeployTensorRtModelInputNasConfig = None,
        original_name: str = None,
        project_name: str = None,
        provision_config: DeployTensorRtModelInputProvisionConfig = None,
        region: str = None,
        report_status_url: str = None,
        role: str = None,
        timeout: int = None,
        trace_id: str = None,
        vpc_config: DeployTensorRtModelInputVpcConfig = None,
    ):
        self.account_id = account_id
        self.concurrency_config = concurrency_config
        self.cpu = cpu
        self.description = description
        self.disk_size = disk_size
        self.env_name = env_name
        self.environment_variables = environment_variables
        self.gpu_config = gpu_config
        self.http_trigger = http_trigger
        self.image_name = image_name
        self.instance_concurrency = instance_concurrency
        self.log_config = log_config
        self.memory_size = memory_size
        self.model_config = model_config
        # This parameter is required.
        self.name = name
        self.nas_config = nas_config
        self.original_name = original_name
        self.project_name = project_name
        self.provision_config = provision_config
        self.region = region
        self.report_status_url = report_status_url
        # This parameter is required.
        self.role = role
        self.timeout = timeout
        self.trace_id = trace_id
        self.vpc_config = vpc_config

    def validate(self):
        if self.concurrency_config:
            self.concurrency_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.http_trigger:
            self.http_trigger.validate()
        if self.log_config:
            self.log_config.validate()
        if self.model_config:
            self.model_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.provision_config:
            self.provision_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountID'] = self.account_id
        if self.concurrency_config is not None:
            result['concurrencyConfig'] = self.concurrency_config.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.http_trigger is not None:
            result['httpTrigger'] = self.http_trigger.to_map()
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.original_name is not None:
            result['originalName'] = self.original_name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.provision_config is not None:
            result['provisionConfig'] = self.provision_config.to_map()
        if self.region is not None:
            result['region'] = self.region
        if self.report_status_url is not None:
            result['reportStatusURL'] = self.report_status_url
        if self.role is not None:
            result['role'] = self.role
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountID') is not None:
            self.account_id = m.get('accountID')
        if m.get('concurrencyConfig') is not None:
            temp_model = DeployTensorRtModelInputConcurrencyConfig()
            self.concurrency_config = temp_model.from_map(m['concurrencyConfig'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuConfig') is not None:
            temp_model = DeployTensorRtModelInputGpuConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('httpTrigger') is not None:
            temp_model = DeployTensorRtModelInputHttpTrigger()
            self.http_trigger = temp_model.from_map(m['httpTrigger'])
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('logConfig') is not None:
            temp_model = DeployTensorRtModelInputLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('modelConfig') is not None:
            temp_model = DeployTensorRtModelInputModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nasConfig') is not None:
            temp_model = DeployTensorRtModelInputNasConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('originalName') is not None:
            self.original_name = m.get('originalName')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('provisionConfig') is not None:
            temp_model = DeployTensorRtModelInputProvisionConfig()
            self.provision_config = temp_model.from_map(m['provisionConfig'])
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('reportStatusURL') is not None:
            self.report_status_url = m.get('reportStatusURL')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('vpcConfig') is not None:
            temp_model = DeployTensorRtModelInputVpcConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class DeployTensorRtModelOutputData(TeaModel):
    def __init__(
        self,
        deployment_task_id: str = None,
        error_message: str = None,
        finished: bool = None,
        service_name: str = None,
        trace_id: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        self.deployment_task_id = deployment_task_id
        self.error_message = error_message
        self.finished = finished
        self.service_name = service_name
        self.trace_id = trace_id
        self.url_internet = url_internet
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_task_id is not None:
            result['deploymentTaskID'] = self.deployment_task_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.finished is not None:
            result['finished'] = self.finished
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.trace_id is not None:
            result['traceID'] = self.trace_id
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentTaskID') is not None:
            self.deployment_task_id = m.get('deploymentTaskID')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('traceID') is not None:
            self.trace_id = m.get('traceID')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class DeployTensorRtModelOutput(TeaModel):
    def __init__(
        self,
        data: DeployTensorRtModelOutputData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeployTensorRtModelOutputData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployVllmModelAsyncOutput(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployVllmModelInputConcurrencyConfig(TeaModel):
    def __init__(
        self,
        reserved_concurrency: int = None,
    ):
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class DeployVllmModelInputGpuConfig(TeaModel):
    def __init__(
        self,
        gpu_memory_size: int = None,
        gpu_type: str = None,
    ):
        self.gpu_memory_size = gpu_memory_size
        self.gpu_type = gpu_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        return self


class DeployVllmModelInputHttpTriggerTriggerConfig(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        disable_urlinternet: bool = None,
        dsable_urlinternet: bool = None,
        methods: List[str] = None,
    ):
        self.auth_type = auth_type
        self.disable_urlinternet = disable_urlinternet
        self.dsable_urlinternet = dsable_urlinternet
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet
        if self.dsable_urlinternet is not None:
            result['dsableURLInternet'] = self.dsable_urlinternet
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')
        if m.get('dsableURLInternet') is not None:
            self.dsable_urlinternet = m.get('dsableURLInternet')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class DeployVllmModelInputHttpTrigger(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
        trigger_config: DeployVllmModelInputHttpTriggerTriggerConfig = None,
    ):
        self.qualifier = qualifier
        self.trigger_config = trigger_config

    def validate(self):
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('triggerConfig') is not None:
            temp_model = DeployVllmModelInputHttpTriggerTriggerConfig()
            self.trigger_config = temp_model.from_map(m['triggerConfig'])
        return self


class DeployVllmModelInputLogConfig(TeaModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        self.enable_instance_metrics = enable_instance_metrics
        self.enable_request_metrics = enable_request_metrics
        self.log_begin_rule = log_begin_rule
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics
        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics
        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')
        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')
        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class DeployVllmModelInputModelConfigFmkVllmConfig(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        block_size: int = None,
        chat_template: str = None,
        dtype: str = None,
        full_text_postfix: str = None,
        gpu_memory_utilization: float = None,
        load_format: str = None,
        max_model_len: int = None,
        max_parallel_loading_workers: int = None,
        quantization: str = None,
        served_model_name: str = None,
        swap_space: int = None,
    ):
        self.api_key = api_key
        self.block_size = block_size
        self.chat_template = chat_template
        self.dtype = dtype
        self.full_text_postfix = full_text_postfix
        self.gpu_memory_utilization = gpu_memory_utilization
        self.load_format = load_format
        self.max_model_len = max_model_len
        self.max_parallel_loading_workers = max_parallel_loading_workers
        self.quantization = quantization
        self.served_model_name = served_model_name
        self.swap_space = swap_space

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['apiKey'] = self.api_key
        if self.block_size is not None:
            result['blockSize'] = self.block_size
        if self.chat_template is not None:
            result['chatTemplate'] = self.chat_template
        if self.dtype is not None:
            result['dtype'] = self.dtype
        if self.full_text_postfix is not None:
            result['fullTextPostfix'] = self.full_text_postfix
        if self.gpu_memory_utilization is not None:
            result['gpuMemoryUtilization'] = self.gpu_memory_utilization
        if self.load_format is not None:
            result['loadFormat'] = self.load_format
        if self.max_model_len is not None:
            result['maxModelLen'] = self.max_model_len
        if self.max_parallel_loading_workers is not None:
            result['maxParallelLoadingWorkers'] = self.max_parallel_loading_workers
        if self.quantization is not None:
            result['quantization'] = self.quantization
        if self.served_model_name is not None:
            result['servedModelName'] = self.served_model_name
        if self.swap_space is not None:
            result['swapSpace'] = self.swap_space
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')
        if m.get('blockSize') is not None:
            self.block_size = m.get('blockSize')
        if m.get('chatTemplate') is not None:
            self.chat_template = m.get('chatTemplate')
        if m.get('dtype') is not None:
            self.dtype = m.get('dtype')
        if m.get('fullTextPostfix') is not None:
            self.full_text_postfix = m.get('fullTextPostfix')
        if m.get('gpuMemoryUtilization') is not None:
            self.gpu_memory_utilization = m.get('gpuMemoryUtilization')
        if m.get('loadFormat') is not None:
            self.load_format = m.get('loadFormat')
        if m.get('maxModelLen') is not None:
            self.max_model_len = m.get('maxModelLen')
        if m.get('maxParallelLoadingWorkers') is not None:
            self.max_parallel_loading_workers = m.get('maxParallelLoadingWorkers')
        if m.get('quantization') is not None:
            self.quantization = m.get('quantization')
        if m.get('servedModelName') is not None:
            self.served_model_name = m.get('servedModelName')
        if m.get('swapSpace') is not None:
            self.swap_space = m.get('swapSpace')
        return self


class DeployVllmModelInputModelConfig(TeaModel):
    def __init__(
        self,
        fmk_vllm_config: DeployVllmModelInputModelConfigFmkVllmConfig = None,
        framework: str = None,
        multi_model_config: List[ModelConfig] = None,
        prefix: str = None,
        source_type: str = None,
        src_model_scope_model_id: str = None,
        src_model_scope_model_revision: str = None,
        src_model_scope_token: str = None,
        src_oss_bucket: str = None,
        src_oss_path: str = None,
        src_oss_region: str = None,
        sync_strategy: str = None,
    ):
        self.fmk_vllm_config = fmk_vllm_config
        self.framework = framework
        self.multi_model_config = multi_model_config
        self.prefix = prefix
        self.source_type = source_type
        self.src_model_scope_model_id = src_model_scope_model_id
        self.src_model_scope_model_revision = src_model_scope_model_revision
        self.src_model_scope_token = src_model_scope_token
        self.src_oss_bucket = src_oss_bucket
        self.src_oss_path = src_oss_path
        self.src_oss_region = src_oss_region
        self.sync_strategy = sync_strategy

    def validate(self):
        if self.fmk_vllm_config:
            self.fmk_vllm_config.validate()
        if self.multi_model_config:
            for k in self.multi_model_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fmk_vllm_config is not None:
            result['fmkVllmConfig'] = self.fmk_vllm_config.to_map()
        if self.framework is not None:
            result['framework'] = self.framework
        result['multiModelConfig'] = []
        if self.multi_model_config is not None:
            for k in self.multi_model_config:
                result['multiModelConfig'].append(k.to_map() if k else None)
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.src_model_scope_model_id is not None:
            result['srcModelScopeModelID'] = self.src_model_scope_model_id
        if self.src_model_scope_model_revision is not None:
            result['srcModelScopeModelRevision'] = self.src_model_scope_model_revision
        if self.src_model_scope_token is not None:
            result['srcModelScopeToken'] = self.src_model_scope_token
        if self.src_oss_bucket is not None:
            result['srcOssBucket'] = self.src_oss_bucket
        if self.src_oss_path is not None:
            result['srcOssPath'] = self.src_oss_path
        if self.src_oss_region is not None:
            result['srcOssRegion'] = self.src_oss_region
        if self.sync_strategy is not None:
            result['syncStrategy'] = self.sync_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fmkVllmConfig') is not None:
            temp_model = DeployVllmModelInputModelConfigFmkVllmConfig()
            self.fmk_vllm_config = temp_model.from_map(m['fmkVllmConfig'])
        if m.get('framework') is not None:
            self.framework = m.get('framework')
        self.multi_model_config = []
        if m.get('multiModelConfig') is not None:
            for k in m.get('multiModelConfig'):
                temp_model = ModelConfig()
                self.multi_model_config.append(temp_model.from_map(k))
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('srcModelScopeModelID') is not None:
            self.src_model_scope_model_id = m.get('srcModelScopeModelID')
        if m.get('srcModelScopeModelRevision') is not None:
            self.src_model_scope_model_revision = m.get('srcModelScopeModelRevision')
        if m.get('srcModelScopeToken') is not None:
            self.src_model_scope_token = m.get('srcModelScopeToken')
        if m.get('srcOssBucket') is not None:
            self.src_oss_bucket = m.get('srcOssBucket')
        if m.get('srcOssPath') is not None:
            self.src_oss_path = m.get('srcOssPath')
        if m.get('srcOssRegion') is not None:
            self.src_oss_region = m.get('srcOssRegion')
        if m.get('syncStrategy') is not None:
            self.sync_strategy = m.get('syncStrategy')
        return self


class DeployVllmModelInputNasConfigMountPoints(TeaModel):
    def __init__(
        self,
        enable_tls: bool = None,
        mount_dir: str = None,
        server_addr: str = None,
    ):
        self.enable_tls = enable_tls
        self.mount_dir = mount_dir
        self.server_addr = server_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tls is not None:
            result['enableTLS'] = self.enable_tls
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir
        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableTLS') is not None:
            self.enable_tls = m.get('enableTLS')
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')
        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')
        return self


class DeployVllmModelInputNasConfig(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[DeployVllmModelInputNasConfigMountPoints] = None,
        user_id: int = None,
    ):
        self.group_id = group_id
        self.mount_points = mount_points
        self.user_id = user_id

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['mountPoints'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k in m.get('mountPoints'):
                temp_model = DeployVllmModelInputNasConfigMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeployVllmModelInputProvisionConfigScheduledActions(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.schedule_expression = schedule_expression
        self.start_time = start_time
        self.target = target
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class DeployVllmModelInputProvisionConfig(TeaModel):
    def __init__(
        self,
        always_allocate_gpu: bool = None,
        scheduled_actions: List[DeployVllmModelInputProvisionConfigScheduledActions] = None,
        target: int = None,
    ):
        self.always_allocate_gpu = always_allocate_gpu
        self.scheduled_actions = scheduled_actions
        self.target = target

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_gpu is not None:
            result['alwaysAllocateGPU'] = self.always_allocate_gpu
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateGPU') is not None:
            self.always_allocate_gpu = m.get('alwaysAllocateGPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = DeployVllmModelInputProvisionConfigScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class DeployVllmModelInputVpcConfig(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class DeployVllmModelInput(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        concurrency_config: DeployVllmModelInputConcurrencyConfig = None,
        cpu: float = None,
        description: str = None,
        disk_size: int = None,
        env_name: str = None,
        environment_variables: Dict[str, Any] = None,
        gpu_config: DeployVllmModelInputGpuConfig = None,
        http_trigger: DeployVllmModelInputHttpTrigger = None,
        image_name: str = None,
        instance_concurrency: int = None,
        log_config: DeployVllmModelInputLogConfig = None,
        memory_size: int = None,
        model_config: DeployVllmModelInputModelConfig = None,
        name: str = None,
        nas_config: DeployVllmModelInputNasConfig = None,
        original_name: str = None,
        project_name: str = None,
        provision_config: DeployVllmModelInputProvisionConfig = None,
        region: str = None,
        report_status_url: str = None,
        role: str = None,
        timeout: int = None,
        trace_id: str = None,
        vpc_config: DeployVllmModelInputVpcConfig = None,
    ):
        self.account_id = account_id
        self.concurrency_config = concurrency_config
        self.cpu = cpu
        self.description = description
        self.disk_size = disk_size
        self.env_name = env_name
        self.environment_variables = environment_variables
        self.gpu_config = gpu_config
        self.http_trigger = http_trigger
        self.image_name = image_name
        self.instance_concurrency = instance_concurrency
        self.log_config = log_config
        self.memory_size = memory_size
        self.model_config = model_config
        # This parameter is required.
        self.name = name
        self.nas_config = nas_config
        self.original_name = original_name
        self.project_name = project_name
        self.provision_config = provision_config
        self.region = region
        self.report_status_url = report_status_url
        # This parameter is required.
        self.role = role
        self.timeout = timeout
        self.trace_id = trace_id
        self.vpc_config = vpc_config

    def validate(self):
        if self.concurrency_config:
            self.concurrency_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.http_trigger:
            self.http_trigger.validate()
        if self.log_config:
            self.log_config.validate()
        if self.model_config:
            self.model_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.provision_config:
            self.provision_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountID'] = self.account_id
        if self.concurrency_config is not None:
            result['concurrencyConfig'] = self.concurrency_config.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.http_trigger is not None:
            result['httpTrigger'] = self.http_trigger.to_map()
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.original_name is not None:
            result['originalName'] = self.original_name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.provision_config is not None:
            result['provisionConfig'] = self.provision_config.to_map()
        if self.region is not None:
            result['region'] = self.region
        if self.report_status_url is not None:
            result['reportStatusURL'] = self.report_status_url
        if self.role is not None:
            result['role'] = self.role
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountID') is not None:
            self.account_id = m.get('accountID')
        if m.get('concurrencyConfig') is not None:
            temp_model = DeployVllmModelInputConcurrencyConfig()
            self.concurrency_config = temp_model.from_map(m['concurrencyConfig'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuConfig') is not None:
            temp_model = DeployVllmModelInputGpuConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('httpTrigger') is not None:
            temp_model = DeployVllmModelInputHttpTrigger()
            self.http_trigger = temp_model.from_map(m['httpTrigger'])
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('logConfig') is not None:
            temp_model = DeployVllmModelInputLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('modelConfig') is not None:
            temp_model = DeployVllmModelInputModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nasConfig') is not None:
            temp_model = DeployVllmModelInputNasConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('originalName') is not None:
            self.original_name = m.get('originalName')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('provisionConfig') is not None:
            temp_model = DeployVllmModelInputProvisionConfig()
            self.provision_config = temp_model.from_map(m['provisionConfig'])
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('reportStatusURL') is not None:
            self.report_status_url = m.get('reportStatusURL')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('vpcConfig') is not None:
            temp_model = DeployVllmModelInputVpcConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class DeployVllmModelOutputData(TeaModel):
    def __init__(
        self,
        deployment_task_id: str = None,
        error_message: str = None,
        finished: bool = None,
        model_name: str = None,
        service_name: str = None,
        trace_id: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        self.deployment_task_id = deployment_task_id
        self.error_message = error_message
        self.finished = finished
        self.model_name = model_name
        self.service_name = service_name
        self.trace_id = trace_id
        self.url_internet = url_internet
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_task_id is not None:
            result['deploymentTaskID'] = self.deployment_task_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.finished is not None:
            result['finished'] = self.finished
        if self.model_name is not None:
            result['modelName'] = self.model_name
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.trace_id is not None:
            result['traceID'] = self.trace_id
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentTaskID') is not None:
            self.deployment_task_id = m.get('deploymentTaskID')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('traceID') is not None:
            self.trace_id = m.get('traceID')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class DeployVllmModelOutput(TeaModel):
    def __init__(
        self,
        data: DeployVllmModelOutputData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeployVllmModelOutputData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DownloadModelOutputData(TeaModel):
    def __init__(
        self,
        model_path: str = None,
        task_type: str = None,
    ):
        self.model_path = model_path
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_path is not None:
            result['modelPath'] = self.model_path
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelPath') is not None:
            self.model_path = m.get('modelPath')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class DownloadModelOutput(TeaModel):
    def __init__(
        self,
        data: DownloadModelOutputData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        # This parameter is required.
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DownloadModelOutputData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class OssSourceConfig(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        object: str = None,
    ):
        self.bucket = bucket
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.object is not None:
            result['object'] = self.object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('object') is not None:
            self.object = m.get('object')
        return self


class EventFilterConfig(TeaModel):
    def __init__(
        self,
        branch: BranchFilter = None,
    ):
        self.branch = branch

    def validate(self):
        if self.branch:
            self.branch.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branch') is not None:
            temp_model = BranchFilter()
            self.branch = temp_model.from_map(m['branch'])
        return self


class RepositorySourceConfig(TeaModel):
    def __init__(
        self,
        code_version: CodeVersionReference = None,
        filter: EventFilterConfig = None,
        repository_name: str = None,
    ):
        self.code_version = code_version
        self.filter = filter
        # This parameter is required.
        self.repository_name = repository_name

    def validate(self):
        if self.code_version:
            self.code_version.validate()
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_version is not None:
            result['codeVersion'] = self.code_version.to_map()
        if self.filter is not None:
            result['filter'] = self.filter.to_map()
        if self.repository_name is not None:
            result['repositoryName'] = self.repository_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeVersion') is not None:
            temp_model = CodeVersionReference()
            self.code_version = temp_model.from_map(m['codeVersion'])
        if m.get('filter') is not None:
            temp_model = EventFilterConfig()
            self.filter = temp_model.from_map(m['filter'])
        if m.get('repositoryName') is not None:
            self.repository_name = m.get('repositoryName')
        return self


class TemplateSourceConfig(TeaModel):
    def __init__(
        self,
        download_url: str = None,
        name: str = None,
    ):
        self.download_url = download_url
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class SourceConfig(TeaModel):
    def __init__(
        self,
        oss: OssSourceConfig = None,
        repository: RepositorySourceConfig = None,
        template: TemplateSourceConfig = None,
    ):
        self.oss = oss
        self.repository = repository
        self.template = template

    def validate(self):
        if self.oss:
            self.oss.validate()
        if self.repository:
            self.repository.validate()
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss is not None:
            result['oss'] = self.oss.to_map()
        if self.repository is not None:
            result['repository'] = self.repository.to_map()
        if self.template is not None:
            result['template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oss') is not None:
            temp_model = OssSourceConfig()
            self.oss = temp_model.from_map(m['oss'])
        if m.get('repository') is not None:
            temp_model = RepositorySourceConfig()
            self.repository = temp_model.from_map(m['repository'])
        if m.get('template') is not None:
            temp_model = TemplateSourceConfig()
            self.template = temp_model.from_map(m['template'])
        return self


class Variable(TeaModel):
    def __init__(
        self,
        encrypted: bool = None,
        sensitive: bool = None,
        value: Any = None,
    ):
        self.encrypted = encrypted
        self.sensitive = sensitive
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.sensitive is not None:
            result['sensitive'] = self.sensitive
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ServiceConfig(TeaModel):
    def __init__(
        self,
        artifact: ArtifactMeta = None,
        build: BuildConfig = None,
        component: str = None,
        props: Dict[str, Any] = None,
        source: SourceConfig = None,
        type: str = None,
        variables: Dict[str, Variable] = None,
    ):
        self.artifact = artifact
        self.build = build
        self.component = component
        self.props = props
        self.source = source
        self.type = type
        self.variables = variables

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.build:
            self.build.validate()
        if self.source:
            self.source.validate()
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()
        if self.build is not None:
            result['build'] = self.build.to_map()
        if self.component is not None:
            result['component'] = self.component
        if self.props is not None:
            result['props'] = self.props
        if self.source is not None:
            result['source'] = self.source.to_map()
        if self.type is not None:
            result['type'] = self.type
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifact') is not None:
            temp_model = ArtifactMeta()
            self.artifact = temp_model.from_map(m['artifact'])
        if m.get('build') is not None:
            temp_model = BuildConfig()
            self.build = temp_model.from_map(m['build'])
        if m.get('component') is not None:
            self.component = m.get('component')
        if m.get('props') is not None:
            self.props = m.get('props')
        if m.get('source') is not None:
            temp_model = SourceConfig()
            self.source = temp_model.from_map(m['source'])
        if m.get('type') is not None:
            self.type = m.get('type')
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = Variable()
                self.variables[k] = temp_model.from_map(v)
        return self


class EnvironmentStagedConfigs(TeaModel):
    def __init__(
        self,
        services: Dict[str, ServiceConfig] = None,
        variables: Dict[str, Variable] = None,
    ):
        self.services = services
        self.variables = variables

    def validate(self):
        if self.services:
            for v in self.services.values():
                if v:
                    v.validate()
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['services'] = {}
        if self.services is not None:
            for k, v in self.services.items():
                result['services'][k] = v.to_map()
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.services = {}
        if m.get('services') is not None:
            for k, v in m.get('services').items():
                temp_model = ServiceConfig()
                self.services[k] = temp_model.from_map(v)
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = Variable()
                self.variables[k] = temp_model.from_map(v)
        return self


class EnvironmentSpec(TeaModel):
    def __init__(
        self,
        role_arn: str = None,
        staged_configs: EnvironmentStagedConfigs = None,
        type: str = None,
    ):
        self.role_arn = role_arn
        self.staged_configs = staged_configs
        self.type = type

    def validate(self):
        if self.staged_configs:
            self.staged_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.staged_configs is not None:
            result['stagedConfigs'] = self.staged_configs.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('stagedConfigs') is not None:
            temp_model = EnvironmentStagedConfigs()
            self.staged_configs = temp_model.from_map(m['stagedConfigs'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ServiceInstanceLatestDeployment(TeaModel):
    def __init__(
        self,
        finished_time: str = None,
        name: str = None,
        phase: str = None,
        start_time: str = None,
    ):
        self.finished_time = finished_time
        self.name = name
        self.phase = phase
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.name is not None:
            result['name'] = self.name
        if self.phase is not None:
            result['phase'] = self.phase
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ServiceInstance(TeaModel):
    def __init__(
        self,
        config: ServiceConfig = None,
        latest_deployment: ServiceInstanceLatestDeployment = None,
        outputs: Dict[str, Any] = None,
        variables: Dict[str, Variable] = None,
    ):
        self.config = config
        self.latest_deployment = latest_deployment
        self.outputs = outputs
        self.variables = variables

    def validate(self):
        if self.config:
            self.config.validate()
        if self.latest_deployment:
            self.latest_deployment.validate()
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.latest_deployment is not None:
            result['latestDeployment'] = self.latest_deployment.to_map()
        if self.outputs is not None:
            result['outputs'] = self.outputs
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = ServiceConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('latestDeployment') is not None:
            temp_model = ServiceInstanceLatestDeployment()
            self.latest_deployment = temp_model.from_map(m['latestDeployment'])
        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = Variable()
                self.variables[k] = temp_model.from_map(v)
        return self


class EnvironmentStatus(TeaModel):
    def __init__(
        self,
        latest_environment_deployment_name: str = None,
        observed_generation: int = None,
        observed_time: str = None,
        services_instances: Dict[str, ServiceInstance] = None,
        services_with_pending_changes: List[str] = None,
    ):
        self.latest_environment_deployment_name = latest_environment_deployment_name
        self.observed_generation = observed_generation
        self.observed_time = observed_time
        self.services_instances = services_instances
        self.services_with_pending_changes = services_with_pending_changes

    def validate(self):
        if self.services_instances:
            for v in self.services_instances.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latest_environment_deployment_name is not None:
            result['latestEnvironmentDeploymentName'] = self.latest_environment_deployment_name
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.observed_time is not None:
            result['observedTime'] = self.observed_time
        result['servicesInstances'] = {}
        if self.services_instances is not None:
            for k, v in self.services_instances.items():
                result['servicesInstances'][k] = v.to_map()
        if self.services_with_pending_changes is not None:
            result['servicesWithPendingChanges'] = self.services_with_pending_changes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latestEnvironmentDeploymentName') is not None:
            self.latest_environment_deployment_name = m.get('latestEnvironmentDeploymentName')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        self.services_instances = {}
        if m.get('servicesInstances') is not None:
            for k, v in m.get('servicesInstances').items():
                temp_model = ServiceInstance()
                self.services_instances[k] = temp_model.from_map(v)
        if m.get('servicesWithPendingChanges') is not None:
            self.services_with_pending_changes = m.get('servicesWithPendingChanges')
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
        if m.get('spec') is not None:
            temp_model = EnvironmentSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = EnvironmentStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class EnvironmentBaseline(TeaModel):
    def __init__(
        self,
        services_instances: Dict[str, ServiceInstance] = None,
        variables: Dict[str, Variable] = None,
    ):
        self.services_instances = services_instances
        self.variables = variables

    def validate(self):
        if self.services_instances:
            for v in self.services_instances.values():
                if v:
                    v.validate()
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['servicesInstances'] = {}
        if self.services_instances is not None:
            for k, v in self.services_instances.items():
                result['servicesInstances'][k] = v.to_map()
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.services_instances = {}
        if m.get('servicesInstances') is not None:
            for k, v in m.get('servicesInstances').items():
                temp_model = ServiceInstance()
                self.services_instances[k] = temp_model.from_map(v)
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = Variable()
                self.variables[k] = temp_model.from_map(v)
        return self


class EnvironmentChanges(TeaModel):
    def __init__(
        self,
        services: Dict[str, Any] = None,
    ):
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.services is not None:
            result['services'] = self.services
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('services') is not None:
            self.services = m.get('services')
        return self


class EnvironmentSnapshot(TeaModel):
    def __init__(
        self,
        services: Dict[str, ServiceInstance] = None,
    ):
        self.services = services

    def validate(self):
        if self.services:
            for v in self.services.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['services'] = {}
        if self.services is not None:
            for k, v in self.services.items():
                result['services'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.services = {}
        if m.get('services') is not None:
            for k, v in m.get('services').items():
                temp_model = ServiceInstance()
                self.services[k] = temp_model.from_map(v)
        return self


class WebhookCodeContext(TeaModel):
    def __init__(
        self,
        branch: str = None,
        commit_id: str = None,
        description: str = None,
        event_type: str = None,
        message: str = None,
        pr_type: str = None,
        repo_url: str = None,
        source_branch: str = None,
        tag: str = None,
        target_branch: str = None,
        title: str = None,
    ):
        self.branch = branch
        self.commit_id = commit_id
        self.description = description
        self.event_type = event_type
        self.message = message
        self.pr_type = pr_type
        self.repo_url = repo_url
        self.source_branch = source_branch
        self.tag = tag
        self.target_branch = target_branch
        self.title = title

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
        if self.description is not None:
            result['description'] = self.description
        if self.event_type is not None:
            result['eventType'] = self.event_type
        if self.message is not None:
            result['message'] = self.message
        if self.pr_type is not None:
            result['prType'] = self.pr_type
        if self.repo_url is not None:
            result['repoUrl'] = self.repo_url
        if self.source_branch is not None:
            result['sourceBranch'] = self.source_branch
        if self.tag is not None:
            result['tag'] = self.tag
        if self.target_branch is not None:
            result['targetBranch'] = self.target_branch
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commitID') is not None:
            self.commit_id = m.get('commitID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('prType') is not None:
            self.pr_type = m.get('prType')
        if m.get('repoUrl') is not None:
            self.repo_url = m.get('repoUrl')
        if m.get('sourceBranch') is not None:
            self.source_branch = m.get('sourceBranch')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('targetBranch') is not None:
            self.target_branch = m.get('targetBranch')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class EnvironmentDeploymentSpec(TeaModel):
    def __init__(
        self,
        baseline: EnvironmentSnapshot = None,
        changes: EnvironmentChanges = None,
        skip_remove_resources: bool = None,
        target: EnvironmentStagedConfigs = None,
        webhook_code_context: WebhookCodeContext = None,
    ):
        self.baseline = baseline
        self.changes = changes
        self.skip_remove_resources = skip_remove_resources
        self.target = target
        self.webhook_code_context = webhook_code_context

    def validate(self):
        if self.baseline:
            self.baseline.validate()
        if self.changes:
            self.changes.validate()
        if self.target:
            self.target.validate()
        if self.webhook_code_context:
            self.webhook_code_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline is not None:
            result['baseline'] = self.baseline.to_map()
        if self.changes is not None:
            result['changes'] = self.changes.to_map()
        if self.skip_remove_resources is not None:
            result['skipRemoveResources'] = self.skip_remove_resources
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.webhook_code_context is not None:
            result['webhookCodeContext'] = self.webhook_code_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseline') is not None:
            temp_model = EnvironmentSnapshot()
            self.baseline = temp_model.from_map(m['baseline'])
        if m.get('changes') is not None:
            temp_model = EnvironmentChanges()
            self.changes = temp_model.from_map(m['changes'])
        if m.get('skipRemoveResources') is not None:
            self.skip_remove_resources = m.get('skipRemoveResources')
        if m.get('target') is not None:
            temp_model = EnvironmentStagedConfigs()
            self.target = temp_model.from_map(m['target'])
        if m.get('webhookCodeContext') is not None:
            temp_model = WebhookCodeContext()
            self.webhook_code_context = temp_model.from_map(m['webhookCodeContext'])
        return self


class EnvironmentDeploymentStatus(TeaModel):
    def __init__(
        self,
        finished_time: str = None,
        phase: str = None,
        pipeline_name: str = None,
        service_deployments: Dict[str, str] = None,
    ):
        self.finished_time = finished_time
        self.phase = phase
        self.pipeline_name = pipeline_name
        self.service_deployments = service_deployments

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.phase is not None:
            result['phase'] = self.phase
        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name
        if self.service_deployments is not None:
            result['serviceDeployments'] = self.service_deployments
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')
        if m.get('serviceDeployments') is not None:
            self.service_deployments = m.get('serviceDeployments')
        return self


class EnvironmentDeployment(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        spec: EnvironmentDeploymentSpec = None,
        status: EnvironmentDeploymentStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.kind = kind
        self.labels = labels
        # This parameter is required.
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
        if self.description is not None:
            result['description'] = self.description
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
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
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = EnvironmentDeploymentSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = EnvironmentDeploymentStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class FinalizeConfig(TeaModel):
    def __init__(
        self,
        steps: List[Any] = None,
    ):
        self.steps = steps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.steps is not None:
            result['steps'] = self.steps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('steps') is not None:
            self.steps = m.get('steps')
        return self


class GetModelStatusOutputData(TeaModel):
    def __init__(
        self,
        current_bytes: int = None,
        err_message: str = None,
        file_size: int = None,
        finished: bool = None,
        finished_time: int = None,
        speed: int = None,
        start_time: int = None,
        total: int = None,
    ):
        self.current_bytes = current_bytes
        self.err_message = err_message
        self.file_size = file_size
        self.finished = finished
        self.finished_time = finished_time
        self.speed = speed
        self.start_time = start_time
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_bytes is not None:
            result['currentBytes'] = self.current_bytes
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.finished is not None:
            result['finished'] = self.finished
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.speed is not None:
            result['speed'] = self.speed
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentBytes') is not None:
            self.current_bytes = m.get('currentBytes')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('speed') is not None:
            self.speed = m.get('speed')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetModelStatusOutput(TeaModel):
    def __init__(
        self,
        data: GetModelStatusOutputData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetModelStatusOutputData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
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


class InitializeConfig(TeaModel):
    def __init__(
        self,
        steps: List[Any] = None,
    ):
        self.steps = steps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.steps is not None:
            result['steps'] = self.steps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('steps') is not None:
            self.steps = m.get('steps')
        return self


class MCPServerInstallationConfig(TeaModel):
    def __init__(
        self,
        args: str = None,
        command: str = None,
        env: Dict[str, str] = None,
        transport_type: str = None,
        url: str = None,
    ):
        self.args = args
        self.command = command
        self.env = env
        self.transport_type = transport_type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        if self.env is not None:
            result['env'] = self.env
        if self.transport_type is not None:
            result['transportType'] = self.transport_type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('env') is not None:
            self.env = m.get('env')
        if m.get('transportType') is not None:
            self.transport_type = m.get('transportType')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class MCPInstallationConfig(TeaModel):
    def __init__(
        self,
        mcp_servers: MCPServerInstallationConfig = None,
    ):
        self.mcp_servers = mcp_servers

    def validate(self):
        if self.mcp_servers:
            self.mcp_servers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mcp_servers is not None:
            result['mcpServers'] = self.mcp_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mcpServers') is not None:
            temp_model = MCPServerInstallationConfig()
            self.mcp_servers = temp_model.from_map(m['mcpServers'])
        return self


class ModelAsyncTask(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        finished: bool = None,
        finished_time: int = None,
        result: Any = None,
        start_time: int = None,
        task_type: str = None,
        update_time: int = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        self.finished = finished
        self.finished_time = finished_time
        self.result = result
        self.start_time = start_time
        self.task_type = task_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.finished is not None:
            result['finished'] = self.finished
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.result is not None:
            result['result'] = self.result
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ModelFile(TeaModel):
    def __init__(
        self,
        is_dir: bool = None,
        mode_time: int = None,
        name: str = None,
        path: str = None,
        size: int = None,
    ):
        self.is_dir = is_dir
        self.mode_time = mode_time
        self.name = name
        self.path = path
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.mode_time is not None:
            result['modeTime'] = self.mode_time
        if self.name is not None:
            result['name'] = self.name
        if self.path is not None:
            result['path'] = self.path
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('modeTime') is not None:
            self.mode_time = m.get('modeTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ModelFilePreview(TeaModel):
    def __init__(
        self,
        content: str = None,
        hash: str = None,
        is_compressed_image: bool = None,
        is_dir: bool = None,
        name: str = None,
        path: str = None,
        size: int = None,
        unpreviewable: bool = None,
    ):
        self.content = content
        self.hash = hash
        self.is_compressed_image = is_compressed_image
        self.is_dir = is_dir
        self.name = name
        self.path = path
        self.size = size
        self.unpreviewable = unpreviewable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.hash is not None:
            result['hash'] = self.hash
        if self.is_compressed_image is not None:
            result['isCompressedImage'] = self.is_compressed_image
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.path is not None:
            result['path'] = self.path
        if self.size is not None:
            result['size'] = self.size
        if self.unpreviewable is not None:
            result['unpreviewable'] = self.unpreviewable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('hash') is not None:
            self.hash = m.get('hash')
        if m.get('isCompressedImage') is not None:
            self.is_compressed_image = m.get('isCompressedImage')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('unpreviewable') is not None:
            self.unpreviewable = m.get('unpreviewable')
        return self


class ModelProvider(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ModelProviderAuthorization(TeaModel):
    def __init__(
        self,
        auth_config: Dict[str, str] = None,
        type: str = None,
    ):
        self.auth_config = auth_config
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            self.auth_config = m.get('authConfig')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ModelProviderSchema(TeaModel):
    def __init__(
        self,
        detail: str = None,
        type: str = None,
    ):
        self.detail = detail
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ModelProviderSpec(TeaModel):
    def __init__(
        self,
        authorization: ModelProviderAuthorization = None,
        schema: ModelProviderSchema = None,
    ):
        self.authorization = authorization
        self.schema = schema

    def validate(self):
        if self.authorization:
            self.authorization.validate()
        if self.schema:
            self.schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization is not None:
            result['authorization'] = self.authorization.to_map()
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorization') is not None:
            temp_model = ModelProviderAuthorization()
            self.authorization = temp_model.from_map(m['authorization'])
        if m.get('schema') is not None:
            temp_model = ModelProviderSchema()
            self.schema = temp_model.from_map(m['schema'])
        return self


class ModelTask(TeaModel):
    def __init__(
        self,
        current_bytes: str = None,
        err_code: str = None,
        err_msg: str = None,
        extra: Any = None,
        file_size: float = None,
        finish_time: float = None,
        finished: bool = None,
        finished_time: float = None,
        id: str = None,
        params: str = None,
        result: Any = None,
        speed: str = None,
        start_time: float = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        total: float = None,
        total_bytes: str = None,
        update_time: float = None,
    ):
        self.current_bytes = current_bytes
        self.err_code = err_code
        self.err_msg = err_msg
        self.extra = extra
        self.file_size = file_size
        self.finish_time = finish_time
        self.finished = finished
        self.finished_time = finished_time
        self.id = id
        self.params = params
        self.result = result
        self.speed = speed
        self.start_time = start_time
        self.status = status
        self.task_id = task_id
        self.task_type = task_type
        self.total = total
        self.total_bytes = total_bytes
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_bytes is not None:
            result['currentBytes'] = self.current_bytes
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.extra is not None:
            result['extra'] = self.extra
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.finished is not None:
            result['finished'] = self.finished
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.id is not None:
            result['id'] = self.id
        if self.params is not None:
            result['params'] = self.params
        if self.result is not None:
            result['result'] = self.result
        if self.speed is not None:
            result['speed'] = self.speed
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.total is not None:
            result['total'] = self.total
        if self.total_bytes is not None:
            result['totalBytes'] = self.total_bytes
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentBytes') is not None:
            self.current_bytes = m.get('currentBytes')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('speed') is not None:
            self.speed = m.get('speed')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('totalBytes') is not None:
            self.total_bytes = m.get('totalBytes')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
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


class OperationModelFileAction(TeaModel):
    def __init__(
        self,
        action: str = None,
        destination: str = None,
        source: str = None,
        target: str = None,
    ):
        # This parameter is required.
        self.action = action
        self.destination = destination
        self.source = source
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.destination is not None:
            result['destination'] = self.destination
        if self.source is not None:
            result['source'] = self.source
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('destination') is not None:
            self.destination = m.get('destination')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('target') is not None:
            self.target = m.get('target')
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


class ServiceMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ProjectStatus(TeaModel):
    def __init__(
        self,
        services: List[ServiceMeta] = None,
    ):
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = ServiceMeta()
                self.services.append(temp_model.from_map(k))
        return self


class Project(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        status: ProjectStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.status = status
        self.uid = uid

    def validate(self):
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
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
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
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            temp_model = ProjectStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ProjectSpec(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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


class Repository(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        spec: RepositorySpec = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
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
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
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
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = RepositorySpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ServiceBaseline(TeaModel):
    def __init__(
        self,
        service_instance: ServiceInstance = None,
    ):
        self.service_instance = service_instance

    def validate(self):
        if self.service_instance:
            self.service_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_instance is not None:
            result['serviceInstance'] = self.service_instance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceInstance') is not None:
            temp_model = ServiceInstance()
            self.service_instance = temp_model.from_map(m['serviceInstance'])
        return self


class ServiceChanges(TeaModel):
    def __init__(
        self,
        merge: Dict[str, Any] = None,
    ):
        self.merge = merge

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merge is not None:
            result['merge'] = self.merge
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('merge') is not None:
            self.merge = m.get('merge')
        return self


class ServiceCommandStep(TeaModel):
    def __init__(
        self,
        path: str = None,
        run: str = None,
    ):
        self.path = path
        self.run = run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.run is not None:
            result['run'] = self.run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('run') is not None:
            self.run = m.get('run')
        return self


class ServiceComponentStep(TeaModel):
    def __init__(
        self,
        component: str = None,
    ):
        self.component = component

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component is not None:
            result['component'] = self.component
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('component') is not None:
            self.component = m.get('component')
        return self


class ServiceDeploymentStatus(TeaModel):
    def __init__(
        self,
        finished_time: str = None,
        phase: str = None,
        pipeline_name: str = None,
        start_time: str = None,
        task_name: str = None,
    ):
        self.finished_time = finished_time
        self.phase = phase
        self.pipeline_name = pipeline_name
        self.start_time = start_time
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.phase is not None:
            result['phase'] = self.phase
        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.task_name is not None:
            result['taskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        return self


class ServiceDeployment(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        environment_deployment_name: str = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        status: ServiceDeploymentStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.environment_deployment_name = environment_deployment_name
        self.kind = kind
        self.labels = labels
        # This parameter is required.
        self.name = name
        self.status = status
        self.uid = uid

    def validate(self):
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
        if self.environment_deployment_name is not None:
            result['environmentDeploymentName'] = self.environment_deployment_name
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
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
        if m.get('environmentDeploymentName') is not None:
            self.environment_deployment_name = m.get('environmentDeploymentName')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            temp_model = ServiceDeploymentStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ServiceDeploymentSpec(TeaModel):
    def __init__(
        self,
        baseline: ServiceBaseline = None,
        changes: ServiceChanges = None,
        skip_remove_resources: bool = None,
        target: ServiceBaseline = None,
    ):
        self.baseline = baseline
        self.changes = changes
        self.skip_remove_resources = skip_remove_resources
        self.target = target

    def validate(self):
        if self.baseline:
            self.baseline.validate()
        if self.changes:
            self.changes.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline is not None:
            result['baseline'] = self.baseline.to_map()
        if self.changes is not None:
            result['changes'] = self.changes.to_map()
        if self.skip_remove_resources is not None:
            result['skipRemoveResources'] = self.skip_remove_resources
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseline') is not None:
            temp_model = ServiceBaseline()
            self.baseline = temp_model.from_map(m['baseline'])
        if m.get('changes') is not None:
            temp_model = ServiceChanges()
            self.changes = temp_model.from_map(m['changes'])
        if m.get('skipRemoveResources') is not None:
            self.skip_remove_resources = m.get('skipRemoveResources')
        if m.get('target') is not None:
            temp_model = ServiceBaseline()
            self.target = temp_model.from_map(m['target'])
        return self


class ServicePluginStep(TeaModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        plugin: str = None,
    ):
        self.args = args
        self.plugin = plugin

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.plugin is not None:
            result['plugin'] = self.plugin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('plugin') is not None:
            self.plugin = m.get('plugin')
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


class TemplateParameterSchemaRoleExtension(TeaModel):
    def __init__(
        self,
        authorities: List[str] = None,
        name: str = None,
        service: str = None,
    ):
        self.authorities = authorities
        self.name = name
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorities is not None:
            result['authorities'] = self.authorities
        if self.name is not None:
            result['name'] = self.name
        if self.service is not None:
            result['service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorities') is not None:
            self.authorities = m.get('authorities')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('service') is not None:
            self.service = m.get('service')
        return self


class TemplateParameterSchema(TeaModel):
    def __init__(
        self,
        default: Any = None,
        description: str = None,
        enum: List[str] = None,
        pattern: str = None,
        required: bool = None,
        role_extension: TemplateParameterSchemaRoleExtension = None,
        sensitive: bool = None,
        title: str = None,
        type: str = None,
    ):
        self.default = default
        self.description = description
        self.enum = enum
        self.pattern = pattern
        self.required = required
        self.role_extension = role_extension
        self.sensitive = sensitive
        self.title = title
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.role_extension:
            self.role_extension.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default is not None:
            result['default'] = self.default
        if self.description is not None:
            result['description'] = self.description
        if self.enum is not None:
            result['enum'] = self.enum
        if self.pattern is not None:
            result['pattern'] = self.pattern
        if self.required is not None:
            result['required'] = self.required
        if self.role_extension is not None:
            result['roleExtension'] = self.role_extension.to_map()
        if self.sensitive is not None:
            result['sensitive'] = self.sensitive
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enum') is not None:
            self.enum = m.get('enum')
        if m.get('pattern') is not None:
            self.pattern = m.get('pattern')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('roleExtension') is not None:
            temp_model = TemplateParameterSchemaRoleExtension()
            self.role_extension = temp_model.from_map(m['roleExtension'])
        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class TemplateServiceConfig(TeaModel):
    def __init__(
        self,
        artifact: ArtifactMeta = None,
        build: BuildConfig = None,
        component: str = None,
        props: Dict[str, Any] = None,
        source: SourceConfig = None,
        type: str = None,
        variables: Dict[str, TemplateParameterSchema] = None,
    ):
        self.artifact = artifact
        self.build = build
        self.component = component
        self.props = props
        self.source = source
        self.type = type
        self.variables = variables

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.build:
            self.build.validate()
        if self.source:
            self.source.validate()
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()
        if self.build is not None:
            result['build'] = self.build.to_map()
        if self.component is not None:
            result['component'] = self.component
        if self.props is not None:
            result['props'] = self.props
        if self.source is not None:
            result['source'] = self.source.to_map()
        if self.type is not None:
            result['type'] = self.type
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifact') is not None:
            temp_model = ArtifactMeta()
            self.artifact = temp_model.from_map(m['artifact'])
        if m.get('build') is not None:
            temp_model = BuildConfig()
            self.build = temp_model.from_map(m['build'])
        if m.get('component') is not None:
            self.component = m.get('component')
        if m.get('props') is not None:
            self.props = m.get('props')
        if m.get('source') is not None:
            temp_model = SourceConfig()
            self.source = temp_model.from_map(m['source'])
        if m.get('type') is not None:
            self.type = m.get('type')
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = TemplateParameterSchema()
                self.variables[k] = temp_model.from_map(v)
        return self


class TemplateSpecSource(TeaModel):
    def __init__(
        self,
        repository: RepositorySourceConfig = None,
    ):
        self.repository = repository

    def validate(self):
        if self.repository:
            self.repository.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repository is not None:
            result['repository'] = self.repository.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('repository') is not None:
            temp_model = RepositorySourceConfig()
            self.repository = temp_model.from_map(m['repository'])
        return self


class TemplateSpec(TeaModel):
    def __init__(
        self,
        author: str = None,
        category: str = None,
        license: str = None,
        package_name: str = None,
        readme: str = None,
        registry_token: str = None,
        services: Dict[str, TemplateServiceConfig] = None,
        source: TemplateSpecSource = None,
        variables: Dict[str, TemplateParameterSchema] = None,
        version: str = None,
    ):
        # This parameter is required.
        self.author = author
        # This parameter is required.
        self.category = category
        self.license = license
        self.package_name = package_name
        # This parameter is required.
        self.readme = readme
        self.registry_token = registry_token
        self.services = services
        self.source = source
        self.variables = variables
        self.version = version

    def validate(self):
        if self.services:
            for v in self.services.values():
                if v:
                    v.validate()
        if self.source:
            self.source.validate()
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['author'] = self.author
        if self.category is not None:
            result['category'] = self.category
        if self.license is not None:
            result['license'] = self.license
        if self.package_name is not None:
            result['packageName'] = self.package_name
        if self.readme is not None:
            result['readme'] = self.readme
        if self.registry_token is not None:
            result['registryToken'] = self.registry_token
        result['services'] = {}
        if self.services is not None:
            for k, v in self.services.items():
                result['services'][k] = v.to_map()
        if self.source is not None:
            result['source'] = self.source.to_map()
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('author') is not None:
            self.author = m.get('author')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('license') is not None:
            self.license = m.get('license')
        if m.get('packageName') is not None:
            self.package_name = m.get('packageName')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('registryToken') is not None:
            self.registry_token = m.get('registryToken')
        self.services = {}
        if m.get('services') is not None:
            for k, v in m.get('services').items():
                temp_model = TemplateServiceConfig()
                self.services[k] = temp_model.from_map(v)
        if m.get('source') is not None:
            temp_model = TemplateSpecSource()
            self.source = temp_model.from_map(m['source'])
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = TemplateParameterSchema()
                self.variables[k] = temp_model.from_map(v)
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class TemplateStatusLatestDeployment(TeaModel):
    def __init__(
        self,
        finished_time: str = None,
        phase: str = None,
        pipeline_name: str = None,
        start_time: str = None,
    ):
        self.finished_time = finished_time
        self.phase = phase
        self.pipeline_name = pipeline_name
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.phase is not None:
            result['phase'] = self.phase
        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class TemplateStatus(TeaModel):
    def __init__(
        self,
        latest_deployment: TemplateStatusLatestDeployment = None,
        latest_version: str = None,
        package_url: str = None,
        phase: str = None,
        template_url: str = None,
    ):
        self.latest_deployment = latest_deployment
        self.latest_version = latest_version
        self.package_url = package_url
        self.phase = phase
        self.template_url = template_url

    def validate(self):
        if self.latest_deployment:
            self.latest_deployment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latest_deployment is not None:
            result['latestDeployment'] = self.latest_deployment.to_map()
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.package_url is not None:
            result['packageUrl'] = self.package_url
        if self.phase is not None:
            result['phase'] = self.phase
        if self.template_url is not None:
            result['templateUrl'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latestDeployment') is not None:
            temp_model = TemplateStatusLatestDeployment()
            self.latest_deployment = temp_model.from_map(m['latestDeployment'])
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('packageUrl') is not None:
            self.package_url = m.get('packageUrl')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('templateUrl') is not None:
            self.template_url = m.get('templateUrl')
        return self


class Template(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        spec: TemplateSpec = None,
        status: TemplateStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.kind = kind
        self.labels = labels
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
        if self.description is not None:
            result['description'] = self.description
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
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
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
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
        return self


class TemplateVariableValueMap(TeaModel):
    def __init__(
        self,
        services: Dict[str, dict] = None,
        shared: Dict[str, Any] = None,
    ):
        self.services = services
        self.shared = shared

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.services is not None:
            result['services'] = self.services
        if self.shared is not None:
            result['shared'] = self.shared
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('services') is not None:
            self.services = m.get('services')
        if m.get('shared') is not None:
            self.shared = m.get('shared')
        return self


class TemplateConfig(TeaModel):
    def __init__(
        self,
        parameters: Dict[str, str] = None,
        service_name_changes: Dict[str, str] = None,
        template_name: str = None,
        variable_values: TemplateVariableValueMap = None,
    ):
        self.parameters = parameters
        self.service_name_changes = service_name_changes
        # This parameter is required.
        self.template_name = template_name
        self.variable_values = variable_values

    def validate(self):
        if self.variable_values:
            self.variable_values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.service_name_changes is not None:
            result['serviceNameChanges'] = self.service_name_changes
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.variable_values is not None:
            result['variableValues'] = self.variable_values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('serviceNameChanges') is not None:
            self.service_name_changes = m.get('serviceNameChanges')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('variableValues') is not None:
            temp_model = TemplateVariableValueMap()
            self.variable_values = temp_model.from_map(m['variableValues'])
        return self


class TemplateRevisionStatus(TeaModel):
    def __init__(
        self,
        package_url: str = None,
        phase: str = None,
        pipeline_name: str = None,
        template_url: str = None,
    ):
        self.package_url = package_url
        self.phase = phase
        self.pipeline_name = pipeline_name
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_url is not None:
            result['packageUrl'] = self.package_url
        if self.phase is not None:
            result['phase'] = self.phase
        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name
        if self.template_url is not None:
            result['templateUrl'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('packageUrl') is not None:
            self.package_url = m.get('packageUrl')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')
        if m.get('templateUrl') is not None:
            self.template_url = m.get('templateUrl')
        return self


class TemplateRevision(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        spec: TemplateSpec = None,
        status: TemplateRevisionStatus = None,
        template_name: str = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.kind = kind
        self.labels = labels
        self.name = name
        self.spec = spec
        self.status = status
        self.template_name = template_name
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
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = TemplateSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = TemplateRevisionStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class Tool(TeaModel):
    def __init__(
        self,
        method: str = None,
        path: str = None,
        tool_id: str = None,
        tool_name: str = None,
    ):
        self.method = method
        self.path = path
        self.tool_id = tool_id
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.path is not None:
            result['path'] = self.path
        if self.tool_id is not None:
            result['toolId'] = self.tool_id
        if self.tool_name is not None:
            result['toolName'] = self.tool_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('toolId') is not None:
            self.tool_id = m.get('toolId')
        if m.get('toolName') is not None:
            self.tool_name = m.get('toolName')
        return self


class ToolsetSchema(TeaModel):
    def __init__(
        self,
        detail: str = None,
        type: str = None,
    ):
        self.detail = detail
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ToolsetSpec(TeaModel):
    def __init__(
        self,
        schema: ToolsetSchema = None,
    ):
        self.schema = schema

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('schema') is not None:
            temp_model = ToolsetSchema()
            self.schema = temp_model.from_map(m['schema'])
        return self


class ToolsetStatus(TeaModel):
    def __init__(
        self,
        observed_generation: int = None,
        observed_time: str = None,
        outputs: Dict[str, Any] = None,
        phase: str = None,
    ):
        self.observed_generation = observed_generation
        self.observed_time = observed_time
        self.outputs = outputs
        self.phase = phase

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.observed_time is not None:
            result['observedTime'] = self.observed_time
        if self.outputs is not None:
            result['outputs'] = self.outputs
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class Toolset(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        kind: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        spec: ToolsetSpec = None,
        status: ToolsetStatus = None,
        uid: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.kind = kind
        self.labels = labels
        # This parameter is required.
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
        if self.description is not None:
            result['description'] = self.description
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
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
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = ToolsetSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = ToolsetStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ToolsetAuthorization(TeaModel):
    def __init__(
        self,
        auth_config: Dict[str, str] = None,
        type: str = None,
    ):
        self.auth_config = auth_config
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            self.auth_config = m.get('authConfig')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OpenStructOssSourceConfig(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        object: str = None,
    ):
        self.bucket = bucket
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.object is not None:
            result['object'] = self.object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('object') is not None:
            self.object = m.get('object')
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


class CreateArtifactRequest(TeaModel):
    def __init__(
        self,
        body: Artifact = None,
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
            temp_model = Artifact()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Artifact = None,
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
            temp_model = Artifact()
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


class CreateToolsetRequest(TeaModel):
    def __init__(
        self,
        body: Toolset = None,
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
            temp_model = Toolset()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateToolsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Toolset = None,
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
            temp_model = Toolset()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteArtifactResponse(TeaModel):
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


class DeleteProjectResponse(TeaModel):
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


class DeleteToolsetResponse(TeaModel):
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


class DeployEnvironmentRequest(TeaModel):
    def __init__(
        self,
        body: DeployEnvironmentOptions = None,
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
            temp_model = DeployEnvironmentOptions()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnvironmentDeployment = None,
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
            temp_model = EnvironmentDeployment()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchArtifactDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ArtifactCode = None,
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
            temp_model = ArtifactCode()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchArtifactTempBucketTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ArtifactTempBucketToken = None,
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
            temp_model = ArtifactTempBucketToken()
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


class GetArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Artifact = None,
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
            temp_model = Artifact()
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


class GetEnvironmentDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnvironmentDeployment = None,
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
            temp_model = EnvironmentDeployment()
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


class GetServiceDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ServiceDeployment = None,
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
            temp_model = ServiceDeployment()
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


class GetToolsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Toolset = None,
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
            temp_model = Toolset()
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


class ListServiceDeploymentsRequest(TeaModel):
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


class ListServiceDeploymentsShrinkRequest(TeaModel):
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


class ListServiceDeploymentsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ServiceDeployment] = None,
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
                temp_model = ServiceDeployment()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListServiceDeploymentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceDeploymentsResponseBody = None,
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
            temp_model = ListServiceDeploymentsResponseBody()
            self.body = temp_model.from_map(m['body'])
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


class ListToolsetsRequest(TeaModel):
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


class ListToolsetsShrinkRequest(TeaModel):
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


class ListToolsetsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Toolset] = None,
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
                temp_model = Toolset()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListToolsetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListToolsetsResponseBody = None,
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
            temp_model = ListToolsetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviewEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnvironmentDeploymentSpec = None,
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
            temp_model = EnvironmentDeploymentSpec()
            self.body = temp_model.from_map(m['body'])
        return self


class PutArtifactRequest(TeaModel):
    def __init__(
        self,
        body: Artifact = None,
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
            temp_model = Artifact()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Artifact = None,
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
            temp_model = Artifact()
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


class RenderServicesByTemplateRequest(TeaModel):
    def __init__(
        self,
        parameters: Dict[str, Any] = None,
        project_name: str = None,
        service_name_changes: Dict[str, str] = None,
        template_name: str = None,
        variable_values: TemplateVariableValueMap = None,
    ):
        self.parameters = parameters
        self.project_name = project_name
        self.service_name_changes = service_name_changes
        # This parameter is required.
        self.template_name = template_name
        self.variable_values = variable_values

    def validate(self):
        if self.variable_values:
            self.variable_values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.service_name_changes is not None:
            result['serviceNameChanges'] = self.service_name_changes
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.variable_values is not None:
            result['variableValues'] = self.variable_values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('serviceNameChanges') is not None:
            self.service_name_changes = m.get('serviceNameChanges')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('variableValues') is not None:
            temp_model = TemplateVariableValueMap()
            self.variable_values = temp_model.from_map(m['variableValues'])
        return self


class RenderServicesByTemplateResponseBody(TeaModel):
    def __init__(
        self,
        changed_service_names: Dict[str, str] = None,
        services: Dict[str, ServiceConfig] = None,
        variables: Dict[str, Variable] = None,
    ):
        self.changed_service_names = changed_service_names
        self.services = services
        self.variables = variables

    def validate(self):
        if self.services:
            for v in self.services.values():
                if v:
                    v.validate()
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.changed_service_names is not None:
            result['changedServiceNames'] = self.changed_service_names
        result['services'] = {}
        if self.services is not None:
            for k, v in self.services.items():
                result['services'][k] = v.to_map()
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changedServiceNames') is not None:
            self.changed_service_names = m.get('changedServiceNames')
        self.services = {}
        if m.get('services') is not None:
            for k, v in m.get('services').items():
                temp_model = ServiceConfig()
                self.services[k] = temp_model.from_map(v)
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = Variable()
                self.variables[k] = temp_model.from_map(v)
        return self


class RenderServicesByTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenderServicesByTemplateResponseBody = None,
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
            temp_model = RenderServicesByTemplateResponseBody()
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


class UpdateProjectRequest(TeaModel):
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


class UpdateToolsetRequest(TeaModel):
    def __init__(
        self,
        body: Toolset = None,
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
            temp_model = Toolset()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateToolsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Toolset = None,
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
            temp_model = Toolset()
            self.body = temp_model.from_map(m['body'])
        return self


