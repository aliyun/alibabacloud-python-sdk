# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class FeatureViewConfigValuePartitionsValue(TeaModel):
    def __init__(
        self,
        value: str = None,
        values: List[str] = None,
        start_value: str = None,
        end_value: str = None,
    ):
        self.value = value
        self.values = values
        self.start_value = start_value
        self.end_value = end_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.values is not None:
            result['Values'] = self.values
        if self.start_value is not None:
            result['StartValue'] = self.start_value
        if self.end_value is not None:
            result['EndValue'] = self.end_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('StartValue') is not None:
            self.start_value = m.get('StartValue')
        if m.get('EndValue') is not None:
            self.end_value = m.get('EndValue')
        return self


class FeatureViewConfigValue(TeaModel):
    def __init__(
        self,
        partitions: Dict[str, FeatureViewConfigValuePartitionsValue] = None,
        event_time: str = None,
        equal: bool = None,
        use_mock: bool = None,
    ):
        self.partitions = partitions
        self.event_time = event_time
        self.equal = equal
        self.use_mock = use_mock

    def validate(self):
        if self.partitions:
            for v in self.partitions.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Partitions'] = {}
        if self.partitions is not None:
            for k, v in self.partitions.items():
                result['Partitions'][k] = v.to_map()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.equal is not None:
            result['Equal'] = self.equal
        if self.use_mock is not None:
            result['UseMock'] = self.use_mock
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.partitions = {}
        if m.get('Partitions') is not None:
            for k, v in m.get('Partitions').items():
                temp_model = FeatureViewConfigValuePartitionsValue()
                self.partitions[k] = temp_model.from_map(v)
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Equal') is not None:
            self.equal = m.get('Equal')
        if m.get('UseMock') is not None:
            self.use_mock = m.get('UseMock')
        return self


class CheckInstanceDatasourceRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        type: str = None,
        uri: str = None,
    ):
        self.config = config
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
        if self.config is not None:
            result['Config'] = self.config
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CheckInstanceDatasourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CheckInstanceDatasourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckInstanceDatasourceResponseBody = None,
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
            temp_model = CheckInstanceDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckModelFeatureFGFeatureResponseBodyFGCheckResults(TeaModel):
    def __init__(
        self,
        message: str = None,
        rule_code: str = None,
        status: bool = None,
    ):
        self.message = message
        self.rule_code = rule_code
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.rule_code is not None:
            result['RuleCode'] = self.rule_code
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RuleCode') is not None:
            self.rule_code = m.get('RuleCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CheckModelFeatureFGFeatureResponseBody(TeaModel):
    def __init__(
        self,
        fgcheck_results: List[CheckModelFeatureFGFeatureResponseBodyFGCheckResults] = None,
        request_id: str = None,
    ):
        self.fgcheck_results = fgcheck_results
        self.request_id = request_id

    def validate(self):
        if self.fgcheck_results:
            for k in self.fgcheck_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FGCheckResults'] = []
        if self.fgcheck_results is not None:
            for k in self.fgcheck_results:
                result['FGCheckResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fgcheck_results = []
        if m.get('FGCheckResults') is not None:
            for k in m.get('FGCheckResults'):
                temp_model = CheckModelFeatureFGFeatureResponseBodyFGCheckResults()
                self.fgcheck_results.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CheckModelFeatureFGFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckModelFeatureFGFeatureResponseBody = None,
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
            temp_model = CheckModelFeatureFGFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasourceRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        type: str = None,
        uri: str = None,
        workspace_id: str = None,
    ):
        self.config = config
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.uri = uri
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDatasourceResponseBody(TeaModel):
    def __init__(
        self,
        datasource_id: str = None,
        request_id: str = None,
    ):
        self.datasource_id = datasource_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasourceResponseBody = None,
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
            temp_model = CreateDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFeatureEntityRequest(TeaModel):
    def __init__(
        self,
        join_id: str = None,
        name: str = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.join_id = join_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateFeatureEntityResponseBody(TeaModel):
    def __init__(
        self,
        feature_entity_id: str = None,
        request_id: str = None,
    ):
        self.feature_entity_id = feature_entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFeatureEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFeatureEntityResponseBody = None,
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
            temp_model = CreateFeatureEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFeatureViewRequestFieldsTransformInput(TeaModel):
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
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFeatureViewRequestFieldsTransform(TeaModel):
    def __init__(
        self,
        input: List[CreateFeatureViewRequestFieldsTransformInput] = None,
        llmconfig_id: int = None,
        type: str = None,
    ):
        self.input = input
        self.llmconfig_id = llmconfig_id
        self.type = type

    def validate(self):
        if self.input:
            for k in self.input:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Input'] = []
        if self.input is not None:
            for k in self.input:
                result['Input'].append(k.to_map() if k else None)
        if self.llmconfig_id is not None:
            result['LLMConfigId'] = self.llmconfig_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input = []
        if m.get('Input') is not None:
            for k in m.get('Input'):
                temp_model = CreateFeatureViewRequestFieldsTransformInput()
                self.input.append(temp_model.from_map(k))
        if m.get('LLMConfigId') is not None:
            self.llmconfig_id = m.get('LLMConfigId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFeatureViewRequestFields(TeaModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        transform: List[CreateFeatureViewRequestFieldsTransform] = None,
        type: str = None,
    ):
        self.attributes = attributes
        self.name = name
        self.transform = transform
        self.type = type

    def validate(self):
        if self.transform:
            for k in self.transform:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        result['Transform'] = []
        if self.transform is not None:
            for k in self.transform:
                result['Transform'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.transform = []
        if m.get('Transform') is not None:
            for k in m.get('Transform'):
                temp_model = CreateFeatureViewRequestFieldsTransform()
                self.transform.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFeatureViewRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        feature_entity_id: str = None,
        fields: List[CreateFeatureViewRequestFields] = None,
        name: str = None,
        project_id: str = None,
        register_datasource_id: str = None,
        register_table: str = None,
        sync_online_table: bool = None,
        ttl: int = None,
        tags: List[str] = None,
        type: str = None,
        write_method: str = None,
        write_to_feature_db: bool = None,
    ):
        self.config = config
        self.feature_entity_id = feature_entity_id
        self.fields = fields
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        self.register_datasource_id = register_datasource_id
        self.register_table = register_table
        # This parameter is required.
        self.sync_online_table = sync_online_table
        self.ttl = ttl
        self.tags = tags
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.write_method = write_method
        self.write_to_feature_db = write_to_feature_db

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.register_datasource_id is not None:
            result['RegisterDatasourceId'] = self.register_datasource_id
        if self.register_table is not None:
            result['RegisterTable'] = self.register_table
        if self.sync_online_table is not None:
            result['SyncOnlineTable'] = self.sync_online_table
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.write_method is not None:
            result['WriteMethod'] = self.write_method
        if self.write_to_feature_db is not None:
            result['WriteToFeatureDB'] = self.write_to_feature_db
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = CreateFeatureViewRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegisterDatasourceId') is not None:
            self.register_datasource_id = m.get('RegisterDatasourceId')
        if m.get('RegisterTable') is not None:
            self.register_table = m.get('RegisterTable')
        if m.get('SyncOnlineTable') is not None:
            self.sync_online_table = m.get('SyncOnlineTable')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WriteMethod') is not None:
            self.write_method = m.get('WriteMethod')
        if m.get('WriteToFeatureDB') is not None:
            self.write_to_feature_db = m.get('WriteToFeatureDB')
        return self


class CreateFeatureViewResponseBody(TeaModel):
    def __init__(
        self,
        feature_view_id: str = None,
        request_id: str = None,
    ):
        self.feature_view_id = feature_view_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFeatureViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFeatureViewResponseBody = None,
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
            temp_model = CreateFeatureViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
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
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLLMConfigRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        batch_size: int = None,
        max_tokens: int = None,
        model: str = None,
        name: str = None,
        rps: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.base_url = base_url
        self.batch_size = batch_size
        self.max_tokens = max_tokens
        # This parameter is required.
        self.model = model
        # This parameter is required.
        self.name = name
        self.rps = rps
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens
        if self.model is not None:
            result['Model'] = self.model
        if self.name is not None:
            result['Name'] = self.name
        if self.rps is not None:
            result['Rps'] = self.rps
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rps') is not None:
            self.rps = m.get('Rps')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateLLMConfigResponseBody(TeaModel):
    def __init__(
        self,
        llmconfig_id: str = None,
        request_id: str = None,
    ):
        self.llmconfig_id = llmconfig_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.llmconfig_id is not None:
            result['LLMConfigId'] = self.llmconfig_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LLMConfigId') is not None:
            self.llmconfig_id = m.get('LLMConfigId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLLMConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLLMConfigResponseBody = None,
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
            temp_model = CreateLLMConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLabelTableRequestFields(TeaModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.attributes = attributes
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateLabelTableRequest(TeaModel):
    def __init__(
        self,
        datasource_id: str = None,
        fields: List[CreateLabelTableRequestFields] = None,
        name: str = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.datasource_id = datasource_id
        # This parameter is required.
        self.fields = fields
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = CreateLabelTableRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateLabelTableResponseBody(TeaModel):
    def __init__(
        self,
        label_table_id: str = None,
        request_id: str = None,
    ):
        self.label_table_id = label_table_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLabelTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLabelTableResponseBody = None,
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
            temp_model = CreateLabelTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelFeatureRequestFeatures(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        feature_view_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.alias_name = alias_name
        # This parameter is required.
        self.feature_view_id = feature_view_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateModelFeatureRequest(TeaModel):
    def __init__(
        self,
        features: List[CreateModelFeatureRequestFeatures] = None,
        label_priority_level: int = None,
        label_table_id: str = None,
        name: str = None,
        project_id: str = None,
        sequence_feature_view_ids: List[str] = None,
    ):
        # This parameter is required.
        self.features = features
        self.label_priority_level = label_priority_level
        # This parameter is required.
        self.label_table_id = label_table_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        self.sequence_feature_view_ids = sequence_feature_view_ids

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        if self.label_priority_level is not None:
            result['LabelPriorityLevel'] = self.label_priority_level
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sequence_feature_view_ids is not None:
            result['SequenceFeatureViewIds'] = self.sequence_feature_view_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = CreateModelFeatureRequestFeatures()
                self.features.append(temp_model.from_map(k))
        if m.get('LabelPriorityLevel') is not None:
            self.label_priority_level = m.get('LabelPriorityLevel')
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SequenceFeatureViewIds') is not None:
            self.sequence_feature_view_ids = m.get('SequenceFeatureViewIds')
        return self


class CreateModelFeatureResponseBody(TeaModel):
    def __init__(
        self,
        model_feature_id: str = None,
        request_id: str = None,
    ):
        self.model_feature_id = model_feature_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_feature_id is not None:
            result['ModelFeatureId'] = self.model_feature_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelFeatureId') is not None:
            self.model_feature_id = m.get('ModelFeatureId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModelFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModelFeatureResponseBody = None,
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
            temp_model = CreateModelFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        offline_datasource_id: str = None,
        offline_life_cycle: int = None,
        online_datasource_id: str = None,
        workspace_id: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.offline_datasource_id = offline_datasource_id
        self.offline_life_cycle = offline_life_cycle
        # This parameter is required.
        self.online_datasource_id = online_datasource_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.offline_datasource_id is not None:
            result['OfflineDatasourceId'] = self.offline_datasource_id
        if self.offline_life_cycle is not None:
            result['OfflineLifeCycle'] = self.offline_life_cycle
        if self.online_datasource_id is not None:
            result['OnlineDatasourceId'] = self.online_datasource_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OfflineDatasourceId') is not None:
            self.offline_datasource_id = m.get('OfflineDatasourceId')
        if m.get('OfflineLifeCycle') is not None:
            self.offline_life_cycle = m.get('OfflineLifeCycle')
        if m.get('OnlineDatasourceId') is not None:
            self.online_datasource_id = m.get('OnlineDatasourceId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        request_id: str = None,
    ):
        self.project_id = project_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectResponseBody = None,
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceIdentityRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        # This parameter is required.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateServiceIdentityRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        role_name: str = None,
    ):
        self.code = code
        self.request_id = request_id
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateServiceIdentityRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceIdentityRoleResponseBody = None,
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
            temp_model = CreateServiceIdentityRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasourceResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatasourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasourceResponseBody = None,
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
            temp_model = DeleteDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFeatureEntityResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFeatureEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFeatureEntityResponseBody = None,
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
            temp_model = DeleteFeatureEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFeatureViewResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFeatureViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFeatureViewResponseBody = None,
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
            temp_model = DeleteFeatureViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLLMConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLLMConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLLMConfigResponseBody = None,
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
            temp_model = DeleteLLMConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLabelTableResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLabelTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLabelTableResponseBody = None,
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
            temp_model = DeleteLabelTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelFeatureResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteModelFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteModelFeatureResponseBody = None,
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
            temp_model = DeleteModelFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class ExportModelFeatureTrainingSetTableRequestLabelInputConfig(TeaModel):
    def __init__(
        self,
        event_time: str = None,
        partitions: Dict[str, dict] = None,
    ):
        self.event_time = event_time
        self.partitions = partitions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.partitions is not None:
            result['Partitions'] = self.partitions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')
        return self


class ExportModelFeatureTrainingSetTableRequestTrainingSetConfig(TeaModel):
    def __init__(
        self,
        partitions: Dict[str, dict] = None,
    ):
        self.partitions = partitions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partitions is not None:
            result['Partitions'] = self.partitions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')
        return self


class ExportModelFeatureTrainingSetTableRequest(TeaModel):
    def __init__(
        self,
        feature_view_config: Dict[str, FeatureViewConfigValue] = None,
        label_input_config: ExportModelFeatureTrainingSetTableRequestLabelInputConfig = None,
        real_time_iterate_interval: int = None,
        real_time_partition_count_value: int = None,
        training_set_config: ExportModelFeatureTrainingSetTableRequestTrainingSetConfig = None,
    ):
        self.feature_view_config = feature_view_config
        self.label_input_config = label_input_config
        self.real_time_iterate_interval = real_time_iterate_interval
        self.real_time_partition_count_value = real_time_partition_count_value
        self.training_set_config = training_set_config

    def validate(self):
        if self.feature_view_config:
            for v in self.feature_view_config.values():
                if v:
                    v.validate()
        if self.label_input_config:
            self.label_input_config.validate()
        if self.training_set_config:
            self.training_set_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureViewConfig'] = {}
        if self.feature_view_config is not None:
            for k, v in self.feature_view_config.items():
                result['FeatureViewConfig'][k] = v.to_map()
        if self.label_input_config is not None:
            result['LabelInputConfig'] = self.label_input_config.to_map()
        if self.real_time_iterate_interval is not None:
            result['RealTimeIterateInterval'] = self.real_time_iterate_interval
        if self.real_time_partition_count_value is not None:
            result['RealTimePartitionCountValue'] = self.real_time_partition_count_value
        if self.training_set_config is not None:
            result['TrainingSetConfig'] = self.training_set_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_view_config = {}
        if m.get('FeatureViewConfig') is not None:
            for k, v in m.get('FeatureViewConfig').items():
                temp_model = FeatureViewConfigValue()
                self.feature_view_config[k] = temp_model.from_map(v)
        if m.get('LabelInputConfig') is not None:
            temp_model = ExportModelFeatureTrainingSetTableRequestLabelInputConfig()
            self.label_input_config = temp_model.from_map(m['LabelInputConfig'])
        if m.get('RealTimeIterateInterval') is not None:
            self.real_time_iterate_interval = m.get('RealTimeIterateInterval')
        if m.get('RealTimePartitionCountValue') is not None:
            self.real_time_partition_count_value = m.get('RealTimePartitionCountValue')
        if m.get('TrainingSetConfig') is not None:
            temp_model = ExportModelFeatureTrainingSetTableRequestTrainingSetConfig()
            self.training_set_config = temp_model.from_map(m['TrainingSetConfig'])
        return self


class ExportModelFeatureTrainingSetTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ExportModelFeatureTrainingSetTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportModelFeatureTrainingSetTableResponseBody = None,
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
            temp_model = ExportModelFeatureTrainingSetTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasourceResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        datasource_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        request_id: str = None,
        type: str = None,
        uri: str = None,
        workspace_id: str = None,
    ):
        self.config = config
        self.datasource_id = datasource_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.request_id = request_id
        self.type = type
        self.uri = uri
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDatasourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasourceResponseBody = None,
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
            temp_model = GetDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasourceTableResponseBodyFields(TeaModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
    ):
        self.attributes = attributes
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetDatasourceTableResponseBody(TeaModel):
    def __init__(
        self,
        fields: List[GetDatasourceTableResponseBodyFields] = None,
        request_id: str = None,
        table_name: str = None,
    ):
        self.fields = fields
        self.request_id = request_id
        self.table_name = table_name

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = GetDatasourceTableResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetDatasourceTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasourceTableResponseBody = None,
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
            temp_model = GetDatasourceTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureEntityResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        join_id: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
        request_id: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.join_id = join_id
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFeatureEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFeatureEntityResponseBody = None,
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
            temp_model = GetFeatureEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureViewResponseBodyFieldsTransformInput(TeaModel):
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
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetFeatureViewResponseBodyFieldsTransform(TeaModel):
    def __init__(
        self,
        input: List[GetFeatureViewResponseBodyFieldsTransformInput] = None,
        llmconfig_id: int = None,
        type: str = None,
    ):
        self.input = input
        self.llmconfig_id = llmconfig_id
        self.type = type

    def validate(self):
        if self.input:
            for k in self.input:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Input'] = []
        if self.input is not None:
            for k in self.input:
                result['Input'].append(k.to_map() if k else None)
        if self.llmconfig_id is not None:
            result['LLMConfigId'] = self.llmconfig_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input = []
        if m.get('Input') is not None:
            for k in m.get('Input'):
                temp_model = GetFeatureViewResponseBodyFieldsTransformInput()
                self.input.append(temp_model.from_map(k))
        if m.get('LLMConfigId') is not None:
            self.llmconfig_id = m.get('LLMConfigId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetFeatureViewResponseBodyFields(TeaModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        transform: List[GetFeatureViewResponseBodyFieldsTransform] = None,
        type: str = None,
    ):
        self.attributes = attributes
        self.name = name
        self.transform = transform
        self.type = type

    def validate(self):
        if self.transform:
            for k in self.transform:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        result['Transform'] = []
        if self.transform is not None:
            for k in self.transform:
                result['Transform'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.transform = []
        if m.get('Transform') is not None:
            for k in m.get('Transform'):
                temp_model = GetFeatureViewResponseBodyFieldsTransform()
                self.transform.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetFeatureViewResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        feature_entity_id: str = None,
        feature_entity_name: str = None,
        fields: List[GetFeatureViewResponseBodyFields] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        gmt_sync_time: str = None,
        join_id: str = None,
        last_sync_config: str = None,
        mock_table_name: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
        publish_table_script: str = None,
        register_datasource_id: str = None,
        register_datasource_name: str = None,
        register_table: str = None,
        request_id: str = None,
        sync_online_table: bool = None,
        ttl: int = None,
        tags: List[str] = None,
        type: str = None,
        write_method: str = None,
        write_to_feature_db: bool = None,
    ):
        self.config = config
        self.feature_entity_id = feature_entity_id
        self.feature_entity_name = feature_entity_name
        self.fields = fields
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.gmt_sync_time = gmt_sync_time
        self.join_id = join_id
        self.last_sync_config = last_sync_config
        self.mock_table_name = mock_table_name
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name
        self.publish_table_script = publish_table_script
        self.register_datasource_id = register_datasource_id
        self.register_datasource_name = register_datasource_name
        self.register_table = register_table
        self.request_id = request_id
        self.sync_online_table = sync_online_table
        self.ttl = ttl
        self.tags = tags
        self.type = type
        self.write_method = write_method
        self.write_to_feature_db = write_to_feature_db

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        if self.feature_entity_name is not None:
            result['FeatureEntityName'] = self.feature_entity_name
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.gmt_sync_time is not None:
            result['GmtSyncTime'] = self.gmt_sync_time
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.last_sync_config is not None:
            result['LastSyncConfig'] = self.last_sync_config
        if self.mock_table_name is not None:
            result['MockTableName'] = self.mock_table_name
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.publish_table_script is not None:
            result['PublishTableScript'] = self.publish_table_script
        if self.register_datasource_id is not None:
            result['RegisterDatasourceId'] = self.register_datasource_id
        if self.register_datasource_name is not None:
            result['RegisterDatasourceName'] = self.register_datasource_name
        if self.register_table is not None:
            result['RegisterTable'] = self.register_table
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_online_table is not None:
            result['SyncOnlineTable'] = self.sync_online_table
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.write_method is not None:
            result['WriteMethod'] = self.write_method
        if self.write_to_feature_db is not None:
            result['WriteToFeatureDB'] = self.write_to_feature_db
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        if m.get('FeatureEntityName') is not None:
            self.feature_entity_name = m.get('FeatureEntityName')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = GetFeatureViewResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('GmtSyncTime') is not None:
            self.gmt_sync_time = m.get('GmtSyncTime')
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('LastSyncConfig') is not None:
            self.last_sync_config = m.get('LastSyncConfig')
        if m.get('MockTableName') is not None:
            self.mock_table_name = m.get('MockTableName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('PublishTableScript') is not None:
            self.publish_table_script = m.get('PublishTableScript')
        if m.get('RegisterDatasourceId') is not None:
            self.register_datasource_id = m.get('RegisterDatasourceId')
        if m.get('RegisterDatasourceName') is not None:
            self.register_datasource_name = m.get('RegisterDatasourceName')
        if m.get('RegisterTable') is not None:
            self.register_table = m.get('RegisterTable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncOnlineTable') is not None:
            self.sync_online_table = m.get('SyncOnlineTable')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WriteMethod') is not None:
            self.write_method = m.get('WriteMethod')
        if m.get('WriteToFeatureDB') is not None:
            self.write_to_feature_db = m.get('WriteToFeatureDB')
        return self


class GetFeatureViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFeatureViewResponseBody = None,
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
            temp_model = GetFeatureViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyFeatureDBInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceResponseBodyFeatureDBInstanceInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        feature_dbinfo: GetInstanceResponseBodyFeatureDBInfo = None,
        feature_dbinstance_info: GetInstanceResponseBodyFeatureDBInstanceInfo = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        message: str = None,
        progress: float = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.feature_dbinfo = feature_dbinfo
        self.feature_dbinstance_info = feature_dbinstance_info
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.message = message
        self.progress = progress
        self.region_id = region_id
        self.request_id = request_id
        self.status = status
        self.type = type

    def validate(self):
        if self.feature_dbinfo:
            self.feature_dbinfo.validate()
        if self.feature_dbinstance_info:
            self.feature_dbinstance_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_dbinfo is not None:
            result['FeatureDBInfo'] = self.feature_dbinfo.to_map()
        if self.feature_dbinstance_info is not None:
            result['FeatureDBInstanceInfo'] = self.feature_dbinstance_info.to_map()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureDBInfo') is not None:
            temp_model = GetInstanceResponseBodyFeatureDBInfo()
            self.feature_dbinfo = temp_model.from_map(m['FeatureDBInfo'])
        if m.get('FeatureDBInstanceInfo') is not None:
            temp_model = GetInstanceResponseBodyFeatureDBInstanceInfo()
            self.feature_dbinstance_info = temp_model.from_map(m['FeatureDBInstanceInfo'])
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLLMConfigResponseBody(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        batch_size: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        llmconfig_id: str = None,
        max_tokens: int = None,
        model: str = None,
        name: str = None,
        request_id: str = None,
        rps: int = None,
        workspace_id: str = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.batch_size = batch_size
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.llmconfig_id = llmconfig_id
        self.max_tokens = max_tokens
        self.model = model
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.rps = rps
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.llmconfig_id is not None:
            result['LLMConfigId'] = self.llmconfig_id
        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens
        if self.model is not None:
            result['Model'] = self.model
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rps is not None:
            result['Rps'] = self.rps
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LLMConfigId') is not None:
            self.llmconfig_id = m.get('LLMConfigId')
        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rps') is not None:
            self.rps = m.get('Rps')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetLLMConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLLMConfigResponseBody = None,
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
            temp_model = GetLLMConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLabelTableResponseBodyFields(TeaModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
    ):
        self.attributes = attributes
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetLabelTableResponseBody(TeaModel):
    def __init__(
        self,
        datasource_id: str = None,
        datasource_name: str = None,
        fields: List[GetLabelTableResponseBodyFields] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
        related_model_features: List[str] = None,
        request_id: str = None,
    ):
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.fields = fields
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name
        self.related_model_features = related_model_features
        self.request_id = request_id

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.related_model_features is not None:
            result['RelatedModelFeatures'] = self.related_model_features
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = GetLabelTableResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RelatedModelFeatures') is not None:
            self.related_model_features = m.get('RelatedModelFeatures')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLabelTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLabelTableResponseBody = None,
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
            temp_model = GetLabelTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelFeatureResponseBodyFeatures(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        feature_view_id: str = None,
        feature_view_name: str = None,
        name: str = None,
        type: str = None,
    ):
        self.alias_name = alias_name
        self.feature_view_id = feature_view_id
        self.feature_view_name = feature_view_name
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.feature_view_name is not None:
            result['FeatureViewName'] = self.feature_view_name
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('FeatureViewName') is not None:
            self.feature_view_name = m.get('FeatureViewName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetModelFeatureResponseBodyRelationsDomains(TeaModel):
    def __init__(
        self,
        domain_type: str = None,
        id: str = None,
        name: str = None,
    ):
        self.domain_type = domain_type
        # Domain ID。
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetModelFeatureResponseBodyRelationsLinks(TeaModel):
    def __init__(
        self,
        from_: str = None,
        link: str = None,
        to: str = None,
    ):
        self.from_ = from_
        self.link = link
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.link is not None:
            result['Link'] = self.link
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetModelFeatureResponseBodyRelations(TeaModel):
    def __init__(
        self,
        domains: List[GetModelFeatureResponseBodyRelationsDomains] = None,
        links: List[GetModelFeatureResponseBodyRelationsLinks] = None,
    ):
        self.domains = domains
        self.links = links

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()
        if self.links:
            for k in self.links:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        result['Links'] = []
        if self.links is not None:
            for k in self.links:
                result['Links'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = GetModelFeatureResponseBodyRelationsDomains()
                self.domains.append(temp_model.from_map(k))
        self.links = []
        if m.get('Links') is not None:
            for k in m.get('Links'):
                temp_model = GetModelFeatureResponseBodyRelationsLinks()
                self.links.append(temp_model.from_map(k))
        return self


class GetModelFeatureResponseBody(TeaModel):
    def __init__(
        self,
        export_training_set_table_script: str = None,
        features: List[GetModelFeatureResponseBodyFeatures] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        label_priority_level: int = None,
        label_table_id: str = None,
        label_table_name: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
        relations: GetModelFeatureResponseBodyRelations = None,
        request_id: str = None,
        training_set_fgtable: str = None,
        training_set_table: str = None,
    ):
        self.export_training_set_table_script = export_training_set_table_script
        self.features = features
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.label_priority_level = label_priority_level
        self.label_table_id = label_table_id
        self.label_table_name = label_table_name
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name
        self.relations = relations
        self.request_id = request_id
        self.training_set_fgtable = training_set_fgtable
        self.training_set_table = training_set_table

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()
        if self.relations:
            self.relations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_training_set_table_script is not None:
            result['ExportTrainingSetTableScript'] = self.export_training_set_table_script
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.label_priority_level is not None:
            result['LabelPriorityLevel'] = self.label_priority_level
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.label_table_name is not None:
            result['LabelTableName'] = self.label_table_name
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.relations is not None:
            result['Relations'] = self.relations.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.training_set_fgtable is not None:
            result['TrainingSetFGTable'] = self.training_set_fgtable
        if self.training_set_table is not None:
            result['TrainingSetTable'] = self.training_set_table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportTrainingSetTableScript') is not None:
            self.export_training_set_table_script = m.get('ExportTrainingSetTableScript')
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = GetModelFeatureResponseBodyFeatures()
                self.features.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LabelPriorityLevel') is not None:
            self.label_priority_level = m.get('LabelPriorityLevel')
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('LabelTableName') is not None:
            self.label_table_name = m.get('LabelTableName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Relations') is not None:
            temp_model = GetModelFeatureResponseBodyRelations()
            self.relations = temp_model.from_map(m['Relations'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrainingSetFGTable') is not None:
            self.training_set_fgtable = m.get('TrainingSetFGTable')
        if m.get('TrainingSetTable') is not None:
            self.training_set_table = m.get('TrainingSetTable')
        return self


class GetModelFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModelFeatureResponseBody = None,
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
            temp_model = GetModelFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelFeatureFGFeatureResponseBodyLookupFeatures(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        feature_name: str = None,
        key_feature_domain: str = None,
        key_feature_name: str = None,
        map_feature_domain: str = None,
        map_feature_name: str = None,
        value_type: str = None,
    ):
        self.default_value = default_value
        self.feature_name = feature_name
        self.key_feature_domain = key_feature_domain
        self.key_feature_name = key_feature_name
        self.map_feature_domain = map_feature_domain
        self.map_feature_name = map_feature_name
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.key_feature_domain is not None:
            result['KeyFeatureDomain'] = self.key_feature_domain
        if self.key_feature_name is not None:
            result['KeyFeatureName'] = self.key_feature_name
        if self.map_feature_domain is not None:
            result['MapFeatureDomain'] = self.map_feature_domain
        if self.map_feature_name is not None:
            result['MapFeatureName'] = self.map_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('KeyFeatureDomain') is not None:
            self.key_feature_domain = m.get('KeyFeatureDomain')
        if m.get('KeyFeatureName') is not None:
            self.key_feature_name = m.get('KeyFeatureName')
        if m.get('MapFeatureDomain') is not None:
            self.map_feature_domain = m.get('MapFeatureDomain')
        if m.get('MapFeatureName') is not None:
            self.map_feature_name = m.get('MapFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class GetModelFeatureFGFeatureResponseBodyRawFeatures(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        feature_domain: str = None,
        feature_name: str = None,
        feature_type: str = None,
        input_feature_name: str = None,
        value_type: str = None,
    ):
        self.default_value = default_value
        self.feature_domain = feature_domain
        self.feature_name = feature_name
        self.feature_type = feature_type
        self.input_feature_name = input_feature_name
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_domain is not None:
            result['FeatureDomain'] = self.feature_domain
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.input_feature_name is not None:
            result['InputFeatureName'] = self.input_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureDomain') is not None:
            self.feature_domain = m.get('FeatureDomain')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('InputFeatureName') is not None:
            self.input_feature_name = m.get('InputFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class GetModelFeatureFGFeatureResponseBodySequenceFeaturesSubFeatures(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        feature_domain: str = None,
        feature_name: str = None,
        feature_type: str = None,
        input_feature_name: str = None,
        value_type: str = None,
    ):
        self.default_value = default_value
        self.feature_domain = feature_domain
        self.feature_name = feature_name
        self.feature_type = feature_type
        self.input_feature_name = input_feature_name
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_domain is not None:
            result['FeatureDomain'] = self.feature_domain
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.input_feature_name is not None:
            result['InputFeatureName'] = self.input_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureDomain') is not None:
            self.feature_domain = m.get('FeatureDomain')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('InputFeatureName') is not None:
            self.input_feature_name = m.get('InputFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class GetModelFeatureFGFeatureResponseBodySequenceFeatures(TeaModel):
    def __init__(
        self,
        attribute_delim: str = None,
        feature_name: str = None,
        sequence_delim: str = None,
        sequence_length: int = None,
        sub_features: List[GetModelFeatureFGFeatureResponseBodySequenceFeaturesSubFeatures] = None,
    ):
        self.attribute_delim = attribute_delim
        self.feature_name = feature_name
        self.sequence_delim = sequence_delim
        self.sequence_length = sequence_length
        self.sub_features = sub_features

    def validate(self):
        if self.sub_features:
            for k in self.sub_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_delim is not None:
            result['AttributeDelim'] = self.attribute_delim
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.sequence_delim is not None:
            result['SequenceDelim'] = self.sequence_delim
        if self.sequence_length is not None:
            result['SequenceLength'] = self.sequence_length
        result['SubFeatures'] = []
        if self.sub_features is not None:
            for k in self.sub_features:
                result['SubFeatures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeDelim') is not None:
            self.attribute_delim = m.get('AttributeDelim')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('SequenceDelim') is not None:
            self.sequence_delim = m.get('SequenceDelim')
        if m.get('SequenceLength') is not None:
            self.sequence_length = m.get('SequenceLength')
        self.sub_features = []
        if m.get('SubFeatures') is not None:
            for k in m.get('SubFeatures'):
                temp_model = GetModelFeatureFGFeatureResponseBodySequenceFeaturesSubFeatures()
                self.sub_features.append(temp_model.from_map(k))
        return self


class GetModelFeatureFGFeatureResponseBody(TeaModel):
    def __init__(
        self,
        lookup_features: List[GetModelFeatureFGFeatureResponseBodyLookupFeatures] = None,
        raw_features: List[GetModelFeatureFGFeatureResponseBodyRawFeatures] = None,
        request_id: str = None,
        reserves: List[str] = None,
        sequence_features: List[GetModelFeatureFGFeatureResponseBodySequenceFeatures] = None,
    ):
        self.lookup_features = lookup_features
        self.raw_features = raw_features
        self.request_id = request_id
        self.reserves = reserves
        self.sequence_features = sequence_features

    def validate(self):
        if self.lookup_features:
            for k in self.lookup_features:
                if k:
                    k.validate()
        if self.raw_features:
            for k in self.raw_features:
                if k:
                    k.validate()
        if self.sequence_features:
            for k in self.sequence_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LookupFeatures'] = []
        if self.lookup_features is not None:
            for k in self.lookup_features:
                result['LookupFeatures'].append(k.to_map() if k else None)
        result['RawFeatures'] = []
        if self.raw_features is not None:
            for k in self.raw_features:
                result['RawFeatures'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reserves is not None:
            result['Reserves'] = self.reserves
        result['SequenceFeatures'] = []
        if self.sequence_features is not None:
            for k in self.sequence_features:
                result['SequenceFeatures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lookup_features = []
        if m.get('LookupFeatures') is not None:
            for k in m.get('LookupFeatures'):
                temp_model = GetModelFeatureFGFeatureResponseBodyLookupFeatures()
                self.lookup_features.append(temp_model.from_map(k))
        self.raw_features = []
        if m.get('RawFeatures') is not None:
            for k in m.get('RawFeatures'):
                temp_model = GetModelFeatureFGFeatureResponseBodyRawFeatures()
                self.raw_features.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Reserves') is not None:
            self.reserves = m.get('Reserves')
        self.sequence_features = []
        if m.get('SequenceFeatures') is not None:
            for k in m.get('SequenceFeatures'):
                temp_model = GetModelFeatureFGFeatureResponseBodySequenceFeatures()
                self.sequence_features.append(temp_model.from_map(k))
        return self


class GetModelFeatureFGFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModelFeatureFGFeatureResponseBody = None,
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
            temp_model = GetModelFeatureFGFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelFeatureFGInfoResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetModelFeatureFGInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModelFeatureFGInfoResponseBody = None,
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
            temp_model = GetModelFeatureFGInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        feature_entity_count: int = None,
        feature_view_count: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        model_count: int = None,
        name: str = None,
        offline_datasource_id: str = None,
        offline_datasource_name: str = None,
        offline_datasource_type: str = None,
        offline_lifecycle: int = None,
        online_datasource_id: str = None,
        online_datasource_name: str = None,
        online_datasource_type: str = None,
        owner: str = None,
        request_id: str = None,
    ):
        self.description = description
        self.feature_entity_count = feature_entity_count
        self.feature_view_count = feature_view_count
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.model_count = model_count
        self.name = name
        self.offline_datasource_id = offline_datasource_id
        self.offline_datasource_name = offline_datasource_name
        self.offline_datasource_type = offline_datasource_type
        self.offline_lifecycle = offline_lifecycle
        self.online_datasource_id = online_datasource_id
        self.online_datasource_name = online_datasource_name
        self.online_datasource_type = online_datasource_type
        self.owner = owner
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.feature_entity_count is not None:
            result['FeatureEntityCount'] = self.feature_entity_count
        if self.feature_view_count is not None:
            result['FeatureViewCount'] = self.feature_view_count
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.model_count is not None:
            result['ModelCount'] = self.model_count
        if self.name is not None:
            result['Name'] = self.name
        if self.offline_datasource_id is not None:
            result['OfflineDatasourceId'] = self.offline_datasource_id
        if self.offline_datasource_name is not None:
            result['OfflineDatasourceName'] = self.offline_datasource_name
        if self.offline_datasource_type is not None:
            result['OfflineDatasourceType'] = self.offline_datasource_type
        if self.offline_lifecycle is not None:
            result['OfflineLifecycle'] = self.offline_lifecycle
        if self.online_datasource_id is not None:
            result['OnlineDatasourceId'] = self.online_datasource_id
        if self.online_datasource_name is not None:
            result['OnlineDatasourceName'] = self.online_datasource_name
        if self.online_datasource_type is not None:
            result['OnlineDatasourceType'] = self.online_datasource_type
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FeatureEntityCount') is not None:
            self.feature_entity_count = m.get('FeatureEntityCount')
        if m.get('FeatureViewCount') is not None:
            self.feature_view_count = m.get('FeatureViewCount')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ModelCount') is not None:
            self.model_count = m.get('ModelCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OfflineDatasourceId') is not None:
            self.offline_datasource_id = m.get('OfflineDatasourceId')
        if m.get('OfflineDatasourceName') is not None:
            self.offline_datasource_name = m.get('OfflineDatasourceName')
        if m.get('OfflineDatasourceType') is not None:
            self.offline_datasource_type = m.get('OfflineDatasourceType')
        if m.get('OfflineLifecycle') is not None:
            self.offline_lifecycle = m.get('OfflineLifecycle')
        if m.get('OnlineDatasourceId') is not None:
            self.online_datasource_id = m.get('OnlineDatasourceId')
        if m.get('OnlineDatasourceName') is not None:
            self.online_datasource_name = m.get('OnlineDatasourceName')
        if m.get('OnlineDatasourceType') is not None:
            self.online_datasource_type = m.get('OnlineDatasourceType')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectResponseBody = None,
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
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectFeatureEntityResponseBody(TeaModel):
    def __init__(
        self,
        feature_entity_id: str = None,
        join_id: str = None,
        name: str = None,
        project_name: str = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        self.feature_entity_id = feature_entity_id
        self.join_id = join_id
        self.name = name
        self.project_name = project_name
        self.request_id = request_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetProjectFeatureEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectFeatureEntityResponseBody = None,
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
            temp_model = GetProjectFeatureEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceIdentityRoleResponseBody(TeaModel):
    def __init__(
        self,
        policy: str = None,
        request_id: str = None,
        role_name: str = None,
    ):
        self.policy = policy
        self.request_id = request_id
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetServiceIdentityRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceIdentityRoleResponseBody = None,
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
            temp_model = GetServiceIdentityRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        gmt_create_time: str = None,
        gmt_executed_time: str = None,
        gmt_finished_time: str = None,
        gmt_modified_time: str = None,
        object_id: str = None,
        object_type: str = None,
        project_id: str = None,
        project_name: str = None,
        request_id: str = None,
        running_config: str = None,
        status: str = None,
        type: str = None,
    ):
        self.config = config
        self.gmt_create_time = gmt_create_time
        self.gmt_executed_time = gmt_executed_time
        self.gmt_finished_time = gmt_finished_time
        self.gmt_modified_time = gmt_modified_time
        self.object_id = object_id
        self.object_type = object_type
        self.project_id = project_id
        self.project_name = project_name
        self.request_id = request_id
        self.running_config = running_config
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_executed_time is not None:
            result['GmtExecutedTime'] = self.gmt_executed_time
        if self.gmt_finished_time is not None:
            result['GmtFinishedTime'] = self.gmt_finished_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.running_config is not None:
            result['RunningConfig'] = self.running_config
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtExecutedTime') is not None:
            self.gmt_executed_time = m.get('GmtExecutedTime')
        if m.get('GmtFinishedTime') is not None:
            self.gmt_finished_time = m.get('GmtFinishedTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunningConfig') is not None:
            self.running_config = m.get('RunningConfig')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResponseBody = None,
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
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasourceFeatureViewsRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        end_date: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        project_name: str = None,
        show_storage_usage: bool = None,
        sort_by: str = None,
        start_date: str = None,
        type: str = None,
        verbose: bool = None,
    ):
        self.all = all
        self.end_date = end_date
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.project_name = project_name
        self.show_storage_usage = show_storage_usage
        self.sort_by = sort_by
        self.start_date = start_date
        self.type = type
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.show_storage_usage is not None:
            result['ShowStorageUsage'] = self.show_storage_usage
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.type is not None:
            result['Type'] = self.type
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ShowStorageUsage') is not None:
            self.show_storage_usage = m.get('ShowStorageUsage')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatisticsReadWriteCount(TeaModel):
    def __init__(
        self,
        date: str = None,
        read_count: int = None,
        write_count: int = None,
    ):
        self.date = date
        self.read_count = read_count
        self.write_count = write_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.read_count is not None:
            result['ReadCount'] = self.read_count
        if self.write_count is not None:
            result['WriteCount'] = self.write_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')
        if m.get('WriteCount') is not None:
            self.write_count = m.get('WriteCount')
        return self


class ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatistics(TeaModel):
    def __init__(
        self,
        disk_usage: float = None,
        memory_usage: float = None,
        read_write_count: List[ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatisticsReadWriteCount] = None,
        row_count: int = None,
    ):
        self.disk_usage = disk_usage
        self.memory_usage = memory_usage
        self.read_write_count = read_write_count
        self.row_count = row_count

    def validate(self):
        if self.read_write_count:
            for k in self.read_write_count:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage
        if self.memory_usage is not None:
            result['MemoryUsage'] = self.memory_usage
        result['ReadWriteCount'] = []
        if self.read_write_count is not None:
            for k in self.read_write_count:
                result['ReadWriteCount'].append(k.to_map() if k else None)
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')
        if m.get('MemoryUsage') is not None:
            self.memory_usage = m.get('MemoryUsage')
        self.read_write_count = []
        if m.get('ReadWriteCount') is not None:
            for k in m.get('ReadWriteCount'):
                temp_model = ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatisticsReadWriteCount()
                self.read_write_count.append(temp_model.from_map(k))
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        return self


class ListDatasourceFeatureViewsResponseBodyFeatureViews(TeaModel):
    def __init__(
        self,
        config: str = None,
        feature_entity_name: str = None,
        feature_view_id: str = None,
        name: str = None,
        project_name: str = None,
        ttl: int = None,
        type: str = None,
        usage_statistics: ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatistics = None,
    ):
        self.config = config
        self.feature_entity_name = feature_entity_name
        self.feature_view_id = feature_view_id
        self.name = name
        self.project_name = project_name
        self.ttl = ttl
        self.type = type
        self.usage_statistics = usage_statistics

    def validate(self):
        if self.usage_statistics:
            self.usage_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_entity_name is not None:
            result['FeatureEntityName'] = self.feature_entity_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        if self.usage_statistics is not None:
            result['UsageStatistics'] = self.usage_statistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureEntityName') is not None:
            self.feature_entity_name = m.get('FeatureEntityName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UsageStatistics') is not None:
            temp_model = ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatistics()
            self.usage_statistics = temp_model.from_map(m['UsageStatistics'])
        return self


class ListDatasourceFeatureViewsResponseBodyTotalUsageStatisticsTotalReadWriteCount(TeaModel):
    def __init__(
        self,
        date: str = None,
        total_read_count: int = None,
        total_write_count: int = None,
    ):
        self.date = date
        self.total_read_count = total_read_count
        self.total_write_count = total_write_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.total_read_count is not None:
            result['TotalReadCount'] = self.total_read_count
        if self.total_write_count is not None:
            result['TotalWriteCount'] = self.total_write_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('TotalReadCount') is not None:
            self.total_read_count = m.get('TotalReadCount')
        if m.get('TotalWriteCount') is not None:
            self.total_write_count = m.get('TotalWriteCount')
        return self


class ListDatasourceFeatureViewsResponseBodyTotalUsageStatistics(TeaModel):
    def __init__(
        self,
        total_disk_usage: float = None,
        total_memory_usage: float = None,
        total_read_write_count: List[ListDatasourceFeatureViewsResponseBodyTotalUsageStatisticsTotalReadWriteCount] = None,
    ):
        self.total_disk_usage = total_disk_usage
        self.total_memory_usage = total_memory_usage
        self.total_read_write_count = total_read_write_count

    def validate(self):
        if self.total_read_write_count:
            for k in self.total_read_write_count:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_disk_usage is not None:
            result['TotalDiskUsage'] = self.total_disk_usage
        if self.total_memory_usage is not None:
            result['TotalMemoryUsage'] = self.total_memory_usage
        result['TotalReadWriteCount'] = []
        if self.total_read_write_count is not None:
            for k in self.total_read_write_count:
                result['TotalReadWriteCount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalDiskUsage') is not None:
            self.total_disk_usage = m.get('TotalDiskUsage')
        if m.get('TotalMemoryUsage') is not None:
            self.total_memory_usage = m.get('TotalMemoryUsage')
        self.total_read_write_count = []
        if m.get('TotalReadWriteCount') is not None:
            for k in m.get('TotalReadWriteCount'):
                temp_model = ListDatasourceFeatureViewsResponseBodyTotalUsageStatisticsTotalReadWriteCount()
                self.total_read_write_count.append(temp_model.from_map(k))
        return self


class ListDatasourceFeatureViewsResponseBody(TeaModel):
    def __init__(
        self,
        feature_views: List[ListDatasourceFeatureViewsResponseBodyFeatureViews] = None,
        total_count: int = None,
        total_usage_statistics: ListDatasourceFeatureViewsResponseBodyTotalUsageStatistics = None,
        request_id: str = None,
    ):
        self.feature_views = feature_views
        self.total_count = total_count
        self.total_usage_statistics = total_usage_statistics
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.feature_views:
            for k in self.feature_views:
                if k:
                    k.validate()
        if self.total_usage_statistics:
            self.total_usage_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureViews'] = []
        if self.feature_views is not None:
            for k in self.feature_views:
                result['FeatureViews'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_usage_statistics is not None:
            result['TotalUsageStatistics'] = self.total_usage_statistics.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_views = []
        if m.get('FeatureViews') is not None:
            for k in m.get('FeatureViews'):
                temp_model = ListDatasourceFeatureViewsResponseBodyFeatureViews()
                self.feature_views.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalUsageStatistics') is not None:
            temp_model = ListDatasourceFeatureViewsResponseBodyTotalUsageStatistics()
            self.total_usage_statistics = temp_model.from_map(m['TotalUsageStatistics'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListDatasourceFeatureViewsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasourceFeatureViewsResponseBody = None,
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
            temp_model = ListDatasourceFeatureViewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasourceTablesRequest(TeaModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListDatasourceTablesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tables: List[str] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.tables = tables
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tables is not None:
            result['Tables'] = self.tables
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatasourceTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasourceTablesResponseBody = None,
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
            temp_model = ListDatasourceTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasourcesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.type = type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasourcesResponseBodyDatasources(TeaModel):
    def __init__(
        self,
        config: str = None,
        datasource_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        type: str = None,
        uri: str = None,
        workspace_id: str = None,
    ):
        self.config = config
        self.datasource_id = datasource_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.type = type
        self.uri = uri
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasourcesResponseBody(TeaModel):
    def __init__(
        self,
        datasources: List[ListDatasourcesResponseBodyDatasources] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.datasources = datasources
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.datasources:
            for k in self.datasources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datasources'] = []
        if self.datasources is not None:
            for k in self.datasources:
                result['Datasources'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datasources = []
        if m.get('Datasources') is not None:
            for k in m.get('Datasources'):
                temp_model = ListDatasourcesResponseBodyDatasources()
                self.datasources.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatasourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasourcesResponseBody = None,
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
            temp_model = ListDatasourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureEntitiesRequest(TeaModel):
    def __init__(
        self,
        feature_entity_ids: List[str] = None,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_by: str = None,
    ):
        self.feature_entity_ids = feature_entity_ids
        self.name = name
        self.order = order
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_ids is not None:
            result['FeatureEntityIds'] = self.feature_entity_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureEntityIds') is not None:
            self.feature_entity_ids = m.get('FeatureEntityIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListFeatureEntitiesShrinkRequest(TeaModel):
    def __init__(
        self,
        feature_entity_ids_shrink: str = None,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_by: str = None,
    ):
        self.feature_entity_ids_shrink = feature_entity_ids_shrink
        self.name = name
        self.order = order
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_ids_shrink is not None:
            result['FeatureEntityIds'] = self.feature_entity_ids_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureEntityIds') is not None:
            self.feature_entity_ids_shrink = m.get('FeatureEntityIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListFeatureEntitiesResponseBodyFeatureEntities(TeaModel):
    def __init__(
        self,
        feature_entity_id: str = None,
        gmt_create_time: str = None,
        join_id: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.feature_entity_id = feature_entity_id
        self.gmt_create_time = gmt_create_time
        self.join_id = join_id
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListFeatureEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        feature_entities: List[ListFeatureEntitiesResponseBodyFeatureEntities] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.feature_entities = feature_entities
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.feature_entities:
            for k in self.feature_entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureEntities'] = []
        if self.feature_entities is not None:
            for k in self.feature_entities:
                result['FeatureEntities'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_entities = []
        if m.get('FeatureEntities') is not None:
            for k in m.get('FeatureEntities'):
                temp_model = ListFeatureEntitiesResponseBodyFeatureEntities()
                self.feature_entities.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeatureEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureEntitiesResponseBody = None,
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
            temp_model = ListFeatureEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureViewFieldRelationshipsResponseBodyRelationshipsModels(TeaModel):
    def __init__(
        self,
        feature_alias_name: str = None,
        model_id: str = None,
        model_name: str = None,
    ):
        self.feature_alias_name = feature_alias_name
        self.model_id = model_id
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_alias_name is not None:
            result['FeatureAliasName'] = self.feature_alias_name
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureAliasName') is not None:
            self.feature_alias_name = m.get('FeatureAliasName')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class ListFeatureViewFieldRelationshipsResponseBodyRelationships(TeaModel):
    def __init__(
        self,
        feature_name: str = None,
        models: List[ListFeatureViewFieldRelationshipsResponseBodyRelationshipsModels] = None,
        offline_table_name: str = None,
        online_table_name: str = None,
    ):
        self.feature_name = feature_name
        self.models = models
        self.offline_table_name = offline_table_name
        self.online_table_name = online_table_name

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        result['Models'] = []
        if self.models is not None:
            for k in self.models:
                result['Models'].append(k.to_map() if k else None)
        if self.offline_table_name is not None:
            result['OfflineTableName'] = self.offline_table_name
        if self.online_table_name is not None:
            result['OnlineTableName'] = self.online_table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        self.models = []
        if m.get('Models') is not None:
            for k in m.get('Models'):
                temp_model = ListFeatureViewFieldRelationshipsResponseBodyRelationshipsModels()
                self.models.append(temp_model.from_map(k))
        if m.get('OfflineTableName') is not None:
            self.offline_table_name = m.get('OfflineTableName')
        if m.get('OnlineTableName') is not None:
            self.online_table_name = m.get('OnlineTableName')
        return self


class ListFeatureViewFieldRelationshipsResponseBody(TeaModel):
    def __init__(
        self,
        relationships: List[ListFeatureViewFieldRelationshipsResponseBodyRelationships] = None,
        request_id: str = None,
    ):
        self.relationships = relationships
        self.request_id = request_id

    def validate(self):
        if self.relationships:
            for k in self.relationships:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Relationships'] = []
        if self.relationships is not None:
            for k in self.relationships:
                result['Relationships'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.relationships = []
        if m.get('Relationships') is not None:
            for k in m.get('Relationships'):
                temp_model = ListFeatureViewFieldRelationshipsResponseBodyRelationships()
                self.relationships.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureViewFieldRelationshipsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureViewFieldRelationshipsResponseBody = None,
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
            temp_model = ListFeatureViewFieldRelationshipsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureViewOnlineFeaturesRequest(TeaModel):
    def __init__(
        self,
        join_ids: List[str] = None,
    ):
        # This parameter is required.
        self.join_ids = join_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ids is not None:
            result['JoinIds'] = self.join_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinIds') is not None:
            self.join_ids = m.get('JoinIds')
        return self


class ListFeatureViewOnlineFeaturesShrinkRequest(TeaModel):
    def __init__(
        self,
        join_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.join_ids_shrink = join_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ids_shrink is not None:
            result['JoinIds'] = self.join_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinIds') is not None:
            self.join_ids_shrink = m.get('JoinIds')
        return self


class ListFeatureViewOnlineFeaturesResponseBody(TeaModel):
    def __init__(
        self,
        online_features: List[str] = None,
        request_id: str = None,
    ):
        self.online_features = online_features
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_features is not None:
            result['OnlineFeatures'] = self.online_features
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineFeatures') is not None:
            self.online_features = m.get('OnlineFeatures')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureViewOnlineFeaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureViewOnlineFeaturesResponseBody = None,
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
            temp_model = ListFeatureViewOnlineFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureViewRelationshipsResponseBodyRelationshipsModels(TeaModel):
    def __init__(
        self,
        model_id: str = None,
        model_name: str = None,
    ):
        self.model_id = model_id
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class ListFeatureViewRelationshipsResponseBodyRelationships(TeaModel):
    def __init__(
        self,
        feature_view_name: str = None,
        models: List[ListFeatureViewRelationshipsResponseBodyRelationshipsModels] = None,
        project_name: str = None,
    ):
        self.feature_view_name = feature_view_name
        self.models = models
        self.project_name = project_name

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_view_name is not None:
            result['FeatureViewName'] = self.feature_view_name
        result['Models'] = []
        if self.models is not None:
            for k in self.models:
                result['Models'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureViewName') is not None:
            self.feature_view_name = m.get('FeatureViewName')
        self.models = []
        if m.get('Models') is not None:
            for k in m.get('Models'):
                temp_model = ListFeatureViewRelationshipsResponseBodyRelationshipsModels()
                self.models.append(temp_model.from_map(k))
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListFeatureViewRelationshipsResponseBody(TeaModel):
    def __init__(
        self,
        relationships: List[ListFeatureViewRelationshipsResponseBodyRelationships] = None,
        request_id: str = None,
    ):
        self.relationships = relationships
        self.request_id = request_id

    def validate(self):
        if self.relationships:
            for k in self.relationships:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Relationships'] = []
        if self.relationships is not None:
            for k in self.relationships:
                result['Relationships'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.relationships = []
        if m.get('Relationships') is not None:
            for k in m.get('Relationships'):
                temp_model = ListFeatureViewRelationshipsResponseBodyRelationships()
                self.relationships.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureViewRelationshipsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureViewRelationshipsResponseBody = None,
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
            temp_model = ListFeatureViewRelationshipsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureViewsRequest(TeaModel):
    def __init__(
        self,
        feature_name: str = None,
        feature_view_ids: List[str] = None,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_by: str = None,
        tag: str = None,
        type: str = None,
    ):
        self.feature_name = feature_name
        self.feature_view_ids = feature_view_ids
        self.name = name
        self.order = order
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.sort_by = sort_by
        self.tag = tag
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_view_ids is not None:
            result['FeatureViewIds'] = self.feature_view_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureViewIds') is not None:
            self.feature_view_ids = m.get('FeatureViewIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFeatureViewsShrinkRequest(TeaModel):
    def __init__(
        self,
        feature_name: str = None,
        feature_view_ids_shrink: str = None,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_by: str = None,
        tag: str = None,
        type: str = None,
    ):
        self.feature_name = feature_name
        self.feature_view_ids_shrink = feature_view_ids_shrink
        self.name = name
        self.order = order
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.sort_by = sort_by
        self.tag = tag
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_view_ids_shrink is not None:
            result['FeatureViewIds'] = self.feature_view_ids_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureViewIds') is not None:
            self.feature_view_ids_shrink = m.get('FeatureViewIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFeatureViewsResponseBodyFeatureViews(TeaModel):
    def __init__(
        self,
        feature_entity_name: str = None,
        feature_view_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
        register_datasource_id: str = None,
        register_datasource_name: str = None,
        register_table: str = None,
        ttl: int = None,
        type: str = None,
        write_to_feature_db: bool = None,
    ):
        self.feature_entity_name = feature_entity_name
        self.feature_view_id = feature_view_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name
        self.register_datasource_id = register_datasource_id
        self.register_datasource_name = register_datasource_name
        self.register_table = register_table
        self.ttl = ttl
        self.type = type
        self.write_to_feature_db = write_to_feature_db

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_name is not None:
            result['FeatureEntityName'] = self.feature_entity_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.register_datasource_id is not None:
            result['RegisterDatasourceId'] = self.register_datasource_id
        if self.register_datasource_name is not None:
            result['RegisterDatasourceName'] = self.register_datasource_name
        if self.register_table is not None:
            result['RegisterTable'] = self.register_table
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        if self.write_to_feature_db is not None:
            result['WriteToFeatureDB'] = self.write_to_feature_db
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureEntityName') is not None:
            self.feature_entity_name = m.get('FeatureEntityName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegisterDatasourceId') is not None:
            self.register_datasource_id = m.get('RegisterDatasourceId')
        if m.get('RegisterDatasourceName') is not None:
            self.register_datasource_name = m.get('RegisterDatasourceName')
        if m.get('RegisterTable') is not None:
            self.register_table = m.get('RegisterTable')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WriteToFeatureDB') is not None:
            self.write_to_feature_db = m.get('WriteToFeatureDB')
        return self


class ListFeatureViewsResponseBody(TeaModel):
    def __init__(
        self,
        feature_views: List[ListFeatureViewsResponseBodyFeatureViews] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.feature_views = feature_views
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.feature_views:
            for k in self.feature_views:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureViews'] = []
        if self.feature_views is not None:
            for k in self.feature_views:
                result['FeatureViews'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_views = []
        if m.get('FeatureViews') is not None:
            for k in m.get('FeatureViews'):
                temp_model = ListFeatureViewsResponseBodyFeatureViews()
                self.feature_views.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeatureViewsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureViewsResponseBody = None,
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
            temp_model = ListFeatureViewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        status: str = None,
    ):
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstancesFeatureDBInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstancesFeatureDBInstanceInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        feature_dbinfo: ListInstancesResponseBodyInstancesFeatureDBInfo = None,
        feature_dbinstance_info: ListInstancesResponseBodyInstancesFeatureDBInstanceInfo = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.feature_dbinfo = feature_dbinfo
        self.feature_dbinstance_info = feature_dbinstance_info
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.instance_id = instance_id
        self.region_id = region_id
        self.status = status
        self.type = type

    def validate(self):
        if self.feature_dbinfo:
            self.feature_dbinfo.validate()
        if self.feature_dbinstance_info:
            self.feature_dbinstance_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_dbinfo is not None:
            result['FeatureDBInfo'] = self.feature_dbinfo.to_map()
        if self.feature_dbinstance_info is not None:
            result['FeatureDBInstanceInfo'] = self.feature_dbinstance_info.to_map()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureDBInfo') is not None:
            temp_model = ListInstancesResponseBodyInstancesFeatureDBInfo()
            self.feature_dbinfo = temp_model.from_map(m['FeatureDBInfo'])
        if m.get('FeatureDBInstanceInfo') is not None:
            temp_model = ListInstancesResponseBodyInstancesFeatureDBInstanceInfo()
            self.feature_dbinstance_info = temp_model.from_map(m['FeatureDBInstanceInfo'])
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLLMConfigsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListLLMConfigsResponseBodyLLMConfigs(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        batch_size: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        llmconfig_id: str = None,
        max_tokens: int = None,
        model: str = None,
        name: str = None,
        resource_group_id: str = None,
        rps: int = None,
        workspace_id: str = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.batch_size = batch_size
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.llmconfig_id = llmconfig_id
        self.max_tokens = max_tokens
        self.model = model
        self.name = name
        self.resource_group_id = resource_group_id
        self.rps = rps
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.llmconfig_id is not None:
            result['LLMConfigId'] = self.llmconfig_id
        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens
        if self.model is not None:
            result['Model'] = self.model
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rps is not None:
            result['Rps'] = self.rps
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LLMConfigId') is not None:
            self.llmconfig_id = m.get('LLMConfigId')
        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Rps') is not None:
            self.rps = m.get('Rps')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListLLMConfigsResponseBody(TeaModel):
    def __init__(
        self,
        llmconfigs: List[ListLLMConfigsResponseBodyLLMConfigs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # This parameter is required.
        self.llmconfigs = llmconfigs
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.llmconfigs:
            for k in self.llmconfigs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LLMConfigs'] = []
        if self.llmconfigs is not None:
            for k in self.llmconfigs:
                result['LLMConfigs'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.llmconfigs = []
        if m.get('LLMConfigs') is not None:
            for k in m.get('LLMConfigs'):
                temp_model = ListLLMConfigsResponseBodyLLMConfigs()
                self.llmconfigs.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLLMConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLLMConfigsResponseBody = None,
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
            temp_model = ListLLMConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLabelTablesRequest(TeaModel):
    def __init__(
        self,
        label_table_ids: List[str] = None,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_by: str = None,
    ):
        self.label_table_ids = label_table_ids
        self.name = name
        self.order = order
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_table_ids is not None:
            result['LabelTableIds'] = self.label_table_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelTableIds') is not None:
            self.label_table_ids = m.get('LabelTableIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListLabelTablesShrinkRequest(TeaModel):
    def __init__(
        self,
        label_table_ids_shrink: str = None,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_by: str = None,
    ):
        self.label_table_ids_shrink = label_table_ids_shrink
        self.name = name
        self.order = order
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_table_ids_shrink is not None:
            result['LabelTableIds'] = self.label_table_ids_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelTableIds') is not None:
            self.label_table_ids_shrink = m.get('LabelTableIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListLabelTablesResponseBodyLabelTables(TeaModel):
    def __init__(
        self,
        datasource_id: str = None,
        datasource_name: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        label_table_id: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.label_table_id = label_table_id
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListLabelTablesResponseBody(TeaModel):
    def __init__(
        self,
        label_tables: List[ListLabelTablesResponseBodyLabelTables] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.label_tables = label_tables
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.label_tables:
            for k in self.label_tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelTables'] = []
        if self.label_tables is not None:
            for k in self.label_tables:
                result['LabelTables'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_tables = []
        if m.get('LabelTables') is not None:
            for k in m.get('LabelTables'):
                temp_model = ListLabelTablesResponseBodyLabelTables()
                self.label_tables.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLabelTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLabelTablesResponseBody = None,
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
            temp_model = ListLabelTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelFeatureAvailableFeaturesRequest(TeaModel):
    def __init__(
        self,
        feature_name: str = None,
    ):
        self.feature_name = feature_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        return self


class ListModelFeatureAvailableFeaturesResponseBodyAvaliableFeatures(TeaModel):
    def __init__(
        self,
        name: str = None,
        source_name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.name = name
        self.source_name = source_name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListModelFeatureAvailableFeaturesResponseBody(TeaModel):
    def __init__(
        self,
        avaliable_features: List[ListModelFeatureAvailableFeaturesResponseBodyAvaliableFeatures] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.avaliable_features = avaliable_features
        self.total_count = total_count
        self.request_id = request_id

    def validate(self):
        if self.avaliable_features:
            for k in self.avaliable_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvaliableFeatures'] = []
        if self.avaliable_features is not None:
            for k in self.avaliable_features:
                result['AvaliableFeatures'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.avaliable_features = []
        if m.get('AvaliableFeatures') is not None:
            for k in m.get('AvaliableFeatures'):
                temp_model = ListModelFeatureAvailableFeaturesResponseBodyAvaliableFeatures()
                self.avaliable_features.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListModelFeatureAvailableFeaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModelFeatureAvailableFeaturesResponseBody = None,
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
            temp_model = ListModelFeatureAvailableFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelFeaturesRequest(TeaModel):
    def __init__(
        self,
        model_feature_ids: List[str] = None,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_by: str = None,
    ):
        self.model_feature_ids = model_feature_ids
        self.name = name
        self.order = order
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_feature_ids is not None:
            result['ModelFeatureIds'] = self.model_feature_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelFeatureIds') is not None:
            self.model_feature_ids = m.get('ModelFeatureIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListModelFeaturesShrinkRequest(TeaModel):
    def __init__(
        self,
        model_feature_ids_shrink: str = None,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_by: str = None,
    ):
        self.model_feature_ids_shrink = model_feature_ids_shrink
        self.name = name
        self.order = order
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_feature_ids_shrink is not None:
            result['ModelFeatureIds'] = self.model_feature_ids_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelFeatureIds') is not None:
            self.model_feature_ids_shrink = m.get('ModelFeatureIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListModelFeaturesResponseBodyModelFeatures(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        label_table_name: str = None,
        model_feature_id: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.label_table_name = label_table_name
        self.model_feature_id = model_feature_id
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.label_table_name is not None:
            result['LabelTableName'] = self.label_table_name
        if self.model_feature_id is not None:
            result['ModelFeatureId'] = self.model_feature_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LabelTableName') is not None:
            self.label_table_name = m.get('LabelTableName')
        if m.get('ModelFeatureId') is not None:
            self.model_feature_id = m.get('ModelFeatureId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListModelFeaturesResponseBody(TeaModel):
    def __init__(
        self,
        model_features: List[ListModelFeaturesResponseBodyModelFeatures] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.model_features = model_features
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.model_features:
            for k in self.model_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModelFeatures'] = []
        if self.model_features is not None:
            for k in self.model_features:
                result['ModelFeatures'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_features = []
        if m.get('ModelFeatures') is not None:
            for k in m.get('ModelFeatures'):
                temp_model = ListModelFeaturesResponseBodyModelFeatures()
                self.model_features.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListModelFeaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModelFeaturesResponseBody = None,
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
            temp_model = ListModelFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectFeatureViewsResponseBodyFeatureViewsFeatures(TeaModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
    ):
        self.attributes = attributes
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListProjectFeatureViewsResponseBodyFeatureViews(TeaModel):
    def __init__(
        self,
        feature_view_id: str = None,
        features: List[ListProjectFeatureViewsResponseBodyFeatureViewsFeatures] = None,
        name: str = None,
        type: str = None,
    ):
        self.feature_view_id = feature_view_id
        self.features = features
        self.name = name
        self.type = type

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = ListProjectFeatureViewsResponseBodyFeatureViewsFeatures()
                self.features.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListProjectFeatureViewsResponseBody(TeaModel):
    def __init__(
        self,
        feature_views: List[ListProjectFeatureViewsResponseBodyFeatureViews] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.feature_views = feature_views
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.feature_views:
            for k in self.feature_views:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureViews'] = []
        if self.feature_views is not None:
            for k in self.feature_views:
                result['FeatureViews'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_views = []
        if m.get('FeatureViews') is not None:
            for k in m.get('FeatureViews'):
                temp_model = ListProjectFeatureViewsResponseBodyFeatureViews()
                self.feature_views.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProjectFeatureViewsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectFeatureViewsResponseBody = None,
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
            temp_model = ListProjectFeatureViewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectFeaturesRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        filter: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
    ):
        self.alias_name = alias_name
        self.filter = filter
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListProjectFeaturesResponseBodyFeatures(TeaModel):
    def __init__(
        self,
        alias_names: str = None,
        feature_view_id: str = None,
        feature_view_name: str = None,
        gmt_create_time: str = None,
        model_feature_count: int = None,
        name: str = None,
        owner: str = None,
        type: str = None,
    ):
        self.alias_names = alias_names
        self.feature_view_id = feature_view_id
        self.feature_view_name = feature_view_name
        self.gmt_create_time = gmt_create_time
        self.model_feature_count = model_feature_count
        self.name = name
        self.owner = owner
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_names is not None:
            result['AliasNames'] = self.alias_names
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.feature_view_name is not None:
            result['FeatureViewName'] = self.feature_view_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.model_feature_count is not None:
            result['ModelFeatureCount'] = self.model_feature_count
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasNames') is not None:
            self.alias_names = m.get('AliasNames')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('FeatureViewName') is not None:
            self.feature_view_name = m.get('FeatureViewName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('ModelFeatureCount') is not None:
            self.model_feature_count = m.get('ModelFeatureCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListProjectFeaturesResponseBody(TeaModel):
    def __init__(
        self,
        features: List[ListProjectFeaturesResponseBodyFeatures] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.features = features
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = ListProjectFeaturesResponseBodyFeatures()
                self.features.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectFeaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectFeaturesResponseBody = None,
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
            temp_model = ListProjectFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_ids: List[str] = None,
        sort_by: str = None,
        workspace_id: str = None,
    ):
        self.name = name
        self.order = order
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_ids = project_ids
        self.sort_by = sort_by
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListProjectsShrinkRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_ids_shrink: str = None,
        sort_by: str = None,
        workspace_id: str = None,
    ):
        self.name = name
        self.order = order
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_ids_shrink = project_ids_shrink
        self.sort_by = sort_by
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_ids_shrink is not None:
            result['ProjectIds'] = self.project_ids_shrink
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectIds') is not None:
            self.project_ids_shrink = m.get('ProjectIds')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListProjectsResponseBodyProjects(TeaModel):
    def __init__(
        self,
        description: str = None,
        feature_entity_count: int = None,
        feature_view_count: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        model_count: int = None,
        name: str = None,
        offline_datasource_id: str = None,
        offline_datasource_name: str = None,
        offline_datasource_type: str = None,
        offline_lifecycle: int = None,
        online_datasource_id: str = None,
        online_datasource_name: str = None,
        online_datasource_type: str = None,
        owner: str = None,
        project_id: str = None,
    ):
        self.description = description
        self.feature_entity_count = feature_entity_count
        self.feature_view_count = feature_view_count
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.model_count = model_count
        self.name = name
        self.offline_datasource_id = offline_datasource_id
        self.offline_datasource_name = offline_datasource_name
        self.offline_datasource_type = offline_datasource_type
        self.offline_lifecycle = offline_lifecycle
        self.online_datasource_id = online_datasource_id
        self.online_datasource_name = online_datasource_name
        self.online_datasource_type = online_datasource_type
        self.owner = owner
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.feature_entity_count is not None:
            result['FeatureEntityCount'] = self.feature_entity_count
        if self.feature_view_count is not None:
            result['FeatureViewCount'] = self.feature_view_count
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.model_count is not None:
            result['ModelCount'] = self.model_count
        if self.name is not None:
            result['Name'] = self.name
        if self.offline_datasource_id is not None:
            result['OfflineDatasourceId'] = self.offline_datasource_id
        if self.offline_datasource_name is not None:
            result['OfflineDatasourceName'] = self.offline_datasource_name
        if self.offline_datasource_type is not None:
            result['OfflineDatasourceType'] = self.offline_datasource_type
        if self.offline_lifecycle is not None:
            result['OfflineLifecycle'] = self.offline_lifecycle
        if self.online_datasource_id is not None:
            result['OnlineDatasourceId'] = self.online_datasource_id
        if self.online_datasource_name is not None:
            result['OnlineDatasourceName'] = self.online_datasource_name
        if self.online_datasource_type is not None:
            result['OnlineDatasourceType'] = self.online_datasource_type
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FeatureEntityCount') is not None:
            self.feature_entity_count = m.get('FeatureEntityCount')
        if m.get('FeatureViewCount') is not None:
            self.feature_view_count = m.get('FeatureViewCount')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ModelCount') is not None:
            self.model_count = m.get('ModelCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OfflineDatasourceId') is not None:
            self.offline_datasource_id = m.get('OfflineDatasourceId')
        if m.get('OfflineDatasourceName') is not None:
            self.offline_datasource_name = m.get('OfflineDatasourceName')
        if m.get('OfflineDatasourceType') is not None:
            self.offline_datasource_type = m.get('OfflineDatasourceType')
        if m.get('OfflineLifecycle') is not None:
            self.offline_lifecycle = m.get('OfflineLifecycle')
        if m.get('OnlineDatasourceId') is not None:
            self.online_datasource_id = m.get('OnlineDatasourceId')
        if m.get('OnlineDatasourceName') is not None:
            self.online_datasource_name = m.get('OnlineDatasourceName')
        if m.get('OnlineDatasourceType') is not None:
            self.online_datasource_type = m.get('OnlineDatasourceType')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        projects: List[ListProjectsResponseBodyProjects] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.projects = projects
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = ListProjectsResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListTaskLogsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTaskLogsResponseBody(TeaModel):
    def __init__(
        self,
        logs: List[str] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.logs = logs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTaskLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTaskLogsResponseBody = None,
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
            temp_model = ListTaskLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        object_id: str = None,
        object_type: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        status: str = None,
        task_ids: List[str] = None,
        type: str = None,
    ):
        self.object_id = object_id
        self.object_type = object_type
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.status = status
        self.task_ids = task_ids
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(
        self,
        object_id: str = None,
        object_type: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        status: str = None,
        task_ids_shrink: str = None,
        type: str = None,
    ):
        self.object_id = object_id
        self.object_type = object_type
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.status = status
        self.task_ids_shrink = task_ids_shrink
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_ids_shrink is not None:
            result['TaskIds'] = self.task_ids_shrink
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskIds') is not None:
            self.task_ids_shrink = m.get('TaskIds')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_executed_time: str = None,
        gmt_finished_time: str = None,
        object_id: str = None,
        object_type: str = None,
        project_id: str = None,
        project_name: str = None,
        status: str = None,
        task_id: str = None,
        type: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_executed_time = gmt_executed_time
        self.gmt_finished_time = gmt_finished_time
        self.object_id = object_id
        self.object_type = object_type
        self.project_id = project_id
        self.project_name = project_name
        self.status = status
        self.task_id = task_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_executed_time is not None:
            result['GmtExecutedTime'] = self.gmt_executed_time
        if self.gmt_finished_time is not None:
            result['GmtFinishedTime'] = self.gmt_finished_time
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtExecutedTime') is not None:
            self.gmt_executed_time = m.get('GmtExecutedTime')
        if m.get('GmtFinishedTime') is not None:
            self.gmt_finished_time = m.get('GmtFinishedTime')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[ListTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
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
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishFeatureViewTableRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        event_time: str = None,
        mode: str = None,
        offline_to_online: bool = None,
        partitions: Dict[str, dict] = None,
    ):
        self.config = config
        self.event_time = event_time
        # This parameter is required.
        self.mode = mode
        # This parameter is required.
        self.offline_to_online = offline_to_online
        self.partitions = partitions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.offline_to_online is not None:
            result['OfflineToOnline'] = self.offline_to_online
        if self.partitions is not None:
            result['Partitions'] = self.partitions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OfflineToOnline') is not None:
            self.offline_to_online = m.get('OfflineToOnline')
        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')
        return self


class PublishFeatureViewTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class PublishFeatureViewTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishFeatureViewTableResponseBody = None,
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
            temp_model = PublishFeatureViewTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class StopTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopTaskResponseBody = None,
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
            temp_model = StopTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasourceRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        uri: str = None,
    ):
        self.config = config
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class UpdateDatasourceResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDatasourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDatasourceResponseBody = None,
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
            temp_model = UpdateDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLLMConfigRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        batch_size: int = None,
        max_tokens: int = None,
        model: str = None,
        name: str = None,
        rps: int = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        # This parameter is required.
        self.base_url = base_url
        self.batch_size = batch_size
        # This parameter is required.
        self.max_tokens = max_tokens
        # This parameter is required.
        self.model = model
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens
        if self.model is not None:
            result['Model'] = self.model
        if self.name is not None:
            result['Name'] = self.name
        if self.rps is not None:
            result['Rps'] = self.rps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rps') is not None:
            self.rps = m.get('Rps')
        return self


class UpdateLLMConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLLMConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLLMConfigResponseBody = None,
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
            temp_model = UpdateLLMConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLabelTableRequestFields(TeaModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.attributes = attributes
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateLabelTableRequest(TeaModel):
    def __init__(
        self,
        datasource_id: str = None,
        fields: List[UpdateLabelTableRequestFields] = None,
        name: str = None,
    ):
        self.datasource_id = datasource_id
        # This parameter is required.
        self.fields = fields
        self.name = name

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = UpdateLabelTableRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateLabelTableResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLabelTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLabelTableResponseBody = None,
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
            temp_model = UpdateLabelTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelFeatureRequestFeatures(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        feature_view_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.alias_name = alias_name
        # This parameter is required.
        self.feature_view_id = feature_view_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateModelFeatureRequest(TeaModel):
    def __init__(
        self,
        features: List[UpdateModelFeatureRequestFeatures] = None,
        label_priority_level: int = None,
        label_table_id: str = None,
        sequence_feature_view_ids: List[str] = None,
    ):
        self.features = features
        self.label_priority_level = label_priority_level
        self.label_table_id = label_table_id
        self.sequence_feature_view_ids = sequence_feature_view_ids

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        if self.label_priority_level is not None:
            result['LabelPriorityLevel'] = self.label_priority_level
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.sequence_feature_view_ids is not None:
            result['SequenceFeatureViewIds'] = self.sequence_feature_view_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = UpdateModelFeatureRequestFeatures()
                self.features.append(temp_model.from_map(k))
        if m.get('LabelPriorityLevel') is not None:
            self.label_priority_level = m.get('LabelPriorityLevel')
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('SequenceFeatureViewIds') is not None:
            self.sequence_feature_view_ids = m.get('SequenceFeatureViewIds')
        return self


class UpdateModelFeatureResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateModelFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateModelFeatureResponseBody = None,
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
            temp_model = UpdateModelFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelFeatureFGFeatureRequestLookupFeatures(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        feature_name: str = None,
        key_feature_domain: str = None,
        key_feature_name: str = None,
        map_feature_domain: str = None,
        map_feature_name: str = None,
        value_type: str = None,
    ):
        # This parameter is required.
        self.default_value = default_value
        # This parameter is required.
        self.feature_name = feature_name
        # This parameter is required.
        self.key_feature_domain = key_feature_domain
        # This parameter is required.
        self.key_feature_name = key_feature_name
        # This parameter is required.
        self.map_feature_domain = map_feature_domain
        # This parameter is required.
        self.map_feature_name = map_feature_name
        # This parameter is required.
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.key_feature_domain is not None:
            result['KeyFeatureDomain'] = self.key_feature_domain
        if self.key_feature_name is not None:
            result['KeyFeatureName'] = self.key_feature_name
        if self.map_feature_domain is not None:
            result['MapFeatureDomain'] = self.map_feature_domain
        if self.map_feature_name is not None:
            result['MapFeatureName'] = self.map_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('KeyFeatureDomain') is not None:
            self.key_feature_domain = m.get('KeyFeatureDomain')
        if m.get('KeyFeatureName') is not None:
            self.key_feature_name = m.get('KeyFeatureName')
        if m.get('MapFeatureDomain') is not None:
            self.map_feature_domain = m.get('MapFeatureDomain')
        if m.get('MapFeatureName') is not None:
            self.map_feature_name = m.get('MapFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class UpdateModelFeatureFGFeatureRequestRawFeatures(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        feature_domain: str = None,
        feature_name: str = None,
        feature_type: str = None,
        input_feature_name: str = None,
        value_type: str = None,
    ):
        # This parameter is required.
        self.default_value = default_value
        # This parameter is required.
        self.feature_domain = feature_domain
        # This parameter is required.
        self.feature_name = feature_name
        # This parameter is required.
        self.feature_type = feature_type
        # This parameter is required.
        self.input_feature_name = input_feature_name
        # This parameter is required.
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_domain is not None:
            result['FeatureDomain'] = self.feature_domain
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.input_feature_name is not None:
            result['InputFeatureName'] = self.input_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureDomain') is not None:
            self.feature_domain = m.get('FeatureDomain')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('InputFeatureName') is not None:
            self.input_feature_name = m.get('InputFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class UpdateModelFeatureFGFeatureRequestSequenceFeaturesSubFeatures(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        feature_domain: str = None,
        feature_name: str = None,
        feature_type: str = None,
        input_feature_name: str = None,
        value_type: str = None,
    ):
        # This parameter is required.
        self.default_value = default_value
        # This parameter is required.
        self.feature_domain = feature_domain
        # This parameter is required.
        self.feature_name = feature_name
        # This parameter is required.
        self.feature_type = feature_type
        # This parameter is required.
        self.input_feature_name = input_feature_name
        # This parameter is required.
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_domain is not None:
            result['FeatureDomain'] = self.feature_domain
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.input_feature_name is not None:
            result['InputFeatureName'] = self.input_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureDomain') is not None:
            self.feature_domain = m.get('FeatureDomain')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('InputFeatureName') is not None:
            self.input_feature_name = m.get('InputFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class UpdateModelFeatureFGFeatureRequestSequenceFeatures(TeaModel):
    def __init__(
        self,
        attribute_delim: str = None,
        feature_name: str = None,
        sequence_delim: str = None,
        sequence_length: int = None,
        sub_features: List[UpdateModelFeatureFGFeatureRequestSequenceFeaturesSubFeatures] = None,
    ):
        # This parameter is required.
        self.attribute_delim = attribute_delim
        # This parameter is required.
        self.feature_name = feature_name
        # This parameter is required.
        self.sequence_delim = sequence_delim
        # This parameter is required.
        self.sequence_length = sequence_length
        self.sub_features = sub_features

    def validate(self):
        if self.sub_features:
            for k in self.sub_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_delim is not None:
            result['AttributeDelim'] = self.attribute_delim
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.sequence_delim is not None:
            result['SequenceDelim'] = self.sequence_delim
        if self.sequence_length is not None:
            result['SequenceLength'] = self.sequence_length
        result['SubFeatures'] = []
        if self.sub_features is not None:
            for k in self.sub_features:
                result['SubFeatures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeDelim') is not None:
            self.attribute_delim = m.get('AttributeDelim')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('SequenceDelim') is not None:
            self.sequence_delim = m.get('SequenceDelim')
        if m.get('SequenceLength') is not None:
            self.sequence_length = m.get('SequenceLength')
        self.sub_features = []
        if m.get('SubFeatures') is not None:
            for k in m.get('SubFeatures'):
                temp_model = UpdateModelFeatureFGFeatureRequestSequenceFeaturesSubFeatures()
                self.sub_features.append(temp_model.from_map(k))
        return self


class UpdateModelFeatureFGFeatureRequest(TeaModel):
    def __init__(
        self,
        lookup_features: List[UpdateModelFeatureFGFeatureRequestLookupFeatures] = None,
        raw_features: List[UpdateModelFeatureFGFeatureRequestRawFeatures] = None,
        reserves: List[str] = None,
        sequence_features: List[UpdateModelFeatureFGFeatureRequestSequenceFeatures] = None,
    ):
        self.lookup_features = lookup_features
        self.raw_features = raw_features
        self.reserves = reserves
        self.sequence_features = sequence_features

    def validate(self):
        if self.lookup_features:
            for k in self.lookup_features:
                if k:
                    k.validate()
        if self.raw_features:
            for k in self.raw_features:
                if k:
                    k.validate()
        if self.sequence_features:
            for k in self.sequence_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LookupFeatures'] = []
        if self.lookup_features is not None:
            for k in self.lookup_features:
                result['LookupFeatures'].append(k.to_map() if k else None)
        result['RawFeatures'] = []
        if self.raw_features is not None:
            for k in self.raw_features:
                result['RawFeatures'].append(k.to_map() if k else None)
        if self.reserves is not None:
            result['Reserves'] = self.reserves
        result['SequenceFeatures'] = []
        if self.sequence_features is not None:
            for k in self.sequence_features:
                result['SequenceFeatures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lookup_features = []
        if m.get('LookupFeatures') is not None:
            for k in m.get('LookupFeatures'):
                temp_model = UpdateModelFeatureFGFeatureRequestLookupFeatures()
                self.lookup_features.append(temp_model.from_map(k))
        self.raw_features = []
        if m.get('RawFeatures') is not None:
            for k in m.get('RawFeatures'):
                temp_model = UpdateModelFeatureFGFeatureRequestRawFeatures()
                self.raw_features.append(temp_model.from_map(k))
        if m.get('Reserves') is not None:
            self.reserves = m.get('Reserves')
        self.sequence_features = []
        if m.get('SequenceFeatures') is not None:
            for k in m.get('SequenceFeatures'):
                temp_model = UpdateModelFeatureFGFeatureRequestSequenceFeatures()
                self.sequence_features.append(temp_model.from_map(k))
        return self


class UpdateModelFeatureFGFeatureResponseBody(TeaModel):
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


class UpdateModelFeatureFGFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateModelFeatureFGFeatureResponseBody = None,
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
            temp_model = UpdateModelFeatureFGFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateProjectResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectResponseBody = None,
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteFeatureViewTableRequestUrlDatasource(TeaModel):
    def __init__(
        self,
        delimiter: str = None,
        omit_header: bool = None,
        path: str = None,
    ):
        self.delimiter = delimiter
        self.omit_header = omit_header
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.omit_header is not None:
            result['OmitHeader'] = self.omit_header
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('OmitHeader') is not None:
            self.omit_header = m.get('OmitHeader')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class WriteFeatureViewTableRequest(TeaModel):
    def __init__(
        self,
        mode: str = None,
        partitions: Dict[str, dict] = None,
        url_datasource: WriteFeatureViewTableRequestUrlDatasource = None,
    ):
        # This parameter is required.
        self.mode = mode
        self.partitions = partitions
        self.url_datasource = url_datasource

    def validate(self):
        if self.url_datasource:
            self.url_datasource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.partitions is not None:
            result['Partitions'] = self.partitions
        if self.url_datasource is not None:
            result['UrlDatasource'] = self.url_datasource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')
        if m.get('UrlDatasource') is not None:
            temp_model = WriteFeatureViewTableRequestUrlDatasource()
            self.url_datasource = temp_model.from_map(m['UrlDatasource'])
        return self


class WriteFeatureViewTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class WriteFeatureViewTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: WriteFeatureViewTableResponseBody = None,
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
            temp_model = WriteFeatureViewTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


