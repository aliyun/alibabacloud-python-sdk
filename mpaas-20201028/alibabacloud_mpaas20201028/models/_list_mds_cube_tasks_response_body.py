# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListMdsCubeTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: main_models.ListMdsCubeTasksResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultContent') is not None:
            temp_model = main_models.ListMdsCubeTasksResponseBodyResultContent()
            self.result_content = temp_model.from_map(m.get('ResultContent'))

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class ListMdsCubeTasksResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        data: main_models.ListMdsCubeTasksResponseBodyResultContentData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListMdsCubeTasksResponseBodyResultContentData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMdsCubeTasksResponseBodyResultContentData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListMdsCubeTasksResponseBodyResultContentDataContent] = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.content = content
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListMdsCubeTasksResponseBodyResultContentDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMdsCubeTasksResponseBodyResultContentDataContent(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        id: int = None,
        operator: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        resource_version: str = None,
        task_desc: str = None,
        task_status: int = None,
        template_id: str = None,
        template_resource_id: int = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.id = id
        self.operator = operator
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.resource_version = resource_version
        self.task_desc = task_desc
        self.task_status = task_status
        self.template_id = template_id
        self.template_resource_id = template_resource_id
        self.whitelist_ids = whitelist_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info

        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data

        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num

        if self.id is not None:
            result['Id'] = self.id

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.resource_version is not None:
            result['ResourceVersion'] = self.resource_version

        if self.task_desc is not None:
            result['TaskDesc'] = self.task_desc

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_resource_id is not None:
            result['TemplateResourceId'] = self.template_resource_id

        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')

        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')

        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('ResourceVersion') is not None:
            self.resource_version = m.get('ResourceVersion')

        if m.get('TaskDesc') is not None:
            self.task_desc = m.get('TaskDesc')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateResourceId') is not None:
            self.template_resource_id = m.get('TemplateResourceId')

        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')

        return self

