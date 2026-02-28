# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class QueryInstanceNcdResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.QueryInstanceNcdResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The returned message.
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Content') is not None:
            temp_model = main_models.QueryInstanceNcdResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryInstanceNcdResponseBodyContent(DaraModel):
    def __init__(
        self,
        instance_id_1: str = None,
        instance_id_2: str = None,
        instance_type: str = None,
        ncd: int = None,
    ):
        # Instance 1ID
        self.instance_id_1 = instance_id_1
        # Instance 2ID
        self.instance_id_2 = instance_id_2
        # Instance Type
        # 
        # Valid value:
        # 
        # *   node: Lingjun node.
        # *   lni: lingjun network interface controller.
        self.instance_type = instance_type
        # network communication distance between instances
        self.ncd = ncd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id_1 is not None:
            result['InstanceId1'] = self.instance_id_1

        if self.instance_id_2 is not None:
            result['InstanceId2'] = self.instance_id_2

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ncd is not None:
            result['Ncd'] = self.ncd

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId1') is not None:
            self.instance_id_1 = m.get('InstanceId1')

        if m.get('InstanceId2') is not None:
            self.instance_id_2 = m.get('InstanceId2')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ncd') is not None:
            self.ncd = m.get('Ncd')

        return self

