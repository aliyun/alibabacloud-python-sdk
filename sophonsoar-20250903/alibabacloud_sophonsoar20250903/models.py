# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class FieldInputConfig(TeaModel):
    def __init__(
        self,
        arrayed: bool = None,
        default_value: str = None,
        field_check_regex: str = None,
        field_class: str = None,
        field_configs: List['FieldInputConfig'] = None,
        field_description: str = None,
        field_example: str = None,
        field_name: str = None,
        field_path: str = None,
        field_type: str = None,
        required: bool = None,
    ):
        self.arrayed = arrayed
        self.default_value = default_value
        self.field_check_regex = field_check_regex
        self.field_class = field_class
        self.field_configs = field_configs
        self.field_description = field_description
        self.field_example = field_example
        self.field_name = field_name
        self.field_path = field_path
        self.field_type = field_type
        self.required = required

    def validate(self):
        if self.field_configs:
            for k in self.field_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrayed is not None:
            result['Arrayed'] = self.arrayed
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.field_check_regex is not None:
            result['FieldCheckRegex'] = self.field_check_regex
        if self.field_class is not None:
            result['FieldClass'] = self.field_class
        result['FieldConfigs'] = []
        if self.field_configs is not None:
            for k in self.field_configs:
                result['FieldConfigs'].append(k.to_map() if k else None)
        if self.field_description is not None:
            result['FieldDescription'] = self.field_description
        if self.field_example is not None:
            result['FieldExample'] = self.field_example
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arrayed') is not None:
            self.arrayed = m.get('Arrayed')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FieldCheckRegex') is not None:
            self.field_check_regex = m.get('FieldCheckRegex')
        if m.get('FieldClass') is not None:
            self.field_class = m.get('FieldClass')
        self.field_configs = []
        if m.get('FieldConfigs') is not None:
            for k in m.get('FieldConfigs'):
                temp_model = FieldInputConfig()
                self.field_configs.append(temp_model.from_map(k))
        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')
        if m.get('FieldExample') is not None:
            self.field_example = m.get('FieldExample')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class FieldOutputConfig(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        field_description: str = None,
        field_example: str = None,
        field_name: str = None,
        field_type: str = None,
    ):
        self.default_value = default_value
        self.field_description = field_description
        self.field_example = field_example
        self.field_name = field_name
        self.field_type = field_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.field_description is not None:
            result['FieldDescription'] = self.field_description
        if self.field_example is not None:
            result['FieldExample'] = self.field_example
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')
        if m.get('FieldExample') is not None:
            self.field_example = m.get('FieldExample')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        return self


class CreateComponentAssetRequestComponentAssetValues(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
    ):
        # Field name.
        # 
        # This parameter is required.
        self.field_name = field_name
        # Field value.
        # 
        # This parameter is required.
        self.field_value = field_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        return self


class CreateComponentAssetRequest(TeaModel):
    def __init__(
        self,
        component_asset_name: str = None,
        component_asset_values: List[CreateComponentAssetRequestComponentAssetValues] = None,
        component_name: str = None,
        lang: str = None,
        role_for: int = None,
    ):
        # The name of the asset.
        # 
        # This parameter is required.
        self.component_asset_name = component_asset_name
        # Configuration information of the asset.
        # 
        # This parameter is required.
        self.component_asset_values = component_asset_values
        # The name of the component.
        # 
        # This parameter is required.
        self.component_name = component_name
        # The language type for receiving messages. Values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # Resource directory member account ID.
        self.role_for = role_for

    def validate(self):
        if self.component_asset_values:
            for k in self.component_asset_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_asset_name is not None:
            result['ComponentAssetName'] = self.component_asset_name
        result['ComponentAssetValues'] = []
        if self.component_asset_values is not None:
            for k in self.component_asset_values:
                result['ComponentAssetValues'].append(k.to_map() if k else None)
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetName') is not None:
            self.component_asset_name = m.get('ComponentAssetName')
        self.component_asset_values = []
        if m.get('ComponentAssetValues') is not None:
            for k in m.get('ComponentAssetValues'):
                temp_model = CreateComponentAssetRequestComponentAssetValues()
                self.component_asset_values.append(temp_model.from_map(k))
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class CreateComponentAssetResponseBody(TeaModel):
    def __init__(
        self,
        component_asset_uuid: str = None,
        request_id: str = None,
    ):
        # Asset UUID.
        self.component_asset_uuid = component_asset_uuid
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for this request and can be used to troubleshoot and locate issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_asset_uuid is not None:
            result['ComponentAssetUuid'] = self.component_asset_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetUuid') is not None:
            self.component_asset_uuid = m.get('ComponentAssetUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateComponentAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateComponentAssetResponseBody = None,
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
            temp_model = CreateComponentAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePlaybookRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_description: str = None,
        playbook_input_configs: List[FieldInputConfig] = None,
        playbook_name: str = None,
        playbook_output_configs: List[FieldOutputConfig] = None,
        playbook_param_type: str = None,
        playbook_task_flow: str = None,
        role_for: int = None,
        src_playbook_uuid: str = None,
    ):
        # Language type for receiving messages. Values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # Description of the playbook.
        self.playbook_description = playbook_description
        # Input parameter configuration of the playbook.
        self.playbook_input_configs = playbook_input_configs
        # Name of the playbook, without special characters.
        # 
        # This parameter is required.
        self.playbook_name = playbook_name
        # Output parameter configuration of the playbook.
        self.playbook_output_configs = playbook_output_configs
        # Type of input parameters for the playbook.
        # 
        # - **template-ip**: IP entity.
        # - **template-file**: File entity.
        # - **template-process**: Process entity.
        # - **template-host**: Host entity.
        # - **template-domain**: Domain entity.
        # - **template-container**: Container entity.
        # - **template-incident**: Security incident.
        # - **template-alert**: Security alert.
        # - **custom**: Custom.
        self.playbook_param_type = playbook_param_type
        # Workflow of the playbook.
        self.playbook_task_flow = playbook_task_flow
        # Resource directory member account ID.
        self.role_for = role_for
        # In a copy scenario, the UUID of the source playbook needs to be filled in. When this parameter has a value, all other parameters except the playbook name and description are invalid.
        self.src_playbook_uuid = src_playbook_uuid

    def validate(self):
        if self.playbook_input_configs:
            for k in self.playbook_input_configs:
                if k:
                    k.validate()
        if self.playbook_output_configs:
            for k in self.playbook_output_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_description is not None:
            result['PlaybookDescription'] = self.playbook_description
        result['PlaybookInputConfigs'] = []
        if self.playbook_input_configs is not None:
            for k in self.playbook_input_configs:
                result['PlaybookInputConfigs'].append(k.to_map() if k else None)
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        result['PlaybookOutputConfigs'] = []
        if self.playbook_output_configs is not None:
            for k in self.playbook_output_configs:
                result['PlaybookOutputConfigs'].append(k.to_map() if k else None)
        if self.playbook_param_type is not None:
            result['PlaybookParamType'] = self.playbook_param_type
        if self.playbook_task_flow is not None:
            result['PlaybookTaskFlow'] = self.playbook_task_flow
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.src_playbook_uuid is not None:
            result['SrcPlaybookUuid'] = self.src_playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookDescription') is not None:
            self.playbook_description = m.get('PlaybookDescription')
        self.playbook_input_configs = []
        if m.get('PlaybookInputConfigs') is not None:
            for k in m.get('PlaybookInputConfigs'):
                temp_model = FieldInputConfig()
                self.playbook_input_configs.append(temp_model.from_map(k))
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        self.playbook_output_configs = []
        if m.get('PlaybookOutputConfigs') is not None:
            for k in m.get('PlaybookOutputConfigs'):
                temp_model = FieldOutputConfig()
                self.playbook_output_configs.append(temp_model.from_map(k))
        if m.get('PlaybookParamType') is not None:
            self.playbook_param_type = m.get('PlaybookParamType')
        if m.get('PlaybookTaskFlow') is not None:
            self.playbook_task_flow = m.get('PlaybookTaskFlow')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('SrcPlaybookUuid') is not None:
            self.src_playbook_uuid = m.get('SrcPlaybookUuid')
        return self


