# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetTaskInstanceRelationResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        node_list: main_models.GetTaskInstanceRelationResponseBodyNodeList = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request fails.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        self.node_list = node_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        if self.node_list:
            self.node_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.node_list is not None:
            result['NodeList'] = self.node_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('NodeList') is not None:
            temp_model = main_models.GetTaskInstanceRelationResponseBodyNodeList()
            self.node_list = temp_model.from_map(m.get('NodeList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTaskInstanceRelationResponseBodyNodeList(DaraModel):
    def __init__(
        self,
        node: List[main_models.GetTaskInstanceRelationResponseBodyNodeListNode] = None,
    ):
        self.node = node

    def validate(self):
        if self.node:
            for v1 in self.node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Node'] = []
        if self.node is not None:
            for k1 in self.node:
                result['Node'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node = []
        if m.get('Node') is not None:
            for k1 in m.get('Node'):
                temp_model = main_models.GetTaskInstanceRelationResponseBodyNodeListNode()
                self.node.append(temp_model.from_map(k1))

        return self

class GetTaskInstanceRelationResponseBodyNodeListNode(DaraModel):
    def __init__(
        self,
        business_time: str = None,
        end_time: str = None,
        execute_time: int = None,
        id: int = None,
        message: str = None,
        node_id: int = None,
        node_name: str = None,
        node_type: int = None,
        status: int = None,
    ):
        self.business_time = business_time
        self.end_time = end_time
        self.execute_time = execute_time
        self.id = id
        self.message = message
        self.node_id = node_id
        self.node_name = node_name
        self.node_type = node_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_time is not None:
            result['BusinessTime'] = self.business_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessTime') is not None:
            self.business_time = m.get('BusinessTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

