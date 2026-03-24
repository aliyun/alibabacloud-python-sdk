# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class CreateDocRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        config: str = None,
        content: str = None,
        doc_metadata: List[main_models.CreateDocRequestDocMetadata] = None,
        end_date: str = None,
        meta: str = None,
        start_date: str = None,
        tag_ids: List[int] = None,
        title: str = None,
        url: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.category_id = category_id
        self.config = config
        self.content = content
        self.doc_metadata = doc_metadata
        self.end_date = end_date
        self.meta = meta
        self.start_date = start_date
        self.tag_ids = tag_ids
        # This parameter is required.
        self.title = title
        self.url = url

    def validate(self):
        if self.doc_metadata:
            for v1 in self.doc_metadata:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.config is not None:
            result['Config'] = self.config

        if self.content is not None:
            result['Content'] = self.content

        result['DocMetadata'] = []
        if self.doc_metadata is not None:
            for k1 in self.doc_metadata:
                result['DocMetadata'].append(k1.to_map() if k1 else None)

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.meta is not None:
            result['Meta'] = self.meta

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.doc_metadata = []
        if m.get('DocMetadata') is not None:
            for k1 in m.get('DocMetadata'):
                temp_model = main_models.CreateDocRequestDocMetadata()
                self.doc_metadata.append(temp_model.from_map(k1))

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class CreateDocRequestDocMetadata(DaraModel):
    def __init__(
        self,
        business_view_id: str = None,
        business_view_name: str = None,
        meta_cell_info_dtolist: List[main_models.CreateDocRequestDocMetadataMetaCellInfoDTOList] = None,
    ):
        self.business_view_id = business_view_id
        self.business_view_name = business_view_name
        self.meta_cell_info_dtolist = meta_cell_info_dtolist

    def validate(self):
        if self.meta_cell_info_dtolist:
            for v1 in self.meta_cell_info_dtolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_view_id is not None:
            result['BusinessViewId'] = self.business_view_id

        if self.business_view_name is not None:
            result['BusinessViewName'] = self.business_view_name

        result['MetaCellInfoDTOList'] = []
        if self.meta_cell_info_dtolist is not None:
            for k1 in self.meta_cell_info_dtolist:
                result['MetaCellInfoDTOList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessViewId') is not None:
            self.business_view_id = m.get('BusinessViewId')

        if m.get('BusinessViewName') is not None:
            self.business_view_name = m.get('BusinessViewName')

        self.meta_cell_info_dtolist = []
        if m.get('MetaCellInfoDTOList') is not None:
            for k1 in m.get('MetaCellInfoDTOList'):
                temp_model = main_models.CreateDocRequestDocMetadataMetaCellInfoDTOList()
                self.meta_cell_info_dtolist.append(temp_model.from_map(k1))

        return self

class CreateDocRequestDocMetadataMetaCellInfoDTOList(DaraModel):
    def __init__(
        self,
        field_code: str = None,
        field_name: str = None,
        value: str = None,
    ):
        self.field_code = field_code
        self.field_name = field_name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_code is not None:
            result['FieldCode'] = self.field_code

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldCode') is not None:
            self.field_code = m.get('FieldCode')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

