# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class EnvironmentSpec(TeaModel):
    def __init__(
        self,
        region: str = None,
        role_arn: str = None,
        template: str = None,
        template_variables: Dict[str, Any] = None,
    ):
        # A region ID at Aliyun. For example, "cn-hangzhou"
        self.region = region
        # The ARN (Aliyun Resource Name) of the role designated by a user to allow the system to manage his Aliyun resources. If null, use roleArn of role AliyunFCDefaultRole.
        self.role_arn = role_arn
        # The name of the template for the Environment
        self.template = template
        # Variables for specified template
        self.template_variables = template_variables

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
        # Access key ID
        self.access_key_id = access_key_id
        # Expiration time of the credentials
        self.expiration_time = expiration_time
        # The kind of the credentials
        self.kind = kind
        # Secret access key
        self.secret_access_key = secret_access_key
        # Token
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


class EnvironmentStatus(TeaModel):
    def __init__(
        self,
        credentials: StsCredentials = None,
        message: str = None,
        observed_generation: int = None,
        observed_time: str = None,
        output: Dict[str, Any] = None,
        phase: str = None,
    ):
        # Credentials required for tasks
        self.credentials = credentials
        # A human-readable message indicating details about why the Environment is in this condition
        self.message = message
        # The most recent generation observed
        self.observed_generation = observed_generation
        # Time when the last update of the status is observed
        self.observed_time = observed_time
        # Details of current state of the Environment
        self.output = output
        # A simple, high-level summary of where the Environment is in its lifecycle
        self.phase = phase

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
        if m.get('credentials') is not None:
            temp_model = StsCredentials()
            self.credentials = temp_model.from_map(m['credentials'])
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
        creation_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        name: str = None,
        spec: EnvironmentSpec = None,
        status: EnvironmentStatus = None,
        uid: str = None,
    ):
        # A time representing the server time when this object was created. Clients may not set this value. Populated by the system. Read-only.
        self.creation_time = creation_time
        # Human-readable description of the resource
        self.description = description
        # A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.
        self.generation = generation
        # The kind of the resource
        self.kind = kind
        # Name must be unique within a namespace. Is required when creating resources. Cannot be updated.
        self.name = name
        # Specification of the desired behavior of the Environment
        self.spec = spec
        # Most recently observed status of the Environment. This data may not be up-to-date. Populated by the system. Read-only
        self.status = status
        # Main user ID of an Aliyun account
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
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
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
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
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


class ServiceSpec(TeaModel):
    def __init__(
        self,
        environment: str = None,
        role_arn: str = None,
        template: str = None,
        template_variables: Dict[str, Any] = None,
    ):
        # The name of the associated Environment for the Service
        self.environment = environment
        # The ARN (Aliyun Resource Name) of the role designated by a user to allow the system to manage his Aliyun resources. If null, use roleArn of role AliyunFCDefaultRole.
        self.role_arn = role_arn
        # The name of the template for the Service
        self.template = template
        # Variables for specified template
        self.template_variables = template_variables

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
        return self


class ServiceStatus(TeaModel):
    def __init__(
        self,
        credentials: StsCredentials = None,
        message: str = None,
        observed_generation: int = None,
        observed_time: str = None,
        output: Dict[str, Any] = None,
        phase: str = None,
    ):
        # Credentials required for tasks
        self.credentials = credentials
        # A human-readable message indicating details about why the Service is in this condition
        self.message = message
        # The most recent generation observed
        self.observed_generation = observed_generation
        # Time when the last update of the status is observed
        self.observed_time = observed_time
        # Details of current state of the Service
        self.output = output
        # A simple, high-level summary of where the Service is in its lifecycle
        self.phase = phase

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
        if m.get('credentials') is not None:
            temp_model = StsCredentials()
            self.credentials = temp_model.from_map(m['credentials'])
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
        creation_time: str = None,
        description: str = None,
        generation: int = None,
        kind: str = None,
        name: str = None,
        spec: ServiceSpec = None,
        status: ServiceStatus = None,
        uid: str = None,
    ):
        # A time representing the server time when this object was created. Clients may not set this value. Populated by the system. Read-only.
        self.creation_time = creation_time
        # Human-readable description of the resource
        self.description = description
        # A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.
        self.generation = generation
        # The kind of the resource
        self.kind = kind
        # Name must be unique within a namespace. Is required when creating resources. Cannot be updated.
        self.name = name
        # Specification of the desired behavior of the Service
        self.spec = spec
        # Most recently observed status of the Service. This data may not be up-to-date. Populated by the system. Read-only
        self.status = status
        # Main user ID of an Aliyun account
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
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
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
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
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


class GetEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: Environment = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: Service = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = Service()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: List[Environment] = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Environment()
                self.body.append(temp_model.from_map(k))
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: List[Service] = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Service()
                self.body.append(temp_model.from_map(k))
        return self


class PutEnvironmentRequest(TeaModel):
    def __init__(
        self,
        body: Environment = None,
    ):
        # An environment for serverless deployments
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
        body: Environment = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class PutServiceRequest(TeaModel):
    def __init__(
        self,
        body: Service = None,
    ):
        # A service for serverless deployments
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
        body: Service = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = Service()
            self.body = temp_model.from_map(m['body'])
        return self


