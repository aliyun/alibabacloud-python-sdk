# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class MoveResourcesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        responses: List[main_models.MoveResourcesResponseBodyResponses] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned results.
        self.responses = responses

    def validate(self):
        if self.responses:
            for v1 in self.responses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Responses'] = []
        if self.responses is not None:
            for k1 in self.responses:
                result['Responses'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.responses = []
        if m.get('Responses') is not None:
            for k1 in m.get('Responses'):
                temp_model = main_models.MoveResourcesResponseBodyResponses()
                self.responses.append(temp_model.from_map(k1))

        return self

class MoveResourcesResponseBodyResponses(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service: str = None,
        status: str = None,
    ):
        # The error code returned.
        # 
        # >  This parameter is returned if the resource failed to be moved.
        self.error_code = error_code
        # The error message returned.
        # 
        # >  This parameter is returned if the resource failed to be moved.
        self.error_msg = error_msg
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud service.
        self.service = service
        # The status of the move task. Valid values:
        # 
        # *   SUCCESS
        # *   FAIL
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service is not None:
            result['Service'] = self.service

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

