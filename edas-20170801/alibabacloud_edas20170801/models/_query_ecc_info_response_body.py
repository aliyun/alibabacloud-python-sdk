# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class QueryEccInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        ecc_info: main_models.QueryEccInfoResponseBodyEccInfo = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The information about the ECC.
        self.ecc_info = ecc_info
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ecc_info:
            self.ecc_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.ecc_info is not None:
            result['EccInfo'] = self.ecc_info.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EccInfo') is not None:
            temp_model = main_models.QueryEccInfoResponseBodyEccInfo()
            self.ecc_info = temp_model.from_map(m.get('EccInfo'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryEccInfoResponseBodyEccInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        ecc_id: str = None,
        ecu_id: str = None,
        group_id: str = None,
        group_name: str = None,
        package_md_5: str = None,
        package_version: str = None,
        vpc_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # ECC ID
        self.ecc_id = ecc_id
        # ECU ID
        self.ecu_id = ecu_id
        # The ID of the ECC group.
        self.group_id = group_id
        # The name of the ECC group.
        self.group_name = group_name
        # The MD5 hash value of the deployment package version.
        self.package_md_5 = package_md_5
        # The version of the deployment package.
        self.package_version = package_version
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.ecc_id is not None:
            result['EccId'] = self.ecc_id

        if self.ecu_id is not None:
            result['EcuId'] = self.ecu_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.package_md_5 is not None:
            result['PackageMd5'] = self.package_md_5

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EccId') is not None:
            self.ecc_id = m.get('EccId')

        if m.get('EcuId') is not None:
            self.ecu_id = m.get('EcuId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('PackageMd5') is not None:
            self.package_md_5 = m.get('PackageMd5')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

