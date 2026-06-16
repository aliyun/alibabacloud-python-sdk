# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_antiddos_public20170518 import models as main_models
from darabonba.model import DaraModel

class DescribeBgpPackByIpResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        ddosbgp_info: main_models.DescribeBgpPackByIpResponseBodyDdosbgpInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code of the request.
        # 
        # For more information about status codes, see [Common parameters](https://help.aliyun.com/document_detail/118841.html).
        self.code = code
        # The configurations of the instance that is associated with the asset.
        self.ddosbgp_info = ddosbgp_info
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: yes
        # 
        # - **false**: no
        self.success = success

    def validate(self):
        if self.ddosbgp_info:
            self.ddosbgp_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.ddosbgp_info is not None:
            result['DdosbgpInfo'] = self.ddosbgp_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DdosbgpInfo') is not None:
            temp_model = main_models.DescribeBgpPackByIpResponseBodyDdosbgpInfo()
            self.ddosbgp_info = temp_model.from_map(m.get('DdosbgpInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class DescribeBgpPackByIpResponseBodyDdosbgpInfo(DaraModel):
    def __init__(
        self,
        base_threshold: int = None,
        ddosbgp_instance_id: str = None,
        elastic_threshold: int = None,
        expire_time: int = None,
        ip: str = None,
    ):
        # The basic protection threshold of the instance. Unit: Gbit/s.
        self.base_threshold = base_threshold
        # The ID of the instance.
        self.ddosbgp_instance_id = ddosbgp_instance_id
        # The burstable protection threshold of the instance. Unit: Gbit/s.
        self.elastic_threshold = elastic_threshold
        # The expiration time of the instance. The value is a UNIX timestamp. Unit: milliseconds.
        self.expire_time = expire_time
        # The IP address of the asset.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_threshold is not None:
            result['BaseThreshold'] = self.base_threshold

        if self.ddosbgp_instance_id is not None:
            result['DdosbgpInstanceId'] = self.ddosbgp_instance_id

        if self.elastic_threshold is not None:
            result['ElasticThreshold'] = self.elastic_threshold

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseThreshold') is not None:
            self.base_threshold = m.get('BaseThreshold')

        if m.get('DdosbgpInstanceId') is not None:
            self.ddosbgp_instance_id = m.get('DdosbgpInstanceId')

        if m.get('ElasticThreshold') is not None:
            self.elastic_threshold = m.get('ElasticThreshold')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

