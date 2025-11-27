# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ChatDetailUserInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        role: str = None,
    ):
        self.name = name
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ChatDetail(TeaModel):
    def __init__(
        self,
        content: str = None,
        gmt_create_time: str = None,
        user_info: ChatDetailUserInfo = None,
    ):
        self.content = content
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('UserInfo') is not None:
            temp_model = ChatDetailUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class Chat(TeaModel):
    def __init__(
        self,
        answer: ChatDetail = None,
        chat_id: str = None,
        extra_data: str = None,
        gmt_create_time: str = None,
        gmt_modified: str = None,
        message: str = None,
        owner_id: str = None,
        question: ChatDetail = None,
        session_id: str = None,
        status: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.answer = answer
        self.chat_id = chat_id
        self.extra_data = extra_data
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_modified = gmt_modified
        self.message = message
        self.owner_id = owner_id
        self.question = question
        self.session_id = session_id
        self.status = status
        self.title = title
        self.user_id = user_id

    def validate(self):
        if self.answer:
            self.answer.validate()
        if self.question:
            self.question.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer.to_map()
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.question is not None:
            result['Question'] = self.question.to_map()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            temp_model = ChatDetail()
            self.answer = temp_model.from_map(m['Answer'])
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Question') is not None:
            temp_model = ChatDetail()
            self.question = temp_model.from_map(m['Question'])
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class Feedback(TeaModel):
    def __init__(
        self,
        chat_id: str = None,
        feedback_action: str = None,
        feedback_id: str = None,
        feedback_message: str = None,
        gmt_create_time: str = None,
        gmt_modified: str = None,
        owner_id: str = None,
        session_id: str = None,
        user_id: str = None,
    ):
        self.chat_id = chat_id
        self.feedback_action = feedback_action
        self.feedback_id = feedback_id
        self.feedback_message = feedback_message
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.gmt_modified = gmt_modified
        self.owner_id = owner_id
        self.session_id = session_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id
        if self.feedback_action is not None:
            result['FeedbackAction'] = self.feedback_action
        if self.feedback_id is not None:
            result['FeedbackId'] = self.feedback_id
        if self.feedback_message is not None:
            result['FeedbackMessage'] = self.feedback_message
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')
        if m.get('FeedbackAction') is not None:
            self.feedback_action = m.get('FeedbackAction')
        if m.get('FeedbackId') is not None:
            self.feedback_id = m.get('FeedbackId')
        if m.get('FeedbackMessage') is not None:
            self.feedback_message = m.get('FeedbackMessage')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class Label(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class Session(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified: str = None,
        owner_id: str = None,
        session_id: str = None,
        session_title: str = None,
        user_id: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_modified = gmt_modified
        self.owner_id = owner_id
        self.session_id = session_id
        self.session_title = session_title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_title is not None:
            result['SessionTitle'] = self.session_title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionTitle') is not None:
            self.session_title = m.get('SessionTitle')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchInfoRequestKnowledgeBaseFilters(TeaModel):
    def __init__(
        self,
        collection_name: str = None,
        query: str = None,
        result_limit: int = None,
        score_threshold: float = None,
    ):
        # This parameter is required.
        self.collection_name = collection_name
        # This parameter is required.
        self.query = query
        self.result_limit = result_limit
        self.score_threshold = score_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.query is not None:
            result['Query'] = self.query
        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit
        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')
        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')
        return self


class SearchInfoRequestWebFilters(TeaModel):
    def __init__(
        self,
        include_sites: List[str] = None,
        query: str = None,
        result_limit: int = None,
        score_threshold: float = None,
    ):
        self.include_sites = include_sites
        # This parameter is required.
        self.query = query
        self.result_limit = result_limit
        self.score_threshold = score_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_sites is not None:
            result['IncludeSites'] = self.include_sites
        if self.query is not None:
            result['Query'] = self.query
        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit
        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeSites') is not None:
            self.include_sites = m.get('IncludeSites')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')
        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')
        return self


class SearchInfoRequest(TeaModel):
    def __init__(
        self,
        knowledge_base_filters: List[SearchInfoRequestKnowledgeBaseFilters] = None,
        web_filters: List[SearchInfoRequestWebFilters] = None,
    ):
        self.knowledge_base_filters = knowledge_base_filters
        self.web_filters = web_filters

    def validate(self):
        if self.knowledge_base_filters:
            for k in self.knowledge_base_filters:
                if k:
                    k.validate()
        if self.web_filters:
            for k in self.web_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KnowledgeBaseFilters'] = []
        if self.knowledge_base_filters is not None:
            for k in self.knowledge_base_filters:
                result['KnowledgeBaseFilters'].append(k.to_map() if k else None)
        result['WebFilters'] = []
        if self.web_filters is not None:
            for k in self.web_filters:
                result['WebFilters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_base_filters = []
        if m.get('KnowledgeBaseFilters') is not None:
            for k in m.get('KnowledgeBaseFilters'):
                temp_model = SearchInfoRequestKnowledgeBaseFilters()
                self.knowledge_base_filters.append(temp_model.from_map(k))
        self.web_filters = []
        if m.get('WebFilters') is not None:
            for k in m.get('WebFilters'):
                temp_model = SearchInfoRequestWebFilters()
                self.web_filters.append(temp_model.from_map(k))
        return self


class SearchInfoResponseBodyKnowledgeBaseSearchResults(TeaModel):
    def __init__(
        self,
        index: str = None,
        result_content: str = None,
        score: float = None,
    ):
        self.index = index
        self.result_content = result_content
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.result_content is not None:
            result['ResultContent'] = self.result_content
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('ResultContent') is not None:
            self.result_content = m.get('ResultContent')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class SearchInfoResponseBodyWebSearchResults(TeaModel):
    def __init__(
        self,
        index: str = None,
        result_content: str = None,
        score: float = None,
        source_link: str = None,
    ):
        self.index = index
        self.result_content = result_content
        self.score = score
        self.source_link = source_link

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.result_content is not None:
            result['ResultContent'] = self.result_content
        if self.score is not None:
            result['Score'] = self.score
        if self.source_link is not None:
            result['SourceLink'] = self.source_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('ResultContent') is not None:
            self.result_content = m.get('ResultContent')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SourceLink') is not None:
            self.source_link = m.get('SourceLink')
        return self


class SearchInfoResponseBody(TeaModel):
    def __init__(
        self,
        knowledge_base_search_results: List[SearchInfoResponseBodyKnowledgeBaseSearchResults] = None,
        request_id: str = None,
        web_search_results: List[SearchInfoResponseBodyWebSearchResults] = None,
    ):
        self.knowledge_base_search_results = knowledge_base_search_results
        self.request_id = request_id
        self.web_search_results = web_search_results

    def validate(self):
        if self.knowledge_base_search_results:
            for k in self.knowledge_base_search_results:
                if k:
                    k.validate()
        if self.web_search_results:
            for k in self.web_search_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KnowledgeBaseSearchResults'] = []
        if self.knowledge_base_search_results is not None:
            for k in self.knowledge_base_search_results:
                result['KnowledgeBaseSearchResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WebSearchResults'] = []
        if self.web_search_results is not None:
            for k in self.web_search_results:
                result['WebSearchResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_base_search_results = []
        if m.get('KnowledgeBaseSearchResults') is not None:
            for k in m.get('KnowledgeBaseSearchResults'):
                temp_model = SearchInfoResponseBodyKnowledgeBaseSearchResults()
                self.knowledge_base_search_results.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.web_search_results = []
        if m.get('WebSearchResults') is not None:
            for k in m.get('WebSearchResults'):
                temp_model = SearchInfoResponseBodyWebSearchResults()
                self.web_search_results.append(temp_model.from_map(k))
        return self


class SearchInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


