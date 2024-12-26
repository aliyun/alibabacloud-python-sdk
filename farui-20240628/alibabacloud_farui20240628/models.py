# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List


class CreateTextFileRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        create_time: str = None,
        text_file_name: str = None,
        text_file_url: str = None,
    ):
        self.client_token = client_token
        self.create_time = create_time
        self.text_file_name = text_file_name
        self.text_file_url = text_file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.text_file_name is not None:
            result['TextFileName'] = self.text_file_name
        if self.text_file_url is not None:
            result['TextFileUrl'] = self.text_file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TextFileName') is not None:
            self.text_file_name = m.get('TextFileName')
        if m.get('TextFileUrl') is not None:
            self.text_file_url = m.get('TextFileUrl')
        return self


class CreateTextFileAdvanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        create_time: str = None,
        text_file_name: str = None,
        text_file_url_object: BinaryIO = None,
    ):
        self.client_token = client_token
        self.create_time = create_time
        self.text_file_name = text_file_name
        self.text_file_url_object = text_file_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.text_file_name is not None:
            result['TextFileName'] = self.text_file_name
        if self.text_file_url_object is not None:
            result['TextFileUrl'] = self.text_file_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TextFileName') is not None:
            self.text_file_name = m.get('TextFileName')
        if m.get('TextFileUrl') is not None:
            self.text_file_url_object = m.get('TextFileUrl')
        return self


class CreateTextFileResponseBodyData(TeaModel):
    def __init__(
        self,
        text_file_id: str = None,
        text_file_name: str = None,
        text_file_url: str = None,
    ):
        self.text_file_id = text_file_id
        self.text_file_name = text_file_name
        self.text_file_url = text_file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text_file_id is not None:
            result['TextFileId'] = self.text_file_id
        if self.text_file_name is not None:
            result['TextFileName'] = self.text_file_name
        if self.text_file_url is not None:
            result['TextFileUrl'] = self.text_file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TextFileId') is not None:
            self.text_file_id = m.get('TextFileId')
        if m.get('TextFileName') is not None:
            self.text_file_name = m.get('TextFileName')
        if m.get('TextFileUrl') is not None:
            self.text_file_url = m.get('TextFileUrl')
        return self


class CreateTextFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateTextFileResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateTextFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTextFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTextFileResponseBody = None,
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
            temp_model = CreateTextFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfigCustomRules(TeaModel):
    def __init__(
        self,
        risk_level: str = None,
        rule_desc: str = None,
        rule_title: str = None,
    ):
        self.risk_level = risk_level
        self.rule_desc = rule_desc
        self.rule_title = rule_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        if self.rule_desc is not None:
            result['ruleDesc'] = self.rule_desc
        if self.rule_title is not None:
            result['ruleTitle'] = self.rule_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        if m.get('ruleDesc') is not None:
            self.rule_desc = m.get('ruleDesc')
        if m.get('ruleTitle') is not None:
            self.rule_title = m.get('ruleTitle')
        return self


class RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfig(TeaModel):
    def __init__(
        self,
        custom_rules: List[RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfigCustomRules] = None,
    ):
        self.custom_rules = custom_rules

    def validate(self):
        if self.custom_rules:
            for k in self.custom_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['customRules'] = []
        if self.custom_rules is not None:
            for k in self.custom_rules:
                result['customRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_rules = []
        if m.get('customRules') is not None:
            for k in m.get('customRules'):
                temp_model = RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfigCustomRules()
                self.custom_rules.append(temp_model.from_map(k))
        return self


class RunContractResultGenerationRequestAssistantMetaDataRules(TeaModel):
    def __init__(
        self,
        risk_level: str = None,
        rule_sequence: str = None,
        rule_tag: str = None,
        rule_title: str = None,
    ):
        self.risk_level = risk_level
        self.rule_sequence = rule_sequence
        self.rule_tag = rule_tag
        self.rule_title = rule_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        if self.rule_sequence is not None:
            result['ruleSequence'] = self.rule_sequence
        if self.rule_tag is not None:
            result['ruleTag'] = self.rule_tag
        if self.rule_title is not None:
            result['ruleTitle'] = self.rule_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        if m.get('ruleSequence') is not None:
            self.rule_sequence = m.get('ruleSequence')
        if m.get('ruleTag') is not None:
            self.rule_tag = m.get('ruleTag')
        if m.get('ruleTitle') is not None:
            self.rule_title = m.get('ruleTitle')
        return self


class RunContractResultGenerationRequestAssistantMetaData(TeaModel):
    def __init__(
        self,
        custom_rule_config: RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfig = None,
        file_id: str = None,
        position: str = None,
        rule_task_id: str = None,
        rules: List[RunContractResultGenerationRequestAssistantMetaDataRules] = None,
    ):
        self.custom_rule_config = custom_rule_config
        self.file_id = file_id
        self.position = position
        self.rule_task_id = rule_task_id
        self.rules = rules

    def validate(self):
        if self.custom_rule_config:
            self.custom_rule_config.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_rule_config is not None:
            result['customRuleConfig'] = self.custom_rule_config.to_map()
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.position is not None:
            result['position'] = self.position
        if self.rule_task_id is not None:
            result['ruleTaskId'] = self.rule_task_id
        result['rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customRuleConfig') is not None:
            temp_model = RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfig()
            self.custom_rule_config = temp_model.from_map(m['customRuleConfig'])
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('ruleTaskId') is not None:
            self.rule_task_id = m.get('ruleTaskId')
        self.rules = []
        if m.get('rules') is not None:
            for k in m.get('rules'):
                temp_model = RunContractResultGenerationRequestAssistantMetaDataRules()
                self.rules.append(temp_model.from_map(k))
        return self


class RunContractResultGenerationRequestAssistant(TeaModel):
    def __init__(
        self,
        meta_data: RunContractResultGenerationRequestAssistantMetaData = None,
        type: str = None,
        version: str = None,
    ):
        self.meta_data = meta_data
        self.type = type
        self.version = version

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = RunContractResultGenerationRequestAssistantMetaData()
            self.meta_data = temp_model.from_map(m['metaData'])
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class RunContractResultGenerationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        assistant: RunContractResultGenerationRequestAssistant = None,
        stream: bool = None,
    ):
        self.app_id = app_id
        self.assistant = assistant
        self.stream = stream

    def validate(self):
        if self.assistant:
            self.assistant.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.assistant is not None:
            result['assistant'] = self.assistant.to_map()
        if self.stream is not None:
            result['stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('assistant') is not None:
            temp_model = RunContractResultGenerationRequestAssistant()
            self.assistant = temp_model.from_map(m['assistant'])
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        return self


class RunContractResultGenerationShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        assistant_shrink: str = None,
        stream: bool = None,
    ):
        self.app_id = app_id
        self.assistant_shrink = assistant_shrink
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.assistant_shrink is not None:
            result['assistant'] = self.assistant_shrink
        if self.stream is not None:
            result['stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('assistant') is not None:
            self.assistant_shrink = m.get('assistant')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        return self


class RunContractResultGenerationResponseBodyOutputResultSubRisks(TeaModel):
    def __init__(
        self,
        original_content: str = None,
        result_content: str = None,
        result_type: str = None,
        risk_brief: str = None,
        risk_clause: str = None,
        risk_explain: str = None,
    ):
        self.original_content = original_content
        self.result_content = result_content
        self.result_type = result_type
        self.risk_brief = risk_brief
        self.risk_clause = risk_clause
        self.risk_explain = risk_explain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_content is not None:
            result['originalContent'] = self.original_content
        if self.result_content is not None:
            result['resultContent'] = self.result_content
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.risk_brief is not None:
            result['riskBrief'] = self.risk_brief
        if self.risk_clause is not None:
            result['riskClause'] = self.risk_clause
        if self.risk_explain is not None:
            result['riskExplain'] = self.risk_explain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalContent') is not None:
            self.original_content = m.get('originalContent')
        if m.get('resultContent') is not None:
            self.result_content = m.get('resultContent')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('riskBrief') is not None:
            self.risk_brief = m.get('riskBrief')
        if m.get('riskClause') is not None:
            self.risk_clause = m.get('riskClause')
        if m.get('riskExplain') is not None:
            self.risk_explain = m.get('riskExplain')
        return self


class RunContractResultGenerationResponseBodyOutputResult(TeaModel):
    def __init__(
        self,
        examine_brief: str = None,
        examine_result: str = None,
        risk_level: str = None,
        rule_sequence: str = None,
        rule_tag: str = None,
        rule_title: str = None,
        sub_risks: List[RunContractResultGenerationResponseBodyOutputResultSubRisks] = None,
    ):
        self.examine_brief = examine_brief
        self.examine_result = examine_result
        self.risk_level = risk_level
        self.rule_sequence = rule_sequence
        self.rule_tag = rule_tag
        self.rule_title = rule_title
        self.sub_risks = sub_risks

    def validate(self):
        if self.sub_risks:
            for k in self.sub_risks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.examine_brief is not None:
            result['examineBrief'] = self.examine_brief
        if self.examine_result is not None:
            result['examineResult'] = self.examine_result
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        if self.rule_sequence is not None:
            result['ruleSequence'] = self.rule_sequence
        if self.rule_tag is not None:
            result['ruleTag'] = self.rule_tag
        if self.rule_title is not None:
            result['ruleTitle'] = self.rule_title
        result['subRisks'] = []
        if self.sub_risks is not None:
            for k in self.sub_risks:
                result['subRisks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('examineBrief') is not None:
            self.examine_brief = m.get('examineBrief')
        if m.get('examineResult') is not None:
            self.examine_result = m.get('examineResult')
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        if m.get('ruleSequence') is not None:
            self.rule_sequence = m.get('ruleSequence')
        if m.get('ruleTag') is not None:
            self.rule_tag = m.get('ruleTag')
        if m.get('ruleTitle') is not None:
            self.rule_title = m.get('ruleTitle')
        self.sub_risks = []
        if m.get('subRisks') is not None:
            for k in m.get('subRisks'):
                temp_model = RunContractResultGenerationResponseBodyOutputResultSubRisks()
                self.sub_risks.append(temp_model.from_map(k))
        return self


class RunContractResultGenerationResponseBodyOutput(TeaModel):
    def __init__(
        self,
        result: RunContractResultGenerationResponseBodyOutputResult = None,
        result_task_id: str = None,
    ):
        self.result = result
        self.result_task_id = result_task_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.result_task_id is not None:
            result['resultTaskId'] = self.result_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = RunContractResultGenerationResponseBodyOutputResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('resultTaskId') is not None:
            self.result_task_id = m.get('resultTaskId')
        return self


class RunContractResultGenerationResponseBodyUsage(TeaModel):
    def __init__(
        self,
        input: int = None,
        unit: str = None,
    ):
        self.input = input
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['input'] = self.input
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class RunContractResultGenerationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        output: RunContractResultGenerationResponseBodyOutput = None,
        request_id: str = None,
        success: bool = None,
        usage: RunContractResultGenerationResponseBodyUsage = None,
        http_status_code: str = None,
    ):
        self.code = code
        self.message = message
        self.output = output
        self.request_id = request_id
        self.success = success
        self.usage = usage
        self.http_status_code = http_status_code

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Output') is not None:
            temp_model = RunContractResultGenerationResponseBodyOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Usage') is not None:
            temp_model = RunContractResultGenerationResponseBodyUsage()
            self.usage = temp_model.from_map(m['Usage'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        return self


class RunContractResultGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunContractResultGenerationResponseBody = None,
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
            temp_model = RunContractResultGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunContractRuleGenerationRequestAssistantMetaData(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        position: str = None,
    ):
        self.file_id = file_id
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.position is not None:
            result['position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('position') is not None:
            self.position = m.get('position')
        return self


class RunContractRuleGenerationRequestAssistant(TeaModel):
    def __init__(
        self,
        meta_data: RunContractRuleGenerationRequestAssistantMetaData = None,
        type: str = None,
        version: str = None,
    ):
        self.meta_data = meta_data
        self.type = type
        self.version = version

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = RunContractRuleGenerationRequestAssistantMetaData()
            self.meta_data = temp_model.from_map(m['metaData'])
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class RunContractRuleGenerationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        assistant: RunContractRuleGenerationRequestAssistant = None,
        stream: bool = None,
    ):
        self.app_id = app_id
        self.assistant = assistant
        self.stream = stream

    def validate(self):
        if self.assistant:
            self.assistant.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.assistant is not None:
            result['assistant'] = self.assistant.to_map()
        if self.stream is not None:
            result['stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('assistant') is not None:
            temp_model = RunContractRuleGenerationRequestAssistant()
            self.assistant = temp_model.from_map(m['assistant'])
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        return self


class RunContractRuleGenerationShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        assistant_shrink: str = None,
        stream: bool = None,
    ):
        self.app_id = app_id
        self.assistant_shrink = assistant_shrink
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.assistant_shrink is not None:
            result['assistant'] = self.assistant_shrink
        if self.stream is not None:
            result['stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('assistant') is not None:
            self.assistant_shrink = m.get('assistant')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        return self


class RunContractRuleGenerationResponseBodyOutputRules(TeaModel):
    def __init__(
        self,
        risk_level: str = None,
        rule_sequence: str = None,
        rule_tag: str = None,
        rule_title: str = None,
    ):
        self.risk_level = risk_level
        self.rule_sequence = rule_sequence
        self.rule_tag = rule_tag
        self.rule_title = rule_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        if self.rule_sequence is not None:
            result['ruleSequence'] = self.rule_sequence
        if self.rule_tag is not None:
            result['ruleTag'] = self.rule_tag
        if self.rule_title is not None:
            result['ruleTitle'] = self.rule_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        if m.get('ruleSequence') is not None:
            self.rule_sequence = m.get('ruleSequence')
        if m.get('ruleTag') is not None:
            self.rule_tag = m.get('ruleTag')
        if m.get('ruleTitle') is not None:
            self.rule_title = m.get('ruleTitle')
        return self


class RunContractRuleGenerationResponseBodyOutput(TeaModel):
    def __init__(
        self,
        rule_task_id: str = None,
        rules: List[RunContractRuleGenerationResponseBodyOutputRules] = None,
    ):
        self.rule_task_id = rule_task_id
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_task_id is not None:
            result['ruleTaskId'] = self.rule_task_id
        result['rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleTaskId') is not None:
            self.rule_task_id = m.get('ruleTaskId')
        self.rules = []
        if m.get('rules') is not None:
            for k in m.get('rules'):
                temp_model = RunContractRuleGenerationResponseBodyOutputRules()
                self.rules.append(temp_model.from_map(k))
        return self


class RunContractRuleGenerationResponseBodyUsage(TeaModel):
    def __init__(
        self,
        input: int = None,
        unit: str = None,
    ):
        self.input = input
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['input'] = self.input
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class RunContractRuleGenerationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        output: RunContractRuleGenerationResponseBodyOutput = None,
        request_id: str = None,
        success: bool = None,
        usage: RunContractRuleGenerationResponseBodyUsage = None,
        http_status_code: int = None,
    ):
        self.code = code
        self.message = message
        self.output = output
        self.request_id = request_id
        self.success = success
        self.usage = usage
        self.http_status_code = http_status_code

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Output') is not None:
            temp_model = RunContractRuleGenerationResponseBodyOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Usage') is not None:
            temp_model = RunContractRuleGenerationResponseBodyUsage()
            self.usage = temp_model.from_map(m['Usage'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        return self


class RunContractRuleGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunContractRuleGenerationResponseBody = None,
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
            temp_model = RunContractRuleGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunLegalAdviceConsultationRequestAssistant(TeaModel):
    def __init__(
        self,
        id: str = None,
        meta_data: Dict[str, str] = None,
        type: str = None,
        version: str = None,
    ):
        self.id = id
        self.meta_data = meta_data
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.meta_data is not None:
            result['metaData'] = self.meta_data
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class RunLegalAdviceConsultationRequestThreadMessages(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class RunLegalAdviceConsultationRequestThread(TeaModel):
    def __init__(
        self,
        messages: List[RunLegalAdviceConsultationRequestThreadMessages] = None,
    ):
        self.messages = messages

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['messages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k in m.get('messages'):
                temp_model = RunLegalAdviceConsultationRequestThreadMessages()
                self.messages.append(temp_model.from_map(k))
        return self


class RunLegalAdviceConsultationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        assistant: RunLegalAdviceConsultationRequestAssistant = None,
        stream: bool = None,
        thread: RunLegalAdviceConsultationRequestThread = None,
    ):
        self.app_id = app_id
        self.assistant = assistant
        self.stream = stream
        self.thread = thread

    def validate(self):
        if self.assistant:
            self.assistant.validate()
        if self.thread:
            self.thread.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.assistant is not None:
            result['assistant'] = self.assistant.to_map()
        if self.stream is not None:
            result['stream'] = self.stream
        if self.thread is not None:
            result['thread'] = self.thread.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('assistant') is not None:
            temp_model = RunLegalAdviceConsultationRequestAssistant()
            self.assistant = temp_model.from_map(m['assistant'])
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('thread') is not None:
            temp_model = RunLegalAdviceConsultationRequestThread()
            self.thread = temp_model.from_map(m['thread'])
        return self


class RunLegalAdviceConsultationShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        assistant_shrink: str = None,
        stream: bool = None,
        thread_shrink: str = None,
    ):
        self.app_id = app_id
        self.assistant_shrink = assistant_shrink
        self.stream = stream
        self.thread_shrink = thread_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.assistant_shrink is not None:
            result['assistant'] = self.assistant_shrink
        if self.stream is not None:
            result['stream'] = self.stream
        if self.thread_shrink is not None:
            result['thread'] = self.thread_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('assistant') is not None:
            self.assistant_shrink = m.get('assistant')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('thread') is not None:
            self.thread_shrink = m.get('thread')
        return self


class RunLegalAdviceConsultationResponseBodyUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunLegalAdviceConsultationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response_markdown: str = None,
        round: int = None,
        status: str = None,
        success: bool = None,
        usage: RunLegalAdviceConsultationResponseBodyUsage = None,
        http_status_code: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.response_markdown = response_markdown
        self.round = round
        self.status = status
        self.success = success
        self.usage = usage
        self.http_status_code = http_status_code

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_markdown is not None:
            result['ResponseMarkdown'] = self.response_markdown
        if self.round is not None:
            result['Round'] = self.round
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseMarkdown') is not None:
            self.response_markdown = m.get('ResponseMarkdown')
        if m.get('Round') is not None:
            self.round = m.get('Round')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Usage') is not None:
            temp_model = RunLegalAdviceConsultationResponseBodyUsage()
            self.usage = temp_model.from_map(m['Usage'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        return self


class RunLegalAdviceConsultationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunLegalAdviceConsultationResponseBody = None,
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
            temp_model = RunLegalAdviceConsultationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunSearchCaseFullTextRequestFilterCondition(TeaModel):
    def __init__(
        self,
        case_no: str = None,
        case_title: str = None,
    ):
        self.case_no = case_no
        self.case_title = case_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_no is not None:
            result['caseNo'] = self.case_no
        if self.case_title is not None:
            result['caseTitle'] = self.case_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseNo') is not None:
            self.case_no = m.get('caseNo')
        if m.get('caseTitle') is not None:
            self.case_title = m.get('caseTitle')
        return self


class RunSearchCaseFullTextRequestPageParam(TeaModel):
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
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class RunSearchCaseFullTextRequestThreadMessages(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class RunSearchCaseFullTextRequestThread(TeaModel):
    def __init__(
        self,
        messages: List[RunSearchCaseFullTextRequestThreadMessages] = None,
    ):
        self.messages = messages

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['messages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k in m.get('messages'):
                temp_model = RunSearchCaseFullTextRequestThreadMessages()
                self.messages.append(temp_model.from_map(k))
        return self


class RunSearchCaseFullTextRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        filter_condition: RunSearchCaseFullTextRequestFilterCondition = None,
        page_param: RunSearchCaseFullTextRequestPageParam = None,
        query: str = None,
        query_keywords: List[str] = None,
        sort_key_and_direction: Dict[str, str] = None,
        thread: RunSearchCaseFullTextRequestThread = None,
    ):
        self.app_id = app_id
        self.filter_condition = filter_condition
        # This parameter is required.
        self.page_param = page_param
        # This parameter is required.
        self.query = query
        self.query_keywords = query_keywords
        self.sort_key_and_direction = sort_key_and_direction
        self.thread = thread

    def validate(self):
        if self.filter_condition:
            self.filter_condition.validate()
        if self.page_param:
            self.page_param.validate()
        if self.thread:
            self.thread.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.filter_condition is not None:
            result['filterCondition'] = self.filter_condition.to_map()
        if self.page_param is not None:
            result['pageParam'] = self.page_param.to_map()
        if self.query is not None:
            result['query'] = self.query
        if self.query_keywords is not None:
            result['queryKeywords'] = self.query_keywords
        if self.sort_key_and_direction is not None:
            result['sortKeyAndDirection'] = self.sort_key_and_direction
        if self.thread is not None:
            result['thread'] = self.thread.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('filterCondition') is not None:
            temp_model = RunSearchCaseFullTextRequestFilterCondition()
            self.filter_condition = temp_model.from_map(m['filterCondition'])
        if m.get('pageParam') is not None:
            temp_model = RunSearchCaseFullTextRequestPageParam()
            self.page_param = temp_model.from_map(m['pageParam'])
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('queryKeywords') is not None:
            self.query_keywords = m.get('queryKeywords')
        if m.get('sortKeyAndDirection') is not None:
            self.sort_key_and_direction = m.get('sortKeyAndDirection')
        if m.get('thread') is not None:
            temp_model = RunSearchCaseFullTextRequestThread()
            self.thread = temp_model.from_map(m['thread'])
        return self


class RunSearchCaseFullTextShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        filter_condition_shrink: str = None,
        page_param_shrink: str = None,
        query: str = None,
        query_keywords_shrink: str = None,
        sort_key_and_direction_shrink: str = None,
        thread_shrink: str = None,
    ):
        self.app_id = app_id
        self.filter_condition_shrink = filter_condition_shrink
        # This parameter is required.
        self.page_param_shrink = page_param_shrink
        # This parameter is required.
        self.query = query
        self.query_keywords_shrink = query_keywords_shrink
        self.sort_key_and_direction_shrink = sort_key_and_direction_shrink
        self.thread_shrink = thread_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.filter_condition_shrink is not None:
            result['filterCondition'] = self.filter_condition_shrink
        if self.page_param_shrink is not None:
            result['pageParam'] = self.page_param_shrink
        if self.query is not None:
            result['query'] = self.query
        if self.query_keywords_shrink is not None:
            result['queryKeywords'] = self.query_keywords_shrink
        if self.sort_key_and_direction_shrink is not None:
            result['sortKeyAndDirection'] = self.sort_key_and_direction_shrink
        if self.thread_shrink is not None:
            result['thread'] = self.thread_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('filterCondition') is not None:
            self.filter_condition_shrink = m.get('filterCondition')
        if m.get('pageParam') is not None:
            self.page_param_shrink = m.get('pageParam')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('queryKeywords') is not None:
            self.query_keywords_shrink = m.get('queryKeywords')
        if m.get('sortKeyAndDirection') is not None:
            self.sort_key_and_direction_shrink = m.get('sortKeyAndDirection')
        if m.get('thread') is not None:
            self.thread_shrink = m.get('thread')
        return self


class RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomainTrialCourt(TeaModel):
    def __init__(
        self,
        city: str = None,
        common_level: str = None,
        country: str = None,
        county: str = None,
        district: str = None,
        name: str = None,
        province: str = None,
        special_level: str = None,
    ):
        self.city = city
        self.common_level = common_level
        self.country = country
        self.county = county
        self.district = district
        self.name = name
        self.province = province
        self.special_level = special_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['city'] = self.city
        if self.common_level is not None:
            result['commonLevel'] = self.common_level
        if self.country is not None:
            result['country'] = self.country
        if self.county is not None:
            result['county'] = self.county
        if self.district is not None:
            result['district'] = self.district
        if self.name is not None:
            result['name'] = self.name
        if self.province is not None:
            result['province'] = self.province
        if self.special_level is not None:
            result['specialLevel'] = self.special_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('commonLevel') is not None:
            self.common_level = m.get('commonLevel')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('county') is not None:
            self.county = m.get('county')
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('specialLevel') is not None:
            self.special_level = m.get('specialLevel')
        return self


class RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomain(TeaModel):
    def __init__(
        self,
        abstract_obj: str = None,
        applied_laws: str = None,
        case_basic: str = None,
        case_feature: str = None,
        case_id: str = None,
        case_no: str = None,
        case_summary: str = None,
        case_title: str = None,
        case_type: str = None,
        close_case_cause: str = None,
        court_find_out: str = None,
        court_think: str = None,
        data_from: str = None,
        dispute_focus: str = None,
        dispute_focus_tag: List[str] = None,
        disputedpoints: str = None,
        document_type: str = None,
        keyfacts: str = None,
        legal_basis: str = None,
        litigants: str = None,
        litigation_participant: str = None,
        open_case_cause: str = None,
        pre_trial_process: str = None,
        refer_level: str = None,
        source_content: str = None,
        trial_court: RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomainTrialCourt = None,
        trial_date: str = None,
        trial_level: str = None,
        trial_process: str = None,
        trial_program: str = None,
        verdict: str = None,
    ):
        self.abstract_obj = abstract_obj
        self.applied_laws = applied_laws
        self.case_basic = case_basic
        self.case_feature = case_feature
        self.case_id = case_id
        self.case_no = case_no
        self.case_summary = case_summary
        self.case_title = case_title
        self.case_type = case_type
        self.close_case_cause = close_case_cause
        self.court_find_out = court_find_out
        self.court_think = court_think
        self.data_from = data_from
        self.dispute_focus = dispute_focus
        self.dispute_focus_tag = dispute_focus_tag
        self.disputedpoints = disputedpoints
        self.document_type = document_type
        self.keyfacts = keyfacts
        self.legal_basis = legal_basis
        self.litigants = litigants
        self.litigation_participant = litigation_participant
        self.open_case_cause = open_case_cause
        self.pre_trial_process = pre_trial_process
        self.refer_level = refer_level
        self.source_content = source_content
        self.trial_court = trial_court
        self.trial_date = trial_date
        self.trial_level = trial_level
        self.trial_process = trial_process
        self.trial_program = trial_program
        self.verdict = verdict

    def validate(self):
        if self.trial_court:
            self.trial_court.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abstract_obj is not None:
            result['abstractObj'] = self.abstract_obj
        if self.applied_laws is not None:
            result['appliedLaws'] = self.applied_laws
        if self.case_basic is not None:
            result['caseBasic'] = self.case_basic
        if self.case_feature is not None:
            result['caseFeature'] = self.case_feature
        if self.case_id is not None:
            result['caseId'] = self.case_id
        if self.case_no is not None:
            result['caseNo'] = self.case_no
        if self.case_summary is not None:
            result['caseSummary'] = self.case_summary
        if self.case_title is not None:
            result['caseTitle'] = self.case_title
        if self.case_type is not None:
            result['caseType'] = self.case_type
        if self.close_case_cause is not None:
            result['closeCaseCause'] = self.close_case_cause
        if self.court_find_out is not None:
            result['courtFindOut'] = self.court_find_out
        if self.court_think is not None:
            result['courtThink'] = self.court_think
        if self.data_from is not None:
            result['dataFrom'] = self.data_from
        if self.dispute_focus is not None:
            result['disputeFocus'] = self.dispute_focus
        if self.dispute_focus_tag is not None:
            result['disputeFocusTag'] = self.dispute_focus_tag
        if self.disputedpoints is not None:
            result['disputedpoints'] = self.disputedpoints
        if self.document_type is not None:
            result['documentType'] = self.document_type
        if self.keyfacts is not None:
            result['keyfacts'] = self.keyfacts
        if self.legal_basis is not None:
            result['legalBasis'] = self.legal_basis
        if self.litigants is not None:
            result['litigants'] = self.litigants
        if self.litigation_participant is not None:
            result['litigationParticipant'] = self.litigation_participant
        if self.open_case_cause is not None:
            result['openCaseCause'] = self.open_case_cause
        if self.pre_trial_process is not None:
            result['preTrialProcess'] = self.pre_trial_process
        if self.refer_level is not None:
            result['referLevel'] = self.refer_level
        if self.source_content is not None:
            result['sourceContent'] = self.source_content
        if self.trial_court is not None:
            result['trialCourt'] = self.trial_court.to_map()
        if self.trial_date is not None:
            result['trialDate'] = self.trial_date
        if self.trial_level is not None:
            result['trialLevel'] = self.trial_level
        if self.trial_process is not None:
            result['trialProcess'] = self.trial_process
        if self.trial_program is not None:
            result['trialProgram'] = self.trial_program
        if self.verdict is not None:
            result['verdict'] = self.verdict
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('abstractObj') is not None:
            self.abstract_obj = m.get('abstractObj')
        if m.get('appliedLaws') is not None:
            self.applied_laws = m.get('appliedLaws')
        if m.get('caseBasic') is not None:
            self.case_basic = m.get('caseBasic')
        if m.get('caseFeature') is not None:
            self.case_feature = m.get('caseFeature')
        if m.get('caseId') is not None:
            self.case_id = m.get('caseId')
        if m.get('caseNo') is not None:
            self.case_no = m.get('caseNo')
        if m.get('caseSummary') is not None:
            self.case_summary = m.get('caseSummary')
        if m.get('caseTitle') is not None:
            self.case_title = m.get('caseTitle')
        if m.get('caseType') is not None:
            self.case_type = m.get('caseType')
        if m.get('closeCaseCause') is not None:
            self.close_case_cause = m.get('closeCaseCause')
        if m.get('courtFindOut') is not None:
            self.court_find_out = m.get('courtFindOut')
        if m.get('courtThink') is not None:
            self.court_think = m.get('courtThink')
        if m.get('dataFrom') is not None:
            self.data_from = m.get('dataFrom')
        if m.get('disputeFocus') is not None:
            self.dispute_focus = m.get('disputeFocus')
        if m.get('disputeFocusTag') is not None:
            self.dispute_focus_tag = m.get('disputeFocusTag')
        if m.get('disputedpoints') is not None:
            self.disputedpoints = m.get('disputedpoints')
        if m.get('documentType') is not None:
            self.document_type = m.get('documentType')
        if m.get('keyfacts') is not None:
            self.keyfacts = m.get('keyfacts')
        if m.get('legalBasis') is not None:
            self.legal_basis = m.get('legalBasis')
        if m.get('litigants') is not None:
            self.litigants = m.get('litigants')
        if m.get('litigationParticipant') is not None:
            self.litigation_participant = m.get('litigationParticipant')
        if m.get('openCaseCause') is not None:
            self.open_case_cause = m.get('openCaseCause')
        if m.get('preTrialProcess') is not None:
            self.pre_trial_process = m.get('preTrialProcess')
        if m.get('referLevel') is not None:
            self.refer_level = m.get('referLevel')
        if m.get('sourceContent') is not None:
            self.source_content = m.get('sourceContent')
        if m.get('trialCourt') is not None:
            temp_model = RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomainTrialCourt()
            self.trial_court = temp_model.from_map(m['trialCourt'])
        if m.get('trialDate') is not None:
            self.trial_date = m.get('trialDate')
        if m.get('trialLevel') is not None:
            self.trial_level = m.get('trialLevel')
        if m.get('trialProcess') is not None:
            self.trial_process = m.get('trialProcess')
        if m.get('trialProgram') is not None:
            self.trial_program = m.get('trialProgram')
        if m.get('verdict') is not None:
            self.verdict = m.get('verdict')
        return self


class RunSearchCaseFullTextResponseBodyDataCaseResult(TeaModel):
    def __init__(
        self,
        case_domain: RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomain = None,
        similarity: str = None,
    ):
        self.case_domain = case_domain
        self.similarity = similarity

    def validate(self):
        if self.case_domain:
            self.case_domain.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_domain is not None:
            result['caseDomain'] = self.case_domain.to_map()
        if self.similarity is not None:
            result['similarity'] = self.similarity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseDomain') is not None:
            temp_model = RunSearchCaseFullTextResponseBodyDataCaseResultCaseDomain()
            self.case_domain = temp_model.from_map(m['caseDomain'])
        if m.get('similarity') is not None:
            self.similarity = m.get('similarity')
        return self


class RunSearchCaseFullTextResponseBodyData(TeaModel):
    def __init__(
        self,
        case_result: List[RunSearchCaseFullTextResponseBodyDataCaseResult] = None,
        current_page: int = None,
        page_size: int = None,
        query: str = None,
        query_keywords: List[str] = None,
        total_count: int = None,
    ):
        self.case_result = case_result
        self.current_page = current_page
        self.page_size = page_size
        self.query = query
        self.query_keywords = query_keywords
        self.total_count = total_count

    def validate(self):
        if self.case_result:
            for k in self.case_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['caseResult'] = []
        if self.case_result is not None:
            for k in self.case_result:
                result['caseResult'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query is not None:
            result['query'] = self.query
        if self.query_keywords is not None:
            result['queryKeywords'] = self.query_keywords
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.case_result = []
        if m.get('caseResult') is not None:
            for k in m.get('caseResult'):
                temp_model = RunSearchCaseFullTextResponseBodyDataCaseResult()
                self.case_result.append(temp_model.from_map(k))
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('queryKeywords') is not None:
            self.query_keywords = m.get('queryKeywords')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class RunSearchCaseFullTextResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RunSearchCaseFullTextResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            temp_model = RunSearchCaseFullTextResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RunSearchCaseFullTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunSearchCaseFullTextResponseBody = None,
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
            temp_model = RunSearchCaseFullTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunSearchLawQueryRequestFilterCondition(TeaModel):
    def __init__(
        self,
        law_name: str = None,
    ):
        self.law_name = law_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.law_name is not None:
            result['lawName'] = self.law_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lawName') is not None:
            self.law_name = m.get('lawName')
        return self


class RunSearchLawQueryRequestPageParam(TeaModel):
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
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class RunSearchLawQueryRequestThreadMessages(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class RunSearchLawQueryRequestThread(TeaModel):
    def __init__(
        self,
        messages: List[RunSearchLawQueryRequestThreadMessages] = None,
    ):
        self.messages = messages

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['messages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k in m.get('messages'):
                temp_model = RunSearchLawQueryRequestThreadMessages()
                self.messages.append(temp_model.from_map(k))
        return self


class RunSearchLawQueryRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        filter_condition: RunSearchLawQueryRequestFilterCondition = None,
        page_param: RunSearchLawQueryRequestPageParam = None,
        query: str = None,
        query_keywords: List[str] = None,
        thread: RunSearchLawQueryRequestThread = None,
    ):
        self.app_id = app_id
        self.filter_condition = filter_condition
        self.page_param = page_param
        # This parameter is required.
        self.query = query
        self.query_keywords = query_keywords
        self.thread = thread

    def validate(self):
        if self.filter_condition:
            self.filter_condition.validate()
        if self.page_param:
            self.page_param.validate()
        if self.thread:
            self.thread.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.filter_condition is not None:
            result['filterCondition'] = self.filter_condition.to_map()
        if self.page_param is not None:
            result['pageParam'] = self.page_param.to_map()
        if self.query is not None:
            result['query'] = self.query
        if self.query_keywords is not None:
            result['queryKeywords'] = self.query_keywords
        if self.thread is not None:
            result['thread'] = self.thread.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('filterCondition') is not None:
            temp_model = RunSearchLawQueryRequestFilterCondition()
            self.filter_condition = temp_model.from_map(m['filterCondition'])
        if m.get('pageParam') is not None:
            temp_model = RunSearchLawQueryRequestPageParam()
            self.page_param = temp_model.from_map(m['pageParam'])
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('queryKeywords') is not None:
            self.query_keywords = m.get('queryKeywords')
        if m.get('thread') is not None:
            temp_model = RunSearchLawQueryRequestThread()
            self.thread = temp_model.from_map(m['thread'])
        return self


class RunSearchLawQueryShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        filter_condition_shrink: str = None,
        page_param_shrink: str = None,
        query: str = None,
        query_keywords_shrink: str = None,
        thread_shrink: str = None,
    ):
        self.app_id = app_id
        self.filter_condition_shrink = filter_condition_shrink
        self.page_param_shrink = page_param_shrink
        # This parameter is required.
        self.query = query
        self.query_keywords_shrink = query_keywords_shrink
        self.thread_shrink = thread_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.filter_condition_shrink is not None:
            result['filterCondition'] = self.filter_condition_shrink
        if self.page_param_shrink is not None:
            result['pageParam'] = self.page_param_shrink
        if self.query is not None:
            result['query'] = self.query
        if self.query_keywords_shrink is not None:
            result['queryKeywords'] = self.query_keywords_shrink
        if self.thread_shrink is not None:
            result['thread'] = self.thread_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('filterCondition') is not None:
            self.filter_condition_shrink = m.get('filterCondition')
        if m.get('pageParam') is not None:
            self.page_param_shrink = m.get('pageParam')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('queryKeywords') is not None:
            self.query_keywords_shrink = m.get('queryKeywords')
        if m.get('thread') is not None:
            self.thread_shrink = m.get('thread')
        return self


class RunSearchLawQueryResponseBodyDataLawResultLawDomain(TeaModel):
    def __init__(
        self,
        abolition_basis: str = None,
        implement_year_month_date: str = None,
        invalid_basis: str = None,
        issuing_no: str = None,
        issuing_organ: str = None,
        law_id: str = None,
        law_item_id: str = None,
        law_name: str = None,
        law_order: str = None,
        law_source_content: str = None,
        law_title: str = None,
        modify_basis: str = None,
        potency_level: str = None,
        release_year_month_date: str = None,
        thematic_classify: str = None,
        timeliness: str = None,
    ):
        self.abolition_basis = abolition_basis
        self.implement_year_month_date = implement_year_month_date
        self.invalid_basis = invalid_basis
        self.issuing_no = issuing_no
        self.issuing_organ = issuing_organ
        self.law_id = law_id
        self.law_item_id = law_item_id
        self.law_name = law_name
        self.law_order = law_order
        self.law_source_content = law_source_content
        self.law_title = law_title
        self.modify_basis = modify_basis
        self.potency_level = potency_level
        self.release_year_month_date = release_year_month_date
        self.thematic_classify = thematic_classify
        self.timeliness = timeliness

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abolition_basis is not None:
            result['abolitionBasis'] = self.abolition_basis
        if self.implement_year_month_date is not None:
            result['implementYearMonthDate'] = self.implement_year_month_date
        if self.invalid_basis is not None:
            result['invalidBasis'] = self.invalid_basis
        if self.issuing_no is not None:
            result['issuingNo'] = self.issuing_no
        if self.issuing_organ is not None:
            result['issuingOrgan'] = self.issuing_organ
        if self.law_id is not None:
            result['lawId'] = self.law_id
        if self.law_item_id is not None:
            result['lawItemId'] = self.law_item_id
        if self.law_name is not None:
            result['lawName'] = self.law_name
        if self.law_order is not None:
            result['lawOrder'] = self.law_order
        if self.law_source_content is not None:
            result['lawSourceContent'] = self.law_source_content
        if self.law_title is not None:
            result['lawTitle'] = self.law_title
        if self.modify_basis is not None:
            result['modifyBasis'] = self.modify_basis
        if self.potency_level is not None:
            result['potencyLevel'] = self.potency_level
        if self.release_year_month_date is not None:
            result['releaseYearMonthDate'] = self.release_year_month_date
        if self.thematic_classify is not None:
            result['thematicClassify'] = self.thematic_classify
        if self.timeliness is not None:
            result['timeliness'] = self.timeliness
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('abolitionBasis') is not None:
            self.abolition_basis = m.get('abolitionBasis')
        if m.get('implementYearMonthDate') is not None:
            self.implement_year_month_date = m.get('implementYearMonthDate')
        if m.get('invalidBasis') is not None:
            self.invalid_basis = m.get('invalidBasis')
        if m.get('issuingNo') is not None:
            self.issuing_no = m.get('issuingNo')
        if m.get('issuingOrgan') is not None:
            self.issuing_organ = m.get('issuingOrgan')
        if m.get('lawId') is not None:
            self.law_id = m.get('lawId')
        if m.get('lawItemId') is not None:
            self.law_item_id = m.get('lawItemId')
        if m.get('lawName') is not None:
            self.law_name = m.get('lawName')
        if m.get('lawOrder') is not None:
            self.law_order = m.get('lawOrder')
        if m.get('lawSourceContent') is not None:
            self.law_source_content = m.get('lawSourceContent')
        if m.get('lawTitle') is not None:
            self.law_title = m.get('lawTitle')
        if m.get('modifyBasis') is not None:
            self.modify_basis = m.get('modifyBasis')
        if m.get('potencyLevel') is not None:
            self.potency_level = m.get('potencyLevel')
        if m.get('releaseYearMonthDate') is not None:
            self.release_year_month_date = m.get('releaseYearMonthDate')
        if m.get('thematicClassify') is not None:
            self.thematic_classify = m.get('thematicClassify')
        if m.get('timeliness') is not None:
            self.timeliness = m.get('timeliness')
        return self


class RunSearchLawQueryResponseBodyDataLawResult(TeaModel):
    def __init__(
        self,
        law_domain: RunSearchLawQueryResponseBodyDataLawResultLawDomain = None,
        similarity: str = None,
    ):
        self.law_domain = law_domain
        self.similarity = similarity

    def validate(self):
        if self.law_domain:
            self.law_domain.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.law_domain is not None:
            result['lawDomain'] = self.law_domain.to_map()
        if self.similarity is not None:
            result['similarity'] = self.similarity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lawDomain') is not None:
            temp_model = RunSearchLawQueryResponseBodyDataLawResultLawDomain()
            self.law_domain = temp_model.from_map(m['lawDomain'])
        if m.get('similarity') is not None:
            self.similarity = m.get('similarity')
        return self


class RunSearchLawQueryResponseBodyDataSortKeyAndDirection(TeaModel):
    def __init__(
        self,
        release_year_month_date: str = None,
        similarity: str = None,
    ):
        self.release_year_month_date = release_year_month_date
        self.similarity = similarity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.release_year_month_date is not None:
            result['releaseYearMonthDate'] = self.release_year_month_date
        if self.similarity is not None:
            result['similarity'] = self.similarity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('releaseYearMonthDate') is not None:
            self.release_year_month_date = m.get('releaseYearMonthDate')
        if m.get('similarity') is not None:
            self.similarity = m.get('similarity')
        return self


class RunSearchLawQueryResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        law_result: List[RunSearchLawQueryResponseBodyDataLawResult] = None,
        page_size: int = None,
        query: str = None,
        query_keywords: List[str] = None,
        sort_key_and_direction: RunSearchLawQueryResponseBodyDataSortKeyAndDirection = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.law_result = law_result
        self.page_size = page_size
        self.query = query
        self.query_keywords = query_keywords
        self.sort_key_and_direction = sort_key_and_direction
        self.total_count = total_count

    def validate(self):
        if self.law_result:
            for k in self.law_result:
                if k:
                    k.validate()
        if self.sort_key_and_direction:
            self.sort_key_and_direction.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        result['lawResult'] = []
        if self.law_result is not None:
            for k in self.law_result:
                result['lawResult'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query is not None:
            result['query'] = self.query
        if self.query_keywords is not None:
            result['queryKeywords'] = self.query_keywords
        if self.sort_key_and_direction is not None:
            result['sortKeyAndDirection'] = self.sort_key_and_direction.to_map()
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        self.law_result = []
        if m.get('lawResult') is not None:
            for k in m.get('lawResult'):
                temp_model = RunSearchLawQueryResponseBodyDataLawResult()
                self.law_result.append(temp_model.from_map(k))
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('queryKeywords') is not None:
            self.query_keywords = m.get('queryKeywords')
        if m.get('sortKeyAndDirection') is not None:
            temp_model = RunSearchLawQueryResponseBodyDataSortKeyAndDirection()
            self.sort_key_and_direction = temp_model.from_map(m['sortKeyAndDirection'])
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class RunSearchLawQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RunSearchLawQueryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            temp_model = RunSearchLawQueryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RunSearchLawQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunSearchLawQueryResponseBody = None,
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
            temp_model = RunSearchLawQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


