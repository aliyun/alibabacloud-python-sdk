# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateRetcodeAppResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        retcode_app_data_bean: main_models.CreateRetcodeAppResponseBodyRetcodeAppDataBean = None,
        success: bool = None,
    ):
        # The status code. The status code 200 indicates that the request was successful. If another status code is returned, the request failed.
        self.code = code
        # The response parameters.
        self.data = data
        # The message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The information of the Browser Monitoring task.
        self.retcode_app_data_bean = retcode_app_data_bean
        # Indicates whether the call was successful. Valid values:
        # 
        # - true: The call was successful.
        # - false: The call failed.
        self.success = success

    def validate(self):
        if self.retcode_app_data_bean:
            self.retcode_app_data_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.retcode_app_data_bean is not None:
            result['RetcodeAppDataBean'] = self.retcode_app_data_bean.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetcodeAppDataBean') is not None:
            temp_model = main_models.CreateRetcodeAppResponseBodyRetcodeAppDataBean()
            self.retcode_app_data_bean = temp_model.from_map(m.get('RetcodeAppDataBean'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateRetcodeAppResponseBodyRetcodeAppDataBean(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        pid: str = None,
        resource_group_id: str = None,
        tags: main_models.CreateRetcodeAppResponseBodyRetcodeAppDataBeanTags = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The process identifier (PID) of the application.
        self.pid = pid
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags of the task.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            temp_model = main_models.CreateRetcodeAppResponseBodyRetcodeAppDataBeanTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class CreateRetcodeAppResponseBodyRetcodeAppDataBeanTags(DaraModel):
    def __init__(
        self,
        tags: List[main_models.CreateRetcodeAppResponseBodyRetcodeAppDataBeanTagsTags] = None,
    ):
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateRetcodeAppResponseBodyRetcodeAppDataBeanTagsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateRetcodeAppResponseBodyRetcodeAppDataBeanTagsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

