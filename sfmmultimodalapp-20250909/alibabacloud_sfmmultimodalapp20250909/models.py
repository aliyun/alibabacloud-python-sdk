# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CreateCommandRequestToolExamples(TeaModel):
    def __init__(
        self,
        query: str = None,
    ):
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class CreateCommandRequestToolParams(TeaModel):
    def __init__(
        self,
        param_desc: str = None,
        param_example: str = None,
        param_name: str = None,
    ):
        self.param_desc = param_desc
        self.param_example = param_example
        self.param_name = param_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_desc is not None:
            result['ParamDesc'] = self.param_desc
        if self.param_example is not None:
            result['ParamExample'] = self.param_example
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamDesc') is not None:
            self.param_desc = m.get('ParamDesc')
        if m.get('ParamExample') is not None:
            self.param_example = m.get('ParamExample')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        return self


class CreateCommandRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain_code: str = None,
        domain_name: str = None,
        tool_description: str = None,
        tool_examples: List[CreateCommandRequestToolExamples] = None,
        tool_name: str = None,
        tool_params: List[CreateCommandRequestToolParams] = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.domain_code = domain_code
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.tool_description = tool_description
        self.tool_examples = tool_examples
        # This parameter is required.
        self.tool_name = tool_name
        self.tool_params = tool_params
        self.workspace_id = workspace_id

    def validate(self):
        if self.tool_examples:
            for k in self.tool_examples:
                if k:
                    k.validate()
        if self.tool_params:
            for k in self.tool_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.tool_description is not None:
            result['ToolDescription'] = self.tool_description
        result['ToolExamples'] = []
        if self.tool_examples is not None:
            for k in self.tool_examples:
                result['ToolExamples'].append(k.to_map() if k else None)
        if self.tool_name is not None:
            result['ToolName'] = self.tool_name
        result['ToolParams'] = []
        if self.tool_params is not None:
            for k in self.tool_params:
                result['ToolParams'].append(k.to_map() if k else None)
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ToolDescription') is not None:
            self.tool_description = m.get('ToolDescription')
        self.tool_examples = []
        if m.get('ToolExamples') is not None:
            for k in m.get('ToolExamples'):
                temp_model = CreateCommandRequestToolExamples()
                self.tool_examples.append(temp_model.from_map(k))
        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')
        self.tool_params = []
        if m.get('ToolParams') is not None:
            for k in m.get('ToolParams'):
                temp_model = CreateCommandRequestToolParams()
                self.tool_params.append(temp_model.from_map(k))
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateCommandShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain_code: str = None,
        domain_name: str = None,
        tool_description: str = None,
        tool_examples_shrink: str = None,
        tool_name: str = None,
        tool_params_shrink: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.domain_code = domain_code
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.tool_description = tool_description
        self.tool_examples_shrink = tool_examples_shrink
        # This parameter is required.
        self.tool_name = tool_name
        self.tool_params_shrink = tool_params_shrink
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.tool_description is not None:
            result['ToolDescription'] = self.tool_description
        if self.tool_examples_shrink is not None:
            result['ToolExamples'] = self.tool_examples_shrink
        if self.tool_name is not None:
            result['ToolName'] = self.tool_name
        if self.tool_params_shrink is not None:
            result['ToolParams'] = self.tool_params_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ToolDescription') is not None:
            self.tool_description = m.get('ToolDescription')
        if m.get('ToolExamples') is not None:
            self.tool_examples_shrink = m.get('ToolExamples')
        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')
        if m.get('ToolParams') is not None:
            self.tool_params_shrink = m.get('ToolParams')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateCommandResponseBody(TeaModel):
    def __init__(
        self,
        domain_code: str = None,
        request_id: str = None,
        tool_id: str = None,
    ):
        self.domain_code = domain_code
        self.request_id = request_id
        self.tool_id = tool_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tool_id is not None:
            result['ToolId'] = self.tool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')
        return self


class CreateCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCommandResponseBody = None,
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
            temp_model = CreateCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMmAppRequestBindingConfigCommandsTools(TeaModel):
    def __init__(
        self,
        tool_id: str = None,
    ):
        # This parameter is required.
        self.tool_id = tool_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tool_id is not None:
            result['ToolId'] = self.tool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')
        return self


