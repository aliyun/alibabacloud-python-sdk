# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class ChatRefDocItem(DaraModel):
    def __init__(
        self,
        doc_info: main_models.ChatRefDocInfo = None,
        doc_name: str = None,
        doc_url: str = None,
        origin_doc_name: str = None,
        origin_doc_url: str = None,
        page_num: List[main_models.ChatDocumentPageNum] = None,
        source_type: str = None,
    ):
        self.doc_info = doc_info
        self.doc_name = doc_name
        self.doc_url = doc_url
        self.origin_doc_name = origin_doc_name
        self.origin_doc_url = origin_doc_url
        self.page_num = page_num
        self.source_type = source_type

    def validate(self):
        if self.doc_info:
            self.doc_info.validate()
        if self.page_num:
            for v1 in self.page_num:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_info is not None:
            result['docInfo'] = self.doc_info.to_map()

        if self.doc_name is not None:
            result['docName'] = self.doc_name

        if self.doc_url is not None:
            result['docUrl'] = self.doc_url

        if self.origin_doc_name is not None:
            result['originDocName'] = self.origin_doc_name

        if self.origin_doc_url is not None:
            result['originDocUrl'] = self.origin_doc_url

        result['pageNum'] = []
        if self.page_num is not None:
            for k1 in self.page_num:
                result['pageNum'].append(k1.to_map() if k1 else None)

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docInfo') is not None:
            temp_model = main_models.ChatRefDocInfo()
            self.doc_info = temp_model.from_map(m.get('docInfo'))

        if m.get('docName') is not None:
            self.doc_name = m.get('docName')

        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')

        if m.get('originDocName') is not None:
            self.origin_doc_name = m.get('originDocName')

        if m.get('originDocUrl') is not None:
            self.origin_doc_url = m.get('originDocUrl')

        self.page_num = []
        if m.get('pageNum') is not None:
            for k1 in m.get('pageNum'):
                temp_model = main_models.ChatDocumentPageNum()
                self.page_num.append(temp_model.from_map(k1))

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

