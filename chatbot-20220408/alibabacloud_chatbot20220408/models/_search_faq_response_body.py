# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class SearchFaqResponseBody(DaraModel):
    def __init__(
        self,
        faq_hits: List[main_models.SearchFaqResponseBodyFaqHits] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.faq_hits = faq_hits
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.faq_hits:
            for v1 in self.faq_hits:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FaqHits'] = []
        if self.faq_hits is not None:
            for k1 in self.faq_hits:
                result['FaqHits'].append(k1.to_map() if k1 else None)

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
        self.faq_hits = []
        if m.get('FaqHits') is not None:
            for k1 in m.get('FaqHits'):
                temp_model = main_models.SearchFaqResponseBodyFaqHits()
                self.faq_hits.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchFaqResponseBodyFaqHits(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        effect_status: int = None,
        hit_similar_titles: List[str] = None,
        hit_solutions: List[str] = None,
        knowledge_id: int = None,
        modify_time: str = None,
        modify_user_id: int = None,
        modify_user_name: str = None,
        status: int = None,
        title: str = None,
    ):
        self.category_id = category_id
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.effect_status = effect_status
        self.hit_similar_titles = hit_similar_titles
        self.hit_solutions = hit_solutions
        self.knowledge_id = knowledge_id
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status

        if self.hit_similar_titles is not None:
            result['HitSimilarTitles'] = self.hit_similar_titles

        if self.hit_solutions is not None:
            result['HitSolutions'] = self.hit_solutions

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')

        if m.get('HitSimilarTitles') is not None:
            self.hit_similar_titles = m.get('HitSimilarTitles')

        if m.get('HitSolutions') is not None:
            self.hit_solutions = m.get('HitSolutions')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

