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


