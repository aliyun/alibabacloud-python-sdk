# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aisc20260101 import models as main_models
from darabonba.model import DaraModel

class ListSubTasksResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListSubTasksResponseBodyData] = None,
        page_info: main_models.ListSubTasksResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data = data
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSubTasksResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListSubTasksResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSubTasksResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: str = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.count = count
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSubTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        file_hash: str = None,
        id: int = None,
        target: str = None,
        task_result_message: main_models.ListSubTasksResponseBodyDataTaskResultMessage = None,
        task_status: str = None,
    ):
        self.file_hash = file_hash
        self.id = id
        self.target = target
        self.task_result_message = task_result_message
        self.task_status = task_status

    def validate(self):
        if self.task_result_message:
            self.task_result_message.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash

        if self.id is not None:
            result['Id'] = self.id

        if self.target is not None:
            result['Target'] = self.target

        if self.task_result_message is not None:
            result['TaskResultMessage'] = self.task_result_message.to_map()

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TaskResultMessage') is not None:
            temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessage()
            self.task_result_message = temp_model.from_map(m.get('TaskResultMessage'))

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class ListSubTasksResponseBodyDataTaskResultMessage(DaraModel):
    def __init__(
        self,
        skill_check_result: main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResult = None,
    ):
        self.skill_check_result = skill_check_result

    def validate(self):
        if self.skill_check_result:
            self.skill_check_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skill_check_result is not None:
            result['SkillCheckResult'] = self.skill_check_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkillCheckResult') is not None:
            temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResult()
            self.skill_check_result = temp_model.from_map(m.get('SkillCheckResult'))

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResult(DaraModel):
    def __init__(
        self,
        risk_info: List[main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfo] = None,
    ):
        self.risk_info = risk_info

    def validate(self):
        if self.risk_info:
            for v1 in self.risk_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RiskInfo'] = []
        if self.risk_info is not None:
            for k1 in self.risk_info:
                result['RiskInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.risk_info = []
        if m.get('RiskInfo') is not None:
            for k1 in m.get('RiskInfo'):
                temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfo()
                self.risk_info.append(temp_model.from_map(k1))

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfo(DaraModel):
    def __init__(
        self,
        ext: main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExt = None,
        path: str = None,
        result_type: str = None,
    ):
        self.ext = ext
        self.path = path
        self.result_type = result_type

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext.to_map()

        if self.path is not None:
            result['Path'] = self.path

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExt()
            self.ext = temp_model.from_map(m.get('Ext'))

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExt(DaraModel):
    def __init__(
        self,
        config: main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtConfig = None,
        guardrail: main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtGuardrail = None,
        sensitive: main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtSensitive = None,
        virus: List[main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtVirus] = None,
    ):
        self.config = config
        self.guardrail = guardrail
        self.sensitive = sensitive
        self.virus = virus

    def validate(self):
        if self.config:
            self.config.validate()
        if self.guardrail:
            self.guardrail.validate()
        if self.sensitive:
            self.sensitive.validate()
        if self.virus:
            for v1 in self.virus:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.guardrail is not None:
            result['Guardrail'] = self.guardrail.to_map()

        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive.to_map()

        result['Virus'] = []
        if self.virus is not None:
            for k1 in self.virus:
                result['Virus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('Guardrail') is not None:
            temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtGuardrail()
            self.guardrail = temp_model.from_map(m.get('Guardrail'))

        if m.get('Sensitive') is not None:
            temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtSensitive()
            self.sensitive = temp_model.from_map(m.get('Sensitive'))

        self.virus = []
        if m.get('Virus') is not None:
            for k1 in m.get('Virus'):
                temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtVirus()
                self.virus.append(temp_model.from_map(k1))

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtVirus(DaraModel):
    def __init__(
        self,
        ext: str = None,
        score: int = None,
        type: str = None,
    ):
        self.ext = ext
        self.score = score
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext

        if self.score is not None:
            result['Score'] = self.score

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtSensitive(DaraModel):
    def __init__(
        self,
        detail: List[main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtSensitiveDetail] = None,
    ):
        self.detail = detail

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtSensitiveDetail()
                self.detail.append(temp_model.from_map(k1))

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtSensitiveDetail(DaraModel):
    def __init__(
        self,
        desc: str = None,
        result: List[str] = None,
    ):
        self.desc = desc
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtGuardrail(DaraModel):
    def __init__(
        self,
        detail: List[main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtGuardrailDetail] = None,
        suggestion: str = None,
    ):
        self.detail = detail
        self.suggestion = suggestion

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtGuardrailDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtGuardrailDetail(DaraModel):
    def __init__(
        self,
        level: str = None,
        result: List[main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtGuardrailDetailResult] = None,
        suggestion: str = None,
        type: str = None,
    ):
        self.level = level
        self.result = result
        self.suggestion = suggestion
        self.type = type

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtGuardrailDetailResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtGuardrailDetailResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
        level: str = None,
    ):
        self.confidence = confidence
        self.description = description
        self.label = label
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtConfig(DaraModel):
    def __init__(
        self,
        detail: List[main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtConfigDetail] = None,
    ):
        self.detail = detail

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtConfigDetail()
                self.detail.append(temp_model.from_map(k1))

        return self

class ListSubTasksResponseBodyDataTaskResultMessageSkillCheckResultRiskInfoExtConfigDetail(DaraModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        item_name: str = None,
        line: str = None,
    ):
        self.content = content
        self.description = description
        self.item_name = item_name
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        if self.line is not None:
            result['Line'] = self.line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        return self

