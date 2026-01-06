# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListTemplateResponseBody(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: str = None,
        request_id: str = None,
        template_list: List[main_models.ListTemplateResponseBodyTemplateList] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.has_more = has_more
        self.next_token = next_token
        self.request_id = request_id
        self.template_list = template_list
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.template_list:
            for v1 in self.template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['templateList'] = []
        if self.template_list is not None:
            for k1 in self.template_list:
                result['templateList'].append(k1.to_map() if k1 else None)

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.template_list = []
        if m.get('templateList') is not None:
            for k1 in m.get('templateList'):
                temp_model = main_models.ListTemplateResponseBodyTemplateList()
                self.template_list.append(temp_model.from_map(k1))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class ListTemplateResponseBodyTemplateList(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        create_time: int = None,
        doc_type: str = None,
        id: str = None,
        template_type: str = None,
        title: str = None,
        update_time: int = None,
        workspace_id: str = None,
    ):
        self.cover_url = cover_url
        self.create_time = create_time
        self.doc_type = doc_type
        self.id = id
        self.template_type = template_type
        self.title = title
        self.update_time = update_time
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.id is not None:
            result['Id'] = self.id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.title is not None:
            result['Title'] = self.title

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

