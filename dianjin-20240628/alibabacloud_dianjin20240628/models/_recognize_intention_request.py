# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class RecognizeIntentionRequest(DaraModel):
    def __init__(
        self,
        analysis: bool = None,
        biz_type: str = None,
        conversation: str = None,
        global_intention_list: List[main_models.RecognizeIntentionRequestGlobalIntentionList] = None,
        hierarchical_intention_list: List[main_models.RecognizeIntentionRequestHierarchicalIntentionList] = None,
        intention_domain_code: str = None,
        intention_list: List[main_models.RecognizeIntentionRequestIntentionList] = None,
        op_type: str = None,
        recommend: bool = None,
    ):
        self.analysis = analysis
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.conversation = conversation
        self.global_intention_list = global_intention_list
        self.hierarchical_intention_list = hierarchical_intention_list
        self.intention_domain_code = intention_domain_code
        self.intention_list = intention_list
        self.op_type = op_type
        self.recommend = recommend

    def validate(self):
        if self.global_intention_list:
            for v1 in self.global_intention_list:
                 if v1:
                    v1.validate()
        if self.hierarchical_intention_list:
            for v1 in self.hierarchical_intention_list:
                 if v1:
                    v1.validate()
        if self.intention_list:
            for v1 in self.intention_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis is not None:
            result['analysis'] = self.analysis

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.conversation is not None:
            result['conversation'] = self.conversation

        result['globalIntentionList'] = []
        if self.global_intention_list is not None:
            for k1 in self.global_intention_list:
                result['globalIntentionList'].append(k1.to_map() if k1 else None)

        result['hierarchicalIntentionList'] = []
        if self.hierarchical_intention_list is not None:
            for k1 in self.hierarchical_intention_list:
                result['hierarchicalIntentionList'].append(k1.to_map() if k1 else None)

        if self.intention_domain_code is not None:
            result['intentionDomainCode'] = self.intention_domain_code

        result['intentionList'] = []
        if self.intention_list is not None:
            for k1 in self.intention_list:
                result['intentionList'].append(k1.to_map() if k1 else None)

        if self.op_type is not None:
            result['opType'] = self.op_type

        if self.recommend is not None:
            result['recommend'] = self.recommend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis') is not None:
            self.analysis = m.get('analysis')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('conversation') is not None:
            self.conversation = m.get('conversation')

        self.global_intention_list = []
        if m.get('globalIntentionList') is not None:
            for k1 in m.get('globalIntentionList'):
                temp_model = main_models.RecognizeIntentionRequestGlobalIntentionList()
                self.global_intention_list.append(temp_model.from_map(k1))

        self.hierarchical_intention_list = []
        if m.get('hierarchicalIntentionList') is not None:
            for k1 in m.get('hierarchicalIntentionList'):
                temp_model = main_models.RecognizeIntentionRequestHierarchicalIntentionList()
                self.hierarchical_intention_list.append(temp_model.from_map(k1))

        if m.get('intentionDomainCode') is not None:
            self.intention_domain_code = m.get('intentionDomainCode')

        self.intention_list = []
        if m.get('intentionList') is not None:
            for k1 in m.get('intentionList'):
                temp_model = main_models.RecognizeIntentionRequestIntentionList()
                self.intention_list.append(temp_model.from_map(k1))

        if m.get('opType') is not None:
            self.op_type = m.get('opType')

        if m.get('recommend') is not None:
            self.recommend = m.get('recommend')

        return self

class RecognizeIntentionRequestIntentionList(DaraModel):
    def __init__(
        self,
        description: str = None,
        intention: str = None,
        intention_code: str = None,
        intention_script: str = None,
    ):
        self.description = description
        self.intention = intention
        self.intention_code = intention_code
        self.intention_script = intention_script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.intention is not None:
            result['intention'] = self.intention

        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code

        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('intention') is not None:
            self.intention = m.get('intention')

        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')

        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')

        return self

class RecognizeIntentionRequestHierarchicalIntentionList(DaraModel):
    def __init__(
        self,
        description: str = None,
        intention: str = None,
        intention_code: str = None,
        intention_script: str = None,
    ):
        self.description = description
        self.intention = intention
        self.intention_code = intention_code
        self.intention_script = intention_script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.intention is not None:
            result['intention'] = self.intention

        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code

        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('intention') is not None:
            self.intention = m.get('intention')

        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')

        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')

        return self

class RecognizeIntentionRequestGlobalIntentionList(DaraModel):
    def __init__(
        self,
        description: str = None,
        intention: str = None,
        intention_code: str = None,
        intention_script: str = None,
    ):
        self.description = description
        self.intention = intention
        self.intention_code = intention_code
        self.intention_script = intention_script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.intention is not None:
            result['intention'] = self.intention

        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code

        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('intention') is not None:
            self.intention = m.get('intention')

        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')

        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')

        return self

