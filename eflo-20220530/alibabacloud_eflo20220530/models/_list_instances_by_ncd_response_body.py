# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListInstancesByNcdResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.ListInstancesByNcdResponseBodyContent = None,
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
            temp_model = main_models.ListInstancesByNcdResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstancesByNcdResponseBodyContent(DaraModel):
    def __init__(
        self,
        instance_infos: List[main_models.ListInstancesByNcdResponseBodyContentInstanceInfos] = None,
        instance_type: str = None,
        max_ncd: int = None,
        source_instance_id: str = None,
    ):
        # A collection of instances whose network communication distance from the source instance ID does not exceed maxNcd
        self.instance_infos = instance_infos
        # Instance Type
        # 
        # Valid value:
        # 
        # *   node: Lingjun node.
        # *   lni: lingjun network interface controller.
        self.instance_type = instance_type
        # Maximum communication distance between nodes
        self.max_ncd = max_ncd
        # The ID of the source instance.
        self.source_instance_id = source_instance_id

    def validate(self):
        if self.instance_infos:
            for v1 in self.instance_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceInfos'] = []
        if self.instance_infos is not None:
            for k1 in self.instance_infos:
                result['InstanceInfos'].append(k1.to_map() if k1 else None)

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_ncd is not None:
            result['MaxNcd'] = self.max_ncd

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_infos = []
        if m.get('InstanceInfos') is not None:
            for k1 in m.get('InstanceInfos'):
                temp_model = main_models.ListInstancesByNcdResponseBodyContentInstanceInfos()
                self.instance_infos.append(temp_model.from_map(k1))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxNcd') is not None:
            self.max_ncd = m.get('MaxNcd')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        return self

class ListInstancesByNcdResponseBodyContentInstanceInfos(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ncd: int = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # network communication distance
        self.ncd = ncd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ncd is not None:
            result['Ncd'] = self.ncd

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ncd') is not None:
            self.ncd = m.get('Ncd')

        return self

