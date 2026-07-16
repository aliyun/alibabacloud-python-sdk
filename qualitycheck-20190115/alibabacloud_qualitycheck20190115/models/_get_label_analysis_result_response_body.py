# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetLabelAnalysisResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetLabelAnalysisResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. **200** indicates success. Other values indicate failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The returned result.
        self.data = data
        # The error message returned when the call fails.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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
            temp_model = main_models.GetLabelAnalysisResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetLabelAnalysisResultResponseBodyData(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        tag_list: List[main_models.GetLabelAnalysisResultResponseBodyDataTagList] = None,
        total_tokens: int = None,
        tyxm_plus_count: int = None,
        tyxm_turbo_count: int = None,
    ):
        # The total number of input tokens accumulated during this task.
        self.input_tokens = input_tokens
        # The total number of output tokens accumulated during this task.
        self.output_tokens = output_tokens
        # The tree-structured tag results.
        self.tag_list = tag_list
        # The total number of tokens accumulated during this task.
        self.total_tokens = total_tokens
        # The total number of Qwen-Plus model calls accumulated during this task.
        self.tyxm_plus_count = tyxm_plus_count
        # The total number of Qwen-Turbo model calls accumulated during this task.
        self.tyxm_turbo_count = tyxm_turbo_count

    def validate(self):
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        if self.tyxm_plus_count is not None:
            result['TyxmPlusCount'] = self.tyxm_plus_count

        if self.tyxm_turbo_count is not None:
            result['TyxmTurboCount'] = self.tyxm_turbo_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.GetLabelAnalysisResultResponseBodyDataTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        if m.get('TyxmPlusCount') is not None:
            self.tyxm_plus_count = m.get('TyxmPlusCount')

        if m.get('TyxmTurboCount') is not None:
            self.tyxm_turbo_count = m.get('TyxmTurboCount')

        return self

class GetLabelAnalysisResultResponseBodyDataTagList(DaraModel):
    def __init__(
        self,
        children: List[main_models.GetLabelAnalysisResultResponseBodyDataTagListChildren] = None,
        remarks: str = None,
        tag_name: str = None,
    ):
        # The list of child nodes.
        self.children = children
        # The description of the tag analysis.
        self.remarks = remarks
        # The tag name.
        self.tag_name = tag_name

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.GetLabelAnalysisResultResponseBodyDataTagListChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class GetLabelAnalysisResultResponseBodyDataTagListChildren(DaraModel):
    def __init__(
        self,
        children: List[main_models.GetLabelAnalysisResultResponseBodyDataTagListChildrenChildren] = None,
        remarks: str = None,
        tag_name: str = None,
    ):
        # The list of child nodes.
        self.children = children
        # The description of the tag analysis.
        self.remarks = remarks
        # The tag name.
        self.tag_name = tag_name

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.GetLabelAnalysisResultResponseBodyDataTagListChildrenChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class GetLabelAnalysisResultResponseBodyDataTagListChildrenChildren(DaraModel):
    def __init__(
        self,
        children: List[main_models.GetLabelAnalysisResultResponseBodyDataTagListChildrenChildrenChildren] = None,
        remarks: str = None,
        tag_name: str = None,
    ):
        # The list of child nodes.
        self.children = children
        # The description of the tag analysis.
        self.remarks = remarks
        # The tag name.
        self.tag_name = tag_name

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.GetLabelAnalysisResultResponseBodyDataTagListChildrenChildrenChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class GetLabelAnalysisResultResponseBodyDataTagListChildrenChildrenChildren(DaraModel):
    def __init__(
        self,
        children: List[main_models.GetLabelAnalysisResultResponseBodyDataTagListChildrenChildrenChildrenChildren] = None,
        remarks: str = None,
        tag_name: str = None,
    ):
        # The list of child nodes.
        self.children = children
        # The description of the tag analysis.
        self.remarks = remarks
        # The tag name.
        self.tag_name = tag_name

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.GetLabelAnalysisResultResponseBodyDataTagListChildrenChildrenChildrenChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class GetLabelAnalysisResultResponseBodyDataTagListChildrenChildrenChildrenChildren(DaraModel):
    def __init__(
        self,
        remarks: str = None,
        tag_name: str = None,
    ):
        # The description of the tag analysis.
        self.remarks = remarks
        # The tag name.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

