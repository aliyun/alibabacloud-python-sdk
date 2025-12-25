# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class SubmitSmartAuditRequest(DaraModel):
    def __init__(
        self,
        image_url_list: List[main_models.SubmitSmartAuditRequestImageUrlList] = None,
        note_id: str = None,
        sub_codes: List[str] = None,
        terms_name: str = None,
        text: str = None,
        workspace_id: str = None,
        image_urls: List[main_models.SubmitSmartAuditRequestImageUrls] = None,
    ):
        self.image_url_list = image_url_list
        self.note_id = note_id
        self.sub_codes = sub_codes
        self.terms_name = terms_name
        self.text = text
        self.workspace_id = workspace_id
        self.image_urls = image_urls

    def validate(self):
        if self.image_url_list:
            for v1 in self.image_url_list:
                 if v1:
                    v1.validate()
        if self.image_urls:
            for v1 in self.image_urls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageUrlList'] = []
        if self.image_url_list is not None:
            for k1 in self.image_url_list:
                result['ImageUrlList'].append(k1.to_map() if k1 else None)

        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.sub_codes is not None:
            result['SubCodes'] = self.sub_codes

        if self.terms_name is not None:
            result['TermsName'] = self.terms_name

        if self.text is not None:
            result['Text'] = self.text

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        result['imageUrls'] = []
        if self.image_urls is not None:
            for k1 in self.image_urls:
                result['imageUrls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_url_list = []
        if m.get('ImageUrlList') is not None:
            for k1 in m.get('ImageUrlList'):
                temp_model = main_models.SubmitSmartAuditRequestImageUrlList()
                self.image_url_list.append(temp_model.from_map(k1))

        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('SubCodes') is not None:
            self.sub_codes = m.get('SubCodes')

        if m.get('TermsName') is not None:
            self.terms_name = m.get('TermsName')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        self.image_urls = []
        if m.get('imageUrls') is not None:
            for k1 in m.get('imageUrls'):
                temp_model = main_models.SubmitSmartAuditRequestImageUrls()
                self.image_urls.append(temp_model.from_map(k1))

        return self

class SubmitSmartAuditRequestImageUrls(DaraModel):
    def __init__(
        self,
        id: str = None,
        url: str = None,
    ):
        self.id = id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class SubmitSmartAuditRequestImageUrlList(DaraModel):
    def __init__(
        self,
        id: str = None,
        url: str = None,
    ):
        self.id = id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