class CreatePlaybookResponseBody(TeaModel):
    def __init__(
        self,
        playbook_uuid: str = None,
        request_id: str = None,
    ):
        # UUID of the playbook.
        self.playbook_uuid = playbook_uuid
        # The ID of this request, which is a unique identifier generated by Alibaba Cloud for this request, and can be used for troubleshooting and problem localization.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePlaybookResponseBody = None,
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
            temp_model = CreatePlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteComponentAssetRequest(TeaModel):
    def __init__(
        self,
        component_asset_uuid: str = None,
        lang: str = None,
        role_for: int = None,
    ):
        # Asset UUID.
        # 
        # This parameter is required.
        self.component_asset_uuid = component_asset_uuid
        # Set the language type for requests and received messages, default is **zh**. Values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Resource directory member account ID.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_asset_uuid is not None:
            result['ComponentAssetUuid'] = self.component_asset_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetUuid') is not None:
            self.component_asset_uuid = m.get('ComponentAssetUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeleteComponentAssetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for this request, and can be used to troubleshoot and locate issues.
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


class DeleteComponentAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteComponentAssetResponseBody = None,
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
            temp_model = DeleteComponentAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePlaybookRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
        role_for: int = None,
    ):
        # The language type for requests and received messages. Values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # UUID of the playbook.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # User ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeletePlaybookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for this request, and can be used for troubleshooting and problem localization.
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


class DeletePlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePlaybookResponseBody = None,
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
            temp_model = DeletePlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPlaybookRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
        playbook_version: str = None,
        playbook_version_type: str = None,
        role_for: int = None,
    ):
        # The language type for requests and received messages.
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The version ID of the playbook, which is only effective when **PlaybookVersionType** is **History**.
        self.playbook_version = playbook_version
        # The version type of the playbook, with the following values:
        # 
        # - **Draft**: Editing state.
        # - **Online**: Online version.
        # - **History**: Historical version.
        self.playbook_version_type = playbook_version_type
        # The user ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.playbook_version is not None:
            result['PlaybookVersion'] = self.playbook_version
        if self.playbook_version_type is not None:
            result['PlaybookVersionType'] = self.playbook_version_type
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('PlaybookVersion') is not None:
            self.playbook_version = m.get('PlaybookVersion')
        if m.get('PlaybookVersionType') is not None:
            self.playbook_version_type = m.get('PlaybookVersionType')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetPlaybookResponseBodyPlaybook(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        playbook_description: str = None,
        playbook_extension: str = None,
        playbook_input_configs: List[FieldInputConfig] = None,
        playbook_name: str = None,
        playbook_output_configs: List[FieldOutputConfig] = None,
        playbook_param_type: str = None,
        playbook_params_example: str = None,
        playbook_status: int = None,
        playbook_task_flow: str = None,
        playbook_task_flow_uuid: str = None,
        playbook_type: str = None,
        playbook_uuid: str = None,
        playbook_version: str = None,
        update_time: int = None,
    ):
        # Creation time (in milliseconds).
        self.create_time = create_time
        # Description of the playbook.
        self.playbook_description = playbook_description
        # Extended information of the playbook.
        self.playbook_extension = playbook_extension
        # List of playbook input parameter configurations.
        self.playbook_input_configs = playbook_input_configs
        # Name of the playbook, without special characters.
        self.playbook_name = playbook_name
        # List of playbook output parameter configurations.
        self.playbook_output_configs = playbook_output_configs
        # Parameter type of the playbook, with the following values:
        # 
        # - **template-ip**: IP entity.
        # - **template-file**: File entity.
        # - **template-process**: Process entity.
        # - **template-host**: Host entity.
        # - **template-domain**: Domain entity.
        # - **template-container**: Container entity.
        # - **template-incident**: Security incident.
        # - **template-alert**: Security alert.
        # - **custom**: Custom.
        self.playbook_param_type = playbook_param_type
        # Input example of the playbook.
        self.playbook_params_example = playbook_params_example
        # Publication status of the playbook, with the following values:
        # 
        # - **0**: Unpublished.
        # - **1**: Published.
        self.playbook_status = playbook_status
        # Workflow of the playbook.
        self.playbook_task_flow = playbook_task_flow
        # UUID of the playbook workflow.
        self.playbook_task_flow_uuid = playbook_task_flow_uuid
        # Type of the playbook, with values as follows:
        # 
        # - **preset**: Predefined playbook.
        # - **user**: Custom playbook.
        # - **component**: Security response component.
        self.playbook_type = playbook_type
        # UUID of the playbook.
        self.playbook_uuid = playbook_uuid
        # Version number of the playbook.
        self.playbook_version = playbook_version
        # Update time (in milliseconds).
        self.update_time = update_time

    def validate(self):
        if self.playbook_input_configs:
            for k in self.playbook_input_configs:
                if k:
                    k.validate()
        if self.playbook_output_configs:
            for k in self.playbook_output_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.playbook_description is not None:
            result['PlaybookDescription'] = self.playbook_description
        if self.playbook_extension is not None:
            result['PlaybookExtension'] = self.playbook_extension
        result['PlaybookInputConfigs'] = []
        if self.playbook_input_configs is not None:
            for k in self.playbook_input_configs:
                result['PlaybookInputConfigs'].append(k.to_map() if k else None)
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        result['PlaybookOutputConfigs'] = []
        if self.playbook_output_configs is not None:
            for k in self.playbook_output_configs:
                result['PlaybookOutputConfigs'].append(k.to_map() if k else None)
        if self.playbook_param_type is not None:
            result['PlaybookParamType'] = self.playbook_param_type
        if self.playbook_params_example is not None:
            result['PlaybookParamsExample'] = self.playbook_params_example
        if self.playbook_status is not None:
            result['PlaybookStatus'] = self.playbook_status
        if self.playbook_task_flow is not None:
            result['PlaybookTaskFlow'] = self.playbook_task_flow
        if self.playbook_task_flow_uuid is not None:
            result['PlaybookTaskFlowUuid'] = self.playbook_task_flow_uuid
        if self.playbook_type is not None:
            result['PlaybookType'] = self.playbook_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.playbook_version is not None:
            result['PlaybookVersion'] = self.playbook_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PlaybookDescription') is not None:
            self.playbook_description = m.get('PlaybookDescription')
        if m.get('PlaybookExtension') is not None:
            self.playbook_extension = m.get('PlaybookExtension')
        self.playbook_input_configs = []
        if m.get('PlaybookInputConfigs') is not None:
            for k in m.get('PlaybookInputConfigs'):
                temp_model = FieldInputConfig()
                self.playbook_input_configs.append(temp_model.from_map(k))
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        self.playbook_output_configs = []
        if m.get('PlaybookOutputConfigs') is not None:
            for k in m.get('PlaybookOutputConfigs'):
                temp_model = FieldOutputConfig()
                self.playbook_output_configs.append(temp_model.from_map(k))
        if m.get('PlaybookParamType') is not None:
            self.playbook_param_type = m.get('PlaybookParamType')
        if m.get('PlaybookParamsExample') is not None:
            self.playbook_params_example = m.get('PlaybookParamsExample')
        if m.get('PlaybookStatus') is not None:
            self.playbook_status = m.get('PlaybookStatus')
        if m.get('PlaybookTaskFlow') is not None:
            self.playbook_task_flow = m.get('PlaybookTaskFlow')
        if m.get('PlaybookTaskFlowUuid') is not None:
            self.playbook_task_flow_uuid = m.get('PlaybookTaskFlowUuid')
        if m.get('PlaybookType') is not None:
            self.playbook_type = m.get('PlaybookType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('PlaybookVersion') is not None:
            self.playbook_version = m.get('PlaybookVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        playbook: GetPlaybookResponseBodyPlaybook = None,
        request_id: str = None,
    ):
        # Configuration information of the playbook.
        self.playbook = playbook
        # The ID of this request, a unique identifier generated by Alibaba Cloud for the request, which can be used for troubleshooting and problem localization.
        self.request_id = request_id

    def validate(self):
        if self.playbook:
            self.playbook.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook is not None:
            result['Playbook'] = self.playbook.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Playbook') is not None:
            temp_model = GetPlaybookResponseBodyPlaybook()
            self.playbook = temp_model.from_map(m['Playbook'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPlaybookResponseBody = None,
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
            temp_model = GetPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentAssetsRequest(TeaModel):
    def __init__(
        self,
        component_asset_uuid: str = None,
        component_name: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        role_for: int = None,
    ):
        # Asset UUID.
        self.component_asset_uuid = component_asset_uuid
        # The name of the component.
        self.component_name = component_name
        # The language type for requests and responses. Values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # Maximum number of results to return. Range: 0~100.
        self.max_results = max_results
        # Token for the next query. Value: Not required for the first query or if there is no next query. For subsequent queries, use the NextToken value returned from the previous API call.
        self.next_token = next_token
        # Page number for paginated queries, with a default value of 1.
        self.page_number = page_number
        # Number of items per page for paginated queries. Range: 1~100.
        self.page_size = page_size
        # Resource directory member account ID.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_asset_uuid is not None:
            result['ComponentAssetUuid'] = self.component_asset_uuid
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetUuid') is not None:
            self.component_asset_uuid = m.get('ComponentAssetUuid')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListComponentAssetsResponseBodyComponentAssetsComponentAssetValues(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
    ):
        # Field name.
        self.field_name = field_name
        # Field value.
        self.field_value = field_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        return self


class ListComponentAssetsResponseBodyComponentAssets(TeaModel):
    def __init__(
        self,
        component_asset_name: str = None,
        component_asset_uuid: str = None,
        component_asset_values: List[ListComponentAssetsResponseBodyComponentAssetsComponentAssetValues] = None,
        component_name: str = None,
        create_time: int = None,
        update_time: int = None,
    ):
        # Asset name.
        self.component_asset_name = component_asset_name
        # Asset UUID.
        self.component_asset_uuid = component_asset_uuid
        # Configuration information of the asset.
        self.component_asset_values = component_asset_values
        # The name of the component.
        self.component_name = component_name
        # Creation time.
        self.create_time = create_time
        # Update time.
        self.update_time = update_time

    def validate(self):
        if self.component_asset_values:
            for k in self.component_asset_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_asset_name is not None:
            result['ComponentAssetName'] = self.component_asset_name
        if self.component_asset_uuid is not None:
            result['ComponentAssetUuid'] = self.component_asset_uuid
        result['ComponentAssetValues'] = []
        if self.component_asset_values is not None:
            for k in self.component_asset_values:
                result['ComponentAssetValues'].append(k.to_map() if k else None)
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetName') is not None:
            self.component_asset_name = m.get('ComponentAssetName')
        if m.get('ComponentAssetUuid') is not None:
            self.component_asset_uuid = m.get('ComponentAssetUuid')
        self.component_asset_values = []
        if m.get('ComponentAssetValues') is not None:
            for k in m.get('ComponentAssetValues'):
                temp_model = ListComponentAssetsResponseBodyComponentAssetsComponentAssetValues()
                self.component_asset_values.append(temp_model.from_map(k))
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListComponentAssetsResponseBody(TeaModel):
    def __init__(
        self,
        component_assets: List[ListComponentAssetsResponseBodyComponentAssets] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # List of assets.
        self.component_assets = component_assets
        # The maximum number of results to return. Range: 0~100.
        self.max_results = max_results
        # The token for the next page of results.
        self.next_token = next_token
        # Page number for paginated queries, with a default value of 1.
        self.page_number = page_number
        # The number of items to return per page. Range: 1~100.
        self.page_size = page_size
        # The unique identifier generated by Alibaba Cloud for this request, which can be used for troubleshooting and issue localization.
        self.request_id = request_id
        # Total number of queried items.
        self.total_count = total_count

    def validate(self):
        if self.component_assets:
            for k in self.component_assets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentAssets'] = []
        if self.component_assets is not None:
            for k in self.component_assets:
                result['ComponentAssets'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_assets = []
        if m.get('ComponentAssets') is not None:
            for k in m.get('ComponentAssets'):
                temp_model = ListComponentAssetsResponseBodyComponentAssets()
                self.component_assets.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListComponentAssetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListComponentAssetsResponseBody = None,
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
            temp_model = ListComponentAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentsRequest(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        role_for: int = None,
    ):
        # The name of the component.
        self.component_name = component_name
        # The language type for the request and response. Values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The size of the page. Range: 1~100. Default value: 10.
        self.max_results = max_results
        # The token to start the next page query.
        self.next_token = next_token
        # The page number for pagination, with a default value of 1.
        self.page_number = page_number
        # The number of items per page for pagination. Range: 1~100.
        self.page_size = page_size
        # Resource directory member account ID.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListComponentsResponseBodyComponentsComponentActionsInputConfigs(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        field_description: str = None,
        field_display_config: str = None,
        field_name: str = None,
        field_type: str = None,
        required: bool = None,
    ):
        # Default value.
        self.default_value = default_value
        # Field description information.
        self.field_description = field_description
        # Field display configuration.
        self.field_display_config = field_display_config
        # Field name.
        self.field_name = field_name
        # Field type, with the following values:
        # 
        # - **String**: String.
        # - **Long**: Long integer.
        # - **Integer**: Integer.
        # - **Double**: Double.
        # - **Boolean**: Boolean.
        # - **Complex**: Key-value pair.
        self.field_type = field_type
        # Whether this parameter is required.
        # 
        # - **true**: Required.
        # - **false**: Not required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.field_description is not None:
            result['FieldDescription'] = self.field_description
        if self.field_display_config is not None:
            result['FieldDisplayConfig'] = self.field_display_config
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')
        if m.get('FieldDisplayConfig') is not None:
            self.field_display_config = m.get('FieldDisplayConfig')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class ListComponentsResponseBodyComponentsComponentActionsOutputConfigs(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        field_type: str = None,
    ):
        # Field name.
        self.field_name = field_name
        # Field type, with the following values:
        # 
        # - **String**: String.
        # - **Long**: Long integer.
        # - **Integer**: Integer.
        # - **Double**: Double.
        # - **Boolean**: Boolean.
        # - **Complex**: Key-value pair.
        self.field_type = field_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        return self


class ListComponentsResponseBodyComponentsComponentActions(TeaModel):
    def __init__(
        self,
        component_action_description: str = None,
        component_action_name: str = None,
        input_configs: List[ListComponentsResponseBodyComponentsComponentActionsInputConfigs] = None,
        output_configs: List[ListComponentsResponseBodyComponentsComponentActionsOutputConfigs] = None,
    ):
        # The description of the component action name.
        self.component_action_description = component_action_description
        # The name of the component action.
        self.component_action_name = component_action_name
        # Configuration of input parameters for the action.
        self.input_configs = input_configs
        # Action output parameter configuration.
        self.output_configs = output_configs

    def validate(self):
        if self.input_configs:
            for k in self.input_configs:
                if k:
                    k.validate()
        if self.output_configs:
            for k in self.output_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_action_description is not None:
            result['ComponentActionDescription'] = self.component_action_description
        if self.component_action_name is not None:
            result['ComponentActionName'] = self.component_action_name
        result['InputConfigs'] = []
        if self.input_configs is not None:
            for k in self.input_configs:
                result['InputConfigs'].append(k.to_map() if k else None)
        result['OutputConfigs'] = []
        if self.output_configs is not None:
            for k in self.output_configs:
                result['OutputConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentActionDescription') is not None:
            self.component_action_description = m.get('ComponentActionDescription')
        if m.get('ComponentActionName') is not None:
            self.component_action_name = m.get('ComponentActionName')
        self.input_configs = []
        if m.get('InputConfigs') is not None:
            for k in m.get('InputConfigs'):
                temp_model = ListComponentsResponseBodyComponentsComponentActionsInputConfigs()
                self.input_configs.append(temp_model.from_map(k))
        self.output_configs = []
        if m.get('OutputConfigs') is not None:
            for k in m.get('OutputConfigs'):
                temp_model = ListComponentsResponseBodyComponentsComponentActionsOutputConfigs()
                self.output_configs.append(temp_model.from_map(k))
        return self


class ListComponentsResponseBodyComponentsComponentAssetConfigs(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        encrypted: bool = None,
        field_description: str = None,
        field_name: str = None,
        field_type: str = None,
        required: bool = None,
    ):
        # Default value.
        self.default_value = default_value
        # Whether the field value needs to be encrypted. The range of values is as follows:
        # 
        # - true: Encrypted.
        # - false: Not encrypted.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # Description of the field.
        self.field_description = field_description
        # Field name.
        self.field_name = field_name
        # Field type, with the following values:
        # 
        # - **String**: String.
        # - **Long**: Long integer.
        # - **Integer**: Integer.
        # - **Double**: Double.
        # - **Boolean**: Boolean.
        # - **Complex**: Key-value pair.
        self.field_type = field_type
        # Whether this parameter is required.
        # 
        # - **true**: Required.
        # - **false**: Not required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.field_description is not None:
            result['FieldDescription'] = self.field_description
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class ListComponentsResponseBodyComponents(TeaModel):
    def __init__(
        self,
        component_actions: List[ListComponentsResponseBodyComponentsComponentActions] = None,
        component_alias: str = None,
        component_asset_configs: List[ListComponentsResponseBodyComponentsComponentAssetConfigs] = None,
        component_description: str = None,
        component_extension: str = None,
        component_logo: str = None,
        component_name: str = None,
        create_time: int = None,
        update_time: int = None,
    ):
        # List of component actions.
        self.component_actions = component_actions
        # The alias of the component.
        self.component_alias = component_alias
        # List of asset field configurations.
        self.component_asset_configs = component_asset_configs
        # The description of the component.
        self.component_description = component_description
        # Extended information of the component.
        self.component_extension = component_extension
        # The icon URL of the component.
        self.component_logo = component_logo
        # The name of the component.
        self.component_name = component_name
        # Creation time.
        self.create_time = create_time
        # Update time.
        self.update_time = update_time

    def validate(self):
        if self.component_actions:
            for k in self.component_actions:
                if k:
                    k.validate()
        if self.component_asset_configs:
            for k in self.component_asset_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentActions'] = []
        if self.component_actions is not None:
            for k in self.component_actions:
                result['ComponentActions'].append(k.to_map() if k else None)
        if self.component_alias is not None:
            result['ComponentAlias'] = self.component_alias
        result['ComponentAssetConfigs'] = []
        if self.component_asset_configs is not None:
            for k in self.component_asset_configs:
                result['ComponentAssetConfigs'].append(k.to_map() if k else None)
        if self.component_description is not None:
            result['ComponentDescription'] = self.component_description
        if self.component_extension is not None:
            result['ComponentExtension'] = self.component_extension
        if self.component_logo is not None:
            result['ComponentLogo'] = self.component_logo
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_actions = []
        if m.get('ComponentActions') is not None:
            for k in m.get('ComponentActions'):
                temp_model = ListComponentsResponseBodyComponentsComponentActions()
                self.component_actions.append(temp_model.from_map(k))
        if m.get('ComponentAlias') is not None:
            self.component_alias = m.get('ComponentAlias')
        self.component_asset_configs = []
        if m.get('ComponentAssetConfigs') is not None:
            for k in m.get('ComponentAssetConfigs'):
                temp_model = ListComponentsResponseBodyComponentsComponentAssetConfigs()
                self.component_asset_configs.append(temp_model.from_map(k))
        if m.get('ComponentDescription') is not None:
            self.component_description = m.get('ComponentDescription')
        if m.get('ComponentExtension') is not None:
            self.component_extension = m.get('ComponentExtension')
        if m.get('ComponentLogo') is not None:
            self.component_logo = m.get('ComponentLogo')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListComponentsResponseBody(TeaModel):
    def __init__(
        self,
        components: List[ListComponentsResponseBodyComponents] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # List of components.
        self.components = components
        # Maximum number of results returned in a single request. Range: 1~100.
        self.max_results = max_results
        # Token for the start of the next query.
        self.next_token = next_token
        # Page number for pagination, with a default value of 1.
        self.page_number = page_number
        # Number of items per page for pagination. Range: 1~100.
        self.page_size = page_size
        # The unique identifier generated by Alibaba Cloud for this request, which can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # The total number of items found.
        self.total_count = total_count

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = ListComponentsResponseBodyComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListComponentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListComponentsResponseBody = None,
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
            temp_model = ListComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPlaybooksRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_field: str = None,
        page_number: int = None,
        page_size: int = None,
        playbook_execution_end_time: int = None,
        playbook_execution_start_time: int = None,
        playbook_name: str = None,
        playbook_param_types: List[str] = None,
        playbook_status: int = None,
        playbook_type: str = None,
        playbook_uuids: List[str] = None,
        role_for: int = None,
    ):
        # Language type for request and response messages.
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # Maximum number of results returned in a single request. Range: 1~100.
        self.max_results = max_results
        # Token for the next query start.
        self.next_token = next_token
        # Sorting logic, default is **desc**, with values as follows:
        # - **desc**: Descending order.
        # - **asc**: Ascending order.
        self.order = order
        # Sorting field. Values:
        # 
        # - **UpdateTime**: Sort by update time.
        # - **ExecutionTime**: Sort by the latest execution time.
        self.order_field = order_field
        # Page number for pagination, default value is 1.
        self.page_number = page_number
        # Number of items per page for pagination. Range: 1~100.
        self.page_size = page_size
        # End time of the latest execution of the playbook.
        self.playbook_execution_end_time = playbook_execution_end_time
        # Start time of the latest execution of the playbook.
        self.playbook_execution_start_time = playbook_execution_start_time
        # Name of the playbook, supports fuzzy search.
        self.playbook_name = playbook_name
        # Collection of input parameter types for the playbook.
        self.playbook_param_types = playbook_param_types
        # Publication status of the playbook, with values as follows:
        # 
        # - **0**: Unpublished.
        # - **1**: Published.
        self.playbook_status = playbook_status
        # Type of the playbook, with values as follows:
        # 
        # - **preset**: Predefined playbook.
        # - **user**: Custom playbook.
        # - **component**: Security response component.
        self.playbook_type = playbook_type
        # Collection of UUIDs of playbooks.
        self.playbook_uuids = playbook_uuids
        # User ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_execution_end_time is not None:
            result['PlaybookExecutionEndTime'] = self.playbook_execution_end_time
        if self.playbook_execution_start_time is not None:
            result['PlaybookExecutionStartTime'] = self.playbook_execution_start_time
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_param_types is not None:
            result['PlaybookParamTypes'] = self.playbook_param_types
        if self.playbook_status is not None:
            result['PlaybookStatus'] = self.playbook_status
        if self.playbook_type is not None:
            result['PlaybookType'] = self.playbook_type
        if self.playbook_uuids is not None:
            result['PlaybookUuids'] = self.playbook_uuids
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookExecutionEndTime') is not None:
            self.playbook_execution_end_time = m.get('PlaybookExecutionEndTime')
        if m.get('PlaybookExecutionStartTime') is not None:
            self.playbook_execution_start_time = m.get('PlaybookExecutionStartTime')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookParamTypes') is not None:
            self.playbook_param_types = m.get('PlaybookParamTypes')
        if m.get('PlaybookStatus') is not None:
            self.playbook_status = m.get('PlaybookStatus')
        if m.get('PlaybookType') is not None:
            self.playbook_type = m.get('PlaybookType')
        if m.get('PlaybookUuids') is not None:
            self.playbook_uuids = m.get('PlaybookUuids')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListPlaybooksShrinkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_field: str = None,
        page_number: int = None,
        page_size: int = None,
        playbook_execution_end_time: int = None,
        playbook_execution_start_time: int = None,
        playbook_name: str = None,
        playbook_param_types_shrink: str = None,
        playbook_status: int = None,
        playbook_type: str = None,
        playbook_uuids_shrink: str = None,
        role_for: int = None,
    ):
        # Language type for request and response messages.
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # Maximum number of results returned in a single request. Range: 1~100.
        self.max_results = max_results
        # Token for the next query start.
        self.next_token = next_token
        # Sorting logic, default is **desc**, with values as follows:
        # - **desc**: Descending order.
        # - **asc**: Ascending order.
        self.order = order
        # Sorting field. Values:
        # 
        # - **UpdateTime**: Sort by update time.
        # - **ExecutionTime**: Sort by the latest execution time.
        self.order_field = order_field
        # Page number for pagination, default value is 1.
        self.page_number = page_number
        # Number of items per page for pagination. Range: 1~100.
        self.page_size = page_size
        # End time of the latest execution of the playbook.
        self.playbook_execution_end_time = playbook_execution_end_time
        # Start time of the latest execution of the playbook.
        self.playbook_execution_start_time = playbook_execution_start_time
        # Name of the playbook, supports fuzzy search.
        self.playbook_name = playbook_name
        # Collection of input parameter types for the playbook.
        self.playbook_param_types_shrink = playbook_param_types_shrink
        # Publication status of the playbook, with values as follows:
        # 
        # - **0**: Unpublished.
        # - **1**: Published.
        self.playbook_status = playbook_status
        # Type of the playbook, with values as follows:
        # 
        # - **preset**: Predefined playbook.
        # - **user**: Custom playbook.
        # - **component**: Security response component.
        self.playbook_type = playbook_type
        # Collection of UUIDs of playbooks.
        self.playbook_uuids_shrink = playbook_uuids_shrink
        # User ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_execution_end_time is not None:
            result['PlaybookExecutionEndTime'] = self.playbook_execution_end_time
        if self.playbook_execution_start_time is not None:
            result['PlaybookExecutionStartTime'] = self.playbook_execution_start_time
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_param_types_shrink is not None:
            result['PlaybookParamTypes'] = self.playbook_param_types_shrink
        if self.playbook_status is not None:
            result['PlaybookStatus'] = self.playbook_status
        if self.playbook_type is not None:
            result['PlaybookType'] = self.playbook_type
        if self.playbook_uuids_shrink is not None:
            result['PlaybookUuids'] = self.playbook_uuids_shrink
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookExecutionEndTime') is not None:
            self.playbook_execution_end_time = m.get('PlaybookExecutionEndTime')
        if m.get('PlaybookExecutionStartTime') is not None:
            self.playbook_execution_start_time = m.get('PlaybookExecutionStartTime')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookParamTypes') is not None:
            self.playbook_param_types_shrink = m.get('PlaybookParamTypes')
        if m.get('PlaybookStatus') is not None:
            self.playbook_status = m.get('PlaybookStatus')
        if m.get('PlaybookType') is not None:
            self.playbook_type = m.get('PlaybookType')
        if m.get('PlaybookUuids') is not None:
            self.playbook_uuids_shrink = m.get('PlaybookUuids')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListPlaybooksResponseBodyPlaybooks(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        playbook_description: str = None,
        playbook_extension: str = None,
        playbook_input_configs: List[FieldInputConfig] = None,
        playbook_name: str = None,
        playbook_output_configs: List[FieldOutputConfig] = None,
        playbook_param_type: str = None,
        playbook_status: int = None,
        playbook_type: str = None,
        playbook_uuid: str = None,
        update_time: int = None,
    ):
        # Creation time (in milliseconds).
        self.create_time = create_time
        # Description of the playbook.
        self.playbook_description = playbook_description
        # Extended information of the playbook.
        self.playbook_extension = playbook_extension
        # List of input parameter configurations for the playbook.
        self.playbook_input_configs = playbook_input_configs
        # Name of the playbook.
        self.playbook_name = playbook_name
        # List of output parameter configurations for the playbook.
        self.playbook_output_configs = playbook_output_configs
        # The parameter type of the playbook, with values as follows:
        # 
        # - **template-ip**: IP entity.
        # - **template-file**: File entity.
        # - **template-process**: Process entity.
        # - **template-host**: Host entity.
        # - **template-domain**: Domain entity.
        # - **template-container**: Container entity.
        # - **template-incident**: Security incident.
        # - **template-alert**: Security alert.
        # - **custom**: Custom.
        self.playbook_param_type = playbook_param_type
        # The publication status of the playbook, with values as follows:
        # 
        # - **0**: Unpublished.
        # - **1**: Published.
        self.playbook_status = playbook_status
        # Type of the playbook, with values as follows:
        # 
        # - **preset**: Predefined playbook.
        # - **user**: Custom playbook.
        # - **component**: Security response component.
        self.playbook_type = playbook_type
        # UUID of the playbook.
        self.playbook_uuid = playbook_uuid
        # Update time (in milliseconds).
        self.update_time = update_time

    def validate(self):
        if self.playbook_input_configs:
            for k in self.playbook_input_configs:
                if k:
                    k.validate()
        if self.playbook_output_configs:
            for k in self.playbook_output_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.playbook_description is not None:
            result['PlaybookDescription'] = self.playbook_description
        if self.playbook_extension is not None:
            result['PlaybookExtension'] = self.playbook_extension
        result['PlaybookInputConfigs'] = []
        if self.playbook_input_configs is not None:
            for k in self.playbook_input_configs:
                result['PlaybookInputConfigs'].append(k.to_map() if k else None)
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        result['PlaybookOutputConfigs'] = []
        if self.playbook_output_configs is not None:
            for k in self.playbook_output_configs:
                result['PlaybookOutputConfigs'].append(k.to_map() if k else None)
        if self.playbook_param_type is not None:
            result['PlaybookParamType'] = self.playbook_param_type
        if self.playbook_status is not None:
            result['PlaybookStatus'] = self.playbook_status
        if self.playbook_type is not None:
            result['PlaybookType'] = self.playbook_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PlaybookDescription') is not None:
            self.playbook_description = m.get('PlaybookDescription')
        if m.get('PlaybookExtension') is not None:
            self.playbook_extension = m.get('PlaybookExtension')
        self.playbook_input_configs = []
        if m.get('PlaybookInputConfigs') is not None:
            for k in m.get('PlaybookInputConfigs'):
                temp_model = FieldInputConfig()
                self.playbook_input_configs.append(temp_model.from_map(k))
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        self.playbook_output_configs = []
        if m.get('PlaybookOutputConfigs') is not None:
            for k in m.get('PlaybookOutputConfigs'):
                temp_model = FieldOutputConfig()
                self.playbook_output_configs.append(temp_model.from_map(k))
        if m.get('PlaybookParamType') is not None:
            self.playbook_param_type = m.get('PlaybookParamType')
        if m.get('PlaybookStatus') is not None:
            self.playbook_status = m.get('PlaybookStatus')
        if m.get('PlaybookType') is not None:
            self.playbook_type = m.get('PlaybookType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListPlaybooksResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        playbooks: List[ListPlaybooksResponseBodyPlaybooks] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Maximum number of results allowed to be returned. Range: 0~100.
        self.max_results = max_results
        # Token for the start of the next page query.
        self.next_token = next_token
        # Current page number. The default value is 1.
        self.page_number = page_number
        # Number of items per page in a paginated query.
        self.page_size = page_size
        # List of playbooks.
        self.playbooks = playbooks
        # The unique identifier generated by Alibaba Cloud for this request, which can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # Total number of items found.
        self.total_count = total_count

    def validate(self):
        if self.playbooks:
            for k in self.playbooks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Playbooks'] = []
        if self.playbooks is not None:
            for k in self.playbooks:
                result['Playbooks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.playbooks = []
        if m.get('Playbooks') is not None:
            for k in m.get('Playbooks'):
                temp_model = ListPlaybooksResponseBodyPlaybooks()
                self.playbooks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPlaybooksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPlaybooksResponseBody = None,
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
            temp_model = ListPlaybooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateComponentAssetRequestComponentAssetValues(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
    ):
        # Field name.
        self.field_name = field_name
        # Field value.
        self.field_value = field_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        return self


class UpdateComponentAssetRequest(TeaModel):
    def __init__(
        self,
        component_asset_name: str = None,
        component_asset_uuid: str = None,
        component_asset_values: List[UpdateComponentAssetRequestComponentAssetValues] = None,
        lang: str = None,
        role_for: int = None,
    ):
        # Asset name.
        self.component_asset_name = component_asset_name
        # Asset UUID.
        # 
        # This parameter is required.
        self.component_asset_uuid = component_asset_uuid
        # Configuration information of the asset.
        self.component_asset_values = component_asset_values
        # The language type for the request and response. Values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # Resource directory member account ID.
        self.role_for = role_for

    def validate(self):
        if self.component_asset_values:
            for k in self.component_asset_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_asset_name is not None:
            result['ComponentAssetName'] = self.component_asset_name
        if self.component_asset_uuid is not None:
            result['ComponentAssetUuid'] = self.component_asset_uuid
        result['ComponentAssetValues'] = []
        if self.component_asset_values is not None:
            for k in self.component_asset_values:
                result['ComponentAssetValues'].append(k.to_map() if k else None)
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetName') is not None:
            self.component_asset_name = m.get('ComponentAssetName')
        if m.get('ComponentAssetUuid') is not None:
            self.component_asset_uuid = m.get('ComponentAssetUuid')
        self.component_asset_values = []
        if m.get('ComponentAssetValues') is not None:
            for k in m.get('ComponentAssetValues'):
                temp_model = UpdateComponentAssetRequestComponentAssetValues()
                self.component_asset_values.append(temp_model.from_map(k))
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateComponentAssetResponseBody(TeaModel):
    def __init__(
        self,
        component_asset_uuid: str = None,
        request_id: str = None,
    ):
        # Asset UUID.
        self.component_asset_uuid = component_asset_uuid
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for this request, and can be used to troubleshoot and locate issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_asset_uuid is not None:
            result['ComponentAssetUuid'] = self.component_asset_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetUuid') is not None:
            self.component_asset_uuid = m.get('ComponentAssetUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateComponentAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateComponentAssetResponseBody = None,
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
            temp_model = UpdateComponentAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePlaybookRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_description: str = None,
        playbook_input_configs: List[FieldInputConfig] = None,
        playbook_name: str = None,
        playbook_output_configs: List[FieldOutputConfig] = None,
        playbook_param_type: str = None,
        playbook_task_flow: str = None,
        playbook_uuid: str = None,
        role_for: int = None,
    ):
        # The language type for requests and received messages. Values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # Description of the playbook.
        self.playbook_description = playbook_description
        # List of input parameter configurations for the playbook.
        self.playbook_input_configs = playbook_input_configs
        # The name of the playbook.
        self.playbook_name = playbook_name
        # List of output parameter configurations for the playbook.
        self.playbook_output_configs = playbook_output_configs
        # Type of input parameters for the playbook.
        # 
        # - **template-ip**: IP entity.
        # - **template-file**: File entity.
        # - **template-process**: Process entity.
        # - **template-host**: Host entity.
        # - **template-domain**: Domain entity.
        # - **template-container**: Container entity.
        # - **template-incident**: Security incident.
        # - **template-alert**: Security alert.
        # - **custom**: Custom.
        self.playbook_param_type = playbook_param_type
        # Content of the playbook.
        self.playbook_task_flow = playbook_task_flow
        # UUID of the playbook.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The user ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for

    def validate(self):
        if self.playbook_input_configs:
            for k in self.playbook_input_configs:
                if k:
                    k.validate()
        if self.playbook_output_configs:
            for k in self.playbook_output_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_description is not None:
            result['PlaybookDescription'] = self.playbook_description
        result['PlaybookInputConfigs'] = []
        if self.playbook_input_configs is not None:
            for k in self.playbook_input_configs:
                result['PlaybookInputConfigs'].append(k.to_map() if k else None)
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        result['PlaybookOutputConfigs'] = []
        if self.playbook_output_configs is not None:
            for k in self.playbook_output_configs:
                result['PlaybookOutputConfigs'].append(k.to_map() if k else None)
        if self.playbook_param_type is not None:
            result['PlaybookParamType'] = self.playbook_param_type
        if self.playbook_task_flow is not None:
            result['PlaybookTaskFlow'] = self.playbook_task_flow
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookDescription') is not None:
            self.playbook_description = m.get('PlaybookDescription')
        self.playbook_input_configs = []
        if m.get('PlaybookInputConfigs') is not None:
            for k in m.get('PlaybookInputConfigs'):
                temp_model = FieldInputConfig()
                self.playbook_input_configs.append(temp_model.from_map(k))
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        self.playbook_output_configs = []
        if m.get('PlaybookOutputConfigs') is not None:
            for k in m.get('PlaybookOutputConfigs'):
                temp_model = FieldOutputConfig()
                self.playbook_output_configs.append(temp_model.from_map(k))
        if m.get('PlaybookParamType') is not None:
            self.playbook_param_type = m.get('PlaybookParamType')
        if m.get('PlaybookTaskFlow') is not None:
            self.playbook_task_flow = m.get('PlaybookTaskFlow')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdatePlaybookShrinkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_description: str = None,
        playbook_input_configs_shrink: str = None,
        playbook_name: str = None,
        playbook_output_configs_shrink: str = None,
        playbook_param_type: str = None,
        playbook_task_flow: str = None,
        playbook_uuid: str = None,
        role_for: int = None,
    ):
        # The language type for requests and received messages. Values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # Description of the playbook.
        self.playbook_description = playbook_description
        # List of input parameter configurations for the playbook.
        self.playbook_input_configs_shrink = playbook_input_configs_shrink
        # The name of the playbook.
        self.playbook_name = playbook_name
        # List of output parameter configurations for the playbook.
        self.playbook_output_configs_shrink = playbook_output_configs_shrink
        # Type of input parameters for the playbook.
        # 
        # - **template-ip**: IP entity.
        # - **template-file**: File entity.
        # - **template-process**: Process entity.
        # - **template-host**: Host entity.
        # - **template-domain**: Domain entity.
        # - **template-container**: Container entity.
        # - **template-incident**: Security incident.
        # - **template-alert**: Security alert.
        # - **custom**: Custom.
        self.playbook_param_type = playbook_param_type
        # Content of the playbook.
        self.playbook_task_flow = playbook_task_flow
        # UUID of the playbook.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The user ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_description is not None:
            result['PlaybookDescription'] = self.playbook_description
        if self.playbook_input_configs_shrink is not None:
            result['PlaybookInputConfigs'] = self.playbook_input_configs_shrink
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_output_configs_shrink is not None:
            result['PlaybookOutputConfigs'] = self.playbook_output_configs_shrink
        if self.playbook_param_type is not None:
            result['PlaybookParamType'] = self.playbook_param_type
        if self.playbook_task_flow is not None:
            result['PlaybookTaskFlow'] = self.playbook_task_flow
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookDescription') is not None:
            self.playbook_description = m.get('PlaybookDescription')
        if m.get('PlaybookInputConfigs') is not None:
            self.playbook_input_configs_shrink = m.get('PlaybookInputConfigs')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookOutputConfigs') is not None:
            self.playbook_output_configs_shrink = m.get('PlaybookOutputConfigs')
        if m.get('PlaybookParamType') is not None:
            self.playbook_param_type = m.get('PlaybookParamType')
        if m.get('PlaybookTaskFlow') is not None:
            self.playbook_task_flow = m.get('PlaybookTaskFlow')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdatePlaybookResponseBody(TeaModel):
    def __init__(
        self,
        playbook_uuid: str = None,
        request_id: str = None,
    ):
        # UUID of the playbook.
        self.playbook_uuid = playbook_uuid
        # The ID of this request, which is a unique identifier generated by Alibaba Cloud for the request, and can be used for troubleshooting and problem localization.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePlaybookResponseBody = None,
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
            temp_model = UpdatePlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


