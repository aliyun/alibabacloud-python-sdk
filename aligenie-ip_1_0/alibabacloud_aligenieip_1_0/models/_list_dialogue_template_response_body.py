# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListDialogueTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.ListDialogueTemplateResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        # RequestId
        self.request_id = request_id
        self.result = result

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
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListDialogueTemplateResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListDialogueTemplateResponseBodyResult(DaraModel):
    def __init__(
        self,
        template_detail: main_models.ListDialogueTemplateResponseBodyResultTemplateDetail = None,
        template_id: int = None,
        template_name: str = None,
        type: str = None,
    ):
        self.template_detail = template_detail
        self.template_id = template_id
        self.template_name = template_name
        self.type = type

    def validate(self):
        if self.template_detail:
            self.template_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_detail is not None:
            result['TemplateDetail'] = self.template_detail.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateDetail') is not None:
            temp_model = main_models.ListDialogueTemplateResponseBodyResultTemplateDetail()
            self.template_detail = temp_model.from_map(m.get('TemplateDetail'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDialogueTemplateResponseBodyResultTemplateDetail(DaraModel):
    def __init__(
        self,
        first_dialogue_template: main_models.ListDialogueTemplateResponseBodyResultTemplateDetailFirstDialogueTemplate = None,
        second_dialogue_template: main_models.ListDialogueTemplateResponseBodyResultTemplateDetailSecondDialogueTemplate = None,
    ):
        self.first_dialogue_template = first_dialogue_template
        self.second_dialogue_template = second_dialogue_template

    def validate(self):
        if self.first_dialogue_template:
            self.first_dialogue_template.validate()
        if self.second_dialogue_template:
            self.second_dialogue_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_dialogue_template is not None:
            result['FirstDialogueTemplate'] = self.first_dialogue_template.to_map()

        if self.second_dialogue_template is not None:
            result['SecondDialogueTemplate'] = self.second_dialogue_template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstDialogueTemplate') is not None:
            temp_model = main_models.ListDialogueTemplateResponseBodyResultTemplateDetailFirstDialogueTemplate()
            self.first_dialogue_template = temp_model.from_map(m.get('FirstDialogueTemplate'))

        if m.get('SecondDialogueTemplate') is not None:
            temp_model = main_models.ListDialogueTemplateResponseBodyResultTemplateDetailSecondDialogueTemplate()
            self.second_dialogue_template = temp_model.from_map(m.get('SecondDialogueTemplate'))

        return self

class ListDialogueTemplateResponseBodyResultTemplateDetailSecondDialogueTemplate(DaraModel):
    def __init__(
        self,
        nonzero_price_no_answer: str = None,
        nonzero_price_yes_answer: str = None,
    ):
        self.nonzero_price_no_answer = nonzero_price_no_answer
        self.nonzero_price_yes_answer = nonzero_price_yes_answer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nonzero_price_no_answer is not None:
            result['NonzeroPriceNoAnswer'] = self.nonzero_price_no_answer

        if self.nonzero_price_yes_answer is not None:
            result['NonzeroPriceYesAnswer'] = self.nonzero_price_yes_answer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonzeroPriceNoAnswer') is not None:
            self.nonzero_price_no_answer = m.get('NonzeroPriceNoAnswer')

        if m.get('NonzeroPriceYesAnswer') is not None:
            self.nonzero_price_yes_answer = m.get('NonzeroPriceYesAnswer')

        return self

class ListDialogueTemplateResponseBodyResultTemplateDetailFirstDialogueTemplate(DaraModel):
    def __init__(
        self,
        nonzero_price_yes_answer: str = None,
        zero_price_no_answer: str = None,
        zero_price_yes_answer: str = None,
    ):
        self.nonzero_price_yes_answer = nonzero_price_yes_answer
        self.zero_price_no_answer = zero_price_no_answer
        self.zero_price_yes_answer = zero_price_yes_answer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nonzero_price_yes_answer is not None:
            result['NonzeroPriceYesAnswer'] = self.nonzero_price_yes_answer

        if self.zero_price_no_answer is not None:
            result['ZeroPriceNoAnswer'] = self.zero_price_no_answer

        if self.zero_price_yes_answer is not None:
            result['ZeroPriceYesAnswer'] = self.zero_price_yes_answer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonzeroPriceYesAnswer') is not None:
            self.nonzero_price_yes_answer = m.get('NonzeroPriceYesAnswer')

        if m.get('ZeroPriceNoAnswer') is not None:
            self.zero_price_no_answer = m.get('ZeroPriceNoAnswer')

        if m.get('ZeroPriceYesAnswer') is not None:
            self.zero_price_yes_answer = m.get('ZeroPriceYesAnswer')

        return self

