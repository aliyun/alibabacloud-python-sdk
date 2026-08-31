# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateNodeOpsOwnerResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.UpdateNodeOpsOwnerResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. A value of OK indicates that the request was successful.
        self.code = code
        # The list of per-node operation results.
        self.data = data
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.UpdateNodeOpsOwnerResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateNodeOpsOwnerResponseBodyData(DaraModel):
    def __init__(
        self,
        error_info: str = None,
        id: str = None,
        name: str = None,
        node_from_type: str = None,
        status: str = None,
    ):
        # The failure reason. This value is empty if the operation was successful.
        self.error_info = error_info
        # The node ID. This corresponds to the Id in the NodeIdList request parameter.
        self.id = id
        # The node name.
        self.name = name
        # The node source type.
        self.node_from_type = node_from_type
        # The change result status for the node.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.node_from_type is not None:
            result['NodeFromType'] = self.node_from_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeFromType') is not None:
            self.node_from_type = m.get('NodeFromType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

