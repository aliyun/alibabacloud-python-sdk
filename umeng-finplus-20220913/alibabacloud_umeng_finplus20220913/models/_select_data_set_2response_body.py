# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class SelectDataSet2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SelectDataSet2ResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.SelectDataSet2ResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SelectDataSet2ResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_id: int = None,
        line_num: int = None,
        name: str = None,
        oss_file_count: int = None,
        status: str = None,
        status_msg: str = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.dataset_id = dataset_id
        self.line_num = line_num
        self.name = name
        self.oss_file_count = oss_file_count
        self.status = status
        self.status_msg = status_msg
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.line_num is not None:
            result['lineNum'] = self.line_num

        if self.name is not None:
            result['name'] = self.name

        if self.oss_file_count is not None:
            result['ossFileCount'] = self.oss_file_count

        if self.status is not None:
            result['status'] = self.status

        if self.status_msg is not None:
            result['statusMsg'] = self.status_msg

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('lineNum') is not None:
            self.line_num = m.get('lineNum')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ossFileCount') is not None:
            self.oss_file_count = m.get('ossFileCount')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusMsg') is not None:
            self.status_msg = m.get('statusMsg')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

