# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QueryCopyrightJobResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryCopyrightJobResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status_code = status_code

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryCopyrightJobResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class QueryCopyrightJobResponseBodyData(DaraModel):
    def __init__(
        self,
        callback: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        input: str = None,
        job_id: str = None,
        level: int = None,
        message: str = None,
        output: str = None,
        result: str = None,
        status: str = None,
        user_data: str = None,
        user_id: int = None,
    ):
        self.callback = callback
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.input = input
        self.job_id = job_id
        self.level = level
        self.message = message
        self.output = output
        self.result = result
        self.status = status
        self.user_data = user_data
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback is not None:
            result['Callback'] = self.callback

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.input is not None:
            result['Input'] = self.input

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.level is not None:
            result['Level'] = self.level

        if self.message is not None:
            result['Message'] = self.message

        if self.output is not None:
            result['Output'] = self.output

        if self.result is not None:
            result['Result'] = self.result

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

