# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeSignatureLibVersionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        version: List[main_models.DescribeSignatureLibVersionResponseBodyVersion] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The version information.
        self.version = version

    def validate(self):
        if self.version:
            for v1 in self.version:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Version'] = []
        if self.version is not None:
            for k1 in self.version:
                result['Version'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.version = []
        if m.get('Version') is not None:
            for k1 in m.get('Version'):
                temp_model = main_models.DescribeSignatureLibVersionResponseBodyVersion()
                self.version.append(temp_model.from_map(k1))

        return self

class DescribeSignatureLibVersionResponseBodyVersion(DaraModel):
    def __init__(
        self,
        type: str = None,
        update_time: int = None,
        version: str = None,
    ):
        # The type.
        # 
        # Valid values:
        # 
        # *   ips
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Basic Rules and Virtual Patching
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   intelligence
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Threat Intelligence
        # 
        #     <!-- -->
        self.type = type
        # Update time.
        self.update_time = update_time
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

