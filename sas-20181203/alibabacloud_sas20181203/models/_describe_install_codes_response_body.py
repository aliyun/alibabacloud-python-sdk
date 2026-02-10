# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeInstallCodesResponseBody(DaraModel):
    def __init__(
        self,
        install_codes: List[main_models.DescribeInstallCodesResponseBodyInstallCodes] = None,
        request_id: str = None,
    ):
        # The information about the installation commands.
        self.install_codes = install_codes
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.install_codes:
            for v1 in self.install_codes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstallCodes'] = []
        if self.install_codes is not None:
            for k1 in self.install_codes:
                result['InstallCodes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.install_codes = []
        if m.get('InstallCodes') is not None:
            for k1 in m.get('InstallCodes'):
                temp_model = main_models.DescribeInstallCodesResponseBodyInstallCodes()
                self.install_codes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstallCodesResponseBodyInstallCodes(DaraModel):
    def __init__(
        self,
        captcha_code: str = None,
        expired_date: int = None,
        group_id: int = None,
        group_name: str = None,
        only_image: bool = None,
        os: str = None,
        private_link_endpoint_id: int = None,
        proxy_cluster: str = None,
        vendor_name: str = None,
    ):
        # The verification code for you to manually install the Security Center agent.
        self.captcha_code = captcha_code
        # The timestamp generated when the commands used to install the Security Center agent expire. Unit: milliseconds.
        self.expired_date = expired_date
        # The ID of the server group to which the server belongs.
        self.group_id = group_id
        # The name of the server group to which the server belongs.
        self.group_name = group_name
        # Indicates whether an image is used to install the Security Center agent. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.only_image = only_image
        # The operating system of the server. Valid values:
        # 
        # *   **linux**
        # *   **windows**
        self.os = os
        # The ID of the PrivateLink endpoint.
        self.private_link_endpoint_id = private_link_endpoint_id
        # The name of the proxy cluster.
        self.proxy_cluster = proxy_cluster
        # The name of the server provider.
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.captcha_code is not None:
            result['CaptchaCode'] = self.captcha_code

        if self.expired_date is not None:
            result['ExpiredDate'] = self.expired_date

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.only_image is not None:
            result['OnlyImage'] = self.only_image

        if self.os is not None:
            result['Os'] = self.os

        if self.private_link_endpoint_id is not None:
            result['PrivateLinkEndpointId'] = self.private_link_endpoint_id

        if self.proxy_cluster is not None:
            result['ProxyCluster'] = self.proxy_cluster

        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptchaCode') is not None:
            self.captcha_code = m.get('CaptchaCode')

        if m.get('ExpiredDate') is not None:
            self.expired_date = m.get('ExpiredDate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('OnlyImage') is not None:
            self.only_image = m.get('OnlyImage')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PrivateLinkEndpointId') is not None:
            self.private_link_endpoint_id = m.get('PrivateLinkEndpointId')

        if m.get('ProxyCluster') is not None:
            self.proxy_cluster = m.get('ProxyCluster')

        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')

        return self

