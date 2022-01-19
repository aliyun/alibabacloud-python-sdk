# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ChangeComponentEnumResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeComponentEnumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeComponentEnumResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChangeComponentEnumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScenceRequestDstKnowledgeConditionList(TeaModel):
    def __init__(
        self,
        condition: str = None,
        key: str = None,
        value: str = None,
    ):
        self.condition = condition
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateScenceRequestDstKnowledge(TeaModel):
    def __init__(
        self,
        condition: str = None,
        condition_list: List[CreateScenceRequestDstKnowledgeConditionList] = None,
        limit: int = None,
        name: str = None,
        offset: int = None,
        sort_field: str = None,
        sort_type: str = None,
    ):
        self.condition = condition
        self.condition_list = condition_list
        self.limit = limit
        self.name = name
        self.offset = offset
        self.sort_field = sort_field
        self.sort_type = sort_type

    def validate(self):
        if self.condition_list:
            for k in self.condition_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition
        result['ConditionList'] = []
        if self.condition_list is not None:
            for k in self.condition_list:
                result['ConditionList'].append(k.to_map() if k else None)
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name is not None:
            result['Name'] = self.name
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k in m.get('ConditionList'):
                temp_model = CreateScenceRequestDstKnowledgeConditionList()
                self.condition_list.append(temp_model.from_map(k))
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        return self


class CreateScenceRequestParam(TeaModel):
    def __init__(
        self,
        param_commit: str = None,
        param_key: str = None,
        param_type: str = None,
    ):
        self.param_commit = param_commit
        self.param_key = param_key
        self.param_type = param_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_commit is not None:
            result['ParamCommit'] = self.param_commit
        if self.param_key is not None:
            result['ParamKey'] = self.param_key
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamCommit') is not None:
            self.param_commit = m.get('ParamCommit')
        if m.get('ParamKey') is not None:
            self.param_key = m.get('ParamKey')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        return self


class CreateScenceRequestSrcKnowledgeKnowledge(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateScenceRequestSrcKnowledge(TeaModel):
    def __init__(
        self,
        knowledge: CreateScenceRequestSrcKnowledgeKnowledge = None,
        param: str = None,
    ):
        self.knowledge = knowledge
        self.param = param

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        if self.param is not None:
            result['Param'] = self.param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Knowledge') is not None:
            temp_model = CreateScenceRequestSrcKnowledgeKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        if m.get('Param') is not None:
            self.param = m.get('Param')
        return self


class CreateScenceRequest(TeaModel):
    def __init__(
        self,
        dst_knowledge: CreateScenceRequestDstKnowledge = None,
        graph_id: str = None,
        is_non_profit: bool = None,
        limit: int = None,
        param: List[CreateScenceRequestParam] = None,
        result_type: int = None,
        src_knowledge: List[CreateScenceRequestSrcKnowledge] = None,
        work_name: str = None,
    ):
        self.dst_knowledge = dst_knowledge
        self.graph_id = graph_id
        self.is_non_profit = is_non_profit
        self.limit = limit
        self.param = param
        self.result_type = result_type
        self.src_knowledge = src_knowledge
        self.work_name = work_name

    def validate(self):
        if self.dst_knowledge:
            self.dst_knowledge.validate()
        if self.param:
            for k in self.param:
                if k:
                    k.validate()
        if self.src_knowledge:
            for k in self.src_knowledge:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_knowledge is not None:
            result['DstKnowledge'] = self.dst_knowledge.to_map()
        if self.graph_id is not None:
            result['GraphId'] = self.graph_id
        if self.is_non_profit is not None:
            result['IsNonProfit'] = self.is_non_profit
        if self.limit is not None:
            result['Limit'] = self.limit
        result['Param'] = []
        if self.param is not None:
            for k in self.param:
                result['Param'].append(k.to_map() if k else None)
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        result['SrcKnowledge'] = []
        if self.src_knowledge is not None:
            for k in self.src_knowledge:
                result['SrcKnowledge'].append(k.to_map() if k else None)
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstKnowledge') is not None:
            temp_model = CreateScenceRequestDstKnowledge()
            self.dst_knowledge = temp_model.from_map(m['DstKnowledge'])
        if m.get('GraphId') is not None:
            self.graph_id = m.get('GraphId')
        if m.get('IsNonProfit') is not None:
            self.is_non_profit = m.get('IsNonProfit')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        self.param = []
        if m.get('Param') is not None:
            for k in m.get('Param'):
                temp_model = CreateScenceRequestParam()
                self.param.append(temp_model.from_map(k))
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        self.src_knowledge = []
        if m.get('SrcKnowledge') is not None:
            for k in m.get('SrcKnowledge'):
                temp_model = CreateScenceRequestSrcKnowledge()
                self.src_knowledge.append(temp_model.from_map(k))
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        return self


class CreateScenceResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateScenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateScenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateScenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScenceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DeleteScenceResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteScenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteScenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteScenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScenceResultRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        offset: int = None,
        task_id: str = None,
    ):
        self.limit = limit
        self.offset = offset
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.offset is not None:
            result['offset'] = self.offset
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetScenceResultResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScenceResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetScenceResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetScenceResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScencesListRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        search: str = None,
        size: int = None,
        work_name: str = None,
    ):
        self.page = page
        self.search = search
        self.size = size
        self.work_name = work_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.search is not None:
            result['search'] = self.search
        if self.size is not None:
            result['size'] = self.size
        if self.work_name is not None:
            result['workName'] = self.work_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('workName') is not None:
            self.work_name = m.get('workName')
        return self


class GetScencesListResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScencesListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetScencesListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetScencesListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScenceRequest(TeaModel):
    def __init__(
        self,
        creater: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        param: str = None,
        rule_body: str = None,
        rule_describe: str = None,
        rule_status: str = None,
        scene_id: int = None,
        title: str = None,
        work_id: str = None,
        work_name: str = None,
    ):
        self.creater = creater
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.param = param
        self.rule_body = rule_body
        self.rule_describe = rule_describe
        self.rule_status = rule_status
        self.scene_id = scene_id
        self.title = title
        self.work_id = work_id
        self.work_name = work_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creater is not None:
            result['Creater'] = self.creater
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.param is not None:
            result['Param'] = self.param
        if self.rule_body is not None:
            result['RuleBody'] = self.rule_body
        if self.rule_describe is not None:
            result['RuleDescribe'] = self.rule_describe
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.title is not None:
            result['Title'] = self.title
        if self.work_id is not None:
            result['WorkId'] = self.work_id
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creater') is not None:
            self.creater = m.get('Creater')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('RuleBody') is not None:
            self.rule_body = m.get('RuleBody')
        if m.get('RuleDescribe') is not None:
            self.rule_describe = m.get('RuleDescribe')
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WorkId') is not None:
            self.work_id = m.get('WorkId')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        return self


class ModifyScenceResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyScenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyScenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyScenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryScenceRequestBodyParam(TeaModel):
    def __init__(
        self,
        param_key: str = None,
        param_type: str = None,
        param_value: str = None,
    ):
        self.param_key = param_key
        self.param_type = param_type
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_key is not None:
            result['ParamKey'] = self.param_key
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.param_value is not None:
            result['ParamValue'] = self.param_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamKey') is not None:
            self.param_key = m.get('ParamKey')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')
        return self


class QueryScenceRequestBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        param: List[QueryScenceRequestBodyParam] = None,
    ):
        self.id = id
        self.param = param

    def validate(self):
        if self.param:
            for k in self.param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['Param'] = []
        if self.param is not None:
            for k in self.param:
                result['Param'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param = []
        if m.get('Param') is not None:
            for k in m.get('Param'):
                temp_model = QueryScenceRequestBodyParam()
                self.param.append(temp_model.from_map(k))
        return self


class QueryScenceRequest(TeaModel):
    def __init__(
        self,
        body: List[QueryScenceRequestBody] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = QueryScenceRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class QueryScenceResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryScenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryScenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryScenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StatusScenceRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
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


class StatusScenceResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StatusScenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StatusScenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StatusScenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


