# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class RunDataAnalysisRequest(TeaModel):
    def __init__(
        self,
        generate_sql_only: bool = None,
        query: str = None,
        session_id: str = None,
        specification_type: str = None,
    ):
        self.generate_sql_only = generate_sql_only
        # This parameter is required.
        self.query = query
        self.session_id = session_id
        self.specification_type = specification_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generate_sql_only is not None:
            result['generateSqlOnly'] = self.generate_sql_only
        if self.query is not None:
            result['query'] = self.query
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.specification_type is not None:
            result['specificationType'] = self.specification_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateSqlOnly') is not None:
            self.generate_sql_only = m.get('generateSqlOnly')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('specificationType') is not None:
            self.specification_type = m.get('specificationType')
        return self


class RunDataAnalysisResponseBodyDataSqlData(TeaModel):
    def __init__(
        self,
        column: List[str] = None,
        data: List[Dict[str, Any]] = None,
    ):
        self.column = column
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column is not None:
            result['column'] = self.column
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('column') is not None:
            self.column = m.get('column')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class RunDataAnalysisResponseBodyDataVisualizationData(TeaModel):
    def __init__(
        self,
        plot_type: str = None,
        x_axis: List[str] = None,
        y_axis: List[str] = None,
    ):
        self.plot_type = plot_type
        self.x_axis = x_axis
        self.y_axis = y_axis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plot_type is not None:
            result['plotType'] = self.plot_type
        if self.x_axis is not None:
            result['xAxis'] = self.x_axis
        if self.y_axis is not None:
            result['yAxis'] = self.y_axis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('plotType') is not None:
            self.plot_type = m.get('plotType')
        if m.get('xAxis') is not None:
            self.x_axis = m.get('xAxis')
        if m.get('yAxis') is not None:
            self.y_axis = m.get('yAxis')
        return self


class RunDataAnalysisResponseBodyDataVisualization(TeaModel):
    def __init__(
        self,
        data: RunDataAnalysisResponseBodyDataVisualizationData = None,
        text: str = None,
    ):
        self.data = data
        self.text = text

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = RunDataAnalysisResponseBodyDataVisualizationData()
            self.data = temp_model.from_map(m['data'])
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunDataAnalysisResponseBodyData(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        event: str = None,
        evidence: str = None,
        http_status_code: int = None,
        request_id: str = None,
        rewrite: str = None,
        selector: List[str] = None,
        session_id: str = None,
        sql: str = None,
        sql_data: RunDataAnalysisResponseBodyDataSqlData = None,
        sql_error: str = None,
        visualization: RunDataAnalysisResponseBodyDataVisualization = None,
    ):
        self.error_message = error_message
        self.event = event
        self.evidence = evidence
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.rewrite = rewrite
        self.selector = selector
        self.session_id = session_id
        self.sql = sql
        self.sql_data = sql_data
        self.sql_error = sql_error
        self.visualization = visualization

    def validate(self):
        if self.sql_data:
            self.sql_data.validate()
        if self.visualization:
            self.visualization.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.event is not None:
            result['event'] = self.event
        if self.evidence is not None:
            result['evidence'] = self.evidence
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.rewrite is not None:
            result['rewrite'] = self.rewrite
        if self.selector is not None:
            result['selector'] = self.selector
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.sql is not None:
            result['sql'] = self.sql
        if self.sql_data is not None:
            result['sqlData'] = self.sql_data.to_map()
        if self.sql_error is not None:
            result['sqlError'] = self.sql_error
        if self.visualization is not None:
            result['visualization'] = self.visualization.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('evidence') is not None:
            self.evidence = m.get('evidence')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('rewrite') is not None:
            self.rewrite = m.get('rewrite')
        if m.get('selector') is not None:
            self.selector = m.get('selector')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('sql') is not None:
            self.sql = m.get('sql')
        if m.get('sqlData') is not None:
            temp_model = RunDataAnalysisResponseBodyDataSqlData()
            self.sql_data = temp_model.from_map(m['sqlData'])
        if m.get('sqlError') is not None:
            self.sql_error = m.get('sqlError')
        if m.get('visualization') is not None:
            temp_model = RunDataAnalysisResponseBodyDataVisualization()
            self.visualization = temp_model.from_map(m['visualization'])
        return self


class RunDataAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RunDataAnalysisResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = RunDataAnalysisResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class RunDataAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunDataAnalysisResponseBody = None,
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
            temp_model = RunDataAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


