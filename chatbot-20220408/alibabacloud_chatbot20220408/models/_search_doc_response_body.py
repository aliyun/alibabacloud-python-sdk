# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class SearchDocResponseBody(DaraModel):
    def __init__(
        self,
        doc_hits: List[main_models.SearchDocResponseBodyDocHits] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.doc_hits = doc_hits
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.doc_hits:
            for v1 in self.doc_hits:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DocHits'] = []
        if self.doc_hits is not None:
            for k1 in self.doc_hits:
                result['DocHits'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.doc_hits = []
        if m.get('DocHits') is not None:
            for k1 in m.get('DocHits'):
                temp_model = main_models.SearchDocResponseBodyDocHits()
                self.doc_hits.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchDocResponseBodyDocHits(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        category_id: int = None,
        config: str = None,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        doc_name: str = None,
        doc_tags: List[main_models.SearchDocResponseBodyDocHitsDocTags] = None,
        effect_status: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        meta: str = None,
        modify_time: str = None,
        modify_user_id: int = None,
        modify_user_name: str = None,
        process_can_retry: bool = None,
        process_message: str = None,
        process_status: int = None,
        start_date: str = None,
        status: int = None,
        url: str = None,
    ):
        self.biz_code = biz_code
        self.category_id = category_id
        self.config = config
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.doc_name = doc_name
        self.doc_tags = doc_tags
        self.effect_status = effect_status
        self.end_date = end_date
        self.knowledge_id = knowledge_id
        self.meta = meta
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.process_can_retry = process_can_retry
        self.process_message = process_message
        self.process_status = process_status
        self.start_date = start_date
        self.status = status
        self.url = url

    def validate(self):
        if self.doc_tags:
            for v1 in self.doc_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.config is not None:
            result['Config'] = self.config

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        result['DocTags'] = []
        if self.doc_tags is not None:
            for k1 in self.doc_tags:
                result['DocTags'].append(k1.to_map() if k1 else None)

        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.meta is not None:
            result['Meta'] = self.meta

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

        if self.process_can_retry is not None:
            result['ProcessCanRetry'] = self.process_can_retry

        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message

        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        self.doc_tags = []
        if m.get('DocTags') is not None:
            for k1 in m.get('DocTags'):
                temp_model = main_models.SearchDocResponseBodyDocHitsDocTags()
                self.doc_tags.append(temp_model.from_map(k1))

        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        if m.get('ProcessCanRetry') is not None:
            self.process_can_retry = m.get('ProcessCanRetry')

        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')

        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class SearchDocResponseBodyDocHitsDocTags(DaraModel):
    def __init__(
        self,
        default_tag: bool = None,
        group_id: int = None,
        group_name: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.default_tag = default_tag
        self.group_id = group_id
        self.group_name = group_name
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_tag is not None:
            result['DefaultTag'] = self.default_tag

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultTag') is not None:
            self.default_tag = m.get('DefaultTag')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

