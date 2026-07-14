# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListFlowNodePrototypeV2ResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        data: main_models.ListFlowNodePrototypeV2ResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The error code. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # - true: The call was successful.
        # 
        # - false: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListFlowNodePrototypeV2ResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListFlowNodePrototypeV2ResponseBodyData(DaraModel):
    def __init__(
        self,
        model: List[main_models.ListFlowNodePrototypeV2ResponseBodyDataModel] = None,
    ):
        # A list of the returned data.
        self.model = model

    def validate(self):
        if self.model:
            for v1 in self.model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Model'] = []
        if self.model is not None:
            for k1 in self.model:
                result['Model'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model = []
        if m.get('Model') is not None:
            for k1 in m.get('Model'):
                temp_model = main_models.ListFlowNodePrototypeV2ResponseBodyDataModel()
                self.model.append(temp_model.from_map(k1))

        return self

class ListFlowNodePrototypeV2ResponseBodyDataModel(DaraModel):
    def __init__(
        self,
        code: str = None,
        group_code: str = None,
        public_extend: str = None,
        status: str = None,
    ):
        # The code of the component prototype.
        self.code = code
        # The code of the component group.
        self.group_code = group_code
        # The public extension information. This is a JSON string that contains extension information for the frontend to display the flow component. The fields are described as follows:
        # 
        # - en: The English information about the flow component.
        # 
        # - zh: The Chinese information about the flow component.
        # 
        # - name: The name of the flow component.
        # 
        # - remark: The remarks on the flow component.
        # 
        # - order: The display order of the flow component.
        # 
        # - style: The style of the flow component.
        # 
        # - svg: The URL of the flow component icon.
        # 
        # - icon: This field is deprecated.
        # 
        # - bgcolor: The background color of the icon.
        self.public_extend = public_extend
        # The status of the component prototype. The default value is NORMAL.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.group_code is not None:
            result['GroupCode'] = self.group_code

        if self.public_extend is not None:
            result['PublicExtend'] = self.public_extend

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

        if m.get('PublicExtend') is not None:
            self.public_extend = m.get('PublicExtend')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

