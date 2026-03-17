# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSmartAccessGatewayVersionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        smart_agversions: main_models.DescribeSmartAccessGatewayVersionsResponseBodySmartAGVersions = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        self.smart_agversions = smart_agversions

    def validate(self):
        if self.smart_agversions:
            self.smart_agversions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.smart_agversions is not None:
            result['SmartAGVersions'] = self.smart_agversions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SmartAGVersions') is not None:
            temp_model = main_models.DescribeSmartAccessGatewayVersionsResponseBodySmartAGVersions()
            self.smart_agversions = temp_model.from_map(m.get('SmartAGVersions'))

        return self

class DescribeSmartAccessGatewayVersionsResponseBodySmartAGVersions(DaraModel):
    def __init__(
        self,
        smart_agversion: List[main_models.DescribeSmartAccessGatewayVersionsResponseBodySmartAGVersionsSmartAGVersion] = None,
    ):
        self.smart_agversion = smart_agversion

    def validate(self):
        if self.smart_agversion:
            for v1 in self.smart_agversion:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SmartAGVersion'] = []
        if self.smart_agversion is not None:
            for k1 in self.smart_agversion:
                result['SmartAGVersion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.smart_agversion = []
        if m.get('SmartAGVersion') is not None:
            for k1 in m.get('SmartAGVersion'):
                temp_model = main_models.DescribeSmartAccessGatewayVersionsResponseBodySmartAGVersionsSmartAGVersion()
                self.smart_agversion.append(temp_model.from_map(k1))

        return self

class DescribeSmartAccessGatewayVersionsResponseBodySmartAGVersionsSmartAGVersion(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        type: str = None,
        version_code: str = None,
        version_name: str = None,
    ):
        self.create_time = create_time
        self.type = type
        self.version_code = version_code
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.type is not None:
            result['Type'] = self.type

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

