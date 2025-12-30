# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryMediaIndexJobResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        index_job_info_list: List[main_models.QueryMediaIndexJobResponseBodyIndexJobInfoList] = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response code.
        self.code = code
        # The indexing jobs enabled for the media asset.
        self.index_job_info_list = index_job_info_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.index_job_info_list:
            for v1 in self.index_job_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['IndexJobInfoList'] = []
        if self.index_job_info_list is not None:
            for k1 in self.index_job_info_list:
                result['IndexJobInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.index_job_info_list = []
        if m.get('IndexJobInfoList') is not None:
            for k1 in m.get('IndexJobInfoList'):
                temp_model = main_models.QueryMediaIndexJobResponseBodyIndexJobInfoList()
                self.index_job_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMediaIndexJobResponseBodyIndexJobInfoList(DaraModel):
    def __init__(
        self,
        gmt_finish: str = None,
        gmt_submit: str = None,
        index_type: str = None,
        status: str = None,
    ):
        # The end time of the indexing job.
        self.gmt_finish = gmt_finish
        # The time when the index job was submitted.
        self.gmt_submit = gmt_submit
        # The index type. Valid values:
        # 
        # *   mm: large visual model.
        # *   face: face recognition.
        # *   aiLabel: smart tagging.
        self.index_type = index_type
        # The job status. Valid values:
        # 
        # *   Running
        # *   Success
        # *   Fail
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_finish is not None:
            result['GmtFinish'] = self.gmt_finish

        if self.gmt_submit is not None:
            result['GmtSubmit'] = self.gmt_submit

        if self.index_type is not None:
            result['IndexType'] = self.index_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtFinish') is not None:
            self.gmt_finish = m.get('GmtFinish')

        if m.get('GmtSubmit') is not None:
            self.gmt_submit = m.get('GmtSubmit')

        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

