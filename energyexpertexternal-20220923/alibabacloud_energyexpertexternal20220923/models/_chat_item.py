# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class ChatItem(DaraModel):
    def __init__(
        self,
        answer: str = None,
        create_time: int = None,
        folder_id: str = None,
        folder_name: str = None,
        question: str = None,
        ref_doc_list: List[main_models.ChatRefDocItem] = None,
    ):
        self.answer = answer
        self.create_time = create_time
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.question = question
        self.ref_doc_list = ref_doc_list

    def validate(self):
        if self.ref_doc_list:
            for v1 in self.ref_doc_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['answer'] = self.answer

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.folder_name is not None:
            result['folderName'] = self.folder_name

        if self.question is not None:
            result['question'] = self.question

        result['refDocList'] = []
        if self.ref_doc_list is not None:
            for k1 in self.ref_doc_list:
                result['refDocList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('folderName') is not None:
            self.folder_name = m.get('folderName')

        if m.get('question') is not None:
            self.question = m.get('question')

        self.ref_doc_list = []
        if m.get('refDocList') is not None:
            for k1 in m.get('refDocList'):
                temp_model = main_models.ChatRefDocItem()
                self.ref_doc_list.append(temp_model.from_map(k1))

        return self

