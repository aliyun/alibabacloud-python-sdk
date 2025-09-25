# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any, BinaryIO


class CreateAnnualDocSummaryTaskRequestDocInfos(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_year: int = None,
        end_page: int = None,
        library_id: str = None,
        start_page: int = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        # This parameter is required.
        self.doc_year = doc_year
        self.end_page = end_page
        # This parameter is required.
        self.library_id = library_id
        self.start_page = start_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.doc_year is not None:
            result['docYear'] = self.doc_year
        if self.end_page is not None:
            result['endPage'] = self.end_page
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.start_page is not None:
            result['startPage'] = self.start_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('docYear') is not None:
            self.doc_year = m.get('docYear')
        if m.get('endPage') is not None:
            self.end_page = m.get('endPage')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('startPage') is not None:
            self.start_page = m.get('startPage')
        return self


class CreateAnnualDocSummaryTaskRequest(TeaModel):
    def __init__(
        self,
        ana_years: List[int] = None,
        doc_infos: List[CreateAnnualDocSummaryTaskRequestDocInfos] = None,
        enable_table: bool = None,
        instruction: str = None,
        model_id: str = None,
    ):
        # This parameter is required.
        self.ana_years = ana_years
        # This parameter is required.
        self.doc_infos = doc_infos
        self.enable_table = enable_table
        self.instruction = instruction
        # This parameter is required.
        self.model_id = model_id

    def validate(self):
        if self.doc_infos:
            for k in self.doc_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ana_years is not None:
            result['anaYears'] = self.ana_years
        result['docInfos'] = []
        if self.doc_infos is not None:
            for k in self.doc_infos:
                result['docInfos'].append(k.to_map() if k else None)
        if self.enable_table is not None:
            result['enableTable'] = self.enable_table
        if self.instruction is not None:
            result['instruction'] = self.instruction
        if self.model_id is not None:
            result['modelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anaYears') is not None:
            self.ana_years = m.get('anaYears')
        self.doc_infos = []
        if m.get('docInfos') is not None:
            for k in m.get('docInfos'):
                temp_model = CreateAnnualDocSummaryTaskRequestDocInfos()
                self.doc_infos.append(temp_model.from_map(k))
        if m.get('enableTable') is not None:
            self.enable_table = m.get('enableTable')
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        return self


class CreateAnnualDocSummaryTaskResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class CreateAnnualDocSummaryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAnnualDocSummaryTaskResponseBody = None,
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
            temp_model = CreateAnnualDocSummaryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDialogRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        enable_library: bool = None,
        meta_data: Dict[str, Any] = None,
        play_code: str = None,
        qa_library_list: List[str] = None,
        request_id: str = None,
        self_directed: bool = None,
    ):
        # This parameter is required.
        self.channel = channel
        self.enable_library = enable_library
        self.meta_data = meta_data
        # This parameter is required.
        self.play_code = play_code
        self.qa_library_list = qa_library_list
        # This parameter is required.
        self.request_id = request_id
        self.self_directed = self_directed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.enable_library is not None:
            result['enableLibrary'] = self.enable_library
        if self.meta_data is not None:
            result['metaData'] = self.meta_data
        if self.play_code is not None:
            result['playCode'] = self.play_code
        if self.qa_library_list is not None:
            result['qaLibraryList'] = self.qa_library_list
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.self_directed is not None:
            result['selfDirected'] = self.self_directed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('enableLibrary') is not None:
            self.enable_library = m.get('enableLibrary')
        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')
        if m.get('playCode') is not None:
            self.play_code = m.get('playCode')
        if m.get('qaLibraryList') is not None:
            self.qa_library_list = m.get('qaLibraryList')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('selfDirected') is not None:
            self.self_directed = m.get('selfDirected')
        return self


