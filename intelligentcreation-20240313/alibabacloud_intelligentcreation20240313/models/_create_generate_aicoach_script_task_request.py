# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class CreateGenerateAICoachScriptTaskRequest(DaraModel):
    def __init__(
        self,
        assessment_point: bool = None,
        description: str = None,
        dialogue_key: str = None,
        dialogue_url: str = None,
        doc_list: List[main_models.CreateGenerateAICoachScriptTaskRequestDocList] = None,
        doc_url_list: List[str] = None,
        script_name: str = None,
    ):
        self.assessment_point = assessment_point
        self.description = description
        self.dialogue_key = dialogue_key
        self.dialogue_url = dialogue_url
        self.doc_list = doc_list
        self.doc_url_list = doc_url_list
        self.script_name = script_name

    def validate(self):
        if self.doc_list:
            for v1 in self.doc_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assessment_point is not None:
            result['assessmentPoint'] = self.assessment_point

        if self.description is not None:
            result['description'] = self.description

        if self.dialogue_key is not None:
            result['dialogueKey'] = self.dialogue_key

        if self.dialogue_url is not None:
            result['dialogueUrl'] = self.dialogue_url

        result['docList'] = []
        if self.doc_list is not None:
            for k1 in self.doc_list:
                result['docList'].append(k1.to_map() if k1 else None)

        if self.doc_url_list is not None:
            result['docUrlList'] = self.doc_url_list

        if self.script_name is not None:
            result['scriptName'] = self.script_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assessmentPoint') is not None:
            self.assessment_point = m.get('assessmentPoint')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('dialogueKey') is not None:
            self.dialogue_key = m.get('dialogueKey')

        if m.get('dialogueUrl') is not None:
            self.dialogue_url = m.get('dialogueUrl')

        self.doc_list = []
        if m.get('docList') is not None:
            for k1 in m.get('docList'):
                temp_model = main_models.CreateGenerateAICoachScriptTaskRequestDocList()
                self.doc_list.append(temp_model.from_map(k1))

        if m.get('docUrlList') is not None:
            self.doc_url_list = m.get('docUrlList')

        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')

        return self

class CreateGenerateAICoachScriptTaskRequestDocList(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_name: str = None,
        kb_id: str = None,
    ):
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.kb_id = kb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.doc_name is not None:
            result['docName'] = self.doc_name

        if self.kb_id is not None:
            result['kbId'] = self.kb_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('docName') is not None:
            self.doc_name = m.get('docName')

        if m.get('kbId') is not None:
            self.kb_id = m.get('kbId')

        return self

