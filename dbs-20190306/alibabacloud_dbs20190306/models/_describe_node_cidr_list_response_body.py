# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribeNodeCidrListResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        internet_ips: main_models.DescribeNodeCidrListResponseBodyInternetIPs = None,
        intranet_ips: main_models.DescribeNodeCidrListResponseBodyIntranetIPs = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        self.internet_ips = internet_ips
        self.intranet_ips = intranet_ips
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.internet_ips:
            self.internet_ips.validate()
        if self.intranet_ips:
            self.intranet_ips.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.internet_ips is not None:
            result['InternetIPs'] = self.internet_ips.to_map()

        if self.intranet_ips is not None:
            result['IntranetIPs'] = self.intranet_ips.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InternetIPs') is not None:
            temp_model = main_models.DescribeNodeCidrListResponseBodyInternetIPs()
            self.internet_ips = temp_model.from_map(m.get('InternetIPs'))

        if m.get('IntranetIPs') is not None:
            temp_model = main_models.DescribeNodeCidrListResponseBodyIntranetIPs()
            self.intranet_ips = temp_model.from_map(m.get('IntranetIPs'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeNodeCidrListResponseBodyIntranetIPs(DaraModel):
    def __init__(
        self,
        intranet_ip: List[str] = None,
    ):
        self.intranet_ip = intranet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intranet_ip is not None:
            result['IntranetIP'] = self.intranet_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetIP') is not None:
            self.intranet_ip = m.get('IntranetIP')

        return self

class DescribeNodeCidrListResponseBodyInternetIPs(DaraModel):
    def __init__(
        self,
        internet_ip: List[str] = None,
    ):
        self.internet_ip = internet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_ip is not None:
            result['InternetIP'] = self.internet_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetIP') is not None:
            self.internet_ip = m.get('InternetIP')

        return self