class CreateMmAppRequestBindingConfigCommands(TeaModel):
    def __init__(
        self,
        domain_code: str = None,
        tools: List[CreateMmAppRequestBindingConfigCommandsTools] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.domain_code = domain_code
        self.tools = tools
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.tools:
            for k in self.tools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        result['Tools'] = []
        if self.tools is not None:
            for k in self.tools:
                result['Tools'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        self.tools = []
        if m.get('Tools') is not None:
            for k in m.get('Tools'):
                temp_model = CreateMmAppRequestBindingConfigCommandsTools()
                self.tools.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateMmAppRequestBindingConfig(TeaModel):
    def __init__(
        self,
        commands: List[CreateMmAppRequestBindingConfigCommands] = None,
    ):
        self.commands = commands

    def validate(self):
        if self.commands:
            for k in self.commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Commands'] = []
        if self.commands is not None:
            for k in self.commands:
                result['Commands'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k in m.get('Commands'):
                temp_model = CreateMmAppRequestBindingConfigCommands()
                self.commands.append(temp_model.from_map(k))
        return self


class CreateMmAppRequestConversationConfig(TeaModel):
    def __init__(
        self,
        asr_model: str = None,
        open_asr: bool = None,
        open_tts: bool = None,
        tts_model: str = None,
    ):
        self.asr_model = asr_model
        self.open_asr = open_asr
        self.open_tts = open_tts
        self.tts_model = tts_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_model is not None:
            result['AsrModel'] = self.asr_model
        if self.open_asr is not None:
            result['OpenAsr'] = self.open_asr
        if self.open_tts is not None:
            result['OpenTts'] = self.open_tts
        if self.tts_model is not None:
            result['TtsModel'] = self.tts_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrModel') is not None:
            self.asr_model = m.get('AsrModel')
        if m.get('OpenAsr') is not None:
            self.open_asr = m.get('OpenAsr')
        if m.get('OpenTts') is not None:
            self.open_tts = m.get('OpenTts')
        if m.get('TtsModel') is not None:
            self.tts_model = m.get('TtsModel')
        return self


class CreateMmAppRequestModelConfig(TeaModel):
    def __init__(
        self,
        history_limit: int = None,
        model_type: str = None,
        open_web_search: bool = None,
        text_modal: str = None,
    ):
        self.history_limit = history_limit
        self.model_type = model_type
        self.open_web_search = open_web_search
        self.text_modal = text_modal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_limit is not None:
            result['HistoryLimit'] = self.history_limit
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.open_web_search is not None:
            result['OpenWebSearch'] = self.open_web_search
        if self.text_modal is not None:
            result['TextModal'] = self.text_modal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoryLimit') is not None:
            self.history_limit = m.get('HistoryLimit')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('OpenWebSearch') is not None:
            self.open_web_search = m.get('OpenWebSearch')
        if m.get('TextModal') is not None:
            self.text_modal = m.get('TextModal')
        return self


class CreateMmAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        binding_config: CreateMmAppRequestBindingConfig = None,
        conversation_config: CreateMmAppRequestConversationConfig = None,
        model_config: CreateMmAppRequestModelConfig = None,
        prompt: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.binding_config = binding_config
        self.conversation_config = conversation_config
        self.model_config = model_config
        self.prompt = prompt
        self.workspace_id = workspace_id

    def validate(self):
        if self.binding_config:
            self.binding_config.validate()
        if self.conversation_config:
            self.conversation_config.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.binding_config is not None:
            result['BindingConfig'] = self.binding_config.to_map()
        if self.conversation_config is not None:
            result['ConversationConfig'] = self.conversation_config.to_map()
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BindingConfig') is not None:
            temp_model = CreateMmAppRequestBindingConfig()
            self.binding_config = temp_model.from_map(m['BindingConfig'])
        if m.get('ConversationConfig') is not None:
            temp_model = CreateMmAppRequestConversationConfig()
            self.conversation_config = temp_model.from_map(m['ConversationConfig'])
        if m.get('ModelConfig') is not None:
            temp_model = CreateMmAppRequestModelConfig()
            self.model_config = temp_model.from_map(m['ModelConfig'])
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMmAppShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        binding_config_shrink: str = None,
        conversation_config_shrink: str = None,
        model_config_shrink: str = None,
        prompt: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.binding_config_shrink = binding_config_shrink
        self.conversation_config_shrink = conversation_config_shrink
        self.model_config_shrink = model_config_shrink
        self.prompt = prompt
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.binding_config_shrink is not None:
            result['BindingConfig'] = self.binding_config_shrink
        if self.conversation_config_shrink is not None:
            result['ConversationConfig'] = self.conversation_config_shrink
        if self.model_config_shrink is not None:
            result['ModelConfig'] = self.model_config_shrink
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BindingConfig') is not None:
            self.binding_config_shrink = m.get('BindingConfig')
        if m.get('ConversationConfig') is not None:
            self.conversation_config_shrink = m.get('ConversationConfig')
        if m.get('ModelConfig') is not None:
            self.model_config_shrink = m.get('ModelConfig')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMmAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMmAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMmAppResponseBody = None,
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
            temp_model = CreateMmAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCommandRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain_code: str = None,
        tool_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.domain_code = domain_code
        # This parameter is required.
        self.tool_id = tool_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.tool_id is not None:
            result['ToolId'] = self.tool_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteCommandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCommandResponseBody = None,
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
            temp_model = DeleteCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMmAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteMmAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMmAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMmAppResponseBody = None,
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
            temp_model = DeleteMmAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCommandRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain_code: str = None,
        tool_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.domain_code = domain_code
        # This parameter is required.
        self.tool_id = tool_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.tool_id is not None:
            result['ToolId'] = self.tool_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DescribeCommandResponseBodyToolExamples(TeaModel):
    def __init__(
        self,
        query: str = None,
    ):
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class DescribeCommandResponseBodyToolParams(TeaModel):
    def __init__(
        self,
        param_desc: str = None,
        param_example: str = None,
        param_name: str = None,
    ):
        self.param_desc = param_desc
        self.param_example = param_example
        self.param_name = param_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_desc is not None:
            result['ParamDesc'] = self.param_desc
        if self.param_example is not None:
            result['ParamExample'] = self.param_example
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamDesc') is not None:
            self.param_desc = m.get('ParamDesc')
        if m.get('ParamExample') is not None:
            self.param_example = m.get('ParamExample')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        return self


class DescribeCommandResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        description: str = None,
        domain_code: str = None,
        domain_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        request_id: str = None,
        tool_examples: List[DescribeCommandResponseBodyToolExamples] = None,
        tool_id: str = None,
        tool_name: str = None,
        tool_params: List[DescribeCommandResponseBodyToolParams] = None,
    ):
        self.app_id = app_id
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.description = description
        self.domain_code = domain_code
        self.domain_name = domain_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.request_id = request_id
        self.tool_examples = tool_examples
        self.tool_id = tool_id
        self.tool_name = tool_name
        self.tool_params = tool_params

    def validate(self):
        if self.tool_examples:
            for k in self.tool_examples:
                if k:
                    k.validate()
        if self.tool_params:
            for k in self.tool_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ToolExamples'] = []
        if self.tool_examples is not None:
            for k in self.tool_examples:
                result['ToolExamples'].append(k.to_map() if k else None)
        if self.tool_id is not None:
            result['ToolId'] = self.tool_id
        if self.tool_name is not None:
            result['ToolName'] = self.tool_name
        result['ToolParams'] = []
        if self.tool_params is not None:
            for k in self.tool_params:
                result['ToolParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tool_examples = []
        if m.get('ToolExamples') is not None:
            for k in m.get('ToolExamples'):
                temp_model = DescribeCommandResponseBodyToolExamples()
                self.tool_examples.append(temp_model.from_map(k))
        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')
        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')
        self.tool_params = []
        if m.get('ToolParams') is not None:
            for k in m.get('ToolParams'):
                temp_model = DescribeCommandResponseBodyToolParams()
                self.tool_params.append(temp_model.from_map(k))
        return self


class DescribeCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCommandResponseBody = None,
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
            temp_model = DescribeCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMmAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DescribeMmAppResponseBodyConversationConfig(TeaModel):
    def __init__(
        self,
        asr_model: str = None,
        open_asr: bool = None,
        open_tts: bool = None,
        tts_model: str = None,
    ):
        self.asr_model = asr_model
        self.open_asr = open_asr
        self.open_tts = open_tts
        self.tts_model = tts_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_model is not None:
            result['AsrModel'] = self.asr_model
        if self.open_asr is not None:
            result['OpenAsr'] = self.open_asr
        if self.open_tts is not None:
            result['OpenTts'] = self.open_tts
        if self.tts_model is not None:
            result['TtsModel'] = self.tts_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrModel') is not None:
            self.asr_model = m.get('AsrModel')
        if m.get('OpenAsr') is not None:
            self.open_asr = m.get('OpenAsr')
        if m.get('OpenTts') is not None:
            self.open_tts = m.get('OpenTts')
        if m.get('TtsModel') is not None:
            self.tts_model = m.get('TtsModel')
        return self


class DescribeMmAppResponseBodyModelConfig(TeaModel):
    def __init__(
        self,
        history_limit: int = None,
        model_type: str = None,
        open_web_search: bool = None,
        text_modal: str = None,
    ):
        self.history_limit = history_limit
        self.model_type = model_type
        self.open_web_search = open_web_search
        self.text_modal = text_modal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_limit is not None:
            result['HistoryLimit'] = self.history_limit
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.open_web_search is not None:
            result['OpenWebSearch'] = self.open_web_search
        if self.text_modal is not None:
            result['TextModal'] = self.text_modal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoryLimit') is not None:
            self.history_limit = m.get('HistoryLimit')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('OpenWebSearch') is not None:
            self.open_web_search = m.get('OpenWebSearch')
        if m.get('TextModal') is not None:
            self.text_modal = m.get('TextModal')
        return self


class DescribeMmAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        conversation_config: DescribeMmAppResponseBodyConversationConfig = None,
        create_user_id: str = None,
        create_user_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        model_config: DescribeMmAppResponseBodyModelConfig = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        prompt: str = None,
        publish_version: int = None,
        request_id: str = None,
        status: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.conversation_config = conversation_config
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.model_config = model_config
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.prompt = prompt
        self.publish_version = publish_version
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.conversation_config:
            self.conversation_config.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.conversation_config is not None:
            result['ConversationConfig'] = self.conversation_config.to_map()
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.publish_version is not None:
            result['PublishVersion'] = self.publish_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ConversationConfig') is not None:
            temp_model = DescribeMmAppResponseBodyConversationConfig()
            self.conversation_config = temp_model.from_map(m['ConversationConfig'])
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ModelConfig') is not None:
            temp_model = DescribeMmAppResponseBodyModelConfig()
            self.model_config = temp_model.from_map(m['ModelConfig'])
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('PublishVersion') is not None:
            self.publish_version = m.get('PublishVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMmAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMmAppResponseBody = None,
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
            temp_model = DescribeMmAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommandRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain_code: str = None,
        page_number: int = None,
        page_size: int = None,
        tool_name: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.domain_code = domain_code
        self.page_number = page_number
        self.page_size = page_size
        self.tool_name = tool_name
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tool_name is not None:
            result['ToolName'] = self.tool_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListCommandResponseBodyToolInfoListToolExamples(TeaModel):
    def __init__(
        self,
        query: str = None,
    ):
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class ListCommandResponseBodyToolInfoListToolParams(TeaModel):
    def __init__(
        self,
        param_desc: str = None,
        param_example: str = None,
        param_name: str = None,
    ):
        self.param_desc = param_desc
        self.param_example = param_example
        self.param_name = param_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_desc is not None:
            result['ParamDesc'] = self.param_desc
        if self.param_example is not None:
            result['ParamExample'] = self.param_example
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamDesc') is not None:
            self.param_desc = m.get('ParamDesc')
        if m.get('ParamExample') is not None:
            self.param_example = m.get('ParamExample')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        return self


class ListCommandResponseBodyToolInfoList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        description: str = None,
        domain_code: str = None,
        domain_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        tool_examples: List[ListCommandResponseBodyToolInfoListToolExamples] = None,
        tool_id: str = None,
        tool_name: str = None,
        tool_params: List[ListCommandResponseBodyToolInfoListToolParams] = None,
    ):
        self.app_id = app_id
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.description = description
        self.domain_code = domain_code
        self.domain_name = domain_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.tool_examples = tool_examples
        self.tool_id = tool_id
        self.tool_name = tool_name
        self.tool_params = tool_params

    def validate(self):
        if self.tool_examples:
            for k in self.tool_examples:
                if k:
                    k.validate()
        if self.tool_params:
            for k in self.tool_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        result['ToolExamples'] = []
        if self.tool_examples is not None:
            for k in self.tool_examples:
                result['ToolExamples'].append(k.to_map() if k else None)
        if self.tool_id is not None:
            result['ToolId'] = self.tool_id
        if self.tool_name is not None:
            result['ToolName'] = self.tool_name
        result['ToolParams'] = []
        if self.tool_params is not None:
            for k in self.tool_params:
                result['ToolParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        self.tool_examples = []
        if m.get('ToolExamples') is not None:
            for k in m.get('ToolExamples'):
                temp_model = ListCommandResponseBodyToolInfoListToolExamples()
                self.tool_examples.append(temp_model.from_map(k))
        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')
        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')
        self.tool_params = []
        if m.get('ToolParams') is not None:
            for k in m.get('ToolParams'):
                temp_model = ListCommandResponseBodyToolInfoListToolParams()
                self.tool_params.append(temp_model.from_map(k))
        return self


class ListCommandResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tool_info_list: List[ListCommandResponseBodyToolInfoList] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tool_info_list = tool_info_list
        self.total_count = total_count

    def validate(self):
        if self.tool_info_list:
            for k in self.tool_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ToolInfoList'] = []
        if self.tool_info_list is not None:
            for k in self.tool_info_list:
                result['ToolInfoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tool_info_list = []
        if m.get('ToolInfoList') is not None:
            for k in m.get('ToolInfoList'):
                temp_model = ListCommandResponseBodyToolInfoList()
                self.tool_info_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCommandResponseBody = None,
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
            temp_model = ListCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMmAppRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
        workspace_id: str = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.status = status
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMmAppResponseBodyAppInfoListConversationConfig(TeaModel):
    def __init__(
        self,
        asr_model: str = None,
        open_asr: bool = None,
        open_tts: bool = None,
        tts_model: str = None,
    ):
        self.asr_model = asr_model
        self.open_asr = open_asr
        self.open_tts = open_tts
        self.tts_model = tts_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_model is not None:
            result['AsrModel'] = self.asr_model
        if self.open_asr is not None:
            result['OpenAsr'] = self.open_asr
        if self.open_tts is not None:
            result['OpenTts'] = self.open_tts
        if self.tts_model is not None:
            result['TtsModel'] = self.tts_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrModel') is not None:
            self.asr_model = m.get('AsrModel')
        if m.get('OpenAsr') is not None:
            self.open_asr = m.get('OpenAsr')
        if m.get('OpenTts') is not None:
            self.open_tts = m.get('OpenTts')
        if m.get('TtsModel') is not None:
            self.tts_model = m.get('TtsModel')
        return self


class ListMmAppResponseBodyAppInfoListModelConfig(TeaModel):
    def __init__(
        self,
        history_limit: str = None,
        model_type: str = None,
        open_web_search: bool = None,
        text_modal: str = None,
    ):
        self.history_limit = history_limit
        self.model_type = model_type
        self.open_web_search = open_web_search
        self.text_modal = text_modal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_limit is not None:
            result['HistoryLimit'] = self.history_limit
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.open_web_search is not None:
            result['OpenWebSearch'] = self.open_web_search
        if self.text_modal is not None:
            result['TextModal'] = self.text_modal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoryLimit') is not None:
            self.history_limit = m.get('HistoryLimit')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('OpenWebSearch') is not None:
            self.open_web_search = m.get('OpenWebSearch')
        if m.get('TextModal') is not None:
            self.text_modal = m.get('TextModal')
        return self


class ListMmAppResponseBodyAppInfoList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        conversation_config: ListMmAppResponseBodyAppInfoListConversationConfig = None,
        create_user_id: str = None,
        create_user_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        model_config: ListMmAppResponseBodyAppInfoListModelConfig = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        prompt: str = None,
        publish_version: int = None,
        status: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.conversation_config = conversation_config
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.model_config = model_config
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.prompt = prompt
        self.publish_version = publish_version
        self.status = status

    def validate(self):
        if self.conversation_config:
            self.conversation_config.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.conversation_config is not None:
            result['ConversationConfig'] = self.conversation_config.to_map()
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.publish_version is not None:
            result['PublishVersion'] = self.publish_version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ConversationConfig') is not None:
            temp_model = ListMmAppResponseBodyAppInfoListConversationConfig()
            self.conversation_config = temp_model.from_map(m['ConversationConfig'])
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ModelConfig') is not None:
            temp_model = ListMmAppResponseBodyAppInfoListModelConfig()
            self.model_config = temp_model.from_map(m['ModelConfig'])
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('PublishVersion') is not None:
            self.publish_version = m.get('PublishVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListMmAppResponseBody(TeaModel):
    def __init__(
        self,
        app_info_list: List[ListMmAppResponseBodyAppInfoList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.app_info_list = app_info_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
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
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = ListMmAppResponseBodyAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMmAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMmAppResponseBody = None,
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
            temp_model = ListMmAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishedMmAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListPublishedMmAppResponseBodyPublishedVersionInfoList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        description: str = None,
        gmt_create: str = None,
        publish_time: str = None,
        version: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.description = description
        self.gmt_create = gmt_create
        self.publish_time = publish_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListPublishedMmAppResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        published_version_info_list: List[ListPublishedMmAppResponseBodyPublishedVersionInfoList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.published_version_info_list = published_version_info_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.published_version_info_list:
            for k in self.published_version_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PublishedVersionInfoList'] = []
        if self.published_version_info_list is not None:
            for k in self.published_version_info_list:
                result['PublishedVersionInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.published_version_info_list = []
        if m.get('PublishedVersionInfoList') is not None:
            for k in m.get('PublishedVersionInfoList'):
                temp_model = ListPublishedMmAppResponseBodyPublishedVersionInfoList()
                self.published_version_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublishedMmAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublishedMmAppResponseBody = None,
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
            temp_model = ListPublishedMmAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishMmAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.description = description
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PublishMmAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PublishMmAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishMmAppResponseBody = None,
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
            temp_model = PublishMmAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCommandRequestToolExamples(TeaModel):
    def __init__(
        self,
        query: str = None,
    ):
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class UpdateCommandRequestToolParams(TeaModel):
    def __init__(
        self,
        param_desc: str = None,
        param_example: str = None,
        param_name: str = None,
    ):
        self.param_desc = param_desc
        self.param_example = param_example
        self.param_name = param_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_desc is not None:
            result['ParamDesc'] = self.param_desc
        if self.param_example is not None:
            result['ParamExample'] = self.param_example
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamDesc') is not None:
            self.param_desc = m.get('ParamDesc')
        if m.get('ParamExample') is not None:
            self.param_example = m.get('ParamExample')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        return self


class UpdateCommandRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain_code: str = None,
        domain_name: str = None,
        tool_description: str = None,
        tool_examples: List[UpdateCommandRequestToolExamples] = None,
        tool_id: str = None,
        tool_name: str = None,
        tool_params: List[UpdateCommandRequestToolParams] = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.domain_code = domain_code
        self.domain_name = domain_name
        # This parameter is required.
        self.tool_description = tool_description
        self.tool_examples = tool_examples
        # This parameter is required.
        self.tool_id = tool_id
        # This parameter is required.
        self.tool_name = tool_name
        self.tool_params = tool_params
        self.workspace_id = workspace_id

    def validate(self):
        if self.tool_examples:
            for k in self.tool_examples:
                if k:
                    k.validate()
        if self.tool_params:
            for k in self.tool_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.tool_description is not None:
            result['ToolDescription'] = self.tool_description
        result['ToolExamples'] = []
        if self.tool_examples is not None:
            for k in self.tool_examples:
                result['ToolExamples'].append(k.to_map() if k else None)
        if self.tool_id is not None:
            result['ToolId'] = self.tool_id
        if self.tool_name is not None:
            result['ToolName'] = self.tool_name
        result['ToolParams'] = []
        if self.tool_params is not None:
            for k in self.tool_params:
                result['ToolParams'].append(k.to_map() if k else None)
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ToolDescription') is not None:
            self.tool_description = m.get('ToolDescription')
        self.tool_examples = []
        if m.get('ToolExamples') is not None:
            for k in m.get('ToolExamples'):
                temp_model = UpdateCommandRequestToolExamples()
                self.tool_examples.append(temp_model.from_map(k))
        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')
        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')
        self.tool_params = []
        if m.get('ToolParams') is not None:
            for k in m.get('ToolParams'):
                temp_model = UpdateCommandRequestToolParams()
                self.tool_params.append(temp_model.from_map(k))
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateCommandShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain_code: str = None,
        domain_name: str = None,
        tool_description: str = None,
        tool_examples_shrink: str = None,
        tool_id: str = None,
        tool_name: str = None,
        tool_params_shrink: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.domain_code = domain_code
        self.domain_name = domain_name
        # This parameter is required.
        self.tool_description = tool_description
        self.tool_examples_shrink = tool_examples_shrink
        # This parameter is required.
        self.tool_id = tool_id
        # This parameter is required.
        self.tool_name = tool_name
        self.tool_params_shrink = tool_params_shrink
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.tool_description is not None:
            result['ToolDescription'] = self.tool_description
        if self.tool_examples_shrink is not None:
            result['ToolExamples'] = self.tool_examples_shrink
        if self.tool_id is not None:
            result['ToolId'] = self.tool_id
        if self.tool_name is not None:
            result['ToolName'] = self.tool_name
        if self.tool_params_shrink is not None:
            result['ToolParams'] = self.tool_params_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ToolDescription') is not None:
            self.tool_description = m.get('ToolDescription')
        if m.get('ToolExamples') is not None:
            self.tool_examples_shrink = m.get('ToolExamples')
        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')
        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')
        if m.get('ToolParams') is not None:
            self.tool_params_shrink = m.get('ToolParams')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateCommandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCommandResponseBody = None,
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
            temp_model = UpdateCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMmAppRequestBindingConfigCommandsTools(TeaModel):
    def __init__(
        self,
        tool_id: str = None,
    ):
        # This parameter is required.
        self.tool_id = tool_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tool_id is not None:
            result['ToolId'] = self.tool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')
        return self


class UpdateMmAppRequestBindingConfigCommands(TeaModel):
    def __init__(
        self,
        domain_code: str = None,
        tools: List[UpdateMmAppRequestBindingConfigCommandsTools] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.domain_code = domain_code
        self.tools = tools
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.tools:
            for k in self.tools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        result['Tools'] = []
        if self.tools is not None:
            for k in self.tools:
                result['Tools'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        self.tools = []
        if m.get('Tools') is not None:
            for k in m.get('Tools'):
                temp_model = UpdateMmAppRequestBindingConfigCommandsTools()
                self.tools.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateMmAppRequestBindingConfig(TeaModel):
    def __init__(
        self,
        commands: List[UpdateMmAppRequestBindingConfigCommands] = None,
    ):
        self.commands = commands

    def validate(self):
        if self.commands:
            for k in self.commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Commands'] = []
        if self.commands is not None:
            for k in self.commands:
                result['Commands'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k in m.get('Commands'):
                temp_model = UpdateMmAppRequestBindingConfigCommands()
                self.commands.append(temp_model.from_map(k))
        return self


class UpdateMmAppRequestConversationConfig(TeaModel):
    def __init__(
        self,
        asr_model: str = None,
        open_asr: bool = None,
        open_tts: bool = None,
        tts_model: str = None,
    ):
        self.asr_model = asr_model
        self.open_asr = open_asr
        self.open_tts = open_tts
        self.tts_model = tts_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_model is not None:
            result['AsrModel'] = self.asr_model
        if self.open_asr is not None:
            result['OpenAsr'] = self.open_asr
        if self.open_tts is not None:
            result['OpenTts'] = self.open_tts
        if self.tts_model is not None:
            result['TtsModel'] = self.tts_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrModel') is not None:
            self.asr_model = m.get('AsrModel')
        if m.get('OpenAsr') is not None:
            self.open_asr = m.get('OpenAsr')
        if m.get('OpenTts') is not None:
            self.open_tts = m.get('OpenTts')
        if m.get('TtsModel') is not None:
            self.tts_model = m.get('TtsModel')
        return self


class UpdateMmAppRequestModelConfig(TeaModel):
    def __init__(
        self,
        history_limit: int = None,
        model_type: str = None,
        open_web_search: bool = None,
        text_modal: str = None,
    ):
        self.history_limit = history_limit
        self.model_type = model_type
        self.open_web_search = open_web_search
        self.text_modal = text_modal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_limit is not None:
            result['HistoryLimit'] = self.history_limit
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.open_web_search is not None:
            result['OpenWebSearch'] = self.open_web_search
        if self.text_modal is not None:
            result['TextModal'] = self.text_modal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoryLimit') is not None:
            self.history_limit = m.get('HistoryLimit')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('OpenWebSearch') is not None:
            self.open_web_search = m.get('OpenWebSearch')
        if m.get('TextModal') is not None:
            self.text_modal = m.get('TextModal')
        return self


class UpdateMmAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        binding_config: UpdateMmAppRequestBindingConfig = None,
        conversation_config: UpdateMmAppRequestConversationConfig = None,
        model_config: UpdateMmAppRequestModelConfig = None,
        prompt: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.app_name = app_name
        self.binding_config = binding_config
        self.conversation_config = conversation_config
        self.model_config = model_config
        self.prompt = prompt
        self.workspace_id = workspace_id

    def validate(self):
        if self.binding_config:
            self.binding_config.validate()
        if self.conversation_config:
            self.conversation_config.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.binding_config is not None:
            result['BindingConfig'] = self.binding_config.to_map()
        if self.conversation_config is not None:
            result['ConversationConfig'] = self.conversation_config.to_map()
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BindingConfig') is not None:
            temp_model = UpdateMmAppRequestBindingConfig()
            self.binding_config = temp_model.from_map(m['BindingConfig'])
        if m.get('ConversationConfig') is not None:
            temp_model = UpdateMmAppRequestConversationConfig()
            self.conversation_config = temp_model.from_map(m['ConversationConfig'])
        if m.get('ModelConfig') is not None:
            temp_model = UpdateMmAppRequestModelConfig()
            self.model_config = temp_model.from_map(m['ModelConfig'])
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateMmAppShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        binding_config_shrink: str = None,
        conversation_config_shrink: str = None,
        model_config_shrink: str = None,
        prompt: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.app_name = app_name
        self.binding_config_shrink = binding_config_shrink
        self.conversation_config_shrink = conversation_config_shrink
        self.model_config_shrink = model_config_shrink
        self.prompt = prompt
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.binding_config_shrink is not None:
            result['BindingConfig'] = self.binding_config_shrink
        if self.conversation_config_shrink is not None:
            result['ConversationConfig'] = self.conversation_config_shrink
        if self.model_config_shrink is not None:
            result['ModelConfig'] = self.model_config_shrink
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BindingConfig') is not None:
            self.binding_config_shrink = m.get('BindingConfig')
        if m.get('ConversationConfig') is not None:
            self.conversation_config_shrink = m.get('ConversationConfig')
        if m.get('ModelConfig') is not None:
            self.model_config_shrink = m.get('ModelConfig')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateMmAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMmAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMmAppResponseBody = None,
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
            temp_model = UpdateMmAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


