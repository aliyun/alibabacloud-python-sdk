# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeEntityInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeEntityInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.DescribeEntityInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeEntityInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        entity_id: int = None,
        entity_info: Dict[str, Any] = None,
        entity_type: str = None,
        tip_info: Dict[str, Any] = None,
    ):
        # The logical ID of the entity.
        self.entity_id = entity_id
        # The information about the entry.
        self.entity_info = entity_info
        # The type of the entity. Valid values:
        # 
        # *   ip
        # *   domain
        # *   url
        # *   process
        # *   file
        # *   host
        self.entity_type = entity_type
        # The information about the risk Intelligence.
        self.tip_info = tip_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.tip_info is not None:
            result['TipInfo'] = self.tip_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityInfo') is not None:
            self.entity_info = m.get('EntityInfo')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('TipInfo') is not None:
            self.tip_info = m.get('TipInfo')

        return self

