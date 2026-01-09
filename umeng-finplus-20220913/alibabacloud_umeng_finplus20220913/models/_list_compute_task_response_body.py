# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class ListComputeTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListComputeTaskResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListComputeTaskResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListComputeTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        bc_id: int = None,
        compute_oss_file_title: str = None,
        dataset_ids: str = None,
        ext_info: str = None,
        file_num: int = None,
        name: str = None,
        remarks: str = None,
        status: str = None,
        task_result_list: List[main_models.ListComputeTaskResponseBodyDataTaskResultList] = None,
    ):
        self.app_id = app_id
        self.bc_id = bc_id
        self.compute_oss_file_title = compute_oss_file_title
        self.dataset_ids = dataset_ids
        self.ext_info = ext_info
        self.file_num = file_num
        self.name = name
        self.remarks = remarks
        self.status = status
        self.task_result_list = task_result_list

    def validate(self):
        if self.task_result_list:
            for v1 in self.task_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.bc_id is not None:
            result['bcId'] = self.bc_id

        if self.compute_oss_file_title is not None:
            result['computeOssFileTitle'] = self.compute_oss_file_title

        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids

        if self.ext_info is not None:
            result['extInfo'] = self.ext_info

        if self.file_num is not None:
            result['fileNum'] = self.file_num

        if self.name is not None:
            result['name'] = self.name

        if self.remarks is not None:
            result['remarks'] = self.remarks

        if self.status is not None:
            result['status'] = self.status

        result['taskResultList'] = []
        if self.task_result_list is not None:
            for k1 in self.task_result_list:
                result['taskResultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')

        if m.get('computeOssFileTitle') is not None:
            self.compute_oss_file_title = m.get('computeOssFileTitle')

        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')

        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')

        if m.get('fileNum') is not None:
            self.file_num = m.get('fileNum')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.task_result_list = []
        if m.get('taskResultList') is not None:
            for k1 in m.get('taskResultList'):
                temp_model = main_models.ListComputeTaskResponseBodyDataTaskResultList()
                self.task_result_list.append(temp_model.from_map(k1))

        return self

class ListComputeTaskResponseBodyDataTaskResultList(DaraModel):
    def __init__(
        self,
        bc_id: int = None,
        code: int = None,
        line_num: int = None,
    ):
        self.bc_id = bc_id
        self.code = code
        self.line_num = line_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bc_id is not None:
            result['bcId'] = self.bc_id

        if self.code is not None:
            result['code'] = self.code

        if self.line_num is not None:
            result['lineNum'] = self.line_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('lineNum') is not None:
            self.line_num = m.get('lineNum')

        return self

