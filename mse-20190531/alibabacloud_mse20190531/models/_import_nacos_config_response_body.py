# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ImportNacosConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ImportNacosConfigResponseBodyData = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error message returned.
        self.code = code
        # The number of configurations that are imported.
        self.data = data
        # The details of the data.
        self.dynamic_message = dynamic_message
        # The code returned.
        self.error_code = error_code
        # The ID of the request.
        self.http_status_code = http_status_code
        # The request is successfully processed.
        self.message = message
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.request_id = request_id
        # The error code that is returned.
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

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

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
            temp_model = main_models.ImportNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ImportNacosConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_data: List[main_models.ImportNacosConfigResponseBodyDataFailData] = None,
        skip_count: int = None,
        skip_data: List[main_models.ImportNacosConfigResponseBodyDataSkipData] = None,
        succ_count: int = None,
    ):
        # The data structure.
        self.fail_data = fail_data
        # The information about skipped configurations.
        self.skip_count = skip_count
        # The data structure.
        self.skip_data = skip_data
        # The number of configurations that are skipped.
        self.succ_count = succ_count

    def validate(self):
        if self.fail_data:
            for v1 in self.fail_data:
                 if v1:
                    v1.validate()
        if self.skip_data:
            for v1 in self.skip_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailData'] = []
        if self.fail_data is not None:
            for k1 in self.fail_data:
                result['FailData'].append(k1.to_map() if k1 else None)

        if self.skip_count is not None:
            result['SkipCount'] = self.skip_count

        result['SkipData'] = []
        if self.skip_data is not None:
            for k1 in self.skip_data:
                result['SkipData'].append(k1.to_map() if k1 else None)

        if self.succ_count is not None:
            result['SuccCount'] = self.succ_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_data = []
        if m.get('FailData') is not None:
            for k1 in m.get('FailData'):
                temp_model = main_models.ImportNacosConfigResponseBodyDataFailData()
                self.fail_data.append(temp_model.from_map(k1))

        if m.get('SkipCount') is not None:
            self.skip_count = m.get('SkipCount')

        self.skip_data = []
        if m.get('SkipData') is not None:
            for k1 in m.get('SkipData'):
                temp_model = main_models.ImportNacosConfigResponseBodyDataSkipData()
                self.skip_data.append(temp_model.from_map(k1))

        if m.get('SuccCount') is not None:
            self.succ_count = m.get('SuccCount')

        return self

class ImportNacosConfigResponseBodyDataSkipData(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        # The ID of the group.
        self.data_id = data_id
        # The information about configurations that are failed to be imported.
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.group is not None:
            result['Group'] = self.group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        return self

class ImportNacosConfigResponseBodyDataFailData(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
        reason: str = None,
    ):
        # The ID of the group.
        self.data_id = data_id
        self.group = group
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.group is not None:
            result['Group'] = self.group

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

