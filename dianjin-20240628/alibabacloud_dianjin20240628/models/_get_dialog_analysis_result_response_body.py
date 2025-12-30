# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetDialogAnalysisResultResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetDialogAnalysisResultResponseBodyData = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.GetDialogAnalysisResultResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

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

class GetDialogAnalysisResultResponseBodyData(DaraModel):
    def __init__(
        self,
        dialog_analysis_resp_list: List[main_models.GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespList] = None,
    ):
        self.dialog_analysis_resp_list = dialog_analysis_resp_list

    def validate(self):
        if self.dialog_analysis_resp_list:
            for v1 in self.dialog_analysis_resp_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dialogAnalysisRespList'] = []
        if self.dialog_analysis_resp_list is not None:
            for k1 in self.dialog_analysis_resp_list:
                result['dialogAnalysisRespList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialog_analysis_resp_list = []
        if m.get('dialogAnalysisRespList') is not None:
            for k1 in m.get('dialogAnalysisRespList'):
                temp_model = main_models.GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespList()
                self.dialog_analysis_resp_list.append(temp_model.from_map(k1))

        return self

class GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespList(DaraModel):
    def __init__(
        self,
        analysis_resp: main_models.GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisResp = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisResp()
            self.analysis_resp = temp_model.from_map(m.get('analysisResp'))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('ossUrl') is not None:
            self.oss_url = m.get('ossUrl')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisResp(DaraModel):
    def __init__(
        self,
        dialog_exec_plan: str = None,
        dialog_labels: List[main_models.GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisRespDialogLabels] = None,
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
            for v1 in self.dialog_labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialog_exec_plan is not None:
            result['dialogExecPlan'] = self.dialog_exec_plan

        result['dialogLabels'] = []
        if self.dialog_labels is not None:
            for k1 in self.dialog_labels:
                result['dialogLabels'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('dialogLabels'):
                temp_model = main_models.GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisRespDialogLabels()
                self.dialog_labels.append(temp_model.from_map(k1))

        if m.get('dialogOpenAnalysis') is not None:
            self.dialog_open_analysis = m.get('dialogOpenAnalysis')

        if m.get('dialogProcessAnalysis') is not None:
            self.dialog_process_analysis = m.get('dialogProcessAnalysis')

        if m.get('dialogSop') is not None:
            self.dialog_sop = m.get('dialogSop')

        if m.get('dialogSummary') is not None:
            self.dialog_summary = m.get('dialogSummary')

        return self

class GetDialogAnalysisResultResponseBodyDataDialogAnalysisRespListAnalysisRespDialogLabels(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

