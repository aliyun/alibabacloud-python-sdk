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
        # A list of matching documents.
        self.doc_hits = doc_hits
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of matching entries.
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
        # The business code.
        self.biz_code = biz_code
        # The category ID.
        self.category_id = category_id
        # The splitter for the document. Key: `Splitter`. Valid values:<br>• `paragraphSplitter` (default): Splits the document by paragraph.<br>• `treeSplitter`: Splits the document based on a rule-based hierarchy.<br><br>
        # 
        # The size of each document chunk. Key: `ChunkSize`. Default value: 500. Value range: [200, 800].
        # 
        # The patterns for the rule-based hierarchy. Key: `TreePatterns`. Default value: `[]`.
        # 
        # The source of the document title. Key: `TitleSource`. Valid values:<br>• `ocrTitle` (default): Uses the OCR-identified title.<br>• `docName`: Uses the document name as the title.<br><br>
        self.config = config
        # The time the document was created (UTC).
        self.create_time = create_time
        # The creator ID.
        self.create_user_id = create_user_id
        # The name of the creator.
        self.create_user_name = create_user_name
        # The document name.
        self.doc_name = doc_name
        # A list of the document\\"s tags.
        self.doc_tags = doc_tags
        # The knowledge\\"s effective status, calculated based on `StartDate` and `EndDate`. Valid values:<br>• 20: Active<br>• 21: Expired<br>• 22: Pending<br><br><br>
        self.effect_status = effect_status
        # The time the knowledge expires (UTC).
        self.end_date = end_date
        # The knowledge ID.
        self.knowledge_id = knowledge_id
        # The document metadata.
        self.meta = meta
        # The time the document was last modified (UTC).
        self.modify_time = modify_time
        # The modifier ID.
        self.modify_user_id = modify_user_id
        # The name of the last modifier.
        self.modify_user_name = modify_user_name
        # Indicates whether the task can be retried.<br>• `true`: The task can be retried.<br>• `false`: The task cannot be retried.<br><br>
        self.process_can_retry = process_can_retry
        # The processing message for the task.
        self.process_message = process_message
        # The task\\"s processing status. Valid values:<br>• -1: Queued<br>• 0: Succeeded<br>• 1: Parsing<br>• 2: Processing<br>• 3: Failed<br><br><br><br><br>
        self.process_status = process_status
        # The time the knowledge takes effect (UTC).
        self.start_date = start_date
        # The editing status of the document. Valid values:<br>• 1: Unpublished<br>• 2: Published<br>• 3: Updated but not published<br><br><br>
        self.status = status
        # The OSS URL of the object.
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
        # Indicates whether this is a default tag.
        self.default_tag = default_tag
        # The tag group ID.
        self.group_id = group_id
        # The tag group name.
        self.group_name = group_name
        # The tag ID.
        self.tag_id = tag_id
        # The tag name.
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