class CreateDialogResponseBodyData(TeaModel):
    def __init__(
        self,
        opening_remarks: str = None,
        session_id: str = None,
    ):
        self.opening_remarks = opening_remarks
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.opening_remarks is not None:
            result['openingRemarks'] = self.opening_remarks
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('openingRemarks') is not None:
            self.opening_remarks = m.get('openingRemarks')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class CreateDialogResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: CreateDialogResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = CreateDialogResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class CreateDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDialogResponseBody = None,
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
            temp_model = CreateDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDialogAnalysisTaskRequestConversationListDialogueList(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class CreateDialogAnalysisTaskRequestConversationList(TeaModel):
    def __init__(
        self,
        dialogue_list: List[CreateDialogAnalysisTaskRequestConversationListDialogueList] = None,
    ):
        # This parameter is required.
        self.dialogue_list = dialogue_list

    def validate(self):
        if self.dialogue_list:
            for k in self.dialogue_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k in self.dialogue_list:
                result['dialogueList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k in m.get('dialogueList'):
                temp_model = CreateDialogAnalysisTaskRequestConversationListDialogueList()
                self.dialogue_list.append(temp_model.from_map(k))
        return self


class CreateDialogAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        analysis_nodes: List[str] = None,
        conversation_list: List[CreateDialogAnalysisTaskRequestConversationList] = None,
        meta_data: Dict[str, Any] = None,
        play_code: str = None,
        request_id: str = None,
    ):
        self.analysis_nodes = analysis_nodes
        # This parameter is required.
        self.conversation_list = conversation_list
        self.meta_data = meta_data
        # This parameter is required.
        self.play_code = play_code
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.conversation_list:
            for k in self.conversation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_nodes is not None:
            result['analysisNodes'] = self.analysis_nodes
        result['conversationList'] = []
        if self.conversation_list is not None:
            for k in self.conversation_list:
                result['conversationList'].append(k.to_map() if k else None)
        if self.meta_data is not None:
            result['metaData'] = self.meta_data
        if self.play_code is not None:
            result['playCode'] = self.play_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisNodes') is not None:
            self.analysis_nodes = m.get('analysisNodes')
        self.conversation_list = []
        if m.get('conversationList') is not None:
            for k in m.get('conversationList'):
                temp_model = CreateDialogAnalysisTaskRequestConversationList()
                self.conversation_list.append(temp_model.from_map(k))
        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')
        if m.get('playCode') is not None:
            self.play_code = m.get('playCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateDialogAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: List[str] = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class CreateDialogAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDialogAnalysisTaskResponseBody = None,
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
            temp_model = CreateDialogAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDocsSummaryTaskRequestDocInfos(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        end_page: int = None,
        library_id: str = None,
        start_page: int = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        self.end_page = end_page
        # This parameter is required.
        self.library_id = library_id
        self.start_page = start_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.end_page is not None:
            result['endPage'] = self.end_page
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.start_page is not None:
            result['startPage'] = self.start_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('endPage') is not None:
            self.end_page = m.get('endPage')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('startPage') is not None:
            self.start_page = m.get('startPage')
        return self


class CreateDocsSummaryTaskRequest(TeaModel):
    def __init__(
        self,
        doc_infos: List[CreateDocsSummaryTaskRequestDocInfos] = None,
        enable_table: bool = None,
        instruction: str = None,
        model_id: str = None,
    ):
        # This parameter is required.
        self.doc_infos = doc_infos
        self.enable_table = enable_table
        self.instruction = instruction
        # This parameter is required.
        self.model_id = model_id

    def validate(self):
        if self.doc_infos:
            for k in self.doc_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['docInfos'] = []
        if self.doc_infos is not None:
            for k in self.doc_infos:
                result['docInfos'].append(k.to_map() if k else None)
        if self.enable_table is not None:
            result['enableTable'] = self.enable_table
        if self.instruction is not None:
            result['instruction'] = self.instruction
        if self.model_id is not None:
            result['modelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.doc_infos = []
        if m.get('docInfos') is not None:
            for k in m.get('docInfos'):
                temp_model = CreateDocsSummaryTaskRequestDocInfos()
                self.doc_infos.append(temp_model.from_map(k))
        if m.get('enableTable') is not None:
            self.enable_table = m.get('enableTable')
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        return self


class CreateDocsSummaryTaskResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class CreateDocsSummaryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDocsSummaryTaskResponseBody = None,
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
            temp_model = CreateDocsSummaryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFinReportSummaryTaskRequest(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        enable_table: bool = None,
        end_page: int = None,
        instruction: str = None,
        library_id: str = None,
        model_id: str = None,
        start_page: int = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        # This parameter is required.
        self.enable_table = enable_table
        self.end_page = end_page
        self.instruction = instruction
        # This parameter is required.
        self.library_id = library_id
        # This parameter is required.
        self.model_id = model_id
        self.start_page = start_page
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.enable_table is not None:
            result['enableTable'] = self.enable_table
        if self.end_page is not None:
            result['endPage'] = self.end_page
        if self.instruction is not None:
            result['instruction'] = self.instruction
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.start_page is not None:
            result['startPage'] = self.start_page
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('enableTable') is not None:
            self.enable_table = m.get('enableTable')
        if m.get('endPage') is not None:
            self.end_page = m.get('endPage')
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('startPage') is not None:
            self.start_page = m.get('startPage')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class CreateFinReportSummaryTaskResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class CreateFinReportSummaryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFinReportSummaryTaskResponseBody = None,
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
            temp_model = CreateFinReportSummaryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLibraryRequestIndexSettingChunkStrategy(TeaModel):
    def __init__(
        self,
        doc_tree_split: bool = None,
        doc_tree_split_size: int = None,
        enhance_graph: bool = None,
        enhance_table: bool = None,
        overlap: int = None,
        sentence_split: bool = None,
        sentence_split_size: int = None,
        size: int = None,
        split: bool = None,
    ):
        self.doc_tree_split = doc_tree_split
        self.doc_tree_split_size = doc_tree_split_size
        self.enhance_graph = enhance_graph
        self.enhance_table = enhance_table
        self.overlap = overlap
        self.sentence_split = sentence_split
        self.sentence_split_size = sentence_split_size
        self.size = size
        self.split = split

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_tree_split is not None:
            result['docTreeSplit'] = self.doc_tree_split
        if self.doc_tree_split_size is not None:
            result['docTreeSplitSize'] = self.doc_tree_split_size
        if self.enhance_graph is not None:
            result['enhanceGraph'] = self.enhance_graph
        if self.enhance_table is not None:
            result['enhanceTable'] = self.enhance_table
        if self.overlap is not None:
            result['overlap'] = self.overlap
        if self.sentence_split is not None:
            result['sentenceSplit'] = self.sentence_split
        if self.sentence_split_size is not None:
            result['sentenceSplitSize'] = self.sentence_split_size
        if self.size is not None:
            result['size'] = self.size
        if self.split is not None:
            result['split'] = self.split
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docTreeSplit') is not None:
            self.doc_tree_split = m.get('docTreeSplit')
        if m.get('docTreeSplitSize') is not None:
            self.doc_tree_split_size = m.get('docTreeSplitSize')
        if m.get('enhanceGraph') is not None:
            self.enhance_graph = m.get('enhanceGraph')
        if m.get('enhanceTable') is not None:
            self.enhance_table = m.get('enhanceTable')
        if m.get('overlap') is not None:
            self.overlap = m.get('overlap')
        if m.get('sentenceSplit') is not None:
            self.sentence_split = m.get('sentenceSplit')
        if m.get('sentenceSplitSize') is not None:
            self.sentence_split_size = m.get('sentenceSplitSize')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('split') is not None:
            self.split = m.get('split')
        return self


class CreateLibraryRequestIndexSettingModelConfig(TeaModel):
    def __init__(
        self,
        temperature: float = None,
        top_p: float = None,
    ):
        self.temperature = temperature
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.temperature is not None:
            result['temperature'] = self.temperature
        if self.top_p is not None:
            result['topP'] = self.top_p
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        if m.get('topP') is not None:
            self.top_p = m.get('topP')
        return self


class CreateLibraryRequestIndexSettingQueryEnhancer(TeaModel):
    def __init__(
        self,
        enable_follow_up: bool = None,
        enable_multi_query: bool = None,
        enable_open_qa: bool = None,
        enable_query_rewrite: bool = None,
        enable_session: bool = None,
        local_knowledge_id: str = None,
        with_document_reference: bool = None,
    ):
        self.enable_follow_up = enable_follow_up
        self.enable_multi_query = enable_multi_query
        self.enable_open_qa = enable_open_qa
        self.enable_query_rewrite = enable_query_rewrite
        self.enable_session = enable_session
        self.local_knowledge_id = local_knowledge_id
        self.with_document_reference = with_document_reference

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_follow_up is not None:
            result['enableFollowUp'] = self.enable_follow_up
        if self.enable_multi_query is not None:
            result['enableMultiQuery'] = self.enable_multi_query
        if self.enable_open_qa is not None:
            result['enableOpenQa'] = self.enable_open_qa
        if self.enable_query_rewrite is not None:
            result['enableQueryRewrite'] = self.enable_query_rewrite
        if self.enable_session is not None:
            result['enableSession'] = self.enable_session
        if self.local_knowledge_id is not None:
            result['localKnowledgeId'] = self.local_knowledge_id
        if self.with_document_reference is not None:
            result['withDocumentReference'] = self.with_document_reference
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableFollowUp') is not None:
            self.enable_follow_up = m.get('enableFollowUp')
        if m.get('enableMultiQuery') is not None:
            self.enable_multi_query = m.get('enableMultiQuery')
        if m.get('enableOpenQa') is not None:
            self.enable_open_qa = m.get('enableOpenQa')
        if m.get('enableQueryRewrite') is not None:
            self.enable_query_rewrite = m.get('enableQueryRewrite')
        if m.get('enableSession') is not None:
            self.enable_session = m.get('enableSession')
        if m.get('localKnowledgeId') is not None:
            self.local_knowledge_id = m.get('localKnowledgeId')
        if m.get('withDocumentReference') is not None:
            self.with_document_reference = m.get('withDocumentReference')
        return self


class CreateLibraryRequestIndexSettingRecallStrategy(TeaModel):
    def __init__(
        self,
        document_rank_type: str = None,
        limit: int = None,
    ):
        self.document_rank_type = document_rank_type
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_rank_type is not None:
            result['documentRankType'] = self.document_rank_type
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentRankType') is not None:
            self.document_rank_type = m.get('documentRankType')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class CreateLibraryRequestIndexSettingTextIndexSetting(TeaModel):
    def __init__(
        self,
        category: str = None,
        enable: bool = None,
        index_analyzer: str = None,
        rank_threshold: float = None,
        search_analyzer: str = None,
        top_k: int = None,
    ):
        self.category = category
        self.enable = enable
        self.index_analyzer = index_analyzer
        self.rank_threshold = rank_threshold
        self.search_analyzer = search_analyzer
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.enable is not None:
            result['enable'] = self.enable
        if self.index_analyzer is not None:
            result['indexAnalyzer'] = self.index_analyzer
        if self.rank_threshold is not None:
            result['rankThreshold'] = self.rank_threshold
        if self.search_analyzer is not None:
            result['searchAnalyzer'] = self.search_analyzer
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('indexAnalyzer') is not None:
            self.index_analyzer = m.get('indexAnalyzer')
        if m.get('rankThreshold') is not None:
            self.rank_threshold = m.get('rankThreshold')
        if m.get('searchAnalyzer') is not None:
            self.search_analyzer = m.get('searchAnalyzer')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class CreateLibraryRequestIndexSettingVectorIndexSetting(TeaModel):
    def __init__(
        self,
        category: str = None,
        embedding_type: str = None,
        enable: bool = None,
        rank_threshold: float = None,
        top_k: int = None,
    ):
        self.category = category
        self.embedding_type = embedding_type
        self.enable = enable
        self.rank_threshold = rank_threshold
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.embedding_type is not None:
            result['embeddingType'] = self.embedding_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.rank_threshold is not None:
            result['rankThreshold'] = self.rank_threshold
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('embeddingType') is not None:
            self.embedding_type = m.get('embeddingType')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('rankThreshold') is not None:
            self.rank_threshold = m.get('rankThreshold')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class CreateLibraryRequestIndexSetting(TeaModel):
    def __init__(
        self,
        chunk_strategy: CreateLibraryRequestIndexSettingChunkStrategy = None,
        model_config: CreateLibraryRequestIndexSettingModelConfig = None,
        prompt_role_style: str = None,
        query_enhancer: CreateLibraryRequestIndexSettingQueryEnhancer = None,
        recall_strategy: CreateLibraryRequestIndexSettingRecallStrategy = None,
        text_index_setting: CreateLibraryRequestIndexSettingTextIndexSetting = None,
        vector_index_setting: CreateLibraryRequestIndexSettingVectorIndexSetting = None,
    ):
        self.chunk_strategy = chunk_strategy
        self.model_config = model_config
        self.prompt_role_style = prompt_role_style
        self.query_enhancer = query_enhancer
        self.recall_strategy = recall_strategy
        self.text_index_setting = text_index_setting
        self.vector_index_setting = vector_index_setting

    def validate(self):
        if self.chunk_strategy:
            self.chunk_strategy.validate()
        if self.model_config:
            self.model_config.validate()
        if self.query_enhancer:
            self.query_enhancer.validate()
        if self.recall_strategy:
            self.recall_strategy.validate()
        if self.text_index_setting:
            self.text_index_setting.validate()
        if self.vector_index_setting:
            self.vector_index_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_strategy is not None:
            result['chunkStrategy'] = self.chunk_strategy.to_map()
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.prompt_role_style is not None:
            result['promptRoleStyle'] = self.prompt_role_style
        if self.query_enhancer is not None:
            result['queryEnhancer'] = self.query_enhancer.to_map()
        if self.recall_strategy is not None:
            result['recallStrategy'] = self.recall_strategy.to_map()
        if self.text_index_setting is not None:
            result['textIndexSetting'] = self.text_index_setting.to_map()
        if self.vector_index_setting is not None:
            result['vectorIndexSetting'] = self.vector_index_setting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkStrategy') is not None:
            temp_model = CreateLibraryRequestIndexSettingChunkStrategy()
            self.chunk_strategy = temp_model.from_map(m['chunkStrategy'])
        if m.get('modelConfig') is not None:
            temp_model = CreateLibraryRequestIndexSettingModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('promptRoleStyle') is not None:
            self.prompt_role_style = m.get('promptRoleStyle')
        if m.get('queryEnhancer') is not None:
            temp_model = CreateLibraryRequestIndexSettingQueryEnhancer()
            self.query_enhancer = temp_model.from_map(m['queryEnhancer'])
        if m.get('recallStrategy') is not None:
            temp_model = CreateLibraryRequestIndexSettingRecallStrategy()
            self.recall_strategy = temp_model.from_map(m['recallStrategy'])
        if m.get('textIndexSetting') is not None:
            temp_model = CreateLibraryRequestIndexSettingTextIndexSetting()
            self.text_index_setting = temp_model.from_map(m['textIndexSetting'])
        if m.get('vectorIndexSetting') is not None:
            temp_model = CreateLibraryRequestIndexSettingVectorIndexSetting()
            self.vector_index_setting = temp_model.from_map(m['vectorIndexSetting'])
        return self


class CreateLibraryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        index_setting: CreateLibraryRequestIndexSetting = None,
        library_name: str = None,
    ):
        # This parameter is required.
        self.description = description
        self.index_setting = index_setting
        # This parameter is required.
        self.library_name = library_name

    def validate(self):
        if self.index_setting:
            self.index_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.index_setting is not None:
            result['indexSetting'] = self.index_setting.to_map()
        if self.library_name is not None:
            result['libraryName'] = self.library_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('indexSetting') is not None:
            temp_model = CreateLibraryRequestIndexSetting()
            self.index_setting = temp_model.from_map(m['indexSetting'])
        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')
        return self


class CreateLibraryResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class CreateLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLibraryResponseBody = None,
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
            temp_model = CreateLibraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePdfTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        knowledge: str = None,
        library_id: str = None,
        model_id: str = None,
        translate_to: str = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        self.knowledge = knowledge
        # This parameter is required.
        self.library_id = library_id
        # This parameter is required.
        self.model_id = model_id
        self.translate_to = translate_to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.knowledge is not None:
            result['knowledge'] = self.knowledge
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.translate_to is not None:
            result['translateTo'] = self.translate_to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('knowledge') is not None:
            self.knowledge = m.get('knowledge')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('translateTo') is not None:
            self.translate_to = m.get('translateTo')
        return self


class CreatePdfTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class CreatePdfTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePdfTranslateTaskResponseBody = None,
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
            temp_model = CreatePdfTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePredefinedDocumentRequestChunks(TeaModel):
    def __init__(
        self,
        chunk_meta: Dict[str, Any] = None,
        chunk_order: int = None,
        chunk_text: str = None,
        chunk_type: str = None,
    ):
        self.chunk_meta = chunk_meta
        self.chunk_order = chunk_order
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta
        if self.chunk_order is not None:
            result['chunkOrder'] = self.chunk_order
        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text
        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')
        if m.get('chunkOrder') is not None:
            self.chunk_order = m.get('chunkOrder')
        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')
        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')
        return self


class CreatePredefinedDocumentRequest(TeaModel):
    def __init__(
        self,
        chunks: List[CreatePredefinedDocumentRequestChunks] = None,
        library_id: str = None,
        metadata: Dict[str, Any] = None,
        title: str = None,
    ):
        self.chunks = chunks
        self.library_id = library_id
        self.metadata = metadata
        self.title = title

    def validate(self):
        if self.chunks:
            for k in self.chunks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['chunks'] = []
        if self.chunks is not None:
            for k in self.chunks:
                result['chunks'].append(k.to_map() if k else None)
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('chunks') is not None:
            for k in m.get('chunks'):
                temp_model = CreatePredefinedDocumentRequestChunks()
                self.chunks.append(temp_model.from_map(k))
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CreatePredefinedDocumentResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class CreatePredefinedDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePredefinedDocumentResponseBody = None,
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
            temp_model = CreatePredefinedDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQualityCheckTaskRequestConversationListDialogueList(TeaModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        end: int = None,
        role: str = None,
        type: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        # This parameter is required.
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.end = end
        # This parameter is required.
        self.role = role
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['begin'] = self.begin
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.content is not None:
            result['content'] = self.content
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id
        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type
        if self.end is not None:
            result['end'] = self.end
        if self.role is not None:
            result['role'] = self.role
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('begin') is not None:
            self.begin = m.get('begin')
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')
        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateQualityCheckTaskRequestConversationList(TeaModel):
    def __init__(
        self,
        call_type: str = None,
        customer_id: str = None,
        customer_name: str = None,
        customer_service_id: str = None,
        customer_service_name: str = None,
        dialogue_list: List[CreateQualityCheckTaskRequestConversationListDialogueList] = None,
        gmt_service: str = None,
    ):
        self.call_type = call_type
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_service_id = customer_service_id
        self.customer_service_name = customer_service_name
        # This parameter is required.
        self.dialogue_list = dialogue_list
        self.gmt_service = gmt_service

    def validate(self):
        if self.dialogue_list:
            for k in self.dialogue_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_type is not None:
            result['callType'] = self.call_type
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.customer_name is not None:
            result['customerName'] = self.customer_name
        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id
        if self.customer_service_name is not None:
            result['customerServiceName'] = self.customer_service_name
        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k in self.dialogue_list:
                result['dialogueList'].append(k.to_map() if k else None)
        if self.gmt_service is not None:
            result['gmtService'] = self.gmt_service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callType') is not None:
            self.call_type = m.get('callType')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('customerName') is not None:
            self.customer_name = m.get('customerName')
        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')
        if m.get('customerServiceName') is not None:
            self.customer_service_name = m.get('customerServiceName')
        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k in m.get('dialogueList'):
                temp_model = CreateQualityCheckTaskRequestConversationListDialogueList()
                self.dialogue_list.append(temp_model.from_map(k))
        if m.get('gmtService') is not None:
            self.gmt_service = m.get('gmtService')
        return self


class CreateQualityCheckTaskRequest(TeaModel):
    def __init__(
        self,
        conversation_list: CreateQualityCheckTaskRequestConversationList = None,
        gmt_service: str = None,
        meta_data: Dict[str, str] = None,
        quality_group: List[str] = None,
        request_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.conversation_list = conversation_list
        # This parameter is required.
        self.gmt_service = gmt_service
        self.meta_data = meta_data
        self.quality_group = quality_group
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.conversation_list:
            self.conversation_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_list is not None:
            result['conversationList'] = self.conversation_list.to_map()
        if self.gmt_service is not None:
            result['gmtService'] = self.gmt_service
        if self.meta_data is not None:
            result['metaData'] = self.meta_data
        if self.quality_group is not None:
            result['qualityGroup'] = self.quality_group
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conversationList') is not None:
            temp_model = CreateQualityCheckTaskRequestConversationList()
            self.conversation_list = temp_model.from_map(m['conversationList'])
        if m.get('gmtService') is not None:
            self.gmt_service = m.get('gmtService')
        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')
        if m.get('qualityGroup') is not None:
            self.quality_group = m.get('qualityGroup')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateQualityCheckTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # taskId
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateQualityCheckTaskResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: CreateQualityCheckTaskResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = CreateQualityCheckTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class CreateQualityCheckTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQualityCheckTaskResponseBody = None,
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
            temp_model = CreateQualityCheckTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDocumentRequest(TeaModel):
    def __init__(
        self,
        doc_ids: List[str] = None,
        library_id: str = None,
    ):
        # This parameter is required.
        self.doc_ids = doc_ids
        # This parameter is required.
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_ids is not None:
            result['docIds'] = self.doc_ids
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docIds') is not None:
            self.doc_ids = m.get('docIds')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        return self


class DeleteDocumentResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: bool = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class DeleteDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDocumentResponseBody = None,
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
            temp_model = DeleteDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLibraryRequest(TeaModel):
    def __init__(
        self,
        library_id: str = None,
    ):
        # This parameter is required.
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        return self


class DeleteLibraryResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLibraryResponseBody = None,
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
            temp_model = DeleteLibraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvictTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class EvictTaskResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class EvictTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EvictTaskResponseBody = None,
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
            temp_model = EvictTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenDocQaResultRequest(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        library_id: str = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        # This parameter is required.
        self.library_id = library_id
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GenDocQaResultResponseBodyDataParseQaResults(TeaModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
    ):
        self.answer = answer
        self.question = question

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['answer'] = self.answer
        if self.question is not None:
            result['question'] = self.question
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')
        if m.get('question') is not None:
            self.question = m.get('question')
        return self


class GenDocQaResultResponseBodyData(TeaModel):
    def __init__(
        self,
        current_status: str = None,
        doc_id: str = None,
        library_id: str = None,
        parse_qa_results: List[GenDocQaResultResponseBodyDataParseQaResults] = None,
    ):
        self.current_status = current_status
        self.doc_id = doc_id
        self.library_id = library_id
        self.parse_qa_results = parse_qa_results

    def validate(self):
        if self.parse_qa_results:
            for k in self.parse_qa_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_status is not None:
            result['currentStatus'] = self.current_status
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        result['parseQaResults'] = []
        if self.parse_qa_results is not None:
            for k in self.parse_qa_results:
                result['parseQaResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentStatus') is not None:
            self.current_status = m.get('currentStatus')
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        self.parse_qa_results = []
        if m.get('parseQaResults') is not None:
            for k in m.get('parseQaResults'):
                temp_model = GenDocQaResultResponseBodyDataParseQaResults()
                self.parse_qa_results.append(temp_model.from_map(k))
        return self


class GenDocQaResultResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GenDocQaResultResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GenDocQaResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GenDocQaResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenDocQaResultResponseBody = None,
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
            temp_model = GenDocQaResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        embedding_type_list: List[Dict[str, str]] = None,
        frontend_config: Dict[str, bool] = None,
        library_document_status_list: List[Dict[str, str]] = None,
        llm_helper_type_list: List[Dict[str, str]] = None,
        text_index_category_list: List[str] = None,
        vector_index_category_list: List[str] = None,
    ):
        self.embedding_type_list = embedding_type_list
        self.frontend_config = frontend_config
        self.library_document_status_list = library_document_status_list
        self.llm_helper_type_list = llm_helper_type_list
        self.text_index_category_list = text_index_category_list
        self.vector_index_category_list = vector_index_category_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.embedding_type_list is not None:
            result['embeddingTypeList'] = self.embedding_type_list
        if self.frontend_config is not None:
            result['frontendConfig'] = self.frontend_config
        if self.library_document_status_list is not None:
            result['libraryDocumentStatusList'] = self.library_document_status_list
        if self.llm_helper_type_list is not None:
            result['llmHelperTypeList'] = self.llm_helper_type_list
        if self.text_index_category_list is not None:
            result['textIndexCategoryList'] = self.text_index_category_list
        if self.vector_index_category_list is not None:
            result['vectorIndexCategoryList'] = self.vector_index_category_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('embeddingTypeList') is not None:
            self.embedding_type_list = m.get('embeddingTypeList')
        if m.get('frontendConfig') is not None:
            self.frontend_config = m.get('frontendConfig')
        if m.get('libraryDocumentStatusList') is not None:
            self.library_document_status_list = m.get('libraryDocumentStatusList')
        if m.get('llmHelperTypeList') is not None:
            self.llm_helper_type_list = m.get('llmHelperTypeList')
        if m.get('textIndexCategoryList') is not None:
            self.text_index_category_list = m.get('textIndexCategoryList')
        if m.get('vectorIndexCategoryList') is not None:
            self.vector_index_category_list = m.get('vectorIndexCategoryList')
        return self


class GetAppConfigResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetAppConfigResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetAppConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetAppConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppConfigResponseBody = None,
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
            temp_model = GetAppConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatQuestionRespRequest(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.batch_id = batch_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['batchId'] = self.batch_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class GetChatQuestionRespResponseBodyDataQuestionList(TeaModel):
    def __init__(
        self,
        content: str = None,
        gmt_create: str = None,
        ori_content: str = None,
        reply: str = None,
        session_id: str = None,
        type: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.content = content
        self.gmt_create = gmt_create
        self.ori_content = ori_content
        self.reply = reply
        self.session_id = session_id
        self.type = type
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.ori_content is not None:
            result['oriContent'] = self.ori_content
        if self.reply is not None:
            result['reply'] = self.reply
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('oriContent') is not None:
            self.ori_content = m.get('oriContent')
        if m.get('reply') is not None:
            self.reply = m.get('reply')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class GetChatQuestionRespResponseBodyData(TeaModel):
    def __init__(
        self,
        current_state: str = None,
        question_list: List[GetChatQuestionRespResponseBodyDataQuestionList] = None,
    ):
        self.current_state = current_state
        self.question_list = question_list

    def validate(self):
        if self.question_list:
            for k in self.question_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_state is not None:
            result['currentState'] = self.current_state
        result['questionList'] = []
        if self.question_list is not None:
            for k in self.question_list:
                result['questionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentState') is not None:
            self.current_state = m.get('currentState')
        self.question_list = []
        if m.get('questionList') is not None:
            for k in m.get('questionList'):
                temp_model = GetChatQuestionRespResponseBodyDataQuestionList()
                self.question_list.append(temp_model.from_map(k))
        return self


class GetChatQuestionRespResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetChatQuestionRespResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetChatQuestionRespResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetChatQuestionRespResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatQuestionRespResponseBody = None,
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
            temp_model = GetChatQuestionRespResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDialogAnalysisResultRequest(TeaModel):
    def __init__(
        self,
        asc: bool = None,
        end_time: str = None,
        session_ids: List[str] = None,
        start_time: str = None,
        use_url: bool = None,
    ):
        self.asc = asc
        self.end_time = end_time
        self.session_ids = session_ids
        self.start_time = start_time
        self.use_url = use_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc is not None:
            result['asc'] = self.asc
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.session_ids is not None:
            result['sessionIds'] = self.session_ids
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.use_url is not None:
            result['useUrl'] = self.use_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asc') is not None:
            self.asc = m.get('asc')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('sessionIds') is not None:
            self.session_ids = m.get('sessionIds')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('useUrl') is not None:
            self.use_url = m.get('useUrl')
        return self


class GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisRespDialogLabels(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisResp(TeaModel):
    def __init__(
        self,
        dialog_exec_plan: str = None,
        dialog_labels: List[GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisRespDialogLabels] = None,
        dialog_open_analysis: Dict[str, Any] = None,
        dialog_process_analysis: Dict[str, Any] = None,
        dialog_sop: str = None,
        dialog_summary: str = None,
    ):
        self.dialog_exec_plan = dialog_exec_plan
        self.dialog_labels = dialog_labels
        self.dialog_open_analysis = dialog_open_analysis
        self.dialog_process_analysis = dialog_process_analysis
        self.dialog_sop = dialog_sop
        self.dialog_summary = dialog_summary

    def validate(self):
        if self.dialog_labels:
            for k in self.dialog_labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_exec_plan is not None:
            result['dialogExecPlan'] = self.dialog_exec_plan
        result['dialogLabels'] = []
        if self.dialog_labels is not None:
            for k in self.dialog_labels:
                result['dialogLabels'].append(k.to_map() if k else None)
        if self.dialog_open_analysis is not None:
            result['dialogOpenAnalysis'] = self.dialog_open_analysis
        if self.dialog_process_analysis is not None:
            result['dialogProcessAnalysis'] = self.dialog_process_analysis
        if self.dialog_sop is not None:
            result['dialogSop'] = self.dialog_sop
        if self.dialog_summary is not None:
            result['dialogSummary'] = self.dialog_summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dialogExecPlan') is not None:
            self.dialog_exec_plan = m.get('dialogExecPlan')
        self.dialog_labels = []
        if m.get('dialogLabels') is not None:
            for k in m.get('dialogLabels'):
                temp_model = GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisRespDialogLabels()
                self.dialog_labels.append(temp_model.from_map(k))
        if m.get('dialogOpenAnalysis') is not None:
            self.dialog_open_analysis = m.get('dialogOpenAnalysis')
        if m.get('dialogProcessAnalysis') is not None:
            self.dialog_process_analysis = m.get('dialogProcessAnalysis')
        if m.get('dialogSop') is not None:
            self.dialog_sop = m.get('dialogSop')
        if m.get('dialogSummary') is not None:
            self.dialog_summary = m.get('dialogSummary')
        return self


class GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespList(TeaModel):
    def __init__(
        self,
        analysis_resp: GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisResp = None,
        gmt_create: str = None,
        oss_url: str = None,
        session_id: str = None,
        status: str = None,
    ):
        self.analysis_resp = analysis_resp
        self.gmt_create = gmt_create
        self.oss_url = oss_url
        self.session_id = session_id
        self.status = status

    def validate(self):
        if self.analysis_resp:
            self.analysis_resp.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_resp is not None:
            result['analysisResp'] = self.analysis_resp.to_map()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.oss_url is not None:
            result['ossUrl'] = self.oss_url
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisResp') is not None:
            temp_model = GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisResp()
            self.analysis_resp = temp_model.from_map(m['analysisResp'])
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('ossUrl') is not None:
            self.oss_url = m.get('ossUrl')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetDialogAnalysisResultResponseBodyData(TeaModel):
    def __init__(
        self,
        dialog_analysis_resp_list: List[GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespList] = None,
    ):
        self.dialog_analysis_resp_list = dialog_analysis_resp_list

    def validate(self):
        if self.dialog_analysis_resp_list:
            for k in self.dialog_analysis_resp_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dialogAnalysisRespList'] = []
        if self.dialog_analysis_resp_list is not None:
            for k in self.dialog_analysis_resp_list:
                result['dialogAnalysisRespList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialog_analysis_resp_list = []
        if m.get('dialogAnalysisRespList') is not None:
            for k in m.get('dialogAnalysisRespList'):
                temp_model = GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespList()
                self.dialog_analysis_resp_list.append(temp_model.from_map(k))
        return self


class GetDialogAnalysisResultResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetDialogAnalysisResultResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetDialogAnalysisResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetDialogAnalysisResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDialogAnalysisResultResponseBody = None,
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
            temp_model = GetDialogAnalysisResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDialogDetailRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class GetDialogDetailResponseBodyDataDialogueList(TeaModel):
    def __init__(
        self,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        hang_up_dialog: bool = None,
        id: int = None,
        intent_code: str = None,
        intent_name: str = None,
        role: str = None,
        type: str = None,
    ):
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.hang_up_dialog = hang_up_dialog
        self.id = id
        self.intent_code = intent_code
        self.intent_name = intent_name
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id
        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type
        if self.hang_up_dialog is not None:
            result['hangUpDialog'] = self.hang_up_dialog
        if self.id is not None:
            result['id'] = self.id
        if self.intent_code is not None:
            result['intentCode'] = self.intent_code
        if self.intent_name is not None:
            result['intentName'] = self.intent_name
        if self.role is not None:
            result['role'] = self.role
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')
        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')
        if m.get('hangUpDialog') is not None:
            self.hang_up_dialog = m.get('hangUpDialog')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('intentCode') is not None:
            self.intent_code = m.get('intentCode')
        if m.get('intentName') is not None:
            self.intent_name = m.get('intentName')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetDialogDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        dialogue_list: List[GetDialogDetailResponseBodyDataDialogueList] = None,
        gmt_create: str = None,
        status: str = None,
        total_dialog_turns: int = None,
        valid_dialog_turns: int = None,
    ):
        self.dialogue_list = dialogue_list
        self.gmt_create = gmt_create
        self.status = status
        self.total_dialog_turns = total_dialog_turns
        self.valid_dialog_turns = valid_dialog_turns

    def validate(self):
        if self.dialogue_list:
            for k in self.dialogue_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k in self.dialogue_list:
                result['dialogueList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.status is not None:
            result['status'] = self.status
        if self.total_dialog_turns is not None:
            result['totalDialogTurns'] = self.total_dialog_turns
        if self.valid_dialog_turns is not None:
            result['validDialogTurns'] = self.valid_dialog_turns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k in m.get('dialogueList'):
                temp_model = GetDialogDetailResponseBodyDataDialogueList()
                self.dialogue_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('totalDialogTurns') is not None:
            self.total_dialog_turns = m.get('totalDialogTurns')
        if m.get('validDialogTurns') is not None:
            self.valid_dialog_turns = m.get('validDialogTurns')
        return self


class GetDialogDetailResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetDialogDetailResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetDialogDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetDialogDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDialogDetailResponseBody = None,
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
            temp_model = GetDialogDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDialogLogRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        session_id: str = None,
    ):
        self.id = id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class GetDialogLogResponseBodyDataHitIntentionList(TeaModel):
    def __init__(
        self,
        description: str = None,
        intention_name: str = None,
        intention_script: str = None,
    ):
        self.description = description
        self.intention_name = intention_name
        self.intention_script = intention_script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.intention_name is not None:
            result['intentionName'] = self.intention_name
        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('intentionName') is not None:
            self.intention_name = m.get('intentionName')
        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')
        return self


class GetDialogLogResponseBodyDataIntentionList(TeaModel):
    def __init__(
        self,
        description: str = None,
        intention_name: str = None,
        intention_script: str = None,
    ):
        self.description = description
        self.intention_name = intention_name
        self.intention_script = intention_script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.intention_name is not None:
            result['intentionName'] = self.intention_name
        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('intentionName') is not None:
            self.intention_name = m.get('intentionName')
        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')
        return self


class GetDialogLogResponseBodyData(TeaModel):
    def __init__(
        self,
        analysis_process: str = None,
        conversation_list: str = None,
        hit_intention_list: List[GetDialogLogResponseBodyDataHitIntentionList] = None,
        intention_list: List[GetDialogLogResponseBodyDataIntentionList] = None,
        model_cost_time: int = None,
        recall_list: str = None,
    ):
        self.analysis_process = analysis_process
        self.conversation_list = conversation_list
        self.hit_intention_list = hit_intention_list
        self.intention_list = intention_list
        self.model_cost_time = model_cost_time
        self.recall_list = recall_list

    def validate(self):
        if self.hit_intention_list:
            for k in self.hit_intention_list:
                if k:
                    k.validate()
        if self.intention_list:
            for k in self.intention_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_process is not None:
            result['analysisProcess'] = self.analysis_process
        if self.conversation_list is not None:
            result['conversationList'] = self.conversation_list
        result['hitIntentionList'] = []
        if self.hit_intention_list is not None:
            for k in self.hit_intention_list:
                result['hitIntentionList'].append(k.to_map() if k else None)
        result['intentionList'] = []
        if self.intention_list is not None:
            for k in self.intention_list:
                result['intentionList'].append(k.to_map() if k else None)
        if self.model_cost_time is not None:
            result['modelCostTime'] = self.model_cost_time
        if self.recall_list is not None:
            result['recallList'] = self.recall_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisProcess') is not None:
            self.analysis_process = m.get('analysisProcess')
        if m.get('conversationList') is not None:
            self.conversation_list = m.get('conversationList')
        self.hit_intention_list = []
        if m.get('hitIntentionList') is not None:
            for k in m.get('hitIntentionList'):
                temp_model = GetDialogLogResponseBodyDataHitIntentionList()
                self.hit_intention_list.append(temp_model.from_map(k))
        self.intention_list = []
        if m.get('intentionList') is not None:
            for k in m.get('intentionList'):
                temp_model = GetDialogLogResponseBodyDataIntentionList()
                self.intention_list.append(temp_model.from_map(k))
        if m.get('modelCostTime') is not None:
            self.model_cost_time = m.get('modelCostTime')
        if m.get('recallList') is not None:
            self.recall_list = m.get('recallList')
        return self


class GetDialogLogResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetDialogLogResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetDialogLogResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetDialogLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDialogLogResponseBody = None,
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
            temp_model = GetDialogLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentChunkListRequest(TeaModel):
    def __init__(
        self,
        chunk_id_list: List[str] = None,
        doc_id: str = None,
        library_id: str = None,
        order: str = None,
        order_by: str = None,
        page: int = None,
        page_size: int = None,
        search_query: str = None,
    ):
        self.chunk_id_list = chunk_id_list
        # This parameter is required.
        self.doc_id = doc_id
        # This parameter is required.
        self.library_id = library_id
        self.order = order
        self.order_by = order_by
        self.page = page
        self.page_size = page_size
        self.search_query = search_query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_id_list is not None:
            result['chunkIdList'] = self.chunk_id_list
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.order is not None:
            result['order'] = self.order
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.search_query is not None:
            result['searchQuery'] = self.search_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkIdList') is not None:
            self.chunk_id_list = m.get('chunkIdList')
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')
        return self


class GetDocumentChunkListResponseBodyDataRecordsPos(TeaModel):
    def __init__(
        self,
        axis_array: List[float] = None,
        page: int = None,
        text_highlight_area: List[int] = None,
    ):
        self.axis_array = axis_array
        self.page = page
        self.text_highlight_area = text_highlight_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.axis_array is not None:
            result['axisArray'] = self.axis_array
        if self.page is not None:
            result['page'] = self.page
        if self.text_highlight_area is not None:
            result['textHighlightArea'] = self.text_highlight_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('axisArray') is not None:
            self.axis_array = m.get('axisArray')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('textHighlightArea') is not None:
            self.text_highlight_area = m.get('textHighlightArea')
        return self


class GetDocumentChunkListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_meta: Dict[str, Any] = None,
        chunk_oss_url: str = None,
        chunk_text: str = None,
        chunk_type: str = None,
        doc_id: str = None,
        file_type: str = None,
        library_id: str = None,
        library_name: str = None,
        next_chunk_id: str = None,
        pos: List[GetDocumentChunkListResponseBodyDataRecordsPos] = None,
        pre_chunk_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.chunk_id = chunk_id
        self.chunk_meta = chunk_meta
        self.chunk_oss_url = chunk_oss_url
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type
        self.doc_id = doc_id
        self.file_type = file_type
        self.library_id = library_id
        self.library_name = library_name
        self.next_chunk_id = next_chunk_id
        self.pos = pos
        self.pre_chunk_id = pre_chunk_id
        self.score = score
        self.title = title

    def validate(self):
        if self.pos:
            for k in self.pos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id
        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta
        if self.chunk_oss_url is not None:
            result['chunkOssUrl'] = self.chunk_oss_url
        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text
        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.library_name is not None:
            result['libraryName'] = self.library_name
        if self.next_chunk_id is not None:
            result['nextChunkId'] = self.next_chunk_id
        result['pos'] = []
        if self.pos is not None:
            for k in self.pos:
                result['pos'].append(k.to_map() if k else None)
        if self.pre_chunk_id is not None:
            result['preChunkId'] = self.pre_chunk_id
        if self.score is not None:
            result['score'] = self.score
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')
        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')
        if m.get('chunkOssUrl') is not None:
            self.chunk_oss_url = m.get('chunkOssUrl')
        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')
        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')
        if m.get('nextChunkId') is not None:
            self.next_chunk_id = m.get('nextChunkId')
        self.pos = []
        if m.get('pos') is not None:
            for k in m.get('pos'):
                temp_model = GetDocumentChunkListResponseBodyDataRecordsPos()
                self.pos.append(temp_model.from_map(k))
        if m.get('preChunkId') is not None:
            self.pre_chunk_id = m.get('preChunkId')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetDocumentChunkListResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[GetDocumentChunkListResponseBodyDataRecords] = None,
        total_pages: int = None,
        total_records: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.records = records
        self.total_pages = total_pages
        self.total_records = total_records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.total_pages is not None:
            result['totalPages'] = self.total_pages
        if self.total_records is not None:
            result['totalRecords'] = self.total_records
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetDocumentChunkListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')
        if m.get('totalRecords') is not None:
            self.total_records = m.get('totalRecords')
        return self


class GetDocumentChunkListResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetDocumentChunkListResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetDocumentChunkListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetDocumentChunkListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentChunkListResponseBody = None,
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
            temp_model = GetDocumentChunkListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentListRequest(TeaModel):
    def __init__(
        self,
        library_id: str = None,
        page: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # This parameter is required.
        self.library_id = library_id
        self.page = page
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetDocumentListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        document_meta: Dict[str, Any] = None,
        file_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        library_id: str = None,
        status_code: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.document_meta = document_meta
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.library_id = library_id
        self.status_code = status_code
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.document_meta is not None:
            result['documentMeta'] = self.document_meta
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('documentMeta') is not None:
            self.document_meta = m.get('documentMeta')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetDocumentListResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[GetDocumentListResponseBodyDataRecords] = None,
        total_pages: int = None,
        total_records: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.records = records
        self.total_pages = total_pages
        self.total_records = total_records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.total_pages is not None:
            result['totalPages'] = self.total_pages
        if self.total_records is not None:
            result['totalRecords'] = self.total_records
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetDocumentListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')
        if m.get('totalRecords') is not None:
            self.total_records = m.get('totalRecords')
        return self


class GetDocumentListResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetDocumentListResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetDocumentListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetDocumentListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentListResponseBody = None,
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
            temp_model = GetDocumentListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentUrlRequest(TeaModel):
    def __init__(
        self,
        document_id: str = None,
    ):
        # This parameter is required.
        self.document_id = document_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_id is not None:
            result['documentId'] = self.document_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentId') is not None:
            self.document_id = m.get('documentId')
        return self


class GetDocumentUrlResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetDocumentUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentUrlResponseBody = None,
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
            temp_model = GetDocumentUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFilterDocumentListRequestAnd(TeaModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.boost = boost
        self.key = key
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boost is not None:
            result['boost'] = self.boost
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boost') is not None:
            self.boost = m.get('boost')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetFilterDocumentListRequestOr(TeaModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.boost = boost
        self.key = key
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boost is not None:
            result['boost'] = self.boost
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boost') is not None:
            self.boost = m.get('boost')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetFilterDocumentListRequest(TeaModel):
    def __init__(
        self,
        and_: List[GetFilterDocumentListRequestAnd] = None,
        doc_id_list: List[str] = None,
        library_id: str = None,
        or_: List[GetFilterDocumentListRequestOr] = None,
        page: int = None,
        page_size: int = None,
        status: List[str] = None,
    ):
        self.and_ = and_
        self.doc_id_list = doc_id_list
        # This parameter is required.
        self.library_id = library_id
        self.or_ = or_
        self.page = page
        self.page_size = page_size
        self.status = status

    def validate(self):
        if self.and_:
            for k in self.and_:
                if k:
                    k.validate()
        if self.or_:
            for k in self.or_:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['and'] = []
        if self.and_ is not None:
            for k in self.and_:
                result['and'].append(k.to_map() if k else None)
        if self.doc_id_list is not None:
            result['docIdList'] = self.doc_id_list
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        result['or'] = []
        if self.or_ is not None:
            for k in self.or_:
                result['or'].append(k.to_map() if k else None)
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.and_ = []
        if m.get('and') is not None:
            for k in m.get('and'):
                temp_model = GetFilterDocumentListRequestAnd()
                self.and_.append(temp_model.from_map(k))
        if m.get('docIdList') is not None:
            self.doc_id_list = m.get('docIdList')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        self.or_ = []
        if m.get('or') is not None:
            for k in m.get('or'):
                temp_model = GetFilterDocumentListRequestOr()
                self.or_.append(temp_model.from_map(k))
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetFilterDocumentListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        document_meta: Dict[str, Any] = None,
        file_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        library_id: str = None,
        status_code: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.document_meta = document_meta
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.library_id = library_id
        self.status_code = status_code
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.document_meta is not None:
            result['documentMeta'] = self.document_meta
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('documentMeta') is not None:
            self.document_meta = m.get('documentMeta')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetFilterDocumentListResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[GetFilterDocumentListResponseBodyDataRecords] = None,
        total_pages: int = None,
        total_records: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.records = records
        self.total_pages = total_pages
        self.total_records = total_records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.total_pages is not None:
            result['totalPages'] = self.total_pages
        if self.total_records is not None:
            result['totalRecords'] = self.total_records
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetFilterDocumentListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')
        if m.get('totalRecords') is not None:
            self.total_records = m.get('totalRecords')
        return self


class GetFilterDocumentListResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetFilterDocumentListResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetFilterDocumentListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetFilterDocumentListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFilterDocumentListResponseBody = None,
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
            temp_model = GetFilterDocumentListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistoryListByBizTypeRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        page: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.biz_type = biz_type
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetHistoryListByBizTypeResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        extra_message: Any = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        llm_answer: str = None,
        llm_prompt: str = None,
        llm_type: str = None,
        session_id: str = None,
        user_query: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.extra_message = extra_message
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.llm_answer = llm_answer
        self.llm_prompt = llm_prompt
        self.llm_type = llm_type
        self.session_id = session_id
        self.user_query = user_query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.extra_message is not None:
            result['extraMessage'] = self.extra_message
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.llm_answer is not None:
            result['llmAnswer'] = self.llm_answer
        if self.llm_prompt is not None:
            result['llmPrompt'] = self.llm_prompt
        if self.llm_type is not None:
            result['llmType'] = self.llm_type
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.user_query is not None:
            result['userQuery'] = self.user_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('extraMessage') is not None:
            self.extra_message = m.get('extraMessage')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('llmAnswer') is not None:
            self.llm_answer = m.get('llmAnswer')
        if m.get('llmPrompt') is not None:
            self.llm_prompt = m.get('llmPrompt')
        if m.get('llmType') is not None:
            self.llm_type = m.get('llmType')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('userQuery') is not None:
            self.user_query = m.get('userQuery')
        return self


class GetHistoryListByBizTypeResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[GetHistoryListByBizTypeResponseBodyDataRecords] = None,
        total_pages: int = None,
        total_records: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.records = records
        self.total_pages = total_pages
        self.total_records = total_records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.total_pages is not None:
            result['totalPages'] = self.total_pages
        if self.total_records is not None:
            result['totalRecords'] = self.total_records
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetHistoryListByBizTypeResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')
        if m.get('totalRecords') is not None:
            self.total_records = m.get('totalRecords')
        return self


class GetHistoryListByBizTypeResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetHistoryListByBizTypeResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetHistoryListByBizTypeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetHistoryListByBizTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHistoryListByBizTypeResponseBody = None,
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
            temp_model = GetHistoryListByBizTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLibraryRequest(TeaModel):
    def __init__(
        self,
        library_id: str = None,
    ):
        # This parameter is required.
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        return self


class GetLibraryResponseBodyDataIndexSettingChunkStrategy(TeaModel):
    def __init__(
        self,
        doc_tree_split: bool = None,
        doc_tree_split_size: int = None,
        enhance_graph: bool = None,
        enhance_table: bool = None,
        overlap: int = None,
        sentence_split: bool = None,
        sentence_split_size: int = None,
        size: int = None,
        split: bool = None,
    ):
        self.doc_tree_split = doc_tree_split
        self.doc_tree_split_size = doc_tree_split_size
        self.enhance_graph = enhance_graph
        self.enhance_table = enhance_table
        self.overlap = overlap
        self.sentence_split = sentence_split
        self.sentence_split_size = sentence_split_size
        self.size = size
        self.split = split

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_tree_split is not None:
            result['docTreeSplit'] = self.doc_tree_split
        if self.doc_tree_split_size is not None:
            result['docTreeSplitSize'] = self.doc_tree_split_size
        if self.enhance_graph is not None:
            result['enhanceGraph'] = self.enhance_graph
        if self.enhance_table is not None:
            result['enhanceTable'] = self.enhance_table
        if self.overlap is not None:
            result['overlap'] = self.overlap
        if self.sentence_split is not None:
            result['sentenceSplit'] = self.sentence_split
        if self.sentence_split_size is not None:
            result['sentenceSplitSize'] = self.sentence_split_size
        if self.size is not None:
            result['size'] = self.size
        if self.split is not None:
            result['split'] = self.split
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docTreeSplit') is not None:
            self.doc_tree_split = m.get('docTreeSplit')
        if m.get('docTreeSplitSize') is not None:
            self.doc_tree_split_size = m.get('docTreeSplitSize')
        if m.get('enhanceGraph') is not None:
            self.enhance_graph = m.get('enhanceGraph')
        if m.get('enhanceTable') is not None:
            self.enhance_table = m.get('enhanceTable')
        if m.get('overlap') is not None:
            self.overlap = m.get('overlap')
        if m.get('sentenceSplit') is not None:
            self.sentence_split = m.get('sentenceSplit')
        if m.get('sentenceSplitSize') is not None:
            self.sentence_split_size = m.get('sentenceSplitSize')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('split') is not None:
            self.split = m.get('split')
        return self


class GetLibraryResponseBodyDataIndexSettingModelConfig(TeaModel):
    def __init__(
        self,
        temperature: float = None,
        top_p: float = None,
    ):
        self.temperature = temperature
        # topP
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.temperature is not None:
            result['temperature'] = self.temperature
        if self.top_p is not None:
            result['topP'] = self.top_p
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        if m.get('topP') is not None:
            self.top_p = m.get('topP')
        return self


class GetLibraryResponseBodyDataIndexSettingQueryEnhancer(TeaModel):
    def __init__(
        self,
        enable_follow_up: bool = None,
        enable_multi_query: bool = None,
        enable_open_qa: bool = None,
        enable_query_rewrite: bool = None,
        enable_session: bool = None,
        local_knowledge_id: str = None,
        with_document_reference: bool = None,
    ):
        self.enable_follow_up = enable_follow_up
        self.enable_multi_query = enable_multi_query
        self.enable_open_qa = enable_open_qa
        self.enable_query_rewrite = enable_query_rewrite
        self.enable_session = enable_session
        self.local_knowledge_id = local_knowledge_id
        self.with_document_reference = with_document_reference

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_follow_up is not None:
            result['enableFollowUp'] = self.enable_follow_up
        if self.enable_multi_query is not None:
            result['enableMultiQuery'] = self.enable_multi_query
        if self.enable_open_qa is not None:
            result['enableOpenQa'] = self.enable_open_qa
        if self.enable_query_rewrite is not None:
            result['enableQueryRewrite'] = self.enable_query_rewrite
        if self.enable_session is not None:
            result['enableSession'] = self.enable_session
        if self.local_knowledge_id is not None:
            result['localKnowledgeId'] = self.local_knowledge_id
        if self.with_document_reference is not None:
            result['withDocumentReference'] = self.with_document_reference
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableFollowUp') is not None:
            self.enable_follow_up = m.get('enableFollowUp')
        if m.get('enableMultiQuery') is not None:
            self.enable_multi_query = m.get('enableMultiQuery')
        if m.get('enableOpenQa') is not None:
            self.enable_open_qa = m.get('enableOpenQa')
        if m.get('enableQueryRewrite') is not None:
            self.enable_query_rewrite = m.get('enableQueryRewrite')
        if m.get('enableSession') is not None:
            self.enable_session = m.get('enableSession')
        if m.get('localKnowledgeId') is not None:
            self.local_knowledge_id = m.get('localKnowledgeId')
        if m.get('withDocumentReference') is not None:
            self.with_document_reference = m.get('withDocumentReference')
        return self


class GetLibraryResponseBodyDataIndexSettingRecallStrategy(TeaModel):
    def __init__(
        self,
        document_rank_type: str = None,
        limit: int = None,
    ):
        self.document_rank_type = document_rank_type
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_rank_type is not None:
            result['documentRankType'] = self.document_rank_type
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentRankType') is not None:
            self.document_rank_type = m.get('documentRankType')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class GetLibraryResponseBodyDataIndexSettingTextIndexSetting(TeaModel):
    def __init__(
        self,
        category: str = None,
        enable: bool = None,
        index_analyzer: str = None,
        rank_threshold: float = None,
        search_analyzer: str = None,
        top_k: int = None,
    ):
        self.category = category
        self.enable = enable
        self.index_analyzer = index_analyzer
        self.rank_threshold = rank_threshold
        self.search_analyzer = search_analyzer
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.enable is not None:
            result['enable'] = self.enable
        if self.index_analyzer is not None:
            result['indexAnalyzer'] = self.index_analyzer
        if self.rank_threshold is not None:
            result['rankThreshold'] = self.rank_threshold
        if self.search_analyzer is not None:
            result['searchAnalyzer'] = self.search_analyzer
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('indexAnalyzer') is not None:
            self.index_analyzer = m.get('indexAnalyzer')
        if m.get('rankThreshold') is not None:
            self.rank_threshold = m.get('rankThreshold')
        if m.get('searchAnalyzer') is not None:
            self.search_analyzer = m.get('searchAnalyzer')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class GetLibraryResponseBodyDataIndexSettingVectorIndexSetting(TeaModel):
    def __init__(
        self,
        category: str = None,
        embedding_type: str = None,
        enable: bool = None,
        rank_threshold: float = None,
        top_k: int = None,
    ):
        self.category = category
        self.embedding_type = embedding_type
        self.enable = enable
        self.rank_threshold = rank_threshold
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.embedding_type is not None:
            result['embeddingType'] = self.embedding_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.rank_threshold is not None:
            result['rankThreshold'] = self.rank_threshold
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('embeddingType') is not None:
            self.embedding_type = m.get('embeddingType')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('rankThreshold') is not None:
            self.rank_threshold = m.get('rankThreshold')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class GetLibraryResponseBodyDataIndexSetting(TeaModel):
    def __init__(
        self,
        chunk_strategy: GetLibraryResponseBodyDataIndexSettingChunkStrategy = None,
        model_config: GetLibraryResponseBodyDataIndexSettingModelConfig = None,
        prompt_role_style: str = None,
        query_enhancer: GetLibraryResponseBodyDataIndexSettingQueryEnhancer = None,
        recall_strategy: GetLibraryResponseBodyDataIndexSettingRecallStrategy = None,
        text_index_setting: GetLibraryResponseBodyDataIndexSettingTextIndexSetting = None,
        vector_index_setting: GetLibraryResponseBodyDataIndexSettingVectorIndexSetting = None,
    ):
        self.chunk_strategy = chunk_strategy
        self.model_config = model_config
        self.prompt_role_style = prompt_role_style
        self.query_enhancer = query_enhancer
        self.recall_strategy = recall_strategy
        self.text_index_setting = text_index_setting
        self.vector_index_setting = vector_index_setting

    def validate(self):
        if self.chunk_strategy:
            self.chunk_strategy.validate()
        if self.model_config:
            self.model_config.validate()
        if self.query_enhancer:
            self.query_enhancer.validate()
        if self.recall_strategy:
            self.recall_strategy.validate()
        if self.text_index_setting:
            self.text_index_setting.validate()
        if self.vector_index_setting:
            self.vector_index_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_strategy is not None:
            result['chunkStrategy'] = self.chunk_strategy.to_map()
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.prompt_role_style is not None:
            result['promptRoleStyle'] = self.prompt_role_style
        if self.query_enhancer is not None:
            result['queryEnhancer'] = self.query_enhancer.to_map()
        if self.recall_strategy is not None:
            result['recallStrategy'] = self.recall_strategy.to_map()
        if self.text_index_setting is not None:
            result['textIndexSetting'] = self.text_index_setting.to_map()
        if self.vector_index_setting is not None:
            result['vectorIndexSetting'] = self.vector_index_setting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkStrategy') is not None:
            temp_model = GetLibraryResponseBodyDataIndexSettingChunkStrategy()
            self.chunk_strategy = temp_model.from_map(m['chunkStrategy'])
        if m.get('modelConfig') is not None:
            temp_model = GetLibraryResponseBodyDataIndexSettingModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('promptRoleStyle') is not None:
            self.prompt_role_style = m.get('promptRoleStyle')
        if m.get('queryEnhancer') is not None:
            temp_model = GetLibraryResponseBodyDataIndexSettingQueryEnhancer()
            self.query_enhancer = temp_model.from_map(m['queryEnhancer'])
        if m.get('recallStrategy') is not None:
            temp_model = GetLibraryResponseBodyDataIndexSettingRecallStrategy()
            self.recall_strategy = temp_model.from_map(m['recallStrategy'])
        if m.get('textIndexSetting') is not None:
            temp_model = GetLibraryResponseBodyDataIndexSettingTextIndexSetting()
            self.text_index_setting = temp_model.from_map(m['textIndexSetting'])
        if m.get('vectorIndexSetting') is not None:
            temp_model = GetLibraryResponseBodyDataIndexSettingVectorIndexSetting()
            self.vector_index_setting = temp_model.from_map(m['vectorIndexSetting'])
        return self


class GetLibraryResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        document_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        index_setting: GetLibraryResponseBodyDataIndexSetting = None,
        library_name: str = None,
    ):
        self.description = description
        self.document_count = document_count
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.index_setting = index_setting
        self.library_name = library_name

    def validate(self):
        if self.index_setting:
            self.index_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.document_count is not None:
            result['documentCount'] = self.document_count
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.index_setting is not None:
            result['indexSetting'] = self.index_setting.to_map()
        if self.library_name is not None:
            result['libraryName'] = self.library_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documentCount') is not None:
            self.document_count = m.get('documentCount')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('indexSetting') is not None:
            temp_model = GetLibraryResponseBodyDataIndexSetting()
            self.index_setting = temp_model.from_map(m['indexSetting'])
        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')
        return self


class GetLibraryResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetLibraryResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetLibraryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLibraryResponseBody = None,
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
            temp_model = GetLibraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLibraryListRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        query: str = None,
    ):
        self.page = page
        self.page_size = page_size
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class GetLibraryListResponseBodyDataRecordsIndexSettingChunkStrategy(TeaModel):
    def __init__(
        self,
        doc_tree_split: bool = None,
        doc_tree_split_size: int = None,
        enhance_graph: bool = None,
        enhance_table: bool = None,
        overlap: int = None,
        sentence_split: bool = None,
        sentence_split_size: int = None,
        size: int = None,
        split: bool = None,
    ):
        self.doc_tree_split = doc_tree_split
        self.doc_tree_split_size = doc_tree_split_size
        self.enhance_graph = enhance_graph
        self.enhance_table = enhance_table
        self.overlap = overlap
        self.sentence_split = sentence_split
        self.sentence_split_size = sentence_split_size
        self.size = size
        self.split = split

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_tree_split is not None:
            result['docTreeSplit'] = self.doc_tree_split
        if self.doc_tree_split_size is not None:
            result['docTreeSplitSize'] = self.doc_tree_split_size
        if self.enhance_graph is not None:
            result['enhanceGraph'] = self.enhance_graph
        if self.enhance_table is not None:
            result['enhanceTable'] = self.enhance_table
        if self.overlap is not None:
            result['overlap'] = self.overlap
        if self.sentence_split is not None:
            result['sentenceSplit'] = self.sentence_split
        if self.sentence_split_size is not None:
            result['sentenceSplitSize'] = self.sentence_split_size
        if self.size is not None:
            result['size'] = self.size
        if self.split is not None:
            result['split'] = self.split
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docTreeSplit') is not None:
            self.doc_tree_split = m.get('docTreeSplit')
        if m.get('docTreeSplitSize') is not None:
            self.doc_tree_split_size = m.get('docTreeSplitSize')
        if m.get('enhanceGraph') is not None:
            self.enhance_graph = m.get('enhanceGraph')
        if m.get('enhanceTable') is not None:
            self.enhance_table = m.get('enhanceTable')
        if m.get('overlap') is not None:
            self.overlap = m.get('overlap')
        if m.get('sentenceSplit') is not None:
            self.sentence_split = m.get('sentenceSplit')
        if m.get('sentenceSplitSize') is not None:
            self.sentence_split_size = m.get('sentenceSplitSize')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('split') is not None:
            self.split = m.get('split')
        return self


class GetLibraryListResponseBodyDataRecordsIndexSettingModelConfig(TeaModel):
    def __init__(
        self,
        temperature: float = None,
        top_p: float = None,
    ):
        self.temperature = temperature
        # topP
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.temperature is not None:
            result['temperature'] = self.temperature
        if self.top_p is not None:
            result['topP'] = self.top_p
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        if m.get('topP') is not None:
            self.top_p = m.get('topP')
        return self


class GetLibraryListResponseBodyDataRecordsIndexSettingQueryEnhancer(TeaModel):
    def __init__(
        self,
        enable_follow_up: bool = None,
        enable_multi_query: bool = None,
        enable_open_qa: bool = None,
        enable_query_rewrite: bool = None,
        enable_session: bool = None,
        local_knowledge_id: str = None,
        with_document_reference: bool = None,
    ):
        self.enable_follow_up = enable_follow_up
        self.enable_multi_query = enable_multi_query
        self.enable_open_qa = enable_open_qa
        self.enable_query_rewrite = enable_query_rewrite
        self.enable_session = enable_session
        self.local_knowledge_id = local_knowledge_id
        self.with_document_reference = with_document_reference

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_follow_up is not None:
            result['enableFollowUp'] = self.enable_follow_up
        if self.enable_multi_query is not None:
            result['enableMultiQuery'] = self.enable_multi_query
        if self.enable_open_qa is not None:
            result['enableOpenQa'] = self.enable_open_qa
        if self.enable_query_rewrite is not None:
            result['enableQueryRewrite'] = self.enable_query_rewrite
        if self.enable_session is not None:
            result['enableSession'] = self.enable_session
        if self.local_knowledge_id is not None:
            result['localKnowledgeId'] = self.local_knowledge_id
        if self.with_document_reference is not None:
            result['withDocumentReference'] = self.with_document_reference
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableFollowUp') is not None:
            self.enable_follow_up = m.get('enableFollowUp')
        if m.get('enableMultiQuery') is not None:
            self.enable_multi_query = m.get('enableMultiQuery')
        if m.get('enableOpenQa') is not None:
            self.enable_open_qa = m.get('enableOpenQa')
        if m.get('enableQueryRewrite') is not None:
            self.enable_query_rewrite = m.get('enableQueryRewrite')
        if m.get('enableSession') is not None:
            self.enable_session = m.get('enableSession')
        if m.get('localKnowledgeId') is not None:
            self.local_knowledge_id = m.get('localKnowledgeId')
        if m.get('withDocumentReference') is not None:
            self.with_document_reference = m.get('withDocumentReference')
        return self


class GetLibraryListResponseBodyDataRecordsIndexSettingRecallStrategy(TeaModel):
    def __init__(
        self,
        document_rank_type: str = None,
        limit: int = None,
    ):
        self.document_rank_type = document_rank_type
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_rank_type is not None:
            result['documentRankType'] = self.document_rank_type
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentRankType') is not None:
            self.document_rank_type = m.get('documentRankType')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class GetLibraryListResponseBodyDataRecordsIndexSettingTextIndexSetting(TeaModel):
    def __init__(
        self,
        category: str = None,
        enable: bool = None,
        index_analyzer: str = None,
        rank_threshold: float = None,
        search_analyzer: str = None,
        top_k: int = None,
    ):
        self.category = category
        self.enable = enable
        self.index_analyzer = index_analyzer
        self.rank_threshold = rank_threshold
        self.search_analyzer = search_analyzer
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.enable is not None:
            result['enable'] = self.enable
        if self.index_analyzer is not None:
            result['indexAnalyzer'] = self.index_analyzer
        if self.rank_threshold is not None:
            result['rankThreshold'] = self.rank_threshold
        if self.search_analyzer is not None:
            result['searchAnalyzer'] = self.search_analyzer
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('indexAnalyzer') is not None:
            self.index_analyzer = m.get('indexAnalyzer')
        if m.get('rankThreshold') is not None:
            self.rank_threshold = m.get('rankThreshold')
        if m.get('searchAnalyzer') is not None:
            self.search_analyzer = m.get('searchAnalyzer')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class GetLibraryListResponseBodyDataRecordsIndexSettingVectorIndexSetting(TeaModel):
    def __init__(
        self,
        category: str = None,
        embedding_type: str = None,
        enable: bool = None,
        rank_threshold: float = None,
        top_k: int = None,
    ):
        self.category = category
        self.embedding_type = embedding_type
        self.enable = enable
        self.rank_threshold = rank_threshold
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.embedding_type is not None:
            result['embeddingType'] = self.embedding_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.rank_threshold is not None:
            result['rankThreshold'] = self.rank_threshold
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('embeddingType') is not None:
            self.embedding_type = m.get('embeddingType')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('rankThreshold') is not None:
            self.rank_threshold = m.get('rankThreshold')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class GetLibraryListResponseBodyDataRecordsIndexSetting(TeaModel):
    def __init__(
        self,
        chunk_strategy: GetLibraryListResponseBodyDataRecordsIndexSettingChunkStrategy = None,
        model_config: GetLibraryListResponseBodyDataRecordsIndexSettingModelConfig = None,
        prompt_role_style: str = None,
        query_enhancer: GetLibraryListResponseBodyDataRecordsIndexSettingQueryEnhancer = None,
        recall_strategy: GetLibraryListResponseBodyDataRecordsIndexSettingRecallStrategy = None,
        text_index_setting: GetLibraryListResponseBodyDataRecordsIndexSettingTextIndexSetting = None,
        vector_index_setting: GetLibraryListResponseBodyDataRecordsIndexSettingVectorIndexSetting = None,
    ):
        self.chunk_strategy = chunk_strategy
        self.model_config = model_config
        self.prompt_role_style = prompt_role_style
        self.query_enhancer = query_enhancer
        self.recall_strategy = recall_strategy
        self.text_index_setting = text_index_setting
        self.vector_index_setting = vector_index_setting

    def validate(self):
        if self.chunk_strategy:
            self.chunk_strategy.validate()
        if self.model_config:
            self.model_config.validate()
        if self.query_enhancer:
            self.query_enhancer.validate()
        if self.recall_strategy:
            self.recall_strategy.validate()
        if self.text_index_setting:
            self.text_index_setting.validate()
        if self.vector_index_setting:
            self.vector_index_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_strategy is not None:
            result['chunkStrategy'] = self.chunk_strategy.to_map()
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.prompt_role_style is not None:
            result['promptRoleStyle'] = self.prompt_role_style
        if self.query_enhancer is not None:
            result['queryEnhancer'] = self.query_enhancer.to_map()
        if self.recall_strategy is not None:
            result['recallStrategy'] = self.recall_strategy.to_map()
        if self.text_index_setting is not None:
            result['textIndexSetting'] = self.text_index_setting.to_map()
        if self.vector_index_setting is not None:
            result['vectorIndexSetting'] = self.vector_index_setting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkStrategy') is not None:
            temp_model = GetLibraryListResponseBodyDataRecordsIndexSettingChunkStrategy()
            self.chunk_strategy = temp_model.from_map(m['chunkStrategy'])
        if m.get('modelConfig') is not None:
            temp_model = GetLibraryListResponseBodyDataRecordsIndexSettingModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('promptRoleStyle') is not None:
            self.prompt_role_style = m.get('promptRoleStyle')
        if m.get('queryEnhancer') is not None:
            temp_model = GetLibraryListResponseBodyDataRecordsIndexSettingQueryEnhancer()
            self.query_enhancer = temp_model.from_map(m['queryEnhancer'])
        if m.get('recallStrategy') is not None:
            temp_model = GetLibraryListResponseBodyDataRecordsIndexSettingRecallStrategy()
            self.recall_strategy = temp_model.from_map(m['recallStrategy'])
        if m.get('textIndexSetting') is not None:
            temp_model = GetLibraryListResponseBodyDataRecordsIndexSettingTextIndexSetting()
            self.text_index_setting = temp_model.from_map(m['textIndexSetting'])
        if m.get('vectorIndexSetting') is not None:
            temp_model = GetLibraryListResponseBodyDataRecordsIndexSettingVectorIndexSetting()
            self.vector_index_setting = temp_model.from_map(m['vectorIndexSetting'])
        return self


class GetLibraryListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        description: str = None,
        document_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        index_setting: GetLibraryListResponseBodyDataRecordsIndexSetting = None,
        library_name: str = None,
    ):
        self.description = description
        self.document_count = document_count
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.index_setting = index_setting
        self.library_name = library_name

    def validate(self):
        if self.index_setting:
            self.index_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.document_count is not None:
            result['documentCount'] = self.document_count
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.index_setting is not None:
            result['indexSetting'] = self.index_setting.to_map()
        if self.library_name is not None:
            result['libraryName'] = self.library_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documentCount') is not None:
            self.document_count = m.get('documentCount')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('indexSetting') is not None:
            temp_model = GetLibraryListResponseBodyDataRecordsIndexSetting()
            self.index_setting = temp_model.from_map(m['indexSetting'])
        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')
        return self


class GetLibraryListResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[GetLibraryListResponseBodyDataRecords] = None,
        total_pages: int = None,
        total_records: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.records = records
        self.total_pages = total_pages
        self.total_records = total_records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.total_pages is not None:
            result['totalPages'] = self.total_pages
        if self.total_records is not None:
            result['totalRecords'] = self.total_records
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetLibraryListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')
        if m.get('totalRecords') is not None:
            self.total_records = m.get('totalRecords')
        return self


class GetLibraryListResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetLibraryListResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetLibraryListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetLibraryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLibraryListResponseBody = None,
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
            temp_model = GetLibraryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParseResultRequest(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        library_id: str = None,
        use_url_result: bool = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        # This parameter is required.
        self.library_id = library_id
        self.use_url_result = use_url_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.use_url_result is not None:
            result['useUrlResult'] = self.use_url_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('useUrlResult') is not None:
            self.use_url_result = m.get('useUrlResult')
        return self


class GetParseResultResponseBodyData(TeaModel):
    def __init__(
        self,
        file_type: str = None,
        provider_type: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
        result_url: str = None,
        status: str = None,
    ):
        self.file_type = file_type
        self.provider_type = provider_type
        self.request_id = request_id
        self.result = result
        self.result_url = result_url
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.provider_type is not None:
            result['providerType'] = self.provider_type
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.result_url is not None:
            result['resultUrl'] = self.result_url
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('providerType') is not None:
            self.provider_type = m.get('providerType')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('resultUrl') is not None:
            self.result_url = m.get('resultUrl')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetParseResultResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetParseResultResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetParseResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetParseResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetParseResultResponseBody = None,
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
            temp_model = GetParseResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityCheckTaskResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetQualityCheckTaskResultResponseBodyDataConversationListDialogueList(TeaModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        end: int = None,
        id: int = None,
        role: str = None,
        type: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.end = end
        self.id = id
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['begin'] = self.begin
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.content is not None:
            result['content'] = self.content
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id
        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type
        if self.end is not None:
            result['end'] = self.end
        if self.id is not None:
            result['id'] = self.id
        if self.role is not None:
            result['role'] = self.role
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('begin') is not None:
            self.begin = m.get('begin')
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')
        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetQualityCheckTaskResultResponseBodyDataConversationList(TeaModel):
    def __init__(
        self,
        call_type: str = None,
        customer_id: str = None,
        customer_name: str = None,
        customer_service_id: str = None,
        customer_service_name: str = None,
        dialogue_list: List[GetQualityCheckTaskResultResponseBodyDataConversationListDialogueList] = None,
        gmt_service: str = None,
    ):
        self.call_type = call_type
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_service_id = customer_service_id
        self.customer_service_name = customer_service_name
        self.dialogue_list = dialogue_list
        self.gmt_service = gmt_service

    def validate(self):
        if self.dialogue_list:
            for k in self.dialogue_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_type is not None:
            result['callType'] = self.call_type
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.customer_name is not None:
            result['customerName'] = self.customer_name
        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id
        if self.customer_service_name is not None:
            result['customerServiceName'] = self.customer_service_name
        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k in self.dialogue_list:
                result['dialogueList'].append(k.to_map() if k else None)
        if self.gmt_service is not None:
            result['gmtService'] = self.gmt_service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callType') is not None:
            self.call_type = m.get('callType')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('customerName') is not None:
            self.customer_name = m.get('customerName')
        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')
        if m.get('customerServiceName') is not None:
            self.customer_service_name = m.get('customerServiceName')
        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k in m.get('dialogueList'):
                temp_model = GetQualityCheckTaskResultResponseBodyDataConversationListDialogueList()
                self.dialogue_list.append(temp_model.from_map(k))
        if m.get('gmtService') is not None:
            self.gmt_service = m.get('gmtService')
        return self


class GetQualityCheckTaskResultResponseBodyDataQualityCheckListOriginDialogue(TeaModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        end: int = None,
        id: int = None,
        role: str = None,
        type: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.end = end
        self.id = id
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['begin'] = self.begin
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.content is not None:
            result['content'] = self.content
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id
        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type
        if self.end is not None:
            result['end'] = self.end
        if self.id is not None:
            result['id'] = self.id
        if self.role is not None:
            result['role'] = self.role
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('begin') is not None:
            self.begin = m.get('begin')
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')
        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetQualityCheckTaskResultResponseBodyDataQualityCheckList(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        check_explanation: str = None,
        check_passed: str = None,
        check_process: str = None,
        checked: str = None,
        gmt_end: str = None,
        gmt_start: str = None,
        mode: str = None,
        origin_dialogue: List[GetQualityCheckTaskResultResponseBodyDataQualityCheckListOriginDialogue] = None,
        quality_group_id: str = None,
        rule_description: str = None,
        rule_id: str = None,
        rule_type: str = None,
        sub_node_col: List[Any] = None,
    ):
        self.biz_type = biz_type
        self.check_explanation = check_explanation
        self.check_passed = check_passed
        self.check_process = check_process
        self.checked = checked
        self.gmt_end = gmt_end
        self.gmt_start = gmt_start
        self.mode = mode
        self.origin_dialogue = origin_dialogue
        self.quality_group_id = quality_group_id
        self.rule_description = rule_description
        self.rule_id = rule_id
        self.rule_type = rule_type
        self.sub_node_col = sub_node_col

    def validate(self):
        if self.origin_dialogue:
            for k in self.origin_dialogue:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.check_explanation is not None:
            result['checkExplanation'] = self.check_explanation
        if self.check_passed is not None:
            result['checkPassed'] = self.check_passed
        if self.check_process is not None:
            result['checkProcess'] = self.check_process
        if self.checked is not None:
            result['checked'] = self.checked
        if self.gmt_end is not None:
            result['gmtEnd'] = self.gmt_end
        if self.gmt_start is not None:
            result['gmtStart'] = self.gmt_start
        if self.mode is not None:
            result['mode'] = self.mode
        result['originDialogue'] = []
        if self.origin_dialogue is not None:
            for k in self.origin_dialogue:
                result['originDialogue'].append(k.to_map() if k else None)
        if self.quality_group_id is not None:
            result['qualityGroupId'] = self.quality_group_id
        if self.rule_description is not None:
            result['ruleDescription'] = self.rule_description
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_type is not None:
            result['ruleType'] = self.rule_type
        if self.sub_node_col is not None:
            result['subNodeCol'] = self.sub_node_col
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('checkExplanation') is not None:
            self.check_explanation = m.get('checkExplanation')
        if m.get('checkPassed') is not None:
            self.check_passed = m.get('checkPassed')
        if m.get('checkProcess') is not None:
            self.check_process = m.get('checkProcess')
        if m.get('checked') is not None:
            self.checked = m.get('checked')
        if m.get('gmtEnd') is not None:
            self.gmt_end = m.get('gmtEnd')
        if m.get('gmtStart') is not None:
            self.gmt_start = m.get('gmtStart')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        self.origin_dialogue = []
        if m.get('originDialogue') is not None:
            for k in m.get('originDialogue'):
                temp_model = GetQualityCheckTaskResultResponseBodyDataQualityCheckListOriginDialogue()
                self.origin_dialogue.append(temp_model.from_map(k))
        if m.get('qualityGroupId') is not None:
            self.quality_group_id = m.get('qualityGroupId')
        if m.get('ruleDescription') is not None:
            self.rule_description = m.get('ruleDescription')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')
        if m.get('subNodeCol') is not None:
            self.sub_node_col = m.get('subNodeCol')
        return self


class GetQualityCheckTaskResultResponseBodyData(TeaModel):
    def __init__(
        self,
        conversation_list: GetQualityCheckTaskResultResponseBodyDataConversationList = None,
        gmt_create: str = None,
        gmt_end: str = None,
        gmt_start: str = None,
        quality_check_list: List[GetQualityCheckTaskResultResponseBodyDataQualityCheckList] = None,
        status: str = None,
        task_id: str = None,
    ):
        self.conversation_list = conversation_list
        self.gmt_create = gmt_create
        self.gmt_end = gmt_end
        self.gmt_start = gmt_start
        self.quality_check_list = quality_check_list
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.conversation_list:
            self.conversation_list.validate()
        if self.quality_check_list:
            for k in self.quality_check_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_list is not None:
            result['conversationList'] = self.conversation_list.to_map()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_end is not None:
            result['gmtEnd'] = self.gmt_end
        if self.gmt_start is not None:
            result['gmtStart'] = self.gmt_start
        result['qualityCheckList'] = []
        if self.quality_check_list is not None:
            for k in self.quality_check_list:
                result['qualityCheckList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conversationList') is not None:
            temp_model = GetQualityCheckTaskResultResponseBodyDataConversationList()
            self.conversation_list = temp_model.from_map(m['conversationList'])
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtEnd') is not None:
            self.gmt_end = m.get('gmtEnd')
        if m.get('gmtStart') is not None:
            self.gmt_start = m.get('gmtStart')
        self.quality_check_list = []
        if m.get('qualityCheckList') is not None:
            for k in m.get('qualityCheckList'):
                temp_model = GetQualityCheckTaskResultResponseBodyDataQualityCheckList()
                self.quality_check_list.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetQualityCheckTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetQualityCheckTaskResultResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetQualityCheckTaskResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetQualityCheckTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQualityCheckTaskResultResponseBody = None,
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
            temp_model = GetQualityCheckTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSummaryTaskResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetSummaryTaskResultResponseBodyDataChoicesMessage(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
        tool_calls: List[Dict[str, Any]] = None,
    ):
        self.content = content
        self.role = role
        self.tool_calls = tool_calls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        if self.tool_calls is not None:
            result['toolCalls'] = self.tool_calls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('toolCalls') is not None:
            self.tool_calls = m.get('toolCalls')
        return self


class GetSummaryTaskResultResponseBodyDataChoices(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        index: int = None,
        message: GetSummaryTaskResultResponseBodyDataChoicesMessage = None,
    ):
        self.finish_reason = finish_reason
        self.index = index
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.index is not None:
            result['index'] = self.index
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('message') is not None:
            temp_model = GetSummaryTaskResultResponseBodyDataChoicesMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class GetSummaryTaskResultResponseBodyDataUsage(TeaModel):
    def __init__(
        self,
        image_count: int = None,
        image_tokens: int = None,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.image_count = image_count
        self.image_tokens = image_tokens
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_count is not None:
            result['imageCount'] = self.image_count
        if self.image_tokens is not None:
            result['imageTokens'] = self.image_tokens
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')
        if m.get('imageTokens') is not None:
            self.image_tokens = m.get('imageTokens')
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class GetSummaryTaskResultResponseBodyData(TeaModel):
    def __init__(
        self,
        choices: List[GetSummaryTaskResultResponseBodyDataChoices] = None,
        created: int = None,
        id: str = None,
        model_id: str = None,
        request_id: str = None,
        time: str = None,
        total_tokens: int = None,
        usage: GetSummaryTaskResultResponseBodyDataUsage = None,
    ):
        self.choices = choices
        self.created = created
        self.id = id
        self.model_id = model_id
        self.request_id = request_id
        self.time = time
        self.total_tokens = total_tokens
        self.usage = usage

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['choices'].append(k.to_map() if k else None)
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.time is not None:
            result['time'] = self.time
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k in m.get('choices'):
                temp_model = GetSummaryTaskResultResponseBodyDataChoices()
                self.choices.append(temp_model.from_map(k))
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        if m.get('usage') is not None:
            temp_model = GetSummaryTaskResultResponseBodyDataUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetSummaryTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: GetSummaryTaskResultResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = GetSummaryTaskResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetSummaryTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSummaryTaskResultResponseBody = None,
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
            temp_model = GetSummaryTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: Dict[str, Any] = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResultResponseBody = None,
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
            temp_model = GetTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskStatusResponseBody = None,
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
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokePluginRequest(TeaModel):
    def __init__(
        self,
        params: Dict[str, Any] = None,
        plugin_id: str = None,
    ):
        self.params = params
        self.plugin_id = plugin_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params
        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')
        return self


class InvokePluginResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: Dict[str, Any] = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class InvokePluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvokePluginResponseBody = None,
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
            temp_model = InvokePluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviewDocumentRequest(TeaModel):
    def __init__(
        self,
        document_id: str = None,
    ):
        # This parameter is required.
        self.document_id = document_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_id is not None:
            result['documentId'] = self.document_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentId') is not None:
            self.document_id = m.get('documentId')
        return self


class PreviewDocumentResponseBodyData(TeaModel):
    def __init__(
        self,
        preview_type: str = None,
        title: str = None,
        upload_time: str = None,
        url: str = None,
    ):
        self.preview_type = preview_type
        self.title = title
        self.upload_time = upload_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preview_type is not None:
            result['previewType'] = self.preview_type
        if self.title is not None:
            result['title'] = self.title
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('previewType') is not None:
            self.preview_type = m.get('previewType')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class PreviewDocumentResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: PreviewDocumentResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = PreviewDocumentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class PreviewDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PreviewDocumentResponseBody = None,
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
            temp_model = PreviewDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReIndexRequest(TeaModel):
    def __init__(
        self,
        document_id: str = None,
    ):
        # This parameter is required.
        self.document_id = document_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_id is not None:
            result['documentId'] = self.document_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentId') is not None:
            self.document_id = m.get('documentId')
        return self


class ReIndexResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class ReIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReIndexResponseBody = None,
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
            temp_model = ReIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RealTimeDialogRequestConversationModel(TeaModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        end: int = None,
        role: int = None,
        type: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        # This parameter is required.
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.end = end
        # This parameter is required.
        self.role = role
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['begin'] = self.begin
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.content is not None:
            result['content'] = self.content
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id
        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type
        if self.end is not None:
            result['end'] = self.end
        if self.role is not None:
            result['role'] = self.role
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('begin') is not None:
            self.begin = m.get('begin')
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')
        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RealTimeDialogRequest(TeaModel):
    def __init__(
        self,
        analysis: bool = None,
        biz_type: str = None,
        conversation_model: List[RealTimeDialogRequestConversationModel] = None,
        dialog_memory_turns: int = None,
        meta_data: Dict[str, Any] = None,
        op_type: str = None,
        recommend: bool = None,
        script_content_played: str = None,
        session_id: str = None,
        stream: bool = None,
        user_vad: bool = None,
    ):
        self.analysis = analysis
        self.biz_type = biz_type
        # This parameter is required.
        self.conversation_model = conversation_model
        self.dialog_memory_turns = dialog_memory_turns
        self.meta_data = meta_data
        self.op_type = op_type
        self.recommend = recommend
        self.script_content_played = script_content_played
        # This parameter is required.
        self.session_id = session_id
        self.stream = stream
        self.user_vad = user_vad

    def validate(self):
        if self.conversation_model:
            for k in self.conversation_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis is not None:
            result['analysis'] = self.analysis
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        result['conversationModel'] = []
        if self.conversation_model is not None:
            for k in self.conversation_model:
                result['conversationModel'].append(k.to_map() if k else None)
        if self.dialog_memory_turns is not None:
            result['dialogMemoryTurns'] = self.dialog_memory_turns
        if self.meta_data is not None:
            result['metaData'] = self.meta_data
        if self.op_type is not None:
            result['opType'] = self.op_type
        if self.recommend is not None:
            result['recommend'] = self.recommend
        if self.script_content_played is not None:
            result['scriptContentPlayed'] = self.script_content_played
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.stream is not None:
            result['stream'] = self.stream
        if self.user_vad is not None:
            result['userVad'] = self.user_vad
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis') is not None:
            self.analysis = m.get('analysis')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        self.conversation_model = []
        if m.get('conversationModel') is not None:
            for k in m.get('conversationModel'):
                temp_model = RealTimeDialogRequestConversationModel()
                self.conversation_model.append(temp_model.from_map(k))
        if m.get('dialogMemoryTurns') is not None:
            self.dialog_memory_turns = m.get('dialogMemoryTurns')
        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')
        if m.get('opType') is not None:
            self.op_type = m.get('opType')
        if m.get('recommend') is not None:
            self.recommend = m.get('recommend')
        if m.get('scriptContentPlayed') is not None:
            self.script_content_played = m.get('scriptContentPlayed')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('userVad') is not None:
            self.user_vad = m.get('userVad')
        return self


class RealTimeDialogResponseBodyChoicesDelta(TeaModel):
    def __init__(
        self,
        analysis_process: str = None,
        call_time: str = None,
        hang_up_dialog: bool = None,
        intention_code: str = None,
        intention_name: str = None,
        intention_script: str = None,
        interrupt: bool = None,
        recommend_intention: str = None,
        recommend_script: str = None,
        self_directed_script: str = None,
        self_directed_script_full_content: str = None,
        skip_current_recognize: bool = None,
    ):
        self.analysis_process = analysis_process
        # time
        self.call_time = call_time
        self.hang_up_dialog = hang_up_dialog
        self.intention_code = intention_code
        self.intention_name = intention_name
        self.intention_script = intention_script
        self.interrupt = interrupt
        self.recommend_intention = recommend_intention
        self.recommend_script = recommend_script
        self.self_directed_script = self_directed_script
        self.self_directed_script_full_content = self_directed_script_full_content
        self.skip_current_recognize = skip_current_recognize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_process is not None:
            result['analysisProcess'] = self.analysis_process
        if self.call_time is not None:
            result['callTime'] = self.call_time
        if self.hang_up_dialog is not None:
            result['hangUpDialog'] = self.hang_up_dialog
        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code
        if self.intention_name is not None:
            result['intentionName'] = self.intention_name
        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script
        if self.interrupt is not None:
            result['interrupt'] = self.interrupt
        if self.recommend_intention is not None:
            result['recommendIntention'] = self.recommend_intention
        if self.recommend_script is not None:
            result['recommendScript'] = self.recommend_script
        if self.self_directed_script is not None:
            result['selfDirectedScript'] = self.self_directed_script
        if self.self_directed_script_full_content is not None:
            result['selfDirectedScriptFullContent'] = self.self_directed_script_full_content
        if self.skip_current_recognize is not None:
            result['skipCurrentRecognize'] = self.skip_current_recognize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisProcess') is not None:
            self.analysis_process = m.get('analysisProcess')
        if m.get('callTime') is not None:
            self.call_time = m.get('callTime')
        if m.get('hangUpDialog') is not None:
            self.hang_up_dialog = m.get('hangUpDialog')
        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')
        if m.get('intentionName') is not None:
            self.intention_name = m.get('intentionName')
        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')
        if m.get('interrupt') is not None:
            self.interrupt = m.get('interrupt')
        if m.get('recommendIntention') is not None:
            self.recommend_intention = m.get('recommendIntention')
        if m.get('recommendScript') is not None:
            self.recommend_script = m.get('recommendScript')
        if m.get('selfDirectedScript') is not None:
            self.self_directed_script = m.get('selfDirectedScript')
        if m.get('selfDirectedScriptFullContent') is not None:
            self.self_directed_script_full_content = m.get('selfDirectedScriptFullContent')
        if m.get('skipCurrentRecognize') is not None:
            self.skip_current_recognize = m.get('skipCurrentRecognize')
        return self


class RealTimeDialogResponseBodyChoicesMessage(TeaModel):
    def __init__(
        self,
        analysis_process: str = None,
        call_time: str = None,
        hang_up_dialog: bool = None,
        intention_code: str = None,
        intention_name: str = None,
        intention_script: str = None,
        interrupt: bool = None,
        recommend_intention: str = None,
        recommend_script: str = None,
        self_directed_script: str = None,
        self_directed_script_full_content: str = None,
        skip_current_recognize: bool = None,
    ):
        self.analysis_process = analysis_process
        # time
        self.call_time = call_time
        self.hang_up_dialog = hang_up_dialog
        self.intention_code = intention_code
        self.intention_name = intention_name
        self.intention_script = intention_script
        self.interrupt = interrupt
        self.recommend_intention = recommend_intention
        self.recommend_script = recommend_script
        self.self_directed_script = self_directed_script
        self.self_directed_script_full_content = self_directed_script_full_content
        self.skip_current_recognize = skip_current_recognize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_process is not None:
            result['analysisProcess'] = self.analysis_process
        if self.call_time is not None:
            result['callTime'] = self.call_time
        if self.hang_up_dialog is not None:
            result['hangUpDialog'] = self.hang_up_dialog
        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code
        if self.intention_name is not None:
            result['intentionName'] = self.intention_name
        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script
        if self.interrupt is not None:
            result['interrupt'] = self.interrupt
        if self.recommend_intention is not None:
            result['recommendIntention'] = self.recommend_intention
        if self.recommend_script is not None:
            result['recommendScript'] = self.recommend_script
        if self.self_directed_script is not None:
            result['selfDirectedScript'] = self.self_directed_script
        if self.self_directed_script_full_content is not None:
            result['selfDirectedScriptFullContent'] = self.self_directed_script_full_content
        if self.skip_current_recognize is not None:
            result['skipCurrentRecognize'] = self.skip_current_recognize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisProcess') is not None:
            self.analysis_process = m.get('analysisProcess')
        if m.get('callTime') is not None:
            self.call_time = m.get('callTime')
        if m.get('hangUpDialog') is not None:
            self.hang_up_dialog = m.get('hangUpDialog')
        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')
        if m.get('intentionName') is not None:
            self.intention_name = m.get('intentionName')
        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')
        if m.get('interrupt') is not None:
            self.interrupt = m.get('interrupt')
        if m.get('recommendIntention') is not None:
            self.recommend_intention = m.get('recommendIntention')
        if m.get('recommendScript') is not None:
            self.recommend_script = m.get('recommendScript')
        if m.get('selfDirectedScript') is not None:
            self.self_directed_script = m.get('selfDirectedScript')
        if m.get('selfDirectedScriptFullContent') is not None:
            self.self_directed_script_full_content = m.get('selfDirectedScriptFullContent')
        if m.get('skipCurrentRecognize') is not None:
            self.skip_current_recognize = m.get('skipCurrentRecognize')
        return self


class RealTimeDialogResponseBodyChoices(TeaModel):
    def __init__(
        self,
        delta: RealTimeDialogResponseBodyChoicesDelta = None,
        finish_reason: str = None,
        index: int = None,
        message: RealTimeDialogResponseBodyChoicesMessage = None,
    ):
        self.delta = delta
        self.finish_reason = finish_reason
        self.index = index
        self.message = message

    def validate(self):
        if self.delta:
            self.delta.validate()
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delta is not None:
            result['delta'] = self.delta.to_map()
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.index is not None:
            result['index'] = self.index
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delta') is not None:
            temp_model = RealTimeDialogResponseBodyChoicesDelta()
            self.delta = temp_model.from_map(m['delta'])
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('message') is not None:
            temp_model = RealTimeDialogResponseBodyChoicesMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class RealTimeDialogResponseBody(TeaModel):
    def __init__(
        self,
        choices: List[RealTimeDialogResponseBodyChoices] = None,
        created: str = None,
        id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.choices = choices
        self.created = created
        self.id = id
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['choices'].append(k.to_map() if k else None)
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k in m.get('choices'):
                temp_model = RealTimeDialogResponseBodyChoices()
                self.choices.append(temp_model.from_map(k))
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RealTimeDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RealTimeDialogResponseBody = None,
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
            temp_model = RealTimeDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RealtimeDialogAssistRequestConversationModel(TeaModel):
    def __init__(
        self,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        role: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        # This parameter is required.
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id
        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type
        if self.role is not None:
            result['role'] = self.role
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')
        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RealtimeDialogAssistRequest(TeaModel):
    def __init__(
        self,
        analysis: bool = None,
        biz_type: str = None,
        conversation_model: List[RealtimeDialogAssistRequestConversationModel] = None,
        dialog_memory_turns: int = None,
        hang_up_dialog: bool = None,
        meta_data: Dict[str, Any] = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.analysis = analysis
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.conversation_model = conversation_model
        self.dialog_memory_turns = dialog_memory_turns
        self.hang_up_dialog = hang_up_dialog
        # metaData
        self.meta_data = meta_data
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        if self.conversation_model:
            for k in self.conversation_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis is not None:
            result['analysis'] = self.analysis
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        result['conversationModel'] = []
        if self.conversation_model is not None:
            for k in self.conversation_model:
                result['conversationModel'].append(k.to_map() if k else None)
        if self.dialog_memory_turns is not None:
            result['dialogMemoryTurns'] = self.dialog_memory_turns
        if self.hang_up_dialog is not None:
            result['hangUpDialog'] = self.hang_up_dialog
        if self.meta_data is not None:
            result['metaData'] = self.meta_data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis') is not None:
            self.analysis = m.get('analysis')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        self.conversation_model = []
        if m.get('conversationModel') is not None:
            for k in m.get('conversationModel'):
                temp_model = RealtimeDialogAssistRequestConversationModel()
                self.conversation_model.append(temp_model.from_map(k))
        if m.get('dialogMemoryTurns') is not None:
            self.dialog_memory_turns = m.get('dialogMemoryTurns')
        if m.get('hangUpDialog') is not None:
            self.hang_up_dialog = m.get('hangUpDialog')
        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class RealtimeDialogAssistResponseBodyDataAssistScripts(TeaModel):
    def __init__(
        self,
        assist_script: str = None,
        intent_code: str = None,
        intent_labels: str = None,
        intent_name: str = None,
        is_default: bool = None,
    ):
        self.assist_script = assist_script
        self.intent_code = intent_code
        self.intent_labels = intent_labels
        self.intent_name = intent_name
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assist_script is not None:
            result['assistScript'] = self.assist_script
        if self.intent_code is not None:
            result['intentCode'] = self.intent_code
        if self.intent_labels is not None:
            result['intentLabels'] = self.intent_labels
        if self.intent_name is not None:
            result['intentName'] = self.intent_name
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistScript') is not None:
            self.assist_script = m.get('assistScript')
        if m.get('intentCode') is not None:
            self.intent_code = m.get('intentCode')
        if m.get('intentLabels') is not None:
            self.intent_labels = m.get('intentLabels')
        if m.get('intentName') is not None:
            self.intent_name = m.get('intentName')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        return self


class RealtimeDialogAssistResponseBodyDataAssistSop(TeaModel):
    def __init__(
        self,
        assist_sop: str = None,
        intent_code: str = None,
        intent_name: str = None,
        is_default: bool = None,
    ):
        self.assist_sop = assist_sop
        self.intent_code = intent_code
        self.intent_name = intent_name
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assist_sop is not None:
            result['assistSop'] = self.assist_sop
        if self.intent_code is not None:
            result['intentCode'] = self.intent_code
        if self.intent_name is not None:
            result['intentName'] = self.intent_name
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistSop') is not None:
            self.assist_sop = m.get('assistSop')
        if m.get('intentCode') is not None:
            self.intent_code = m.get('intentCode')
        if m.get('intentName') is not None:
            self.intent_name = m.get('intentName')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        return self


class RealtimeDialogAssistResponseBodyDataConversationModel(TeaModel):
    def __init__(
        self,
        content: str = None,
        customer_id: str = None,
        customer_service_id: str = None,
        customer_service_type: str = None,
        role: str = None,
        type: str = None,
    ):
        self.content = content
        self.customer_id = customer_id
        self.customer_service_id = customer_service_id
        self.customer_service_type = customer_service_type
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.customer_service_id is not None:
            result['customerServiceId'] = self.customer_service_id
        if self.customer_service_type is not None:
            result['customerServiceType'] = self.customer_service_type
        if self.role is not None:
            result['role'] = self.role
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('customerServiceId') is not None:
            self.customer_service_id = m.get('customerServiceId')
        if m.get('customerServiceType') is not None:
            self.customer_service_type = m.get('customerServiceType')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RealtimeDialogAssistResponseBodyData(TeaModel):
    def __init__(
        self,
        analysis_process: str = None,
        assist_scripts: List[RealtimeDialogAssistResponseBodyDataAssistScripts] = None,
        assist_sop: List[RealtimeDialogAssistResponseBodyDataAssistSop] = None,
        conversation_model: List[RealtimeDialogAssistResponseBodyDataConversationModel] = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.analysis_process = analysis_process
        self.assist_scripts = assist_scripts
        self.assist_sop = assist_sop
        self.conversation_model = conversation_model
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        if self.assist_scripts:
            for k in self.assist_scripts:
                if k:
                    k.validate()
        if self.assist_sop:
            for k in self.assist_sop:
                if k:
                    k.validate()
        if self.conversation_model:
            for k in self.conversation_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_process is not None:
            result['analysisProcess'] = self.analysis_process
        result['assistScripts'] = []
        if self.assist_scripts is not None:
            for k in self.assist_scripts:
                result['assistScripts'].append(k.to_map() if k else None)
        result['assistSop'] = []
        if self.assist_sop is not None:
            for k in self.assist_sop:
                result['assistSop'].append(k.to_map() if k else None)
        result['conversationModel'] = []
        if self.conversation_model is not None:
            for k in self.conversation_model:
                result['conversationModel'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisProcess') is not None:
            self.analysis_process = m.get('analysisProcess')
        self.assist_scripts = []
        if m.get('assistScripts') is not None:
            for k in m.get('assistScripts'):
                temp_model = RealtimeDialogAssistResponseBodyDataAssistScripts()
                self.assist_scripts.append(temp_model.from_map(k))
        self.assist_sop = []
        if m.get('assistSop') is not None:
            for k in m.get('assistSop'):
                temp_model = RealtimeDialogAssistResponseBodyDataAssistSop()
                self.assist_sop.append(temp_model.from_map(k))
        self.conversation_model = []
        if m.get('conversationModel') is not None:
            for k in m.get('conversationModel'):
                temp_model = RealtimeDialogAssistResponseBodyDataConversationModel()
                self.conversation_model.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class RealtimeDialogAssistResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: RealtimeDialogAssistResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = RealtimeDialogAssistResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class RealtimeDialogAssistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RealtimeDialogAssistResponseBody = None,
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
            temp_model = RealtimeDialogAssistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebuildTaskRequest(TeaModel):
    def __init__(
        self,
        task_ids: List[str] = None,
    ):
        # This parameter is required.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        return self


class RebuildTaskResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: List[Dict[str, Any]] = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class RebuildTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebuildTaskResponseBody = None,
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
            temp_model = RebuildTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecallDocumentRequestFiltersAnd(TeaModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.boost = boost
        self.key = key
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boost is not None:
            result['boost'] = self.boost
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boost') is not None:
            self.boost = m.get('boost')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class RecallDocumentRequestFiltersOr(TeaModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.boost = boost
        self.key = key
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boost is not None:
            result['boost'] = self.boost
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boost') is not None:
            self.boost = m.get('boost')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class RecallDocumentRequestFilters(TeaModel):
    def __init__(
        self,
        and_: List[RecallDocumentRequestFiltersAnd] = None,
        chunk_type: str = None,
        doc_id_list: List[str] = None,
        library_id: str = None,
        or_: List[RecallDocumentRequestFiltersOr] = None,
        status: List[str] = None,
    ):
        self.and_ = and_
        self.chunk_type = chunk_type
        self.doc_id_list = doc_id_list
        # This parameter is required.
        self.library_id = library_id
        self.or_ = or_
        self.status = status

    def validate(self):
        if self.and_:
            for k in self.and_:
                if k:
                    k.validate()
        if self.or_:
            for k in self.or_:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['and'] = []
        if self.and_ is not None:
            for k in self.and_:
                result['and'].append(k.to_map() if k else None)
        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type
        if self.doc_id_list is not None:
            result['docIdList'] = self.doc_id_list
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        result['or'] = []
        if self.or_ is not None:
            for k in self.or_:
                result['or'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.and_ = []
        if m.get('and') is not None:
            for k in m.get('and'):
                temp_model = RecallDocumentRequestFiltersAnd()
                self.and_.append(temp_model.from_map(k))
        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')
        if m.get('docIdList') is not None:
            self.doc_id_list = m.get('docIdList')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        self.or_ = []
        if m.get('or') is not None:
            for k in m.get('or'):
                temp_model = RecallDocumentRequestFiltersOr()
                self.or_.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class RecallDocumentRequest(TeaModel):
    def __init__(
        self,
        filters: List[RecallDocumentRequestFilters] = None,
        query: str = None,
        rearrangement: bool = None,
        top_k: int = None,
    ):
        self.filters = filters
        # This parameter is required.
        self.query = query
        self.rearrangement = rearrangement
        self.top_k = top_k

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['filters'].append(k.to_map() if k else None)
        if self.query is not None:
            result['query'] = self.query
        if self.rearrangement is not None:
            result['rearrangement'] = self.rearrangement
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('filters') is not None:
            for k in m.get('filters'):
                temp_model = RecallDocumentRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('rearrangement') is not None:
            self.rearrangement = m.get('rearrangement')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class RecallDocumentResponseBodyDataChunkListPos(TeaModel):
    def __init__(
        self,
        axis_array: List[float] = None,
        page: int = None,
        text_highlight_area: List[int] = None,
    ):
        self.axis_array = axis_array
        self.page = page
        self.text_highlight_area = text_highlight_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.axis_array is not None:
            result['axisArray'] = self.axis_array
        if self.page is not None:
            result['page'] = self.page
        if self.text_highlight_area is not None:
            result['textHighlightArea'] = self.text_highlight_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('axisArray') is not None:
            self.axis_array = m.get('axisArray')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('textHighlightArea') is not None:
            self.text_highlight_area = m.get('textHighlightArea')
        return self


class RecallDocumentResponseBodyDataChunkList(TeaModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_meta: Dict[str, Any] = None,
        chunk_oss_url: str = None,
        chunk_text: str = None,
        chunk_type: str = None,
        doc_id: str = None,
        file_type: str = None,
        library_id: str = None,
        library_name: str = None,
        next_chunk_id: str = None,
        pos: List[RecallDocumentResponseBodyDataChunkListPos] = None,
        pre_chunk_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.chunk_id = chunk_id
        self.chunk_meta = chunk_meta
        self.chunk_oss_url = chunk_oss_url
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type
        self.doc_id = doc_id
        self.file_type = file_type
        self.library_id = library_id
        self.library_name = library_name
        self.next_chunk_id = next_chunk_id
        self.pos = pos
        self.pre_chunk_id = pre_chunk_id
        self.score = score
        self.title = title

    def validate(self):
        if self.pos:
            for k in self.pos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id
        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta
        if self.chunk_oss_url is not None:
            result['chunkOssUrl'] = self.chunk_oss_url
        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text
        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.library_name is not None:
            result['libraryName'] = self.library_name
        if self.next_chunk_id is not None:
            result['nextChunkId'] = self.next_chunk_id
        result['pos'] = []
        if self.pos is not None:
            for k in self.pos:
                result['pos'].append(k.to_map() if k else None)
        if self.pre_chunk_id is not None:
            result['preChunkId'] = self.pre_chunk_id
        if self.score is not None:
            result['score'] = self.score
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')
        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')
        if m.get('chunkOssUrl') is not None:
            self.chunk_oss_url = m.get('chunkOssUrl')
        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')
        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')
        if m.get('nextChunkId') is not None:
            self.next_chunk_id = m.get('nextChunkId')
        self.pos = []
        if m.get('pos') is not None:
            for k in m.get('pos'):
                temp_model = RecallDocumentResponseBodyDataChunkListPos()
                self.pos.append(temp_model.from_map(k))
        if m.get('preChunkId') is not None:
            self.pre_chunk_id = m.get('preChunkId')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class RecallDocumentResponseBodyDataChunkPartListPos(TeaModel):
    def __init__(
        self,
        axis_array: List[float] = None,
        page: int = None,
        text_highlight_area: List[int] = None,
    ):
        self.axis_array = axis_array
        self.page = page
        self.text_highlight_area = text_highlight_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.axis_array is not None:
            result['axisArray'] = self.axis_array
        if self.page is not None:
            result['page'] = self.page
        if self.text_highlight_area is not None:
            result['textHighlightArea'] = self.text_highlight_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('axisArray') is not None:
            self.axis_array = m.get('axisArray')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('textHighlightArea') is not None:
            self.text_highlight_area = m.get('textHighlightArea')
        return self


class RecallDocumentResponseBodyDataChunkPartList(TeaModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_meta: Dict[str, Any] = None,
        chunk_oss_url: str = None,
        chunk_text: str = None,
        chunk_type: str = None,
        doc_id: str = None,
        file_type: str = None,
        library_id: str = None,
        library_name: str = None,
        next_chunk_id: str = None,
        pos: List[RecallDocumentResponseBodyDataChunkPartListPos] = None,
        pre_chunk_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.chunk_id = chunk_id
        self.chunk_meta = chunk_meta
        self.chunk_oss_url = chunk_oss_url
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type
        self.doc_id = doc_id
        self.file_type = file_type
        self.library_id = library_id
        self.library_name = library_name
        self.next_chunk_id = next_chunk_id
        self.pos = pos
        self.pre_chunk_id = pre_chunk_id
        self.score = score
        self.title = title

    def validate(self):
        if self.pos:
            for k in self.pos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id
        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta
        if self.chunk_oss_url is not None:
            result['chunkOssUrl'] = self.chunk_oss_url
        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text
        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.library_name is not None:
            result['libraryName'] = self.library_name
        if self.next_chunk_id is not None:
            result['nextChunkId'] = self.next_chunk_id
        result['pos'] = []
        if self.pos is not None:
            for k in self.pos:
                result['pos'].append(k.to_map() if k else None)
        if self.pre_chunk_id is not None:
            result['preChunkId'] = self.pre_chunk_id
        if self.score is not None:
            result['score'] = self.score
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')
        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')
        if m.get('chunkOssUrl') is not None:
            self.chunk_oss_url = m.get('chunkOssUrl')
        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')
        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')
        if m.get('nextChunkId') is not None:
            self.next_chunk_id = m.get('nextChunkId')
        self.pos = []
        if m.get('pos') is not None:
            for k in m.get('pos'):
                temp_model = RecallDocumentResponseBodyDataChunkPartListPos()
                self.pos.append(temp_model.from_map(k))
        if m.get('preChunkId') is not None:
            self.pre_chunk_id = m.get('preChunkId')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class RecallDocumentResponseBodyDataDocuments(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        document_meta: Dict[str, Any] = None,
        file_type: str = None,
        gmt_create: str = None,
        library_id: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.document_meta = document_meta
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.library_id = library_id
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.document_meta is not None:
            result['documentMeta'] = self.document_meta
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('documentMeta') is not None:
            self.document_meta = m.get('documentMeta')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class RecallDocumentResponseBodyDataTextChunkListPos(TeaModel):
    def __init__(
        self,
        axis_array: List[float] = None,
        page: int = None,
        text_highlight_area: List[int] = None,
    ):
        self.axis_array = axis_array
        self.page = page
        self.text_highlight_area = text_highlight_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.axis_array is not None:
            result['axisArray'] = self.axis_array
        if self.page is not None:
            result['page'] = self.page
        if self.text_highlight_area is not None:
            result['textHighlightArea'] = self.text_highlight_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('axisArray') is not None:
            self.axis_array = m.get('axisArray')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('textHighlightArea') is not None:
            self.text_highlight_area = m.get('textHighlightArea')
        return self


class RecallDocumentResponseBodyDataTextChunkList(TeaModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_meta: Dict[str, Any] = None,
        chunk_oss_url: str = None,
        chunk_text: str = None,
        chunk_type: str = None,
        doc_id: str = None,
        file_type: str = None,
        library_id: str = None,
        library_name: str = None,
        next_chunk_id: str = None,
        pos: List[RecallDocumentResponseBodyDataTextChunkListPos] = None,
        pre_chunk_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.chunk_id = chunk_id
        self.chunk_meta = chunk_meta
        self.chunk_oss_url = chunk_oss_url
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type
        self.doc_id = doc_id
        self.file_type = file_type
        self.library_id = library_id
        self.library_name = library_name
        self.next_chunk_id = next_chunk_id
        self.pos = pos
        self.pre_chunk_id = pre_chunk_id
        self.score = score
        self.title = title

    def validate(self):
        if self.pos:
            for k in self.pos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id
        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta
        if self.chunk_oss_url is not None:
            result['chunkOssUrl'] = self.chunk_oss_url
        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text
        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.library_name is not None:
            result['libraryName'] = self.library_name
        if self.next_chunk_id is not None:
            result['nextChunkId'] = self.next_chunk_id
        result['pos'] = []
        if self.pos is not None:
            for k in self.pos:
                result['pos'].append(k.to_map() if k else None)
        if self.pre_chunk_id is not None:
            result['preChunkId'] = self.pre_chunk_id
        if self.score is not None:
            result['score'] = self.score
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')
        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')
        if m.get('chunkOssUrl') is not None:
            self.chunk_oss_url = m.get('chunkOssUrl')
        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')
        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')
        if m.get('nextChunkId') is not None:
            self.next_chunk_id = m.get('nextChunkId')
        self.pos = []
        if m.get('pos') is not None:
            for k in m.get('pos'):
                temp_model = RecallDocumentResponseBodyDataTextChunkListPos()
                self.pos.append(temp_model.from_map(k))
        if m.get('preChunkId') is not None:
            self.pre_chunk_id = m.get('preChunkId')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class RecallDocumentResponseBodyDataVectorChunkListPos(TeaModel):
    def __init__(
        self,
        axis_array: List[float] = None,
        page: int = None,
        text_highlight_area: List[int] = None,
    ):
        self.axis_array = axis_array
        self.page = page
        self.text_highlight_area = text_highlight_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.axis_array is not None:
            result['axisArray'] = self.axis_array
        if self.page is not None:
            result['page'] = self.page
        if self.text_highlight_area is not None:
            result['textHighlightArea'] = self.text_highlight_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('axisArray') is not None:
            self.axis_array = m.get('axisArray')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('textHighlightArea') is not None:
            self.text_highlight_area = m.get('textHighlightArea')
        return self


class RecallDocumentResponseBodyDataVectorChunkList(TeaModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_meta: Dict[str, Any] = None,
        chunk_oss_url: str = None,
        chunk_text: str = None,
        chunk_type: str = None,
        doc_id: str = None,
        file_type: str = None,
        library_id: str = None,
        library_name: str = None,
        next_chunk_id: str = None,
        pos: List[RecallDocumentResponseBodyDataVectorChunkListPos] = None,
        pre_chunk_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.chunk_id = chunk_id
        self.chunk_meta = chunk_meta
        self.chunk_oss_url = chunk_oss_url
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type
        self.doc_id = doc_id
        self.file_type = file_type
        self.library_id = library_id
        self.library_name = library_name
        self.next_chunk_id = next_chunk_id
        self.pos = pos
        self.pre_chunk_id = pre_chunk_id
        self.score = score
        self.title = title

    def validate(self):
        if self.pos:
            for k in self.pos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id
        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta
        if self.chunk_oss_url is not None:
            result['chunkOssUrl'] = self.chunk_oss_url
        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text
        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.library_name is not None:
            result['libraryName'] = self.library_name
        if self.next_chunk_id is not None:
            result['nextChunkId'] = self.next_chunk_id
        result['pos'] = []
        if self.pos is not None:
            for k in self.pos:
                result['pos'].append(k.to_map() if k else None)
        if self.pre_chunk_id is not None:
            result['preChunkId'] = self.pre_chunk_id
        if self.score is not None:
            result['score'] = self.score
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')
        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')
        if m.get('chunkOssUrl') is not None:
            self.chunk_oss_url = m.get('chunkOssUrl')
        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')
        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')
        if m.get('nextChunkId') is not None:
            self.next_chunk_id = m.get('nextChunkId')
        self.pos = []
        if m.get('pos') is not None:
            for k in m.get('pos'):
                temp_model = RecallDocumentResponseBodyDataVectorChunkListPos()
                self.pos.append(temp_model.from_map(k))
        if m.get('preChunkId') is not None:
            self.pre_chunk_id = m.get('preChunkId')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class RecallDocumentResponseBodyData(TeaModel):
    def __init__(
        self,
        chunk_list: List[RecallDocumentResponseBodyDataChunkList] = None,
        chunk_part_list: List[RecallDocumentResponseBodyDataChunkPartList] = None,
        chunk_text_list: List[str] = None,
        documents: List[RecallDocumentResponseBodyDataDocuments] = None,
        embedding_elapsed_ms: int = None,
        text_chunk_list: List[RecallDocumentResponseBodyDataTextChunkList] = None,
        text_search_elapsed_ms: int = None,
        total_elapsed_ms: int = None,
        vector_chunk_list: List[RecallDocumentResponseBodyDataVectorChunkList] = None,
        vector_search_elapsed_ms: int = None,
    ):
        self.chunk_list = chunk_list
        self.chunk_part_list = chunk_part_list
        self.chunk_text_list = chunk_text_list
        self.documents = documents
        self.embedding_elapsed_ms = embedding_elapsed_ms
        self.text_chunk_list = text_chunk_list
        self.text_search_elapsed_ms = text_search_elapsed_ms
        self.total_elapsed_ms = total_elapsed_ms
        self.vector_chunk_list = vector_chunk_list
        self.vector_search_elapsed_ms = vector_search_elapsed_ms

    def validate(self):
        if self.chunk_list:
            for k in self.chunk_list:
                if k:
                    k.validate()
        if self.chunk_part_list:
            for k in self.chunk_part_list:
                if k:
                    k.validate()
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()
        if self.text_chunk_list:
            for k in self.text_chunk_list:
                if k:
                    k.validate()
        if self.vector_chunk_list:
            for k in self.vector_chunk_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['chunkList'] = []
        if self.chunk_list is not None:
            for k in self.chunk_list:
                result['chunkList'].append(k.to_map() if k else None)
        result['chunkPartList'] = []
        if self.chunk_part_list is not None:
            for k in self.chunk_part_list:
                result['chunkPartList'].append(k.to_map() if k else None)
        if self.chunk_text_list is not None:
            result['chunkTextList'] = self.chunk_text_list
        result['documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['documents'].append(k.to_map() if k else None)
        if self.embedding_elapsed_ms is not None:
            result['embeddingElapsedMs'] = self.embedding_elapsed_ms
        result['textChunkList'] = []
        if self.text_chunk_list is not None:
            for k in self.text_chunk_list:
                result['textChunkList'].append(k.to_map() if k else None)
        if self.text_search_elapsed_ms is not None:
            result['textSearchElapsedMs'] = self.text_search_elapsed_ms
        if self.total_elapsed_ms is not None:
            result['totalElapsedMs'] = self.total_elapsed_ms
        result['vectorChunkList'] = []
        if self.vector_chunk_list is not None:
            for k in self.vector_chunk_list:
                result['vectorChunkList'].append(k.to_map() if k else None)
        if self.vector_search_elapsed_ms is not None:
            result['vectorSearchElapsedMs'] = self.vector_search_elapsed_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunk_list = []
        if m.get('chunkList') is not None:
            for k in m.get('chunkList'):
                temp_model = RecallDocumentResponseBodyDataChunkList()
                self.chunk_list.append(temp_model.from_map(k))
        self.chunk_part_list = []
        if m.get('chunkPartList') is not None:
            for k in m.get('chunkPartList'):
                temp_model = RecallDocumentResponseBodyDataChunkPartList()
                self.chunk_part_list.append(temp_model.from_map(k))
        if m.get('chunkTextList') is not None:
            self.chunk_text_list = m.get('chunkTextList')
        self.documents = []
        if m.get('documents') is not None:
            for k in m.get('documents'):
                temp_model = RecallDocumentResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('embeddingElapsedMs') is not None:
            self.embedding_elapsed_ms = m.get('embeddingElapsedMs')
        self.text_chunk_list = []
        if m.get('textChunkList') is not None:
            for k in m.get('textChunkList'):
                temp_model = RecallDocumentResponseBodyDataTextChunkList()
                self.text_chunk_list.append(temp_model.from_map(k))
        if m.get('textSearchElapsedMs') is not None:
            self.text_search_elapsed_ms = m.get('textSearchElapsedMs')
        if m.get('totalElapsedMs') is not None:
            self.total_elapsed_ms = m.get('totalElapsedMs')
        self.vector_chunk_list = []
        if m.get('vectorChunkList') is not None:
            for k in m.get('vectorChunkList'):
                temp_model = RecallDocumentResponseBodyDataVectorChunkList()
                self.vector_chunk_list.append(temp_model.from_map(k))
        if m.get('vectorSearchElapsedMs') is not None:
            self.vector_search_elapsed_ms = m.get('vectorSearchElapsedMs')
        return self


class RecallDocumentResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: RecallDocumentResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = RecallDocumentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class RecallDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecallDocumentResponseBody = None,
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
            temp_model = RecallDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeIntentionRequestGlobalIntentionList(TeaModel):
    def __init__(
        self,
        description: str = None,
        intention: str = None,
        intention_code: str = None,
        intention_script: str = None,
    ):
        self.description = description
        self.intention = intention
        self.intention_code = intention_code
        self.intention_script = intention_script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.intention is not None:
            result['intention'] = self.intention
        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code
        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('intention') is not None:
            self.intention = m.get('intention')
        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')
        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')
        return self


class RecognizeIntentionRequestHierarchicalIntentionList(TeaModel):
    def __init__(
        self,
        description: str = None,
        intention: str = None,
        intention_code: str = None,
        intention_script: str = None,
    ):
        self.description = description
        self.intention = intention
        self.intention_code = intention_code
        self.intention_script = intention_script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.intention is not None:
            result['intention'] = self.intention
        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code
        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('intention') is not None:
            self.intention = m.get('intention')
        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')
        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')
        return self


class RecognizeIntentionRequestIntentionList(TeaModel):
    def __init__(
        self,
        description: str = None,
        intention: str = None,
        intention_code: str = None,
        intention_script: str = None,
    ):
        self.description = description
        self.intention = intention
        self.intention_code = intention_code
        self.intention_script = intention_script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.intention is not None:
            result['intention'] = self.intention
        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code
        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('intention') is not None:
            self.intention = m.get('intention')
        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')
        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')
        return self


class RecognizeIntentionRequest(TeaModel):
    def __init__(
        self,
        analysis: bool = None,
        biz_type: str = None,
        conversation: str = None,
        global_intention_list: List[RecognizeIntentionRequestGlobalIntentionList] = None,
        hierarchical_intention_list: List[RecognizeIntentionRequestHierarchicalIntentionList] = None,
        intention_domain_code: str = None,
        intention_list: List[RecognizeIntentionRequestIntentionList] = None,
        op_type: str = None,
        recommend: bool = None,
    ):
        self.analysis = analysis
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.conversation = conversation
        self.global_intention_list = global_intention_list
        self.hierarchical_intention_list = hierarchical_intention_list
        self.intention_domain_code = intention_domain_code
        self.intention_list = intention_list
        self.op_type = op_type
        self.recommend = recommend

    def validate(self):
        if self.global_intention_list:
            for k in self.global_intention_list:
                if k:
                    k.validate()
        if self.hierarchical_intention_list:
            for k in self.hierarchical_intention_list:
                if k:
                    k.validate()
        if self.intention_list:
            for k in self.intention_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis is not None:
            result['analysis'] = self.analysis
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.conversation is not None:
            result['conversation'] = self.conversation
        result['globalIntentionList'] = []
        if self.global_intention_list is not None:
            for k in self.global_intention_list:
                result['globalIntentionList'].append(k.to_map() if k else None)
        result['hierarchicalIntentionList'] = []
        if self.hierarchical_intention_list is not None:
            for k in self.hierarchical_intention_list:
                result['hierarchicalIntentionList'].append(k.to_map() if k else None)
        if self.intention_domain_code is not None:
            result['intentionDomainCode'] = self.intention_domain_code
        result['intentionList'] = []
        if self.intention_list is not None:
            for k in self.intention_list:
                result['intentionList'].append(k.to_map() if k else None)
        if self.op_type is not None:
            result['opType'] = self.op_type
        if self.recommend is not None:
            result['recommend'] = self.recommend
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis') is not None:
            self.analysis = m.get('analysis')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('conversation') is not None:
            self.conversation = m.get('conversation')
        self.global_intention_list = []
        if m.get('globalIntentionList') is not None:
            for k in m.get('globalIntentionList'):
                temp_model = RecognizeIntentionRequestGlobalIntentionList()
                self.global_intention_list.append(temp_model.from_map(k))
        self.hierarchical_intention_list = []
        if m.get('hierarchicalIntentionList') is not None:
            for k in m.get('hierarchicalIntentionList'):
                temp_model = RecognizeIntentionRequestHierarchicalIntentionList()
                self.hierarchical_intention_list.append(temp_model.from_map(k))
        if m.get('intentionDomainCode') is not None:
            self.intention_domain_code = m.get('intentionDomainCode')
        self.intention_list = []
        if m.get('intentionList') is not None:
            for k in m.get('intentionList'):
                temp_model = RecognizeIntentionRequestIntentionList()
                self.intention_list.append(temp_model.from_map(k))
        if m.get('opType') is not None:
            self.op_type = m.get('opType')
        if m.get('recommend') is not None:
            self.recommend = m.get('recommend')
        return self


class RecognizeIntentionResponseBodyData(TeaModel):
    def __init__(
        self,
        analysis_process: str = None,
        intention_code: str = None,
        intention_name: str = None,
        intention_script: str = None,
        recommend_intention: str = None,
        recommend_script: str = None,
    ):
        self.analysis_process = analysis_process
        self.intention_code = intention_code
        self.intention_name = intention_name
        self.intention_script = intention_script
        self.recommend_intention = recommend_intention
        self.recommend_script = recommend_script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_process is not None:
            result['analysisProcess'] = self.analysis_process
        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code
        if self.intention_name is not None:
            result['intentionName'] = self.intention_name
        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script
        if self.recommend_intention is not None:
            result['recommendIntention'] = self.recommend_intention
        if self.recommend_script is not None:
            result['recommendScript'] = self.recommend_script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisProcess') is not None:
            self.analysis_process = m.get('analysisProcess')
        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')
        if m.get('intentionName') is not None:
            self.intention_name = m.get('intentionName')
        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')
        if m.get('recommendIntention') is not None:
            self.recommend_intention = m.get('recommendIntention')
        if m.get('recommendScript') is not None:
            self.recommend_script = m.get('recommendScript')
        return self


class RecognizeIntentionResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: RecognizeIntentionResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = RecognizeIntentionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class RecognizeIntentionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeIntentionResponseBody = None,
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
            temp_model = RecognizeIntentionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunAgentRequest(TeaModel):
    def __init__(
        self,
        bot_id: str = None,
        model_id: str = None,
        stream: bool = None,
        thread_id: str = None,
        use_draft: bool = None,
        user_content: str = None,
        user_inputs: Dict[str, Any] = None,
        version_id: str = None,
    ):
        # This parameter is required.
        self.bot_id = bot_id
        self.model_id = model_id
        self.stream = stream
        self.thread_id = thread_id
        self.use_draft = use_draft
        # This parameter is required.
        self.user_content = user_content
        self.user_inputs = user_inputs
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bot_id is not None:
            result['botId'] = self.bot_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.stream is not None:
            result['stream'] = self.stream
        if self.thread_id is not None:
            result['threadId'] = self.thread_id
        if self.use_draft is not None:
            result['useDraft'] = self.use_draft
        if self.user_content is not None:
            result['userContent'] = self.user_content
        if self.user_inputs is not None:
            result['userInputs'] = self.user_inputs
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('botId') is not None:
            self.bot_id = m.get('botId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')
        if m.get('useDraft') is not None:
            self.use_draft = m.get('useDraft')
        if m.get('userContent') is not None:
            self.user_content = m.get('userContent')
        if m.get('userInputs') is not None:
            self.user_inputs = m.get('userInputs')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class RunAgentResponseBodyDataFunctionCallResponses(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        end_time: str = None,
        function_args: str = None,
        function_name: str = None,
        result: str = None,
        start_time: str = None,
    ):
        self.display_name = display_name
        self.end_time = end_time
        self.function_args = function_args
        self.function_name = function_name
        self.result = result
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.function_args is not None:
            result['functionArgs'] = self.function_args
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.result is not None:
            result['result'] = self.result
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('functionArgs') is not None:
            self.function_args = m.get('functionArgs')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class RunAgentResponseBodyDataResponseChoicesMessage(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
        role_display_name: str = None,
    ):
        self.content = content
        self.role = role
        self.role_display_name = role_display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        if self.role_display_name is not None:
            result['roleDisplayName'] = self.role_display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('roleDisplayName') is not None:
            self.role_display_name = m.get('roleDisplayName')
        return self


class RunAgentResponseBodyDataResponseChoices(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        index: int = None,
        message: RunAgentResponseBodyDataResponseChoicesMessage = None,
    ):
        self.finish_reason = finish_reason
        self.index = index
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.index is not None:
            result['index'] = self.index
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('message') is not None:
            temp_model = RunAgentResponseBodyDataResponseChoicesMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class RunAgentResponseBodyDataResponse(TeaModel):
    def __init__(
        self,
        choices: List[RunAgentResponseBodyDataResponseChoices] = None,
        created: int = None,
        id: str = None,
        model_id: str = None,
        time: str = None,
    ):
        self.choices = choices
        self.created = created
        self.id = id
        self.model_id = model_id
        self.time = time

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['choices'].append(k.to_map() if k else None)
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k in m.get('choices'):
                temp_model = RunAgentResponseBodyDataResponseChoices()
                self.choices.append(temp_model.from_map(k))
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class RunAgentResponseBodyData(TeaModel):
    def __init__(
        self,
        function_call_responses: List[RunAgentResponseBodyDataFunctionCallResponses] = None,
        input_tokens: int = None,
        output_tokens: int = None,
        response: RunAgentResponseBodyDataResponse = None,
        thread_id: str = None,
        trace_id: str = None,
        version_id: str = None,
    ):
        self.function_call_responses = function_call_responses
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.response = response
        self.thread_id = thread_id
        self.trace_id = trace_id
        self.version_id = version_id

    def validate(self):
        if self.function_call_responses:
            for k in self.function_call_responses:
                if k:
                    k.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['functionCallResponses'] = []
        if self.function_call_responses is not None:
            for k in self.function_call_responses:
                result['functionCallResponses'].append(k.to_map() if k else None)
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.response is not None:
            result['response'] = self.response.to_map()
        if self.thread_id is not None:
            result['threadId'] = self.thread_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function_call_responses = []
        if m.get('functionCallResponses') is not None:
            for k in m.get('functionCallResponses'):
                temp_model = RunAgentResponseBodyDataFunctionCallResponses()
                self.function_call_responses.append(temp_model.from_map(k))
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('response') is not None:
            temp_model = RunAgentResponseBodyDataResponse()
            self.response = temp_model.from_map(m['response'])
        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class RunAgentResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: RunAgentResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = RunAgentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class RunAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunAgentResponseBody = None,
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
            temp_model = RunAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunChatResultGenerationRequestMessages(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class RunChatResultGenerationRequestToolsFunctionParameters(TeaModel):
    def __init__(
        self,
        properties: Dict[str, Any] = None,
        type: str = None,
    ):
        self.properties = properties
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RunChatResultGenerationRequestToolsFunction(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        parameters: RunChatResultGenerationRequestToolsFunctionParameters = None,
        required: List[str] = None,
    ):
        self.description = description
        self.name = name
        self.parameters = parameters
        self.required = required

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameters') is not None:
            temp_model = RunChatResultGenerationRequestToolsFunctionParameters()
            self.parameters = temp_model.from_map(m['parameters'])
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class RunChatResultGenerationRequestTools(TeaModel):
    def __init__(
        self,
        function: RunChatResultGenerationRequestToolsFunction = None,
        type: str = None,
    ):
        self.function = function
        self.type = type

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function is not None:
            result['function'] = self.function.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('function') is not None:
            temp_model = RunChatResultGenerationRequestToolsFunction()
            self.function = temp_model.from_map(m['function'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RunChatResultGenerationRequest(TeaModel):
    def __init__(
        self,
        inference_parameters: Dict[str, Any] = None,
        messages: List[RunChatResultGenerationRequestMessages] = None,
        model_id: str = None,
        session_id: str = None,
        stream: bool = None,
        tools: List[RunChatResultGenerationRequestTools] = None,
    ):
        self.inference_parameters = inference_parameters
        # This parameter is required.
        self.messages = messages
        # This parameter is required.
        self.model_id = model_id
        self.session_id = session_id
        self.stream = stream
        self.tools = tools

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()
        if self.tools:
            for k in self.tools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inference_parameters is not None:
            result['inferenceParameters'] = self.inference_parameters
        result['messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['messages'].append(k.to_map() if k else None)
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.stream is not None:
            result['stream'] = self.stream
        result['tools'] = []
        if self.tools is not None:
            for k in self.tools:
                result['tools'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inferenceParameters') is not None:
            self.inference_parameters = m.get('inferenceParameters')
        self.messages = []
        if m.get('messages') is not None:
            for k in m.get('messages'):
                temp_model = RunChatResultGenerationRequestMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        self.tools = []
        if m.get('tools') is not None:
            for k in m.get('tools'):
                temp_model = RunChatResultGenerationRequestTools()
                self.tools.append(temp_model.from_map(k))
        return self


class RunChatResultGenerationResponseBodyChoicesMessage(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
        tool_calls: List[Dict[str, Any]] = None,
    ):
        self.content = content
        self.role = role
        self.tool_calls = tool_calls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        if self.tool_calls is not None:
            result['toolCalls'] = self.tool_calls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('toolCalls') is not None:
            self.tool_calls = m.get('toolCalls')
        return self


class RunChatResultGenerationResponseBodyChoices(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        index: int = None,
        message: RunChatResultGenerationResponseBodyChoicesMessage = None,
    ):
        self.finish_reason = finish_reason
        self.index = index
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.index is not None:
            result['index'] = self.index
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('message') is not None:
            temp_model = RunChatResultGenerationResponseBodyChoicesMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class RunChatResultGenerationResponseBodyUsage(TeaModel):
    def __init__(
        self,
        image_count: int = None,
        image_tokens: int = None,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.image_count = image_count
        self.image_tokens = image_tokens
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_count is not None:
            result['imageCount'] = self.image_count
        if self.image_tokens is not None:
            result['imageTokens'] = self.image_tokens
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')
        if m.get('imageTokens') is not None:
            self.image_tokens = m.get('imageTokens')
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunChatResultGenerationResponseBody(TeaModel):
    def __init__(
        self,
        choices: List[RunChatResultGenerationResponseBodyChoices] = None,
        created: int = None,
        id: str = None,
        model_id: str = None,
        request_id: str = None,
        time: str = None,
        total_tokens: int = None,
        usage: RunChatResultGenerationResponseBodyUsage = None,
    ):
        self.choices = choices
        self.created = created
        self.id = id
        self.model_id = model_id
        self.request_id = request_id
        self.time = time
        self.total_tokens = total_tokens
        self.usage = usage

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['choices'].append(k.to_map() if k else None)
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.time is not None:
            result['time'] = self.time
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k in m.get('choices'):
                temp_model = RunChatResultGenerationResponseBodyChoices()
                self.choices.append(temp_model.from_map(k))
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        if m.get('usage') is not None:
            temp_model = RunChatResultGenerationResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunChatResultGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunChatResultGenerationResponseBody = None,
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
            temp_model = RunChatResultGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunLibraryChatGenerationRequestQueryCriteriaAnd(TeaModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.boost = boost
        self.key = key
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boost is not None:
            result['boost'] = self.boost
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boost') is not None:
            self.boost = m.get('boost')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class RunLibraryChatGenerationRequestQueryCriteriaOr(TeaModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.boost = boost
        self.key = key
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boost is not None:
            result['boost'] = self.boost
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boost') is not None:
            self.boost = m.get('boost')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class RunLibraryChatGenerationRequestQueryCriteria(TeaModel):
    def __init__(
        self,
        and_: List[RunLibraryChatGenerationRequestQueryCriteriaAnd] = None,
        or_: List[RunLibraryChatGenerationRequestQueryCriteriaOr] = None,
    ):
        self.and_ = and_
        self.or_ = or_

    def validate(self):
        if self.and_:
            for k in self.and_:
                if k:
                    k.validate()
        if self.or_:
            for k in self.or_:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['and'] = []
        if self.and_ is not None:
            for k in self.and_:
                result['and'].append(k.to_map() if k else None)
        result['or'] = []
        if self.or_ is not None:
            for k in self.or_:
                result['or'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.and_ = []
        if m.get('and') is not None:
            for k in m.get('and'):
                temp_model = RunLibraryChatGenerationRequestQueryCriteriaAnd()
                self.and_.append(temp_model.from_map(k))
        self.or_ = []
        if m.get('or') is not None:
            for k in m.get('or'):
                temp_model = RunLibraryChatGenerationRequestQueryCriteriaOr()
                self.or_.append(temp_model.from_map(k))
        return self


class RunLibraryChatGenerationRequestTextSearchParameter(TeaModel):
    def __init__(
        self,
        limit: int = None,
        search_analyzer_type: str = None,
    ):
        self.limit = limit
        self.search_analyzer_type = search_analyzer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.search_analyzer_type is not None:
            result['searchAnalyzerType'] = self.search_analyzer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('searchAnalyzerType') is not None:
            self.search_analyzer_type = m.get('searchAnalyzerType')
        return self


class RunLibraryChatGenerationRequestVectorSearchParameter(TeaModel):
    def __init__(
        self,
        limit: int = None,
    ):
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class RunLibraryChatGenerationRequest(TeaModel):
    def __init__(
        self,
        doc_id_list: List[str] = None,
        enable_follow_up: bool = None,
        enable_multi_query: bool = None,
        enable_open_qa: bool = None,
        follow_up_llm: str = None,
        library_id: str = None,
        llm_type: str = None,
        multi_query_llm: str = None,
        query: str = None,
        query_criteria: RunLibraryChatGenerationRequestQueryCriteria = None,
        rerank_type: str = None,
        session_id: str = None,
        stream: bool = None,
        sub_query_list: List[str] = None,
        text_search_parameter: RunLibraryChatGenerationRequestTextSearchParameter = None,
        top_k: int = None,
        vector_search_parameter: RunLibraryChatGenerationRequestVectorSearchParameter = None,
        with_document_reference: bool = None,
    ):
        self.doc_id_list = doc_id_list
        self.enable_follow_up = enable_follow_up
        self.enable_multi_query = enable_multi_query
        self.enable_open_qa = enable_open_qa
        self.follow_up_llm = follow_up_llm
        # This parameter is required.
        self.library_id = library_id
        # This parameter is required.
        self.llm_type = llm_type
        self.multi_query_llm = multi_query_llm
        # This parameter is required.
        self.query = query
        self.query_criteria = query_criteria
        self.rerank_type = rerank_type
        # sessionId
        self.session_id = session_id
        self.stream = stream
        self.sub_query_list = sub_query_list
        self.text_search_parameter = text_search_parameter
        self.top_k = top_k
        self.vector_search_parameter = vector_search_parameter
        self.with_document_reference = with_document_reference

    def validate(self):
        if self.query_criteria:
            self.query_criteria.validate()
        if self.text_search_parameter:
            self.text_search_parameter.validate()
        if self.vector_search_parameter:
            self.vector_search_parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id_list is not None:
            result['docIdList'] = self.doc_id_list
        if self.enable_follow_up is not None:
            result['enableFollowUp'] = self.enable_follow_up
        if self.enable_multi_query is not None:
            result['enableMultiQuery'] = self.enable_multi_query
        if self.enable_open_qa is not None:
            result['enableOpenQa'] = self.enable_open_qa
        if self.follow_up_llm is not None:
            result['followUpLlm'] = self.follow_up_llm
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.llm_type is not None:
            result['llmType'] = self.llm_type
        if self.multi_query_llm is not None:
            result['multiQueryLlm'] = self.multi_query_llm
        if self.query is not None:
            result['query'] = self.query
        if self.query_criteria is not None:
            result['queryCriteria'] = self.query_criteria.to_map()
        if self.rerank_type is not None:
            result['rerankType'] = self.rerank_type
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.stream is not None:
            result['stream'] = self.stream
        if self.sub_query_list is not None:
            result['subQueryList'] = self.sub_query_list
        if self.text_search_parameter is not None:
            result['textSearchParameter'] = self.text_search_parameter.to_map()
        if self.top_k is not None:
            result['topK'] = self.top_k
        if self.vector_search_parameter is not None:
            result['vectorSearchParameter'] = self.vector_search_parameter.to_map()
        if self.with_document_reference is not None:
            result['withDocumentReference'] = self.with_document_reference
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docIdList') is not None:
            self.doc_id_list = m.get('docIdList')
        if m.get('enableFollowUp') is not None:
            self.enable_follow_up = m.get('enableFollowUp')
        if m.get('enableMultiQuery') is not None:
            self.enable_multi_query = m.get('enableMultiQuery')
        if m.get('enableOpenQa') is not None:
            self.enable_open_qa = m.get('enableOpenQa')
        if m.get('followUpLlm') is not None:
            self.follow_up_llm = m.get('followUpLlm')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('llmType') is not None:
            self.llm_type = m.get('llmType')
        if m.get('multiQueryLlm') is not None:
            self.multi_query_llm = m.get('multiQueryLlm')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('queryCriteria') is not None:
            temp_model = RunLibraryChatGenerationRequestQueryCriteria()
            self.query_criteria = temp_model.from_map(m['queryCriteria'])
        if m.get('rerankType') is not None:
            self.rerank_type = m.get('rerankType')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('subQueryList') is not None:
            self.sub_query_list = m.get('subQueryList')
        if m.get('textSearchParameter') is not None:
            temp_model = RunLibraryChatGenerationRequestTextSearchParameter()
            self.text_search_parameter = temp_model.from_map(m['textSearchParameter'])
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        if m.get('vectorSearchParameter') is not None:
            temp_model = RunLibraryChatGenerationRequestVectorSearchParameter()
            self.vector_search_parameter = temp_model.from_map(m['vectorSearchParameter'])
        if m.get('withDocumentReference') is not None:
            self.with_document_reference = m.get('withDocumentReference')
        return self


class RunLibraryChatGenerationResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: Any = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class RunLibraryChatGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunLibraryChatGenerationResponseBody = None,
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
            temp_model = RunLibraryChatGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitChatQuestionRequestQuestionList(TeaModel):
    def __init__(
        self,
        content: str = None,
        gmt_create: str = None,
        reply: str = None,
        session_id: str = None,
        type: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.gmt_create = gmt_create
        self.reply = reply
        # This parameter is required.
        self.session_id = session_id
        self.type = type
        # This parameter is required.
        self.user_id = user_id
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.reply is not None:
            result['reply'] = self.reply
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('reply') is not None:
            self.reply = m.get('reply')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class SubmitChatQuestionRequest(TeaModel):
    def __init__(
        self,
        gmt_service: str = None,
        live_script_content: str = None,
        open_small_talk: bool = None,
        question_list: List[SubmitChatQuestionRequestQuestionList] = None,
        request_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.gmt_service = gmt_service
        # This parameter is required.
        self.live_script_content = live_script_content
        self.open_small_talk = open_small_talk
        # This parameter is required.
        self.question_list = question_list
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        if self.question_list:
            for k in self.question_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_service is not None:
            result['gmtService'] = self.gmt_service
        if self.live_script_content is not None:
            result['liveScriptContent'] = self.live_script_content
        if self.open_small_talk is not None:
            result['openSmallTalk'] = self.open_small_talk
        result['questionList'] = []
        if self.question_list is not None:
            for k in self.question_list:
                result['questionList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtService') is not None:
            self.gmt_service = m.get('gmtService')
        if m.get('liveScriptContent') is not None:
            self.live_script_content = m.get('liveScriptContent')
        if m.get('openSmallTalk') is not None:
            self.open_small_talk = m.get('openSmallTalk')
        self.question_list = []
        if m.get('questionList') is not None:
            for k in m.get('questionList'):
                temp_model = SubmitChatQuestionRequestQuestionList()
                self.question_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class SubmitChatQuestionResponseBodyData(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
    ):
        self.batch_id = batch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['batchId'] = self.batch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')
        return self


class SubmitChatQuestionResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: SubmitChatQuestionResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = SubmitChatQuestionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class SubmitChatQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitChatQuestionResponseBody = None,
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
            temp_model = SubmitChatQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDocumentRequest(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        library_id: str = None,
        meta: Dict[str, Any] = None,
        title: str = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        # This parameter is required.
        self.library_id = library_id
        self.meta = meta
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.meta is not None:
            result['meta'] = self.meta
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class UpdateDocumentResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class UpdateDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDocumentResponseBody = None,
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
            temp_model = UpdateDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDocumentChunkRequestChunks(TeaModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_text: str = None,
    ):
        # This parameter is required.
        self.chunk_id = chunk_id
        # This parameter is required.
        self.chunk_text = chunk_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id
        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')
        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')
        return self


class UpdateDocumentChunkRequest(TeaModel):
    def __init__(
        self,
        chunks: List[UpdateDocumentChunkRequestChunks] = None,
        library_id: str = None,
    ):
        # This parameter is required.
        self.chunks = chunks
        # This parameter is required.
        self.library_id = library_id

    def validate(self):
        if self.chunks:
            for k in self.chunks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['chunks'] = []
        if self.chunks is not None:
            for k in self.chunks:
                result['chunks'].append(k.to_map() if k else None)
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('chunks') is not None:
            for k in m.get('chunks'):
                temp_model = UpdateDocumentChunkRequestChunks()
                self.chunks.append(temp_model.from_map(k))
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        return self


class UpdateDocumentChunkResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class UpdateDocumentChunkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDocumentChunkResponseBody = None,
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
            temp_model = UpdateDocumentChunkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLibraryRequestIndexSettingChunkStrategy(TeaModel):
    def __init__(
        self,
        doc_tree_split: bool = None,
        doc_tree_split_size: int = None,
        enhance_graph: bool = None,
        enhance_table: bool = None,
        overlap: int = None,
        sentence_split: bool = None,
        sentence_split_size: int = None,
        size: int = None,
        split: bool = None,
    ):
        self.doc_tree_split = doc_tree_split
        self.doc_tree_split_size = doc_tree_split_size
        self.enhance_graph = enhance_graph
        self.enhance_table = enhance_table
        self.overlap = overlap
        self.sentence_split = sentence_split
        self.sentence_split_size = sentence_split_size
        self.size = size
        self.split = split

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_tree_split is not None:
            result['docTreeSplit'] = self.doc_tree_split
        if self.doc_tree_split_size is not None:
            result['docTreeSplitSize'] = self.doc_tree_split_size
        if self.enhance_graph is not None:
            result['enhanceGraph'] = self.enhance_graph
        if self.enhance_table is not None:
            result['enhanceTable'] = self.enhance_table
        if self.overlap is not None:
            result['overlap'] = self.overlap
        if self.sentence_split is not None:
            result['sentenceSplit'] = self.sentence_split
        if self.sentence_split_size is not None:
            result['sentenceSplitSize'] = self.sentence_split_size
        if self.size is not None:
            result['size'] = self.size
        if self.split is not None:
            result['split'] = self.split
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docTreeSplit') is not None:
            self.doc_tree_split = m.get('docTreeSplit')
        if m.get('docTreeSplitSize') is not None:
            self.doc_tree_split_size = m.get('docTreeSplitSize')
        if m.get('enhanceGraph') is not None:
            self.enhance_graph = m.get('enhanceGraph')
        if m.get('enhanceTable') is not None:
            self.enhance_table = m.get('enhanceTable')
        if m.get('overlap') is not None:
            self.overlap = m.get('overlap')
        if m.get('sentenceSplit') is not None:
            self.sentence_split = m.get('sentenceSplit')
        if m.get('sentenceSplitSize') is not None:
            self.sentence_split_size = m.get('sentenceSplitSize')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('split') is not None:
            self.split = m.get('split')
        return self


class UpdateLibraryRequestIndexSettingModelConfig(TeaModel):
    def __init__(
        self,
        temperature: float = None,
        top_p: float = None,
    ):
        self.temperature = temperature
        # topP
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.temperature is not None:
            result['temperature'] = self.temperature
        if self.top_p is not None:
            result['topP'] = self.top_p
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        if m.get('topP') is not None:
            self.top_p = m.get('topP')
        return self


class UpdateLibraryRequestIndexSettingQueryEnhancer(TeaModel):
    def __init__(
        self,
        enable_follow_up: bool = None,
        enable_multi_query: bool = None,
        enable_open_qa: bool = None,
        enable_query_rewrite: bool = None,
        enable_session: bool = None,
        local_knowledge_id: str = None,
        with_document_reference: bool = None,
    ):
        self.enable_follow_up = enable_follow_up
        self.enable_multi_query = enable_multi_query
        self.enable_open_qa = enable_open_qa
        self.enable_query_rewrite = enable_query_rewrite
        self.enable_session = enable_session
        self.local_knowledge_id = local_knowledge_id
        self.with_document_reference = with_document_reference

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_follow_up is not None:
            result['enableFollowUp'] = self.enable_follow_up
        if self.enable_multi_query is not None:
            result['enableMultiQuery'] = self.enable_multi_query
        if self.enable_open_qa is not None:
            result['enableOpenQa'] = self.enable_open_qa
        if self.enable_query_rewrite is not None:
            result['enableQueryRewrite'] = self.enable_query_rewrite
        if self.enable_session is not None:
            result['enableSession'] = self.enable_session
        if self.local_knowledge_id is not None:
            result['localKnowledgeId'] = self.local_knowledge_id
        if self.with_document_reference is not None:
            result['withDocumentReference'] = self.with_document_reference
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableFollowUp') is not None:
            self.enable_follow_up = m.get('enableFollowUp')
        if m.get('enableMultiQuery') is not None:
            self.enable_multi_query = m.get('enableMultiQuery')
        if m.get('enableOpenQa') is not None:
            self.enable_open_qa = m.get('enableOpenQa')
        if m.get('enableQueryRewrite') is not None:
            self.enable_query_rewrite = m.get('enableQueryRewrite')
        if m.get('enableSession') is not None:
            self.enable_session = m.get('enableSession')
        if m.get('localKnowledgeId') is not None:
            self.local_knowledge_id = m.get('localKnowledgeId')
        if m.get('withDocumentReference') is not None:
            self.with_document_reference = m.get('withDocumentReference')
        return self


class UpdateLibraryRequestIndexSettingRecallStrategy(TeaModel):
    def __init__(
        self,
        document_rank_type: str = None,
        limit: int = None,
    ):
        self.document_rank_type = document_rank_type
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_rank_type is not None:
            result['documentRankType'] = self.document_rank_type
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentRankType') is not None:
            self.document_rank_type = m.get('documentRankType')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class UpdateLibraryRequestIndexSettingTextIndexSetting(TeaModel):
    def __init__(
        self,
        category: str = None,
        enable: bool = None,
        index_analyzer: str = None,
        rank_threshold: float = None,
        search_analyzer: str = None,
        top_k: int = None,
    ):
        self.category = category
        self.enable = enable
        self.index_analyzer = index_analyzer
        self.rank_threshold = rank_threshold
        self.search_analyzer = search_analyzer
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.enable is not None:
            result['enable'] = self.enable
        if self.index_analyzer is not None:
            result['indexAnalyzer'] = self.index_analyzer
        if self.rank_threshold is not None:
            result['rankThreshold'] = self.rank_threshold
        if self.search_analyzer is not None:
            result['searchAnalyzer'] = self.search_analyzer
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('indexAnalyzer') is not None:
            self.index_analyzer = m.get('indexAnalyzer')
        if m.get('rankThreshold') is not None:
            self.rank_threshold = m.get('rankThreshold')
        if m.get('searchAnalyzer') is not None:
            self.search_analyzer = m.get('searchAnalyzer')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class UpdateLibraryRequestIndexSettingVectorIndexSetting(TeaModel):
    def __init__(
        self,
        category: str = None,
        embedding_type: str = None,
        enable: bool = None,
        rank_threshold: float = None,
        top_k: int = None,
    ):
        self.category = category
        self.embedding_type = embedding_type
        self.enable = enable
        self.rank_threshold = rank_threshold
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.embedding_type is not None:
            result['embeddingType'] = self.embedding_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.rank_threshold is not None:
            result['rankThreshold'] = self.rank_threshold
        if self.top_k is not None:
            result['topK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('embeddingType') is not None:
            self.embedding_type = m.get('embeddingType')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('rankThreshold') is not None:
            self.rank_threshold = m.get('rankThreshold')
        if m.get('topK') is not None:
            self.top_k = m.get('topK')
        return self


class UpdateLibraryRequestIndexSetting(TeaModel):
    def __init__(
        self,
        chunk_strategy: UpdateLibraryRequestIndexSettingChunkStrategy = None,
        model_config: UpdateLibraryRequestIndexSettingModelConfig = None,
        prompt_role_style: str = None,
        query_enhancer: UpdateLibraryRequestIndexSettingQueryEnhancer = None,
        recall_strategy: UpdateLibraryRequestIndexSettingRecallStrategy = None,
        text_index_setting: UpdateLibraryRequestIndexSettingTextIndexSetting = None,
        vector_index_setting: UpdateLibraryRequestIndexSettingVectorIndexSetting = None,
    ):
        self.chunk_strategy = chunk_strategy
        self.model_config = model_config
        self.prompt_role_style = prompt_role_style
        self.query_enhancer = query_enhancer
        self.recall_strategy = recall_strategy
        self.text_index_setting = text_index_setting
        self.vector_index_setting = vector_index_setting

    def validate(self):
        if self.chunk_strategy:
            self.chunk_strategy.validate()
        if self.model_config:
            self.model_config.validate()
        if self.query_enhancer:
            self.query_enhancer.validate()
        if self.recall_strategy:
            self.recall_strategy.validate()
        if self.text_index_setting:
            self.text_index_setting.validate()
        if self.vector_index_setting:
            self.vector_index_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_strategy is not None:
            result['chunkStrategy'] = self.chunk_strategy.to_map()
        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()
        if self.prompt_role_style is not None:
            result['promptRoleStyle'] = self.prompt_role_style
        if self.query_enhancer is not None:
            result['queryEnhancer'] = self.query_enhancer.to_map()
        if self.recall_strategy is not None:
            result['recallStrategy'] = self.recall_strategy.to_map()
        if self.text_index_setting is not None:
            result['textIndexSetting'] = self.text_index_setting.to_map()
        if self.vector_index_setting is not None:
            result['vectorIndexSetting'] = self.vector_index_setting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkStrategy') is not None:
            temp_model = UpdateLibraryRequestIndexSettingChunkStrategy()
            self.chunk_strategy = temp_model.from_map(m['chunkStrategy'])
        if m.get('modelConfig') is not None:
            temp_model = UpdateLibraryRequestIndexSettingModelConfig()
            self.model_config = temp_model.from_map(m['modelConfig'])
        if m.get('promptRoleStyle') is not None:
            self.prompt_role_style = m.get('promptRoleStyle')
        if m.get('queryEnhancer') is not None:
            temp_model = UpdateLibraryRequestIndexSettingQueryEnhancer()
            self.query_enhancer = temp_model.from_map(m['queryEnhancer'])
        if m.get('recallStrategy') is not None:
            temp_model = UpdateLibraryRequestIndexSettingRecallStrategy()
            self.recall_strategy = temp_model.from_map(m['recallStrategy'])
        if m.get('textIndexSetting') is not None:
            temp_model = UpdateLibraryRequestIndexSettingTextIndexSetting()
            self.text_index_setting = temp_model.from_map(m['textIndexSetting'])
        if m.get('vectorIndexSetting') is not None:
            temp_model = UpdateLibraryRequestIndexSettingVectorIndexSetting()
            self.vector_index_setting = temp_model.from_map(m['vectorIndexSetting'])
        return self


class UpdateLibraryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        index_setting: UpdateLibraryRequestIndexSetting = None,
        library_id: str = None,
        library_name: str = None,
    ):
        self.description = description
        self.index_setting = index_setting
        # This parameter is required.
        self.library_id = library_id
        self.library_name = library_name

    def validate(self):
        if self.index_setting:
            self.index_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.index_setting is not None:
            result['indexSetting'] = self.index_setting.to_map()
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        if self.library_name is not None:
            result['libraryName'] = self.library_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('indexSetting') is not None:
            temp_model = UpdateLibraryRequestIndexSetting()
            self.index_setting = temp_model.from_map(m['indexSetting'])
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')
        return self


class UpdateLibraryResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class UpdateLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLibraryResponseBody = None,
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
            temp_model = UpdateLibraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQaLibraryRequestParseQaResults(TeaModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
    ):
        # This parameter is required.
        self.answer = answer
        # This parameter is required.
        self.question = question

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['answer'] = self.answer
        if self.question is not None:
            result['question'] = self.question
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')
        if m.get('question') is not None:
            self.question = m.get('question')
        return self


class UpdateQaLibraryRequest(TeaModel):
    def __init__(
        self,
        parse_qa_results: List[UpdateQaLibraryRequestParseQaResults] = None,
        qa_library_id: str = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.parse_qa_results = parse_qa_results
        self.qa_library_id = qa_library_id
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.parse_qa_results:
            for k in self.parse_qa_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['parseQaResults'] = []
        if self.parse_qa_results is not None:
            for k in self.parse_qa_results:
                result['parseQaResults'].append(k.to_map() if k else None)
        if self.qa_library_id is not None:
            result['qaLibraryId'] = self.qa_library_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parse_qa_results = []
        if m.get('parseQaResults') is not None:
            for k in m.get('parseQaResults'):
                temp_model = UpdateQaLibraryRequestParseQaResults()
                self.parse_qa_results.append(temp_model.from_map(k))
        if m.get('qaLibraryId') is not None:
            self.qa_library_id = m.get('qaLibraryId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateQaLibraryResponseBodyData(TeaModel):
    def __init__(
        self,
        qa_library_id: str = None,
    ):
        self.qa_library_id = qa_library_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qa_library_id is not None:
            result['qaLibraryId'] = self.qa_library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qaLibraryId') is not None:
            self.qa_library_id = m.get('qaLibraryId')
        return self


class UpdateQaLibraryResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: UpdateQaLibraryResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            temp_model = UpdateQaLibraryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class UpdateQaLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQaLibraryResponseBody = None,
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
            temp_model = UpdateQaLibraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDocumentRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        file_name: str = None,
        file_url: str = None,
        library_id: str = None,
    ):
        self.data = data
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_url = file_url
        # This parameter is required.
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        return self


class UploadDocumentAdvanceRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        library_id: str = None,
    ):
        self.data = data
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_url_object = file_url_object
        # This parameter is required.
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_url_object is not None:
            result['fileUrl'] = self.file_url_object
        if self.library_id is not None:
            result['libraryId'] = self.library_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')
        return self


class UploadDocumentResponseBody(TeaModel):
    def __init__(
        self,
        cost: int = None,
        data: str = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.data is not None:
            result['data'] = self.data
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class UploadDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadDocumentResponseBody = None,
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
            temp_model = UploadDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


