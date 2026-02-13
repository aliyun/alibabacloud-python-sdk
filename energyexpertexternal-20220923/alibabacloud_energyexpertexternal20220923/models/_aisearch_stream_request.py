# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class AISearchStreamRequest(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        message: List[main_models.AISearchMessageItem] = None,
        question: str = None,
        resource_type_needed: List[str] = None,
    ):
        # This parameter is required.
        self.folder_id = folder_id
        self.message = message
        # This parameter is required.
        self.question = question
        self.resource_type_needed = resource_type_needed

    def validate(self):
        if self.message:
            for v1 in self.message:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        result['message'] = []
        if self.message is not None:
            for k1 in self.message:
                result['message'].append(k1.to_map() if k1 else None)

        if self.question is not None:
            result['question'] = self.question

        if self.resource_type_needed is not None:
            result['resourceTypeNeeded'] = self.resource_type_needed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        self.message = []
        if m.get('message') is not None:
            for k1 in m.get('message'):
                temp_model = main_models.AISearchMessageItem()
                self.message.append(temp_model.from_map(k1))

        if m.get('question') is not None:
            self.question = m.get('question')

        if m.get('resourceTypeNeeded') is not None:
            self.resource_type_needed = m.get('resourceTypeNeeded')

        return self

