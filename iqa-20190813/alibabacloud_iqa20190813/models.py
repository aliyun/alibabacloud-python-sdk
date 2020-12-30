# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        model_id: str = None,
        project_type: str = None,
    ):
        self.project_name = project_name
        self.model_id = model_id
        self.project_type = project_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project_id: str = None,
    ):
        self.request_id = request_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployServiceRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeployServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeployServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeployServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeProjectResponseBody(TeaModel):
    def __init__(
        self,
        question_count: int = None,
        deploy_available: str = None,
        model_name: str = None,
        request_id: str = None,
        project_name: str = None,
        create_time: int = None,
        project_id: str = None,
        online_service_status: str = None,
        deploy_time: int = None,
        project_type: str = None,
        data_status: str = None,
        model_id: str = None,
        test_service_status: str = None,
    ):
        self.question_count = question_count
        self.deploy_available = deploy_available
        self.model_name = model_name
        self.request_id = request_id
        self.project_name = project_name
        self.create_time = create_time
        self.project_id = project_id
        self.online_service_status = online_service_status
        self.deploy_time = deploy_time
        self.project_type = project_type
        self.data_status = data_status
        self.model_id = model_id
        self.test_service_status = test_service_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.question_count is not None:
            result['QuestionCount'] = self.question_count
        if self.deploy_available is not None:
            result['DeployAvailable'] = self.deploy_available
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.online_service_status is not None:
            result['OnlineServiceStatus'] = self.online_service_status
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        if self.data_status is not None:
            result['DataStatus'] = self.data_status
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.test_service_status is not None:
            result['TestServiceStatus'] = self.test_service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuestionCount') is not None:
            self.question_count = m.get('QuestionCount')
        if m.get('DeployAvailable') is not None:
            self.deploy_available = m.get('DeployAvailable')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('OnlineServiceStatus') is not None:
            self.online_service_status = m.get('OnlineServiceStatus')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        if m.get('DataStatus') is not None:
            self.data_status = m.get('DataStatus')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('TestServiceStatus') is not None:
            self.test_service_status = m.get('TestServiceStatus')
        return self


class DescribeProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPredictResultRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        question: str = None,
        top_k: int = None,
        trace_tag: str = None,
    ):
        self.project_id = project_id
        self.question = question
        self.top_k = top_k
        self.trace_tag = trace_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.question is not None:
            result['Question'] = self.question
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.trace_tag is not None:
            result['TraceTag'] = self.trace_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('TraceTag') is not None:
            self.trace_tag = m.get('TraceTag')
        return self


class GetPredictResultResponseBodyPredictResults(TeaModel):
    def __init__(
        self,
        answer: str = None,
        question_id: str = None,
        rank: int = None,
        score: float = None,
        question: str = None,
    ):
        self.answer = answer
        self.question_id = question_id
        self.rank = rank
        self.score = score
        self.question = question

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.question_id is not None:
            result['QuestionId'] = self.question_id
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.score is not None:
            result['Score'] = self.score
        if self.question is not None:
            result['Question'] = self.question
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('QuestionId') is not None:
            self.question_id = m.get('QuestionId')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        return self


class GetPredictResultResponseBody(TeaModel):
    def __init__(
        self,
        trace: str = None,
        cost_time: int = None,
        top_k: int = None,
        request_id: str = None,
        trace_tag: str = None,
        project_id: str = None,
        question: str = None,
        predict_results: List[GetPredictResultResponseBodyPredictResults] = None,
    ):
        self.trace = trace
        self.cost_time = cost_time
        self.top_k = top_k
        self.request_id = request_id
        self.trace_tag = trace_tag
        self.project_id = project_id
        self.question = question
        self.predict_results = predict_results

    def validate(self):
        if self.predict_results:
            for k in self.predict_results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.trace is not None:
            result['Trace'] = self.trace
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_tag is not None:
            result['TraceTag'] = self.trace_tag
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.question is not None:
            result['Question'] = self.question
        result['PredictResults'] = []
        if self.predict_results is not None:
            for k in self.predict_results:
                result['PredictResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Trace') is not None:
            self.trace = m.get('Trace')
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceTag') is not None:
            self.trace_tag = m.get('TraceTag')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        self.predict_results = []
        if m.get('PredictResults') is not None:
            for k in m.get('PredictResults'):
                temp_model = GetPredictResultResponseBodyPredictResults()
                self.predict_results.append(temp_model.from_map(k))
        return self


class GetPredictResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPredictResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetPredictResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        filter_param: str = None,
        page_number: int = None,
        page_size: int = None,
        project_type: str = None,
    ):
        self.filter_param = filter_param
        self.page_number = page_number
        self.page_size = page_size
        self.project_type = project_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.filter_param is not None:
            result['FilterParam'] = self.filter_param
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterParam') is not None:
            self.filter_param = m.get('FilterParam')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        return self


class ListProjectsResponseBodyProjects(TeaModel):
    def __init__(
        self,
        deploy_available: str = None,
        create_time: int = None,
        project_name: str = None,
        project_id: str = None,
        question_count: int = None,
        deploy_time: int = None,
        project_type: str = None,
        online_service_status: str = None,
        test_service_status: str = None,
        model_name: str = None,
        data_status: str = None,
        model_id: str = None,
    ):
        self.deploy_available = deploy_available
        self.create_time = create_time
        self.project_name = project_name
        self.project_id = project_id
        self.question_count = question_count
        self.deploy_time = deploy_time
        self.project_type = project_type
        self.online_service_status = online_service_status
        self.test_service_status = test_service_status
        self.model_name = model_name
        self.data_status = data_status
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.deploy_available is not None:
            result['DeployAvailable'] = self.deploy_available
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.question_count is not None:
            result['QuestionCount'] = self.question_count
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        if self.online_service_status is not None:
            result['OnlineServiceStatus'] = self.online_service_status
        if self.test_service_status is not None:
            result['TestServiceStatus'] = self.test_service_status
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.data_status is not None:
            result['DataStatus'] = self.data_status
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployAvailable') is not None:
            self.deploy_available = m.get('DeployAvailable')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QuestionCount') is not None:
            self.question_count = m.get('QuestionCount')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        if m.get('OnlineServiceStatus') is not None:
            self.online_service_status = m.get('OnlineServiceStatus')
        if m.get('TestServiceStatus') is not None:
            self.test_service_status = m.get('TestServiceStatus')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('DataStatus') is not None:
            self.data_status = m.get('DataStatus')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        projects: List[ListProjectsResponseBodyProjects] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.projects = projects

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = ListProjectsResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifiyProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        model_id: str = None,
        project_name: str = None,
    ):
        self.project_id = project_id
        self.model_id = model_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ModifiyProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project_id: str = None,
    ):
        self.request_id = request_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ModifiyProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifiyProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifiyProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDictionaryRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        dictionary_file_url: str = None,
        dictionary_data: str = None,
    ):
        self.project_id = project_id
        self.dictionary_file_url = dictionary_file_url
        self.dictionary_data = dictionary_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.dictionary_file_url is not None:
            result['DictionaryFileUrl'] = self.dictionary_file_url
        if self.dictionary_data is not None:
            result['DictionaryData'] = self.dictionary_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DictionaryFileUrl') is not None:
            self.dictionary_file_url = m.get('DictionaryFileUrl')
        if m.get('DictionaryData') is not None:
            self.dictionary_data = m.get('DictionaryData')
        return self


class UploadDictionaryResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        project_id: str = None,
        file_data_count: int = None,
        json_data_count: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.project_id = project_id
        self.file_data_count = file_data_count
        self.json_data_count = json_data_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.file_data_count is not None:
            result['FileDataCount'] = self.file_data_count
        if self.json_data_count is not None:
            result['JsonDataCount'] = self.json_data_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FileDataCount') is not None:
            self.file_data_count = m.get('FileDataCount')
        if m.get('JsonDataCount') is not None:
            self.json_data_count = m.get('JsonDataCount')
        return self


class UploadDictionaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadDictionaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UploadDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDocumentRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        document_file_url: str = None,
        document_data: str = None,
    ):
        self.project_id = project_id
        self.document_file_url = document_file_url
        self.document_data = document_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.document_file_url is not None:
            result['DocumentFileUrl'] = self.document_file_url
        if self.document_data is not None:
            result['DocumentData'] = self.document_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DocumentFileUrl') is not None:
            self.document_file_url = m.get('DocumentFileUrl')
        if m.get('DocumentData') is not None:
            self.document_data = m.get('DocumentData')
        return self


class UploadDocumentResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        project_id: str = None,
        file_data_count: int = None,
        json_data_count: int = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.project_id = project_id
        self.file_data_count = file_data_count
        self.json_data_count = json_data_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.file_data_count is not None:
            result['FileDataCount'] = self.file_data_count
        if self.json_data_count is not None:
            result['JsonDataCount'] = self.json_data_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FileDataCount') is not None:
            self.file_data_count = m.get('FileDataCount')
        if m.get('JsonDataCount') is not None:
            self.json_data_count = m.get('JsonDataCount')
        return self


class UploadDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadDocumentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UploadDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


