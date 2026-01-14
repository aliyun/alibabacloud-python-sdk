# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class BatchAddDocumentRequest(DaraModel):
    def __init__(
        self,
        add_document_infos: List[main_models.AddDocumentInfo] = None,
    ):
        self.add_document_infos = add_document_infos

    def validate(self):
        if self.add_document_infos:
            for v1 in self.add_document_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['addDocumentInfos'] = []
        if self.add_document_infos is not None:
            for k1 in self.add_document_infos:
                result['addDocumentInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_document_infos = []
        if m.get('addDocumentInfos') is not None:
            for k1 in m.get('addDocumentInfos'):
                temp_model = main_models.AddDocumentInfo()
                self.add_document_infos.append(temp_model.from_map(k1))

        return self

